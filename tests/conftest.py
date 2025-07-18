import json
from pathlib import Path

import pytest


@pytest.fixture
def user_filesystem(tmp_path):
    base_dir = Path(tmp_path)
    home_dir = base_dir / "home_dir"
    home_dir.mkdir(parents=True, exist_ok=True)
    cwd_dir = base_dir / "cwd_dir"
    cwd_dir.mkdir(parents=True, exist_ok=True)

    home_config_data = {"username": "home_username", "email": "home@email.com"}
    with open(home_dir / "diffpyconfig.json", "w") as f:
        json.dump(home_config_data, f)

    old_package_dir = base_dir / "package-dir"
    files_only_in_old_project = [
        ".git/index",
        "docs/source/index.rst",
    ]
    files_with_duplicated_name = [
        ".pre-commit-config.yaml",
        "src/__init__.py",
    ]
    for file_name in [*files_only_in_old_project, *files_with_duplicated_name]:
        file_path = old_package_dir / file_name
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.touch()

    yield tmp_path
