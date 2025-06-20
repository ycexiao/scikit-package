import json
from pathlib import Path

import requests

from scikit_package.utils import io


def read_file(path):
    with open(path, "r") as f:
        return f.readlines()


def write_file(path, lines):
    with open(path, "w") as f:
        f.writelines(lines)


def read_skpkg_config():
    """Read the ~/.skpkgrc configuration file."""
    config_path = Path("~/.skpkgrc").expanduser()
    if not config_path.exists():
        raise FileNotFoundError(
            "scikit-packag configuration file ~/.skpkgrc is not found. "
            "Please try again after running 'touch ~/.skpkgrc'."
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
