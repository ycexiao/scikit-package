import os
import subprocess
from pathlib import Path

import requests

SKPKG_CONFIG_FILE = "~/.skpkgrc"
try:
    config_file = os.environ["SKPKG_CONFIG_FILE"]
except KeyError:
    config_file = SKPKG_CONFIG_FILE
config_file = os.path.expandvars(config_file)
config_file = Path(config_file).expanduser()
exist_config = config_file.exists()


def _get_latest_tag(repo_url):
    api_url = (
        repo_url.replace(
            "https://github.com/", "https://api.github.com/repos/"
        )
        + "/tags"
    )
    response = requests.get(api_url)
    tags = response.json()
    return tags[0]["name"]


def run(repo_url):
    """Run cookiecutter with optional config file."""
    tag = _get_latest_tag(repo_url)
    print(f"You are using the latest version of {tag} in {repo_url}.")
    try:
        cmd = ["cookiecutter", repo_url]
        cmd.extend(["--checkout", tag])
        if exist_config:
            cmd.extend(["--config-file", str(config_file)])
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to run scikit-package for the following reason: {e}")
