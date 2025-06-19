import os
import subprocess
from pathlib import Path

SKPKG_CONFIG_FILE = "~/.skpkgrc"
try:
    config_file = os.environ["SKPKG_CONFIG_FILE"]
except KeyError:
    config_file = SKPKG_CONFIG_FILE
config_file = os.path.expandvars(config_file)
config_file = Path(config_file).expanduser()
exist_config = config_file.exists()


def run(repo_url, tag=None):
    """Run cookiecutter with optional config file and optional
    tag/branch/commit."""
    try:
        cmd = ["cookiecutter", repo_url]
        if tag:
            cmd.extend(["--checkout", tag])
        if exist_config:
            cmd.extend(["--config-file", str(config_file)])
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to run scikit-package for the following reason: {e}")
