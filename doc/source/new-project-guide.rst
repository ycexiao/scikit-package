:tocdepth: -1

.. index:: new-project-guide

.. _scikit-package-new-project-header:

<<<<<<< HEAD

==========================
Start a new Python project
==========================
Assume you have already followed a lightweight project with Level-4, which turns a project into a lightweight locally installable Python package.

Here, you will learn how to create a new project with ``scikit-package`` that not only builds new packages but also uses GitHub CI to release your package to PyPI and conda-forge.

Prerequisites
-------------

Level 5 assumes you are familiar with ``pre-commit``, GitHub workflows, and GitHub CI. If you are not familiar with these, we recommend starting from Level 3 and progressing sequentially to Level 4.

There are 5 levels of reusing code. Here is an overview for each level:

<<<<<<< HEAD
Start a new project with ``scikit-package``
-------------------------------------------

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

If you are familiar with Python, we recommend you to start with level 3, where you get to create a project with ``scikit-package`` and also utilize automated linting features and tests folder setup which are useful for sharing codes or uploading your code via GitHub.

Here is the structure. We will go through each file and folder.

.. code-block:: text

    ├── AUTHORS.rst
    ├── CHANGELOG.rst
    ├── CODE_OF_CONDUCT.rst
    ├── LICENSE.rst
    ├── MANIFEST.in
    ├── README.rst
    ├── doc
    ├── news
    ├── pyproject.toml
    ├── requirements
    ├── src
    └── tests

There are some important files and folders you need to pay attention to.

:CHANGELOG.rst: The list of changes made to the package for each version released. When a new release is created, the changelog is automatically updated.
:/doc: The Sphinx documentation folder. The documentation will be built locally first and then automatically built and hosted on GitHub Pages when a new release is created.
:/news: The folder where you will put news items for each pull request. The news items are then automatically compiled into the CHANGELOG.rst when a new release is created.

We will go through the important files and folders with examples together.

Install the package Locally
---------------------------

As we did in Level 4, we will install the package and run the code and tests.

.. code-block:: bash

    pip install -e .

.. note::

    The above command will install all the packages listed in the ``requirements/pip.txt`` file.

Ensure your package is installed correctly by running:

.. code-block:: bash

    pip list

Run the tests locally
---------------------

Install the test requirements.

.. code-block:: bash

    conda install --file requirements/test.txt

Run the tests with ``pytest``. The test files are located in the ``tests`` folder.

.. code-block:: bash

    pytest

Build documentation docally
---------------------------

To reload the HTML file each time you save a change, you can install the ``sphinx-autobuild`` package: ::

    pip install sphinx-reload

Then run the command:

.. code-block:: bash

    sphinx-reload doc

Automate formatting with ``pre-commit`` locally
-----------------------------------------------

Initialize the ``.git`` folder in your project folder:

.. code-block:: bash

    git init
    git checkout -b new-project
    git add README.rst

Install ``pre-commit``: ::

    conda install pre-commit

Run ``pre-commit`` hooks manually and lint the code in the project folder:

.. code-block:: bash

    pre-commit run --all-files

You are now ready to host your project on GitHub, either as a public or private repository.

.. include:: snippets/github-host-project.rst

Automate ``pre-commit`` locally before commit
---------------------------------------------

You want to ensure ``pre-commit`` hooks are automatically running. One of the important features is preventing you from making commits directly to the ``main`` branch.

Set up the ``pre-commit`` hooks by running the command:

.. code-block:: bash

    pre-commit install

If you attempt to push your code to the ``main`` branch, it will prevent you from doing so.

If you want to remove one of the hooks, you can delete the following block in the ``.pre-commit-config.yaml`` file. For example, you can remove the hook that prevents making commits to the ``main`` branch:

.. code-block:: yaml

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: no-commit-to-branch
        name: Prevent Commit to Main Branch
        args: ["--branch", "main"]
        stages: [pre-commit]

.. note::

    If you are working on a public repository, we highly recommend that you develop your code via pull requests.

Setup GitHub Actions CI
------------------------

(Wait for the PR to be merged. Just copy and paste that section)


Add news item for each PR
--------------------------

.. include:: snippets/news-file-format.rst

.. include:: new-project-guide/level-1-tutorial.rst

.. include:: new-project-guide/level-2-tutorial.rst

.. include:: new-project-guide/level-3-tutorial.rst

.. include:: new-project-guide/level-4-tutorial.rst


.. .. include:: snippets/scikit-installation.rst

.. scikit-package main workflow
.. ----------------------------

.. 1. Type ``package create`` inside the project directory.

.. 2. Answer the questions as the following -- note that (default) means to hit enter without modifying anything:

.. .. include:: snippets/package-create-user-inputs.rst

.. Host your new project on GitHub
.. -------------------------------

.. #. Make sure you have a GitHub account.

.. #. Visit ``https://github.com/new``.

.. #. Choose the ``Owner`` and enter the ``Repository name`` and the ``Description``.

.. #. Set ``none`` under ``Add .gitignore`` and ``Choose a licenese``. We will use the ones generated by ``scikit-package``.

.. #. Click the ``Create repository`` to green button to create the repository.

.. #. You will have ``https://github.com/<OWNER>/<project-name>`.

.. #. Initialize the repository ::

..     git init
..     git remote add origin https://github.com/bobleesj/test-package.git
..     git add .
..     git commit -m "skpkg: start a new project with scikit-package"
..     git branch -M main
..     git push --set-upstream origin main
