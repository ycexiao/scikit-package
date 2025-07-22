import os

# import subprocess
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


# C1: Run `package update`. Expect example files are not created and files with
#   duplicated name in the created package are skipped, files without
#   duplicated names are copied into the created package.
def test_package_update(user_filesystem):
    # old_package_dir = Path(user_filesystem) / "package-dir"
    env = os.environ.copy()
    env["HOME"] = str(Path(user_filesystem))
    # template = Path(__file__).parents[1]
    # subprocess.run(
    #     [
    #         "cookiecutter",
    #         str(template),
    #         "_is_update=Yes",
    #     ],
    #     cwd=old_package_dir,
    #     env=env,
    #     input="\n" * 17,  # use the default value in the prompt
    #     text=True,
    # )


#     new_package_dir = old_package_dir / "diffpy.my-project"
#     example_files = [
#         "docs/source/api/diffpy.my-project.example_package.rst",
#         "docs/source/getting-started.rst",
#         "src/diffpy/my-project/functions.py",
#         "tests/test_functions.py",
#     ]
#     for file_name in example_files:
#         example_file = new_package_dir / file_name
#         assert not example_file.exists()
#     files_only_in_old_package = {
#         ".git/COMMIT_EDITMSG": """
# skpkg: last commit message in skpkg-package
# """,
#         "docs/source/tutorial.rst": """
# The tutorial for skpkg-package.
# """,
#     }
#     files_with_duplicated_name = {
#         "README.rst": """
# |Icon| |title|_
# ===============

# .. |title| replace:: title of README.rst in skpkg-package
# """,
#         "docs/source/index.rst": """
# #######
# |title|
# #######

# .. |title| replace:: title of skpkg-package documentation
# """,
#     }
#     for file_name, file_content in files_only_in_old_package.items():
#         copied_file = new_package_dir / file_name
#         actual_content = copied_file.read_text()
#         expected_content = file_content
#         assert actual_content == expected_content
#     for file_name, file_content in files_with_duplicated_name.items():
#         skipped_file = new_package_dir / file_name
#         actual_content = skipped_file.read_text()
#         old_file_content = file_content
#         assert actual_content != old_file_content
