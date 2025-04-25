Level 3. Reuse code across projects
-----------------------------------


Overview
^^^^^^^^^

The goal in Level 3 is to reuse code across multiple projects. Hence, the name associated with this level is ``workspace``. Each project could have many files that would utilize the reusable code.

Also, you will learn to execute and write **unit tests** for your reusable code. Unit tests are small, isolated tests that verify functionality. They help ensure that your code behaves as expected and can catch bugs early in the development process. You might want to run them before sharing code with others or deploying it to more projects.

Lastly, you will also learn to **automate formatting** to keep your code clean and consistent so that others, including you, can save time reading and adding new code.

This tutorial will take about 3-10 minutes.

.. include:: snippets/scikit-installation.rst

Initiate a new project with ``scikit-package``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a new project by running the following command:

.. code-block:: bash

     package create workspace

You will then be asked to enter the ``project-name``. The default value is ``workspace-folder``.
In this example, enter ``data-analysis-project`` as the workspace folder you are about to create.

.. code-block:: bash

     [1/1] workspace_name (workspace-folder): data-analysis-projects

``cd`` into the new directory created by the ``package create workspace`` command above:

.. code-block:: bash

    cd data-analysis-project

Folder structure
^^^^^^^^^^^^^^^^^

When you ``cd`` into the new directory, you will see a folder structure as shown below:

.. code-block:: text

     data-analysis-project/
     ├── README.md
     ├── requirements.txt
     ├── shared_functions.py
     ├── proj-one
     │   ├── __init__.py
     │   └── proj_one_code.py
     └── tests
          ├── __init__.py
          └── test_shared_functions.py

If you would like to add more projects, you can create a new folder under the root directory. For example, you can create a folder called ``proj-two`` and add your code there. This can be extrapolated for as many projects as you like:

.. code-block:: bash

     mkdir proj-two
     cd proj-two
     touch __init__.py
     touch proj_two_code.py


File descriptions
^^^^^^^^^^^^^^^^^^

Now that the folder structure is created, let's go through the files and folders in the project:

- ``README.md`` is a markdown file for project documentation. Typically, it includes a project description, installation instructions, and usage examples. You can edit this file to add your own project information.


- ``shared_functions.py`` is where you define reused code. It includes the following example function to help demonstrate the concept of shared functions. In your project, this is where you would add the code you want to reuse:

.. code-block:: python

     # shared_functions.py
     import numpy as np


     def dot_product(a, b):
          """Calculate the dot product of two vectors."""
          return np.dot(a, b)

- ``proj_one/proj_one_code.py`` shows an example of how to import and use the ``dot_product()`` function from ``shared_functions.py``:

.. code-block:: python

     # proj_one_code.py
     import shared_functions

     a = [1, 2, 3]
     b = [1, 2, 3]
     result = shared_functions.dot_product(a, b)
     print(result)

- ``__init__.py`` files mark directories as Python modules. These are empty by default at this level.

- ``requirements.txt`` lists your project's dependencies, which in this case includes ``numpy`` and ``pytest``:

.. code-block:: python

     # requirements.txt
     numpy
     pytest

- The ``tests`` folder contains tests for your shared functions. For example, ``test_shared_functions.py`` includes tests for the ``dot_product`` function using ``pytest``. General naming convention for test files is ``test_<module_name>.py``. Similarly, test function names should be ``test_<function_name>()``. This is how ``pytest`` recognizes them as test functions:


.. code-block:: python

     # test_shared_functions.py
     import numpy as np
     import pytest
     import shared_functions


     def test_dot_product_2D_list():
     a = [1, 2]
     b = [3, 4]
     expected = 11.0
     actual = shared_functions.dot_product(a, b)
     assert actual == expected


     def test_dot_product_3D_list():
     a = [1, 2, 3]
     b = [4, 5, 6]
     expected = 32.0
     actual = shared_functions.dot_product(a, b)
     assert actual == expected


     @pytest.mark.parametrize(
     "a, b, expected",
     [
          # Test whether the dot product function works with 2D and 3D vectors
          # C1: lists, expect correct float output
          ([1, 2], [3, 4], 11.0),
          ([1, 2, 3], [4, 5, 6], 32.0),
          # C2: tuples, expect correct float output
          ((1, 2), (3, 4), 11.0),
          ((1, 2, 3), (4, 5, 6), 32.0),
          # C3: numpy arrays, expect correct float output
          (np.array([1, 2]), np.array([3, 4]), 11.0),
          (np.array([1, 2, 3]), np.array([4, 5, 6]), 32.0),
     ],
     )
     def test_dot_product(a, b, expected):
     actual = shared_functions.dot_product(a, b)
     assert actual == expected

