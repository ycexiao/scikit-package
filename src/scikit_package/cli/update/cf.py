import os

import click

from scikit_package.utils import api, auth, io
from scikit_package.utils.shell import run

def _update_meta_yaml(meta_file_path, new_version, new_sha256):
    """Update the meta.yaml file with the new version and SHA256."""
    with open(meta_file_path, "r") as file:
        lines = file.readlines()

    with open(meta_file_path, "w") as file:
        for line in lines:
            if "{%- set version =" in line:
                line = f'{{%- set version = "{new_version}" -%}}\n'
            elif "{% set version =" in line:
                line = f'{{% set version = "{new_version}" %}}\n'
            elif "sha256:" in line:
                line = f"  sha256: {new_sha256}\n"
            file.write(line)


def _run_shell_commands(
    cwd, meta_file_path, version, SHA256, username, pkg_name
):
    """Create a PR from a branch name of <new_version> to upstream/main."""
    run("git stash", cwd=cwd)
    run("git checkout main", cwd=cwd)
    run("git pull upstream main", cwd=cwd)
    run(f"git checkout -b {version}", cwd=cwd)
    _update_meta_yaml(meta_file_path, version, SHA256)
    run("git add recipe/meta.yaml", cwd=cwd)
    run(f'git commit -m "release: update to {version}"', cwd=cwd)
    run(f"git push origin {version}", cwd=cwd)
    run(
        f"gh repo set-default conda-forge/{pkg_name}-feedstock",
        cwd=cwd,
    )
    pr_command = (
        f"gh pr create --base main --head {username}:{version} "
        f"--title 'Release {version}' "
    )
    run(pr_command, cwd=cwd)


def update():
    """
    Update the Python package version and SHA256 hash in a meta.yaml file,
    and create a pull request to the upstream feedstock repository.

    Step-by-step process:
    - List the latest versions and SHA256 hashes from PyPI.
    - Prompt the user to select the feedstock to update.
    - Update the meta.yaml file with the new version and SHA256 hash.
    - Commit and push the changes to a <username>/<version> branch on GitHub.
    - Create a pull request to conda-forge/main.
    - Prompt the user to use the pull request template via the CLI.
    """
    feedstock_path = io.get_config_value("feedstock_path")
    feedstocks = [
        f for f in os.listdir(feedstock_path)
        if f.endswith("-feedstock")
        and os.path.isdir(os.path.join(feedstock_path, f))
    ]
    if not feedstocks:
        raise ValueError(
            f"No feedstocks found in {feedstock_path}. "
            "Please ensure you have feedstocks in the given directory."
        )
    print("Available feedstocks:")
    version_map = {}
    for i, feedstock in enumerate(feedstocks, start=1):
        pkg_name = feedstock.replace("-feedstock", "")
        pkg_pypi_data = api.get_PyPI_version_SHA(pkg_name, count=1)
        pkg_version, pkg_sha256 = next(iter(pkg_pypi_data.items()))
        version_map[i] = {
            "package_name": pkg_name,
            "version": pkg_version,
            "sha256": pkg_sha256,
            "feedstock_dir_path": os.path.join(feedstock_path, feedstock),
            "meta_file_path": os.path.join(
                feedstock_path, feedstock, "recipe", "meta.yaml"
            ),
        }
        print(
            f"  {i}. {pkg_name}, {pkg_version}, SHA256: {pkg_sha256[:5]}.."
        )
    choice = click.prompt(
        "Enter the corresponding number of the feedstock you want to update",
        type=click.IntRange(1, len(feedstocks)),
    )
    selected = version_map[choice]
    username = auth.get_github_username()
    _run_shell_commands(
        selected["feedstock_dir_path"],
        selected["meta_file_path"],
        selected["version"],
        selected["sha256"],
        username,
        selected["package_name"],
    )
