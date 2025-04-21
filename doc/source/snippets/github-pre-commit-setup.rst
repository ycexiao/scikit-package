#. Visit https://github.com/apps/pre-commit-ci and click "Configure".

#. Select the repository(s).

#. let's attempt to activate the ``pre-commit CI`` by sending an empty commit to the ``skpkg-proj`` remote branch.

    .. code-block:: bash

        git commit --allow-empty -m "ci: empty commit to test pre-commit CI setup"
        git push

#. Notice you have an additional check in the pull request!