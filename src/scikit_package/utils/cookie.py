import subprocess

from scikit_package.utils import io, pypi


def run(repo_url):
    """Run cookiecutter with optional config file."""
    username_or_orgname = repo_url.split("/")[3]
    repo_name = repo_url.split("/")[4]
    tag = io.get_latest_release_tag(username_or_orgname, repo_name)
    if repo_name == "scikit-package-conda-forge":
        # Ask user input for the name of the package to be created
        package_name = input(
            "Enter the package name to check whether it's available on PyPI: "
        )
        pypi.check_pypi_package_exists(package_name)
    print(f"You are using the latest release version of {tag} in {repo_url}.")
    try:
        cmd = ["cookiecutter", repo_url]
        cmd.extend(["--checkout", tag])
        config_cmd = io.get_config_cmd()
        cmd.extend(config_cmd)
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to run scikit-package for the following reason: {e}")
