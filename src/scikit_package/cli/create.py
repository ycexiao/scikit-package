import json
import shutil
from pathlib import Path

from jinja2 import Template

from scikit_package.utils import cookie

SKPKG_GITHUB_URL = "https://github.com/scikit-package/scikit-package"


def cleanup_examples(project_dir, subcmd, config_dict):
    files_or_dirs_to_be_removed_dict = {
        "workspace": [
            "proj-one",
            "shared_functions.py",
            "tests/test_shared_functions.py",
        ],
        "system": [
            r"src/{{ package_dir_name }}/functions.py",
            "tests/test_functions.py",
        ],
        "public": [
            (r"docs/source/api/{{ package_dir_name }}" ".example_package.rst"),
            "docs/source/getting-started.rst",
            r"src/{{ package_dir_name }}/functions.py",
            "tests/test_functions.py",
            "docs/source/img/scikit-package-logo-text.png",
            "docs/source/snippets/example-table.rst",
        ],
    }
    files_or_dirs_to_be_removed = files_or_dirs_to_be_removed_dict[subcmd]
    for filename in files_or_dirs_to_be_removed:
        filename = Template(filename).render(**config_dict)
        if "src" in filename.split("/")[0]:
            parents = filename.split("/")[:-1]
            name = filename.split("/")[-1]
            parents = [parent.replace(".", "/") for parent in parents]
            filename = "/".join([*parents, name])
        file_path = project_dir / filename
        if file_path.exists():
            if file_path.is_file():
                file_path.unlink()
            else:
                shutil.rmtree(file_path)
        else:
            print(
                f"Unable to find {str(file_path)} to remove. "
                "Cleanup process will continue. Please leave an issue "
                "on GitHub."
            )

    files_to_be_added_dict = {
        "workspace": [],
        "system": [],
        "public": [
            "docs/source/img/.placeholder",
            "docs/source/snippets/.placeholder",
        ],
    }
    files_to_be_added = files_to_be_added_dict[subcmd]
    for filename in files_to_be_added:
        file_path = project_dir / filename
        if not file_path.exists():
            file_path.touch()


def package(args):
    """Run the cookiecutter template for creating a package.

    By default, checkout the latest release tag from the relevant GitHub
    repository.
    """
    items_before_run = [f for f in Path().cwd().iterdir()]
    subcmd = args.subcommand
    if subcmd == "workspace":
        cookie.run(f"{SKPKG_GITHUB_URL}-workspace")
    elif subcmd == "system":
        cookie.run(f"{SKPKG_GITHUB_URL}-system")
    elif subcmd == "public":
        cookie.run(SKPKG_GITHUB_URL)
    elif subcmd == "conda-forge":
        cookie.run(f"{SKPKG_GITHUB_URL}-conda-forge")
    elif subcmd == "manuscript":
        cookie.run(f"{SKPKG_GITHUB_URL}-manuscript")
    items_after_run = [f for f in Path().cwd().iterdir()]
    if args.update:
        print("Create the package in the update mode.")
        generated_dirs = list(set(items_after_run) - set(items_before_run))
        if len(generated_dirs) == 1:
            project_dir = generated_dirs[0]
        else:
            print(
                "Reverting to the normal mode "
                "because scikit-package was unable to identify the generated "
                "package. "
                "Please leave an issue on GitHub."
            )
            return
        created_proj_config_path = project_dir / "cookiecutter.json"
        if created_proj_config_path.exists():
            with open(created_proj_config_path, "r") as f:
                config_dict = json.load(f)
        else:
            print(
                "Reverting to the normal mode "
                "because scikit-package was unable to find cookiecutter.json "
                "in the generated package. "
                "Please leave an issue on GitHub."
            )
            return
        cleanup_examples(project_dir, subcmd, config_dict)
