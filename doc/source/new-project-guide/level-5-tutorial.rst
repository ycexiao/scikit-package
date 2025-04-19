Level 5. Share code as public package
-------------------------------------

Overview
^^^^^^^^

Here you will learn how to use GitHub CI to release your package to PyPI and conda-forge.

What's the difference between level 4 and level 5?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For completeness, we will repeat the steps from Level 4 from installing ``scikit-package``, hosting your project on GitHub, and setting up ``pre-commit CI`` and ``Codecov`` via GitHub Actions.

If you are not ready to share your code with the world, we recommend you continue developing code in Level 4 and conitnue to beneift the simple strcutre. 

Here are a few powertful extra features of Level 5:

- Build documentation locally with Sphinx with liveloading.
- Build and host documentation on GitHub Pages with public URL
- Use GitHub tag to release your package to to GitHub and PyPI
- Use PyPI's uploaded source code to create conda-forge package

Create a new project with ``scikit-package``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: snippets/package-public-user-inputs.rst

Check folder structure
^^^^^^^^^^^^^^^^^^^^^^^

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



.. include:: snippets/naming-practice-namespace.rst

.. include:: new-project-guide/level-4-5-shared-install-tests-host.rst

.. note:: 
    
    What is Codecov? 
    
        Codecov is a tool that helps you track the code coverage of your tests. It provides a web interface to visualize the coverage data and can be integrated with GitHub Actions to automatically upload coverage reports after running tests on each PR.

    Where is the code for ``tests-on-PR``?

        The code for the ``tests-on-PR`` GitHub Action is located in the ``.github/workflows`` directory of your GitHub repository. It is a YAML file that defines the workflow for running tests on pull requests. The workflow is triggered whenever a pull request is opened or updated, and it runs the tests using pytest and uploads the coverage report to Codecov.

Add news items in your pull request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We require that each PR includes a news item of ``<branch-name>.rst`` file under the ``news`` directory. 

#. Create a copy of  ``news/TEMPLATE.rst``.
#. Name the file as ``news/<branch-name>.rst``. e.g., ``news/skpkg-proj.rst``.
#. Do not delete ``news/TEMPLATE.rst``. Leave as it is.
#. Do not modify other section headers in the rst file. Replace ``* <news item>`` with your news item.
#. Check this example PR containing the news file: https://github.com/Billingegroup/scikit-package/pull/299/files
#. ``git add news/skpkg-proj.rst`` and ``git commit -m "chore: Add news item"``

How do you write coomand news file and commit messages?

    For news news, check the guidelines :ref:`here<faq-news-item-practice>`.

    For commit messages, check the guidelines :ref:`here<faq-github-commit-issue-practice>`.


Setup GitHub Actions CI
^^^^^^^^^^^^^^^^^^^^^^^

.. include:: snippets/pre-commit-codecov-github-setup.rst
