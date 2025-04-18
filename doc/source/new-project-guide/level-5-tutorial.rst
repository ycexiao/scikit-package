
Level 5. Share code as public package
-------------------------------------



Prerequisites
^^^^^^^^^^^^^^

Here, you will learn how to create a new project with ``scikit-package`` that not only builds new packages but also uses GitHub CI to release your package to PyPI and conda-forge.

Level 5 assumes you are familiar with ``pre-commit``, GitHub workflows, and GitHub CI. If you are not familiar with these, we recommend starting from Level 3 and progressing sequentially to Level 4.


.. include:: snippets/scikit-installation.rst


Overview
^^^^^^^^

There are 5 levels of reusing code. Here is an overview for each level:

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

Install the package locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As we did in Level 4, we will install the package and run the code and tests.

.. code-block:: bash

    pip install -e .

.. note::

    The above command will install all the packages listed in the ``requirements/pip.txt`` file.

Ensure your package is installed correctly by running:

.. code-block:: bash

    pip list

Run the tests locally
^^^^^^^^^^^^^^^^^^^^^^

Install the test requirements.

.. code-block:: bash

    conda install --file requirements/test.txt

Run the tests with ``pytest``. The test files are located in the ``tests`` folder.

.. code-block:: bash

    pytest

Build documentation docally
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To reload the HTML file each time you save a change, you can install the ``sphinx-autobuild`` package: ::

    pip install sphinx-reload

Then run the command:

.. code-block:: bash

    sphinx-reload doc

Automate formatting with ``pre-commit`` locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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



.. include:: snippets/news-file-format.rst

Setup GitHub Actions CI
^^^^^^^^^^^^^^^^^^^^^^^

.. include:: snippets/pre-commit-codecov-github-setup.rst