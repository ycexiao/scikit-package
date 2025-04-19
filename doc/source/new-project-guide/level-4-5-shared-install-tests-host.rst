





Setup Codecov token for GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: snippets/github-codecov-setup.rst

Now, let's set up ``pre-commit`` to run on each pull request as well.

Check requirements
^^^^^^^^^^^^^^^^^^^

Check the ``pip.txt``, ``conda.txt``, and ``test.txt``, and ``doc.txt`` files under ``requirements``.

:pip.txt: list all PyPI packages required to install the package via `pip install <package-name>`.

:conda.txt: list all Conda packages required for running the package in GitHub CI. It should be typically identcal as the ``pip.txt`` file.

:test.txt: packages required for the testing suite to ensure all tests pass.

:docs.txt: packages required for building the package documentation page.

:build.txt: list all conda packages required for building the package in GitHub CI, including those specified in the build section of meta.yaml (conda-recipe).

.. note::

    Why is it required to list dependencies both under ``pip.txt`` and ``conda.txt``? Please refer to the FAQ section :ref:`here<faq-pip-conda-both-provided>`.
