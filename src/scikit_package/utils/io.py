import json
import os
import shutil
from pathlib import Path

import requests

from scikit_package.utils import io

SKPKG_USER_CONFIG_FILE = "~/.skpkgrc"
try:
    config_file = os.environ["SKPKG_CONFIG_FILE"]
except KeyError:
    config_file = SKPKG_USER_CONFIG_FILE
config_file = os.path.expandvars(config_file)
config_file = Path(config_file).expanduser()

SKPKG_PROJ_CONFIG_FILE = "cookiecutter.json"
proj_config_file = Path(SKPKG_PROJ_CONFIG_FILE).expanduser()


def read_file(path):
    with open(path, "r") as f:
        return f.readlines()


def write_file(path, lines):
    with open(path, "w") as f:
        f.writelines(lines)


def copy_all_files(source_dir, target_dir, exists_ok=False):
    """Copies files from a source directory to a target directory.

    Parameters
    ===========
    source_dir : Path
        The source dir from which all the files will be copied recursively.
    project_dir : Path
        The path to the output directory where the files will be copied to.
    exists_ok : bool
        If False (default), raises FileExistsError if the file exists in both
        source_dir and target_dir.
        If True, files with duplicated names will be skipped and won't be
        copied into target_dir.

    Return
    ======
    None
    """
    if not source_dir.exists():
        raise FileNotFoundError(
            f"Unable to find the source directory: {str(source_dir)}."
        )

    if not any(source_dir.iterdir()):
        raise FileNotFoundError(
            f"Source directory {str(source_dir)} found "
            "but it contains no files. "
        )

    duplicate_files = []
    for item in source_dir.iterdir():
        dest = target_dir / item.name
        if dest.exists():
            duplicate_files.append(item)
    if not exists_ok and len(duplicate_files) != 0:
        duplicate_names = [file.name for file in duplicate_files]
        raise FileExistsError(
            f"{duplicate_names} already exists in target dir: "
            f"{str(target_dir)}. "
        )

    for item in source_dir.iterdir():
        if item in duplicate_files:
            continue
        dest = target_dir / item.name
        if item.is_file():
            shutil.copy(item, dest)
        else:
            shutil.copytree(item, dest)
    return


def read_skpkg_config(config_path=config_file):
    """Read the ~/.skpkgrc configuration file."""
    if not config_path.exists():
        raise FileNotFoundError(
            f"scikit-packag configuration file {str(config_file)} is "
            "not found. Please try again after  running "
            f"'touch {str(config_file)}'."
        )
    with config_path.open() as f:
        return json.load(f)


def get_config_value(key):
    """Given the key, get the value from ~/.skpkgrc."""
    value = io.read_skpkg_config().get(key, None)
    if not value:
        raise ValueError(
            f"No '{key}' is found in your ~/.skpkgrc file. "
            f"Please set '{key}' as instructed in the documentation."
        )
    return value


def get_latest_release_tag(owner, repo):
    """Get the latest release tag from a GitHub repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["tag_name"]


def get_config_cmd(config_file=config_file, proj_config_file=proj_config_file):
    config_cmd = []
    if config_file.exists():
        config_cmd.extend(["--config-file", str(config_file)])
    if proj_config_file.exists():
        extra_context = read_skpkg_config(proj_config_file)
        extra_context_cmd = []
        for key, value in extra_context.items():
            if isinstance(value, list):
                continue
            cmd = key + "=" + value
            extra_context_cmd.append(cmd)
        config_cmd.extend(extra_context_cmd)
    return config_cmd
