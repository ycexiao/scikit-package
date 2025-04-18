Level 3. Reuse code across projects
-----------------------------------


Overview
^^^^^^^^^

The goal in Level 3 to reuse code across multiple projects. Hence the name associated with this level is ``workspace``. Each project could have many files that would like to utilize the reusable code.

Also, you will learn execute and write **unit tests** for your reusable code. Unit tests are small, isolated tests that verify the functionality. They help ensure that your code behaves as expected and can catch bugs early in the development process You might want to run them before you share code with others or deploy to more projects.

Lastly, you will also learn to **automate formatting** to keep you code clean and consistent so that others, including you, can also save time reading and adding new code.

This tutorial will take about 3-10 minutes.

.. include:: snippets/scikit-installation.rst

Initiate a new project with ``scikit-package``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a new project by running the following command:

.. code-block:: bash

     package create workspace

You will then be asked to enter the ``project-name``. The default value is ``workspace_folder``.

``cd`` into the new directory created by the ``package create workspace`` command above:

.. code-block:: bash

    cd <project-name>


Folder structure
^^^^^^^^^^^^^^^^

When you ``cd`` into the new directory, you will see a folder structure as shown below:

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

Please take a look at those files created with your favorite IDE software (e.g., Visual Studio Code, PyCharm, etc.).

See the descriptions below for each file created in the project:

.. note::

     ``calculator.py`` is an example module where you can define functions that are imported across the project folders ``proj_one`` and ``proj_two``. The ``__init__.py`` files are required and empty files that indicate to Python that the directories contain Python modules.

     ``requirements.txt`` is the file where you list Python dependencies. The ``README.md`` file is where you add notes for your project. The ``tests`` folder contains tests for your reusable code.


Install dependencies
^^^^^^^^^^^^^^^^^^^^

You can install the dependencies like ``numpy``  listed in ``requirements.txt`` by running the following command:

.. code-block:: bash

    pip install -r requirements.txt

Set PYTHONPATH
^^^^^^^^^^^^^^^

When code shared across nested different folders, you need to set the ``PYTHONPATH`` environment variable to the current working directory.

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
    python proj_two/reuse_code.py


Run tests
^^^^^^^^^^

Notice that the ``tests`` folder contains a test file called ``test_calculator.py``. You can run the tests by running the following command:

.. code-block:: bash

    pytest tests/test_calculator.py

Or you can simply run:

.. code-block:: bash

     pytest

.. note ::

     ``pytest`` is a testing framework for Python. It will automatically discover and run all the test files in the ``tests`` folder.

.. _pre-commit-manual:

Automatic code formatting with ``pre-`commit``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Notice that there is a hidden file called ``.pre-commit-config.yaml`` in the root directory. This file is used to configure pre-commit "hooks". These hooks are checks that are can be automatically executed when you commit your code to Git, which you will do in Level 4.

In Level 3, you will run these hooks manually for simplicity.

Recall ``pre-commit`` has been already installed in the environment in the previous stage.

Since ``pre-commit`` is meant to work with ``Git``, create a local Git folder in your project folder by running:

.. code-block:: bash

     git init

.. note::

     If you don't understand Git/GitHub, don't worry. For Level 3, it's not needed although it will be used in Level 4 where you will host your code on GitHub and use GitHub's to run these ``pre-commit`` automatically.

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


What's next?
^^^^^^^^^^^^

Notice that it's quite annoying to set ``PYTHONPATH`` every time you open a new terminal. In Level 4, you will learn how to set it permanently by turning your softwarwe into a locally installed package. You will also learn to use ``Git`` and ``GitHub`` to host your code online and share it with others and also enjoy the benefits of ``pre-commit`` hooks and other automatic ``tests`` done not locally but also on GitHub's remote server known as "GitHub Actions".

We highly recommend you are familiar with Git/GitHub before proceeding to Level 4. Feel free to check out our GitHub workflow guide on FAQ :ref:`here<faq-github-workflow>`.
