Install your package locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The goal is to reuse the code in ``calculator.py``. First, you need to build and install the package locally.

.. code-block:: bash

    pip install -e .

What is the ``-e`` flag?

    ``pip install`` will also install the dependencies listed in ``requirements/pip.txt``. The ``-e`` flag indicates that you want to install the package in "editable" mode, which means that any changes you make to the source code will be reflected immediately without needing to reinstall the package. This is useful for development purposes.

Check that the package is installed in the conda environment:

.. code-block:: bash

    pip list

Notice your package name in one of the lines in the output.

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

Host your project on GitHub
^^^^^^^^^^^^^^^^^^^^^^^^^^^

As we have done in Level 3, ``pre-commit`` is a tool that helps you automatically format your code and check for common issues before committing changes to your Git repository.

``pre-commit`` works with Git/GitHub. So, let's first host your project on GitHub.

#. Visit ``https://github.com/new``.

#. Choose the ``Owner`` and enter the ``Repository name`` and the ``Description``.

#. Check ``Add a README file``.

#. Set ``none`` under ``Add .gitignore``.

#. Set ``none`` under ``Choose a license``.

#. Click the ``Create repository`` green button to create the repository.

Push your code to GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash
    git init
    git remote add origin https://github.com/<OWNER>/<project-name>.git
    git pull origin main

Notice that you have pulled the code from the ``remote main branch``, which is the ``README.md`` file that was created. We will use ``README.rst`` instead, so let's delete the ``README.md`` file.

.. code-block:: bash

    rm README.md

Create a new branch from the ``main`` branch.

.. code-block:: bash

    git checkout -b skpkg-proj

Configure ``pre-commit`` to run each time a new commit is made:

.. code-block:: bash
    
    pre-commit install

Let's now stage and commit the code.

.. code-block:: bash
    
    git add .
    git commit -m "skpkg: start a new project with skpkg system template"

If the hooks all pass, you will see the new commit in the git log:

.. code-block:: bash

    git log

Let's now push our code to the new ``skpkg-proj`` local branch and push to the remote ``skpkg-proj`` branch.

.. code-block:: bash

    git push --set-upstream origin skpkg-proj

Create a pull request from ``skpkg-proj`` to ``main``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Visit your GitHub repository.

#. Click on the green button that says ``Compare & pull request``.

#. The PR title can be ``skpkg: start a new project with skpkg system template``.

#. The ``base`` branch should be ``main`` and the ``compare`` branch should be ``skpkg-proj``.

#. Click on the ``Create pull request`` button.

#. Wait for ``Tests on PR`` to run. This is the GitHub Action that runs the ``pytest`` on each pull request.

#. Expect the ``Tests on PR`` to fail with a red check as expected. This is because we have not set up ``Codecov`` in GitHub yet.

#. Do not merge the pull request yet.

#. Follow the next section to set up ``Codecov`` in your GitHub repository.

.. note:: 
    
    What is Codecov? 
    
        Codecov is a tool that helps you track the code coverage of your tests. It provides a web interface to visualize the coverage data and can be integrated with GitHub Actions to automatically upload coverage reports after running tests on each PR.

    Where is the code for ``tests-on-PR``?

        The code for the ``tests-on-PR`` GitHub Action is located in the ``.github/workflows`` directory of your GitHub repository. It is a YAML file that defines the workflow for running tests on pull requests. The workflow is triggered whenever a pull request is opened or updated, and it runs the tests using pytest and uploads the coverage report to Codecov.

Setup Codecov token for GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: snippets/github-codecov-setup.rst

Now, let's set up ``pre-commit`` to run on each pull request as well.

Setup pre-commit CI in GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: snippets/github-pre-commit-setup.rst

Check pre-commit CI and Codecov work by sending an empty commit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since we have ``pre-commit CI`` and ``Codecov`` set up, let's attempt to activate the ``pre-commit CI`` by sending an empty commit to the ``skpkg-proj`` remote branch.

.. code-block:: bash

    git commit --allow-empty -m "ci: empty commit to test codecov/pre-commit CI setup"
    git push

Now, visit your GitHub repository and check the pull request. You should see the ``Codecov`` comment and the ``pre-commit CI`` check.


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
