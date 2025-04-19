Level 4. Reuse code across all files
------------------------------------

Overview
^^^^^^^^

In Level 3, you learned to reuse code across multiple projects. Here, you will learn to reuse code across all files on your local computer by turning your project into an installable Python package. Hence, Level 4 is also referred to as ``system``.

In Level 4, you will also learn to utilize GitHub

This tutorial will take about 10 to 15 minutes.

Prerequisites
^^^^^^^^^^^^^

We assume you have at least hosted one project on GitHub. If you are new to GitHub, please refer to the FAQ guide on GitHub workflow.

.. include:: snippets/scikit-installation.rst


Initiate a project with ``scikit-package``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Run the following command to create a new project with ``scikit-package``:

    .. code-block:: bash

        package create system

#. Anwer the following questions

    :project_name: (my-project)

    :github_org: (billingegroup)

    :github_repo_name: (my-project)

    :conda_pypi_package_dist_name: (my-project)

    :package_dir_name: (my_project)

    :project_owner_name: (Simon Billinge)


#. ``cd`` into the project directory created by the ``package create`` command above:

    .. code-block:: bash

        cd <project-name>

#. Done! Let's proceed to the next section to check the folder structure.

Check folder structure
^^^^^^^^^^^^^^^^^^^^^^

#. When you ``cd`` into the new directory, you will see a folder structure as shown below:

    .. code-block:: text

        my-package/
        ├── LICENSE.rst
        ├── README.rst
        ├── environment.yml
        ├── pyproject.toml
        ├── requirements
        │   ├── conda.txt
        │   ├── pip.txt
        │   └── test.txt
        ├── src
        │   └── my_pacakge
        │       ├── __init__.py
        │       └── calculator.py
        └── tests
            └── test_calculator.py

Install your package locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Build and install the package locally:

    .. code-block:: bash

        pip install -e .

    .. note:: What is the ``-e`` flag?

        ``pip install`` will also install the dependencies listed in ``requirements/pip.txt``. The ``-e`` flag indicates that you want to install the package in "editable" mode, which means that any changes you make to the source code will be reflected immediately without needing to reinstall the package. This is useful for development purposes.

#. Check your package is installed in the conda environment:

    .. code-block:: bash

        pip list

#. Done! Let's now run unit tests with the locally installed package.

Run tests with your locally installed package
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Install the testing dependencies for testing.

    .. code-block:: bash

        conda install --file requirements/test.txt

#. Then, run the tests using the following command:

    .. code-block:: bash

        pytest

#. Ensure tests all pass. 

#. Check that ``tests/test_calculator.py``. Notice you are importin the locally installed package.

#. Congratulations! Your package is now available for use in any Python script or Jupyter notebook in your local computer.

#. Done! Let's nov learn to use automate your code formatting locally.


Automatic code formatting with ``pre-commit``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Notice that there is a hidden file called ``.pre-commit-config.yaml`` in the root directory. This file is used to configure pre-commit "hooks". These hooks are checks that are can be automatically executed when you commit your code to Git.

.. note::

    If you are not familiar wtih Git/GitHub, don't worry. Here, we provide step-by-step instructions here.

#. Initilize a local Git repository in your project folder:

    .. code-block:: bash

        git init

#. Add your files to the local Git repository:

    .. code-block:: bash

        git add .

#. Format your code by running:

    .. code-block:: bash

        pre-commit run --all-files

#. Ensure that all of the checks pass.

    .. code-block:: text

        black....................................................................Passed
        prettier.................................................................Passed
        docformatter.............................................................Passed

    .. note::

        ``black`` is a tool that automatically formats Python code to conform to the PEP 8 style guide. ``prettier`` is a tool that formats code in various languages, including ``.md``, ``.rst``, and ``.json`` files. ``docformatter`` is a tool that formats docstrings in Python code.


#. Done! You have successfully formatted your code. But, let's also make sure these hooks are triggerd automatically when you make a commit.

Trigger pre-commit hooks automatically with Git commit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Configure ``pre-commit`` to run each time a new commit is made:

    .. code-block:: bash

        pre-commit install

#. Let's now stage and commit the code:

    .. code-block:: bash

        git add .
        git commit -m "skpkg: start a new project with skpkg system template"

#. Notice that the hooks all pass. You will see the new commit in the git log:

    .. code-block:: bash

        git log

    .. note::
        
        If one or more of the hooks fail, no commit will be made. But, ``pre-committ`` will automatically lint your code too. If this is the case, simply re-enter the same commit message again.

#. Done. Let's now push your code to GitHub which is a remote/cloud Git repository.