- ``.pre-commit-config.yaml`` is a configuration file for pre-commit hooks. This file is described in further detail below.


Install dependencies
^^^^^^^^^^^^^^^^^^^^

You can install the dependencies like ``numpy`` listed in ``requirements.txt`` by running the following command:

.. code-block:: bash

    pip install -r requirements.txt

Set PYTHONPATH
^^^^^^^^^^^^^^^

When code is shared across nested folders, you need to set the ``PYTHONPATH`` environment variable to the current working directory.

Type ``pwd`` in your command-line tool to see the current working directory.

.. code-block:: bash

     pwd

For example, for a macOS user, it will print something like ``/Users/macbook/downloads/dev/scikit-package/workspace_folder``.

Copy and paste the value while replacing ``<path-to-your-workspace-folder>`` with the path printed above.

.. code-block:: bash

    export PYTHONPATH="${PYTHONPATH}:<path-to-your-workspace-folder>"

For example, using the macOS example above, it would be:

.. code-block:: bash

    export PYTHONPATH="${PYTHONPATH}:/Users/macbook/downloads/dev/scikit-package/workspace_folder"

Run your code
^^^^^^^^^^^^^

Then, you can run the code by running:

.. code-block:: bash

    python proj_one/reuse_code.py


Run tests
^^^^^^^^^^

To run tests using ``pytest``, run the following command:

.. code-block:: bash

    pytest tests/test_calculator.py

Or you can simply run:

.. code-block:: bash

     pytest

.. note ::

     ``pytest`` is a testing framework for Python. It will automatically discover and run all the test files in the ``tests`` folder.

.. _pre-commit-manual:

Automatic code formatting with ``pre-commit``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Notice that there is a hidden file called ``.pre-commit-config.yaml`` in the root directory. This file is used to configure pre-commit "hooks". These hooks are checks that can be automatically executed when you commit your code to Git, which you will do in Level 4.

In Level 3, you will run these hooks manually for simplicity.

Recall ``pre-commit`` has already been installed in the environment in the previous stage.

Since ``pre-commit`` is meant to work with ``Git``, create a local Git folder in your project folder by running:

.. code-block:: bash

     git init
     git add .

.. note::

     If you don't understand Git/GitHub, don't worry. For Level 3, it's not needed, although it will be used in Level 4 where you will host your code on GitHub and use GitHub to run these ``pre-commit`` hooks automatically.

Format your code by running:

.. code-block:: bash

     pre-commit run --all-files

It will then show the following:

.. code-block:: text

     black....................................................................Passed
     prettier.................................................................Passed
     docformatter.............................................................Passed

.. note::

    ``black`` is a tool that automatically formats Python code to conform to the PEP 8 style guide. ``prettier`` is a tool that formats code in various languages, including ``.md``, ``.rst``, and ``.json`` files. ``docformatter`` is a tool that formats docstrings in Python code.

Run ``pre-commit run --all-files`` frequently while developing code.

What's next?
^^^^^^^^^^^^

Notice that it's quite annoying to set ``PYTHONPATH`` every time you open a new terminal. In Level 4, you will learn how to set it permanently by turning your software into a locally installed package. You will also learn to use ``Git`` and ``GitHub`` to host your code online and share it with others and also enjoy the benefits of ``pre-commit`` hooks and other automatic ``tests`` done not locally but also on GitHub's remote server known as "GitHub Actions".

We highly recommend you become familiar with Git/GitHub before proceeding to Level 4. Feel free to check out our GitHub workflow guide in the FAQ :ref:`here<faq-github-workflow>`.
