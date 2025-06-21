import os
import subprocess
from pathlib import Path

from scikit_package.utils import io

SKPKG_CONFIG_FILE = "~/.skpkgrc"
try:
    config_file = os.environ["SKPKG_CONFIG_FILE"]
except KeyError:
    config_file = SKPKG_CONFIG_FILE
config_file = os.path.expandvars(config_file)
config_file = Path(config_file).expanduser()
exist_config = config_file.exists()


def run(repo_url):
    """Run cookiecutter with optional config file."""
    username_or_orgname = repo_url.split("/")[3]
    repo_name = repo_url.split("/")[4]
    tag = io.get_latest_release_tag(username_or_orgname, repo_name)
    print(f"You are using the latest release version of {tag} in {repo_url}.")
    try:
        cmd = ["cookiecutter", repo_url]
        cmd.extend(["--checkout", tag])
        if exist_config:
            cmd.extend(["--config-file", str(config_file)])
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to run scikit-package for the following reason: {e}")