Create a new project on GitHub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Visit `https://github.com/new <https://github.com/new>`_

#. Choose and enter values for ``Owner`` and ``Repository name``.

#. Choose either ``Public`` or ``Private`` for the repository visibility.

#. Check ``Add a README file``.

#. Set ``None`` under ``Add .gitignore``.

#. Set ``None`` under ``Choose a license``.

#. Click the ``Create repository`` green button to create the repository.

#. Done. Let's push your code from your local Git repository to the remote GitHub repository.


Push your code to GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Setup the remote GitHub repository. Let's call this repository ``origin``, a common name for the remote repository.

    .. code-block:: bash

        git remote add origin https://github.com/<OWNER>/<project-name>.git
        

#. Pull the code from the remote ``main`` branch. Recall we had ``README.md`` file created.

    .. code-block:: bash
        
        git pull origin main

#. Remove the ``README.md`` file. We already have ``README.rst`` file created with ``scikit-package``.

    .. code-block:: bash

        rm README.md

#. Create a new local branch from the ``main`` branch. Let's call this branch ``skpkg-proj``.

    .. code-block:: bash

        git checkout -b skpkg-proj

    .. note::

        The ``-b`` flag indicates that you want to create a new branch if it does not already exist.

#. Let's now stage and commit the code.

    .. code-block:: bash
        
        git add README.md
        git commit -m "chore: remove README.md file pulled from remote main branch"

    .. note::

        You may wonder why we ``git add README.md``. While we removed it from our local computer, we still have to let the local Git repository know manually that it has been removed. Recall that when you run ``git init``, it creates a hidden folder called ``.git`` in your local project directory.

#. Let's now push our code to the new ``skpkg-proj`` local branch and push to the remote ``skpkg-proj`` branch.

    .. code-block:: bash

        git push --set-upstream origin skpkg-proj

#. Visit your remote GitHub repository. You should see the new branch ``skpkg-proj``.

#. Done! Let's then push the code from the remote ``skpkg-proj`` to the remote ``main`` branch via a pull request (PR).

Create a pull request from ``skpkg-proj`` to ``main``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Visit your GitHub repository.

#. Click on the new green button that says ``Compare & pull request``.

#. The PR title can be ``skpkg: start a new project with skpkg system template``.

#. The ``base`` branch should be ``main`` and the ``compare`` branch should be ``skpkg-proj``.

#. Click on the ``Create pull request`` button.

#. Wait for ``Tests on PR`` to run and pass. It runs ``pytest`` on the incoming code in each pull request.

#. Merge the PR.

#. Check that your remote ``main`` branch is up to date with the ``skpkg-proj`` branch.

#. Done! Let's now also setup ``pre-commmit`` to run automatically as well.

Setup pre-commit CI in GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: snippets/github-pre-commit-setup.rst





How to develop your code moving forward
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Assume that you have successfully followed the previous steps. Now, you want to add new code to your GitHub repository. Perhaps you are working with a group of people. Here is a high-level overview with step-by-step instructions on how to do that:

#. Pull the latest code from the remote ``main`` branch:

    .. code-block:: bash

        git checkout main
        git pull origin main

    .. note::

        Recall that we referred to ``origin`` as the remote GitHub repository.

#. Ensure that your local ``main`` branch is synced with the remote ``main`` branch by running:

    .. code-block:: bash

        git log

#. Create a new local branch from the ``main`` branch. Let's call this branch ``skpkg-proj``:

    .. code-block:: bash

        git checkout -b <branch-name>

#. Modify any file that you want. Then, stage and commit the changes:

    .. code-block:: bash

        git add <file-modified-added-deleted>
        git commit -m "feat: <your commit message>"

#. Push your code from ``<branch-name>`` to the remote ``<branch-name>`` branch:
    
    .. code-block:: bash

        git push --set-upstream origin <branch-name>

#. Visit your remote GitHub repository. You should see the new branch ``<branch-name>``.

#. Create a pull request from ``<branch-name>`` to ``main``.

#. Notice that you have ``Tests on PR`` and ``pre-commit`` checks.

#. Wait for the checks to run and pass. If they do, merge the PR.

#. Done! Repeat the above!


.. note::

    Make sure you check out the best practices and Billinge group's guidelines for communications and examples in the FAQ section :ref:`here<frequently-asked-questions>`.


What's next?
^^^^^^^^^^^^

Now that you have learned to reuse code across all files on your local computer, it's time to learn how to share your code with others as a publicly installable package that is hosted on PyPI and conda-forge. In Level 5, we will do that!