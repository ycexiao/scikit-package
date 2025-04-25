Level 1. Reuse code within a file
---------------------------------

Overview
^^^^^^^^

By the end of the tutorial, you will be able to reuse code within a file by creating a function. This is the first step in reusing code in Python. You will learn how to create a function and call it multiple times within the same file.

Prerequisites
^^^^^^^^^^^^^

We assume you have a basic understanding of executing a Python script in a command-line tool. We also assume that you have used the ``numpy`` Python library.


Folder structure
^^^^^^^^^^^^^^^^

Here is the folder structure for this example:

.. code-block:: text

    my_project/
    └── example_code.py

Example code
^^^^^^^^^^^^

In the ``example_code.py`` file, define a function called ``dot_product`` that takes two vectors as input and returns their dot product:


.. code-block:: python

    # example_code.py
    import numpy as np

    def dot_product(a, b):
        """Calculate the dot product of two vectors."""
        return np.dot(a, b)

In the same file, copy and paste the block of code below to reuse the function ``dot_product``.

.. code-block:: python

    # Reusing the function within the same file
    v1 = [1, 2]
    v2 = [3, 4]
    print(dot_product(v1, v2))  # returns 11

    v3 = [5, 6]
    v4 = [7, 8]
    print(dot_product(v3, v4))  # returns 83

Install ``numpy`` by running:

.. code-block:: bash

    pip install numpy

Then run

.. code-block:: bash

    python example_code.py

You should see the outputs of 11 and 83 printed.

Here is the full content of the ``example_code.py`` file:

.. code-block:: python

    import numpy as np

    def dot_product(a, b):
        """Calculate the dot product of two vectors."""
        return np.dot(a, b)

    # Reusing the function within the same file
    v1 = [1, 2]
    v2 = [3, 4]
    print(dot_product(v1, v2))  # returns 11

    v3 = [5, 6]
    v4 = [7, 8]
    print(dot_product(v3, v4))  # returns 83


Are you having trouble running the code?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

    For those who are not familiar with Python, ensure you have ``numpy`` installed by running ``pip install numpy`` or ``conda install numpy``.

    If your code still does not run, we recommend setting up a conda environment. conda is an open-source package and environment management software that allows you to create isolated environments to install software, including Python and its packages. The instructions for conda installation can be found at https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html.

    Once you have conda installed on your computer, run the following commands:

Once you have conda installed on your computer, run the following commands:

.. include:: snippets/conda-env-setup-simple.rst

What's next?
^^^^^^^^^^^^

You may proceed to Level 2 below. You will learn to share the ``doc_product`` across multiple Python files and modules.
