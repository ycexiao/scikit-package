import pytest

from scikit_package.utils.pypi import (  # Replace with your actual module
    check_pypi_package_exists,
)


def test_package_exists():
    check_pypi_package_exists("diffpy.pdffit2")


def test_package_does_not_exist_real():
    with pytest.raises(ValueError) as e:
        check_pypi_package_exists("package-does-not-exist")
    assert "package-does-not-exist is not found on PyPI" in str(e.value)
