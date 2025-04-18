Host your new project on GitHub
-------------------------------

#. Visit ``https://github.com/new``.

#. Choose the ``Owner`` and enter the ``Repository name`` and the ``Description``.

#. Check ``Add a README file``.

#. Set ``none`` under ``Add .gitignore``

#. Set ``none`` under ``Choose a licenese``

#. Click the ``Create repository`` to green button to create the repository.

#. Run the following commands to push your local project to GitHub:

    .. code-block:: bash

        git remote add origin https://github.com/<OWNER>/<project-name>.git
        git add .
        git commit -m "skpkg: start a new project with scikit-package"
        git branch -M main
        git push --set-upstream origin main

#. Refresh the GitHub repository page to see that the package is now hosted on GitHub.
