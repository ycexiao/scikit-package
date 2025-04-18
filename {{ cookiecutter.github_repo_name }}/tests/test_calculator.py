import pytest
from {{cookiecutter.package_dir_name}} import calculator


def test_dot_product_2D():
    """Test the dot product function with 2D vectors."""
    a = [1, 2]
    b = [3, 4]
    expected = 11
    actual = calculator.dot_product(a, b)
    assert actual == expected


def test_dot_product_3D():
    """Test the dot product function with 3D vectors."""
    a = [1, 2, 3]
    b = [4, 5, 6]
    expected = 32
    actual = calculator.dot_product(a, b)
    assert actual == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        # Test whether the doc product function works with different vector sizes
        # 2D vectors, expect 11
        ([1, 2], [3, 4], 11),
        # 3D vectors, exppect 32
        ([1, 2, 3], [4, 5, 6], 32),
    ]
)
def test_dot_product(a, b, expected):
    actual = calculator.dot_product(a, b)
    assert actual == expected
