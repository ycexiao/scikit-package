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


def run(repo_url):
    try:
        if exist_config:
            subprocess.run(
                [
                    "cookiecutter",
                    repo_url,
                    "--config-file",
                    config_file,
                ],
                check=True,
            )
        else:
            subprocess.run(
                [
                    "cookiecutter",
                    repo_url,
                ],
                check=True,
            )

    except subprocess.CalledProcessError as e:
        print(f"Failed to run scikit-package for the following reason: {e}")
