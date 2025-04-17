:tocdepth: -1

.. index:: getting-started

.. _getting-started:

===============
Getting started
===============


Are you here to start a new Python project?
-------------------------------------------

There are 5 levels of reusing code. Here is a higher-level overview for each level:

.. list-table:: 5 levels of reusing/sharing code
   :widths: 5 15 40 40
   :header-rows: 1

   * - Level
     - Name
     - Scope
     - How to setup
   * - 1
     - ``function``
     - Reuse code in the single file.
     - (See tutorial)
   * - 2
     - ``module``
     - Reuse code across files.
     - (See tutorial)
   * - 3
     - ``workspace``
     - Reuse code across project folders.
     - ``package create workspace``
   * - 4
     - ``system``
     - Reuse code across any files in the computer.
     - ``package create system``
   * - 5
     - ``public``
     - Share code as publicly installable package.
     - ``package create public``

Please read the Level 1 tutorial. 

Level 1. Reuse code in a single file
------------------------------------

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

Are you having trouble running the code?
----------------------------------------

For those who are not familiar with Python, ensure you have ``numpy`` installed by running ``pip install numpy`` or ``conda install numpy`` in your command-line tool. 

If your code still does not run, please ensure Conda is installed on your local computer. Conda is an open-source package and environment management system that allows you to create isolated environments to install software, including Python and its packages. The instructions for Conda installation can be found at https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html.

Once you have Conda installed on your computer, run the following commands:

.. code-block:: bash

    # Create a new environment, specify the Python version, and install packages
    conda create -n <project-name>_env

    # Activate the environment
    conda activate <project-name>_env

    # Install numpy
    conda install numpy

    # Run the script
    python calculator.py


Are you here to standardize your Python project with scikit-package?
--------------------------------------------------------------------

1. Do you want to standardize your project with ``scikit-package``? Please follow the full instructions :ref:`here <scikit-package-header>`.

2. You already have a scikit project. Do you want to use the latest version of ``scikit-package`` to re-standard your project? Please follow the instructions in :ref:`here <scikit-package-workflow-main>`.



Level 2. Reuse code across multiple files
-----------------------------------------




Are you here to create a new release?
-------------------------------------

Do you want to release your project to ``GitHub``, ``PyPI``, and ``conda-forge`` by creating a tag to your GitHub repository? Start from :ref:`here <release-guide>`.