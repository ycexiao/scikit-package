Level 4. Reuse code across all files
------------------------------------

Overview
^^^^^^^^

In Level 3, you learned to reuse code across multiple projects. Here, you will learn to reuse code across all files on your local computer by turning your project into an installable Python package. Hence, Level 4 is also referred to as ``system``.

In Level 4, you will also learn to utilize GitHub. The first step is setting up ``Codecov`` and ``pre-commit CI`` in your GitHub repository via GitHub CI (continuous integration), which is essentially a set of scripts that run automatically when you push code to your GitHub repository.

``Codecov`` is a tool that reports the test coverage percentage change as a comment on each pull request. It helps you track the code coverage of your tests and provides a web interface to visualize the coverage data.

This way, you can also share your Python scripts as a zip file with your colleagues so that the code can be installed and reused on their computers.

This tutorial will take about 5 to 15 minutes.

Prerequisites
^^^^^^^^^^^^^

We assume you have at least hosted one project on GitHub. If you are new to GitHub, please refer to the FAQ guide on GitHub workflow.

.. include:: snippets/scikit-installation.rst

Initiate a project with ``scikit-package``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    package create system

Then it will ask you the following questions:

    :[1/6]: project_name (diffpy.my-project)

    :[2/6]: project_owner_github_username (sbillinge):

    :[3/6]: github_org (diffpy):

    :[4/6]: github_repo_name (diffpy.my-project):

    :[5/6]: conda_pypi_package_dist_name (diffpy.my-project):

    :[6/6]: package_dir_name (diffpy.my_project):

.. include:: snippets/naming-practice-namespace.rst

``cd`` into the project directory created by the ``package create`` command above:

.. code-block:: bash

    cd <project-name>

Check folder structure
^^^^^^^^^^^^^^^^^^^^^^

When you ``cd`` into the new directory, you will see a folder structure as shown below:

.. code-block:: text

     diffpy.my_project/
        ├── README.rst
        ├── environment.yml
        ├── pyproject.toml
        ├── requirements
        │   ├── README.txt
        │   ├── conda.txt
        │   ├── pip.txt
        │   └── test.txt
        ├── src
        │   └── diffpy
        │       ├── __init__.py
        │       └── my_project
        │           ├── __init__.py
        │           └── calculator.py
        └── tests
            └── test_calculator.py

.. include:: new-project-guide/level-4-5-shared-install-tests-host.rst

Merge your pull request!

What's next?
^^^^^^^^^^^^

Now that you have learned to reuse code across all files on your local computer, it's time to learn how to share your code with others as a publicly installable package that is hosted on PyPI and conda-forge. In Level 5, we will do that!
