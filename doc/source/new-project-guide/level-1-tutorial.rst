Level 1. Reuse code within a file
---------------------------------

This is the simplest level of reusing code. For this tutorial, let's assume you have a function called ``dot_product`` which calculates the dot product of two vectors using NumPy. Here is the folder structure for this example:

.. code-block:: text

    my_project/
    └── calculator.py

In the ``calculator.py`` file, define a function called ``dot_product`` that takes two vectors as input and returns their dot product:

.. code-block:: python

    # calculator.py
    import numpy as np

    def dot_product(a, b):
        """Calculate the dot product of two vectors."""
        return np.dot(a, b)

Below, let's reuse the function within the same file:

.. code-block:: python

    # Reusing the function within the same file
    v1 = [1, 2]
    v2 = [3, 4]
    print(dot_product(v1, v2))  # returns 11

    v3 = [5, 6]
    v4 = [7, 8]
    print(dot_product(v3, v4))  # returns 83

Then run ``python calculator.py`` in the command-line tool. You should see the outputs of 11 and 83 printed.

Here is the full content of the ``calculator.py`` file:

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

.. _setup-up-conda-environment:

Are you having trouble running the code?

.. note::

    For those who are not familiar with Python, ensure you have ``numpy`` installed by running ``pip install numpy`` or ``conda install numpy`` in your command-line tool.

    If your code still does not run, please ensure conda is installed on your local computer. conda is an open-source package and environment management system that allows you to create isolated environments to install software, including Python and its packages. The instructions for conda installation can be found at https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html.

    Once you have conda installed on your computer, run the following commands:

    .. code-block:: bash

        # Create a new environment, specify the Python version, and install packages
        conda create -n <project-name>_env

        # Activate the environment
        conda activate <project-name>_env

        # Install numpy
        conda install numpy

        # Run the script
        python calculator.py
