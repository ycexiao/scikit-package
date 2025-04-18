import numpy as np


def dot_product(a, b):
    """Compute the dot product of two vectors of any size.

    Ensure that the inputs of a and b are of the same size.
    The supported types are Python list, Python tuple, and NumyPy array.

    Parameters
    ----------
    a : array_like
        The first input of vector.
    b : array_like
        The second input vector.

    Returns
    -------
    float
        The dot product of the two vectors.

    Examples
    --------

    Compute the dot product of two lists:
    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> dot_product(a, b)
    32.0

    Compute the dot product of two tuples
    >>> a = (1, 2, 3)
    >>> b = (4, 5, 6)
    >>> dot_product(a, b)
    32.0

    Compute the dot product of two numpy arrays:
    >>> a = np.array([1, 2, 3])
    >>> b = np.array([4, 5, 6])
    >>> dot_product(a, b)
    32.0
    """
    return float(np.dot(a, b))
