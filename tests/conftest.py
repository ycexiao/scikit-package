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

    old_package_dir = home_dir / "package-dir"
    files_in_old_project = [
        ".git/index",
        ".pre-commit-config.yaml",
        "src/__init__.py",
        "tests/test_package.py",
        "docs/source/index.rst",
        "news/TEMPLATE.rst",
    ]
    for file_name in files_in_old_project:
        file_path = old_package_dir / file_name
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.touch()

    yield tmp_path
