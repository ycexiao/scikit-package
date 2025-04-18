Level 4. Reuse code across all files
------------------------------------

Overview
^^^^^^^^

In Level 3, you learned to reuse code acorss multiple projects. Here, you will learn to reuse code across all files in your local computer by turning your project into an installable Python package. Hence, Level 4 is also referred to as ``system``.

This way, you can also share your Python scripts as a zip file with your colleagues so that the code can be installed and reused on their computers.

This tutorial will take about 5 to 15 minutes.

Prerequisites
^^^^^^^^^^^^^

We assume you have at least hosted one project on GitHub. If you are new to GitHub, please refer to the FAQ guide on GitHub workflow.

.. include:: snippets/scikit-installation.rst

Initiate a project with ``scikit-package``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    package create system

Then it will ask you the following questions:

    :[1/6]: project_name (diffpy.my-project)

    :[2/6]: project_owner_github_username (sbillinge):

    :[3/6]: github_org (diffpy):

    :[4/6]: github_repo_name (diffpy.my-project):

    :[5/6]: conda_pypi_package_dist_name (diffpy.my-project):

    :[6/6]: package_dir_name (diffpy.my_project):

Please follow the naming practices recommended by PyPI and GitHub:

.. important::

    Use lowercase letters with each space replaced by ``"-"``. The only instance where an underscore ``"_"`` is for ``package_dir_name``. Underscores are ONLY ALLOWED for importing the package in Python. For example, if you set the ``package_dir_name`` as ``diffpy.my_project``, you will be able to import the package using ``import diffpy.my_project``.

Do you want to import your package with the identifier (group name, organization name) attached, like in ``import <org-name>.<project-name>``.

.. note::

    If you want to be able to ``import diffpy.pdffit``, all you need to do is set the ``project_name`` as ``diffpy.pdffit`` when you create a new project by running the command ``package create system``.

``cd`` into the project directory created by the ``package create`` command above:

.. code-block:: bash

    cd <project-name>


Folder structure
^^^^^^^^^^^^^^^^

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

Install package
^^^^^^^^^^^^^^^

The goal is to reuse the code in ``calculator.py``  First, you need to build and install the package locally.

.. code-block:: bash

    pip install -e .

What is the ``-e`` flag?

    ``pip instasll`` will also the dependencies listed in ``requirements/pip.txt``. The ``-e`` flag indicates that you want to install the package in "editable" mode, which means that any changes you make to the source code will be reflected immediately without needing to reinstall the package. This is useful for development purposes.

Check installation
^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip list

You will see the package name in one of the lines in the output.


Run tests
^^^^^^^^^

Install the testing dependencies that are required for testing.

.. code-block:: bash

    conda install --file requirements/test.txt

Then, run the tests using the following command:

.. code-block:: bash

    pytest

It should pass. That means the scripts located under ``tests`` are able to import the installed package. Great!

Reuse code across any files
^^^^^^^^^^^^^^^^^^^^^^^^^^^

It's time to use the code across any file. Create a Python file anywhere on your computer. Then, import your installed package and use the function ``dot_product`` defined in ``calculator.py``.

Here is an example of how to do this:

.. code-block:: python

    # any python file
    from diffpy.my_project import calculator

    v1 = [1, 2]
    v2 = [3, 4]
    print(calculator.dot_product(v1, v2))  # returns 11

Automate running ``pre-commit`` with git commit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As we have done in Level 3, ``pre-commit`` is a tool that helps you automatically format your code and check for common issues before committing changes to your Git repository.

In Level 3, we manually executed ``pre-commit`` with the following command ``pre-commit run --all-files``. This is useful for running the hooks on all files in your project, but it can be tedious to remember to do this every time you make a commit.

But ultimately, ``pre-committ`` works with Git/GitHub. So, let's first host your project on GitHub first.

.. include:: snippets/github-host-project.rst

Now that your project is hosted with the basic ``README.md`` hosted in the ``main`` branch, we now want to update the code using the pull request workflow instead of pushing the code directly to the ``main`` branch which is public facing and "the source of truth".

In your CLI, run

.. code-block:: bash

    git init
    pre-commit install
    git add .


Now, attempt to make a new commit. 

.. code-block:: bash
    
    git commit -m "skpkg: first commit"

You will see that the hook that prevents you pushing your code to ``main`` fails. This is a good sign! We do not want to directly push our code to ``main``.

.. code-block:: bash

    Prevent Commit to Main Branch............................................Failed
    - hook id: no-commit-to-branch
    - exit code: 1

Since one of the hooks failed, the commit is not created. You can confirm this by running the following command:

.. code-block:: bash

    git log


Now, attempt to make a new commit.

.. code-block:: bash

    git commit -m "Test pre-commit hooks"

This attempts to first run all the hooks defined in the ``.pre-commit-config.yaml`` file. If any of the hooks fail, the commit will be aborted, and you will need to fix the issues before trying to make a commit again.

To double check that the previous commit was successful, you can run the following command:

.. code-block:: bash

    git log

Set up ``pre-commit CI`` in your GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you maintain a project from multiple contributorss, you want to ensure the codebase always passes ``pre-commit`` hooks defined in ``.pre-commit-config.yaml``. Often, external contributors may not have ``pre-commit`` installed locally and attempt to create a pull request (PR).

The ``pre-commit-CI`` app installed in the GitHub repository will first try to lint and format the code in the PR, and then check against the hooks again. If any of the hooks fail, it wilgl clearly mark the pull request with a failed check.

Please see Appendix 1 below on how to set up ``pre-commit CI`` in your GitHub repository.

Set up ``Codecov`` in your GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Codecov is a tool that helps you track the code coverage of your tests. It provides a web interface to visualize the coverage data and can be integrated with GitHub Actions to automatically upload coverage reports after running tests. This is important because when a new feature is requested, we want to ensure the contributor writes tests. If no tests are written for the new code, it will result in failed checks. See Appendix 2 below on how to set up ``Codecov`` in your GitHub repository.

.. include:: snippets/pre-commit-codecov-github-setup.rst
