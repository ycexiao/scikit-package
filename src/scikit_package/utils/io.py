import json
import os
from pathlib import Path

from scikit_package.utils import io

try:
    SKPKG_USER_CONFIG_FILE = os.environ["SKPKG_CONFIG_FILE"]
except KeyError:
    SKPKG_USER_CONFIG_FILE = "~/.skpkgrc"
SKPKG_PROJ_CONFIG_FILE = ".skpkgrc"


def read_file(path):
    with open(path, "r") as f:
        return f.readlines()


def write_file(path, lines):
    with open(path, "w") as f:
        f.writelines(lines)


def read_skpkg_config(config_file=SKPKG_USER_CONFIG_FILE):
    """Read the configuration file."""
    config_path = Path(config_file).expanduser()
    if not config_path.exists():
        raise FileNotFoundError(
            f"scikit-packag configuration file {config_file} is not found. "
            f"Please try again after running 'touch {config_file}'."
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


def get_config_cmd():
    config_cmd = []
    user_config_path = Path(
        os.path.expandvars(SKPKG_USER_CONFIG_FILE)
    ).expanduser()
    if user_config_path.exists():
        config_cmd.extend(["--config-file", str(user_config_path)])

    try:
        proj_config_dict = read_skpkg_config(SKPKG_PROJ_CONFIG_FILE)
        overwrite_context = [
            key + "=" + value
            for key, value in proj_config_dict.items()
            if not (value.startswith("[") and value.endswith("]"))
        ]
    except FileNotFoundError:
        overwrite_context = []
    config_cmd.extend(overwrite_context)
    return config_cmd
