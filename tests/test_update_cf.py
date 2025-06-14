import pytest
import tempfile
from unittest.mock import patch, MagicMock
from pathlib import Path

from scikit_package.cli.update.cf import (
    _update_meta_yaml,
    _check_branch_exists,
    _check_remote_exists,
    _list_feedstock,
    _run_commands,
    update,
)

def test_update_meta_yaml_realistic():
    original_meta = """{%- set version = "1.0.5" -%}
package:
  name: {{ name|lower }}
  version: {{ version }}

source:
  url: https://pypi.org/packages/source/{{ name[0] }}/{{ name }}/{{ name }}-{{ version }}.tar.gz
  sha256: 1b71d398d73800db32b09785af0e755e2bebb1d508fd8fa319ca16379386e98e
"""
    new_version = "1.0.6"
    new_sha256 = "123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0"
    with tempfile.TemporaryDirectory() as tmpdir:
        meta_file = Path(tmpdir) / "meta.yaml"
        meta_file.write_text(original_meta)
        _update_meta_yaml(str(meta_file), new_version, new_sha256)
        updated_lines = meta_file.read_text().splitlines()
        assert updated_lines[0] == f'{{%- set version = "1.0.6" -%}}'
        assert updated_lines[1] == "package"
        assert updated_lines[2] == "  name: {{ name|lower }}"
        assert updated_lines[7] == f"  sha256: 123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0"
