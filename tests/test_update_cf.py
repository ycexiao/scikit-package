from pathlib import Path

from scikit_package.cli.update.cf import _update_meta_yaml


def test_update_meta_yaml_realistic(tmpdir):
    original_meta = """{%- set version = "1.0.5" -%}
package:
  name: {{ name|lower }}
  version: {{ version }}

source:
  url: https://pypi.org/packages/source/{{ name[0] }}/{{ name }}/{{ name }}-{{ version }}.tar.gz  # noqa: E501
  sha256: 1b71d398d73800db32b09785af0e7
"""
    new_version = "1.0.6"
    new_sha256 = "123456789abcdef0123456789"
    expected_updated_meta = """{%- set version = "1.0.6" -%}
package:
  name: {{ name|lower }}
  version: {{ version }}

source:
  url: https://pypi.org/packages/source/{{ name[0] }}/{{ name }}/{{ name }}-{{ version }}.tar.gz  # noqa: E501
  sha256: 123456789abcdef0123456789
"""
    meta_file = Path(tmpdir) / "meta.yaml"
    meta_file.write_text(original_meta)
    _update_meta_yaml(str(meta_file), new_version, new_sha256)
    updated_meta = meta_file.read_text()
    assert updated_meta == expected_updated_meta


# C1: All the required files exist in the old package dir and there are no
#   duplicate file names in the target dir. Expect example files are created
#   and all the required files are safely copied over.
# C2: All the required files exist in the old package dir but there are
#   duplicate file names in the target path. Expect example files are created,
#   files without duplicate name are safely copied over, and files with
#   duplicate names are skipped.
def test_update_package():
    assert False


# C1: Some required files are missing in the old package dir. Expect
#   FileNotFound error.
def test_update_package_bad():
    assert False
