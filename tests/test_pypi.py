import pytest
from scikit_package.utils.pypi import check_pypi_package_exists  # Replace with your actual module


def test_package_exists():
    check_pypi_package_exists("diffpy.pdffit2")

def test_package_does_not_exist_real():
    with pytest.raises(ValueError) as e:
        check_pypi_package_exists("thispackageshallnotexist")
    assert "No matching package found" in str(e.value)