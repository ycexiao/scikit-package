Level 4. Reuse code across all files
------------------------------------

First, you need to create a new conda environment. You can do this by running the following command in your terminal:

.. code-block:: bash

    conda create -n <project-name>_env scikit-package
    conda activate <project-name>_env

Initiate a project
^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    package create system


Then it will ask you the following questions:

    [1/6] project_name (diffpy.my-project):

    [2/6] project_owner_github_username (sbillinge):

    [3/6] github_org (diffpy):

    [4/6] github_repo_name (diffpy.my-project):

    [5/6] conda_pypi_package_dist_name (diffpy.my-project):

    [6/6] package_dir_name (diffpy.my_project):


.. important::

    Use lowercase letters with each space separated by ``"-"``. This naming practice is recommended by GitHub and PyPI. ``"_"`` is used for ``package_dir_name``, which is the name for importing the package in Python.


``cd`` into the project directory created by the ``package create`` command above:

.. code-block:: bash

    cd <project-name>

You will then have a folder structure as shown below.

.. code-block:: text

     diffpy.utils/
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
        │       └── utils
        │           ├── __init__.py
        │           └── calculator.py
        └── tests
            └── test_calculator.py

Install package
^^^^^^^^^^^^^^^

The goal is to reuse the code in ``calculator.py`` across all files in the project. First, you need to build and install the package locally.

.. code-block:: bash

    pip install -e .

It also installs the dependencies listed in ``requirements/pip.txt``. The ``-e`` flag indicates that you want to install the package in "editable" mode, which means that any changes you make to the source code will be reflected immediately without needing to reinstall the package. This is useful for development purposes.

Ensure the package is installed by running the following command:

Check installation
^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip list

You will see the package name in one of the lines in the output.


Run tests
^^^^^^^^^

Install the testing dependencies that are required for testing.

.. code-block:: bash

    pip install -r requirements/test.txt

Then, run the tests using the following command:

.. code-block:: bash

    pytest tests

It should pass. That means the scripts located under ``tests`` are able to import the installed package.


Reuse code across any files
^^^^^^^^^^^^^^^^^^^^^^^^^^^

It's time to use the code across any file. Create a Python file anywhere on your computer. Then, simply import the package and use the function ``dot_product`` defined in ``calculator.py``. Here is an example of how to do this:

.. code-block:: python

    # any python file
    from diffpy.utils import calculator

    v1 = [1, 2]
    v2 = [3, 4]
    print(calculator.dot_product(v1, v2))  # returns 11

Use ``pre-commit`` to format code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Then, feel free to run ``pre-commit`` to automate your code formatting manually by following the instructions provided at the end of Level 3 :ref:`here<pre-commit-manual>`.


(optional) Automate running pre-commit when a new git commit is attempted
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While you can run ``pre-commit`` manually, it is also possible to have these ``pre-commit`` hooks run automatically when you make a commit.


.. note::

    Here, we assume you are familiar with the general GitHub workflow. If you are not, please refer to the FAQ guide on GitHub workflow.

First, ensure that git is initialized in your project folder. You can do this by running the following command:

.. code-block:: bash

    git init
    git add .

Then ensure that ``pre-commit`` is run automatically before a new commit is made:

.. code-block::

    pre-commit install

You can set it up as follows by first initializing the git repository and then running the following commands:

.. code-block:: bash

    git commit -m "Test pre-commit hooks"

This attempts to first run all the hooks defined in the ``.pre-commit-config.yaml`` file. If any of the hooks fail, the commit will be aborted, and you will need to fix the issues before trying to make a commit again.

To double check that the previous commit was successful, you can run the following command:

.. code-block:: bash

    git log


(optional, important) Set up ``pre-commit CI`` in your GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you maintain a project from multiple contributorss, you want to ensure the codebase always passes ``pre-commit`` hooks defined in ``.pre-commit-config.yaml``. Often, external contributors may not have ``pre-commit`` installed locally and attempt to create a pull request (PR).

The ``pre-commit-CI`` app installed in the GitHub repository will first try to lint and format the code in the PR, and then check against the hooks again. If any of the hooks fail, it wilgl clearly mark the pull request with a failed check.

Please see Appendix 1 below on how to set up ``pre-commit CI`` in your GitHub repository.

(optional) Set up ``Codecov`` in your GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Codecov is a tool that helps you track the code coverage of your tests. It provides a web interface to visualize the coverage data and can be integrated with GitHub Actions to automatically upload coverage reports after running tests. This is important because when a new feature is requested, we want to ensure the contributor writes tests. If no tests are written for the new code, it will result in failed checks. See Appendix 2 below on how to set up ``Codecov`` in your GitHub repository.

.. include:: snippets/pre-commit-codecov-github-setup.rst
