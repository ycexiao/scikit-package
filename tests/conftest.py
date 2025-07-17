import json
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def files_in_old_project():
    file_names = [
        "AUTHORS.rst",
        "CHANGELOG.rst",
        ".codecov.yml",
        "CODE-OF-CONDUCT.rst",
        ".codespell/ignore_lines.txt",
        "docs/source/index.rst",
        ".flake8",
        ".git/index",
        ".github/ISSUE_TEMPLATE/bug_feature.md",
        ".gignore",
        ".isort.cfg",
        "LICENSE.rst",
        "MANIFEST.in",
        "news/TEMPLATE.rst",
        ".pre-commit-config.yaml",
        "pyprojec.toml",
        "README.rst",
        ".readthedocs.yaml",
        "requirements/pip.txt",
        "src/__init__.py",
        "src/skpkg-package/__init__.py",
        "tests/test_package.py",
    ]
    yield file_names


@pytest.fixture
def user_filesystem(tmp_path, files_in_old_project):
    base_dir = Path(tmp_path)
    home_dir = base_dir / "home_dir"
    home_dir.mkdir(parents=True, exist_ok=True)
    cwd_dir = base_dir / "cwd_dir"
    cwd_dir.mkdir(parents=True, exist_ok=True)

    home_config_data = {"username": "home_username", "email": "home@email.com"}
    with open(home_dir / "diffpyconfig.json", "w") as f:
        json.dump(home_config_data, f)

    old_package_dir = home_dir / "package-dir"
    for file_name in files_in_old_project:
        file_path = old_package_dir / file_name
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.touch()

    yield tmp_path
