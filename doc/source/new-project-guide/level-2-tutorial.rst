Level 2. Reuse code across files
--------------------------------

In Level 1, you learned to use a block of code in a single file. Here, the goal is to resue the same code across multiple files.

Here is the project structure for this example:

.. code-block:: text

    my_project/
    ├── calculator.py
    ├── file_one.py
    └── file_two.py

In the ``calculator.py`` file, define a function called ``dot_product`` that takes two vectors as input and returns their dot product:

.. code-block:: python

    # calculator.py
    import numpy as np

    def dot_product(a, b):
        """Calculate the dot product of two vectors."""
        return np.dot(a, b)

For ``file_one.py`` and ``file_one.py``, you are able to import the function ``dot_product`` from the ``calculator.py`` file and use it in the same way as in Level 1. Here is the content of each file:

.. code-block:: python

    # file_one.py
    from calculator import dot_product

    v1 = [1, 2]
    v2 = [3, 4]
    print(dot_product(v1, v2))  # returns 11

    # file_two.py
    from calculator import dot_product

    v3 = [5, 6]
    v4 = [7, 8]
    print(dot_product(v3, v4))  # returns 83`

If you want to just import the module, you may also do this:

.. code-block:: python

    # file_one.py
    import calculator

    v1 = [1, 2]
    v2 = [3, 4]
    print(calculator.dot_product(v1, v2))  # returns 11

    # file_two.py
    import calculator

    v3 = [5, 6]
    v4 = [7, 8]
    print(calculator.dot_product(v3, v4))  # returns 83


If you have trouble running the code, ensure you follow the instructions in Level 1 on settin up a conda environment and installing the numpy package :ref:`here<_setup-up-conda-environment>`.