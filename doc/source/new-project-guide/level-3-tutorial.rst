Level 3. Reuse code across projects
-----------------------------------

Unlike Levels 1 and 2, from Level 3 through Level 5, you will set up a working environment for your project with conda and use ``scikit-package`` to initiate a new project.

First, create a conda environment for your project and install ``scikit-package`` at the same time.

.. code-block:: bash

    conda create -n <project-name>_env scikit-package
    conda activate <project-name>_env

Initiate a project
^^^^^^^^^^^^^^^^^^

.. code-block:: bash

     package create workspace

You will then be asked to enter the ``project-name``. The default value is ``workspace_folder``.

``cd`` into the new directory created by the ``package create`` command above:

.. code-block:: bash

    cd <project-name>

You will then have a folder structure as shown below.

.. code-block:: text

     workspace_folder/
     ├── README.md
     ├── requirements.txt
     ├── calculator.py
     ├── proj_one
     │   ├── __init__.py
     │   └── reuse_code.py
     ├── proj_two
     │   ├── __init__.py
     │   └── reuse_code.py
     └── tests
          ├── __init__.py
          └── test_calculator.py

.. note::

     ``calculator.py`` is the template code where you can define functions that are imported across the project folders ``proj_one`` and ``proj_two``. The ``__init__.py`` files are required and empty files that indicate to Python that the directories contain Python modules.

     ``requirements.txt`` is the file where you list Python dependencies. The ``README.md`` file is where you add notes for your project. The ``tests`` folder contains tests for your reusable code.


Install dependencies
^^^^^^^^^^^^^^^^^^^^

You can install the dependencies listed in ``requirements.txt`` by running the following command:

.. code-block:: bash

    pip install -r requirements.txt


Run code
^^^^^^^^

It is not as simple as running ``python proj_one/reuse_code.py``. You need to set the ``PYTHONPATH`` environment variable to the current working directory. This is because the ``proj_one`` and ``proj_two`` folders are not in the same directory as the ``calculator.py`` file.

Type ``pwd`` in your command-line tool to see the current working directory.

.. code-block:: bash

     pwd

For example, for a macOS user, it will print something like this: ``/Users/macbook/downloads/dev/scikit-package/workspace_folder``.
Then, copy and paste the value into the ``PYTHONPATH`` environment variable.

.. code-block:: bash

    export PYTHONPATH="${PYTHONPATH}:<path-to-your-workspace-folder>"

For example, it could be something like this:

.. code-block:: bash

    export PYTHONPATH="${PYTHONPATH}:/Users/macbook/downloads/dev/scikit-package/workspace_folder"

Then, you can run the code by running:

.. code-block:: bash

    python proj_one/reuse_code.py
    python proj_two/reuse_code.py


Run tests
^^^^^^^^^

Notice that the ``tests`` folder contains a test file called ``test_calculator.py``. You can run the tests by running the following command:

.. code-block:: bash

    pytest tests/test_calculator.py

Or you can simply run:

.. code-block:: bash

     pytest

``pytest`` is a testing framework for Python. It will automatically discover and run all the test files in the ``tests`` folder.



.. _pre-commit-manual:

Automatic code formatting with ``pre-`commit``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You may want to format your code automatically. Notice that there is a file called ``.pre-commit-config.yaml`` in the root directory of your project. This file is used to configure pre-commit hooks, which are scripts that run automatically before you commit your code to Git. However, we are not using GitHub here, but we will just simply run the pre-commit hooks manually in Level 3 for simplicity.

To use ``pre-commit``, you need to install it first.

.. code-block:: bash

     pip install pre-commit

Then you can initialize a local Git folder in your project folder by running:

.. code-block:: bash

     git init

You are ready to format your code by running:

.. code-block:: bash

     pre-commit run --all-files

It will then show the following:

.. code-block:: text

     black....................................................................Passed
     prettier.................................................................Passed
     docformatter.............................................................Passed

.. note::

    ``black`` is a tool that automatically formats Python code to conform to the PEP 8 style guide. ``prettier`` is a tool that formats code in various languages, including ``.md``, ``.rst``, and ``.json`` files. ``docformatter`` is a tool that formats docstrings in Python code.


What's next?
^^^^^^^^^^^^

In Level 4, you will learn to set up this ``pre-commit`` with GitHub Actions to automatically format the code. Then, you will also learn to setup a **locally installabe package** that you don't have to manually set the ``PYTHONPATH`` environment variable.
