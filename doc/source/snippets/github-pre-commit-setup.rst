.. _pre-commit-github-repo-setup:

``Pre-commit CI`` is available as a GitHub app that executes pre-commit hooks in each pull request. This GitHub app will automatically attempt to lint code and format docstrings according to the hooks provided in ``.pre-commit-config.yaml``.

To configure ``pre-commit CI``, follow the simple steps below:

#. Visit https://github.com/apps/pre-commit-ci and click "Configure".

#. Select the repository(s).

#. let's attempt to activate the ``pre-commit CI`` by sending an empty commit to the ``skpkg-proj`` remote branch.

.. code-block:: bash

    git commit --allow-empty -m "ci: empty commit to test pre-commit CI setup"
    git push

#. Notice you have an additional check in the pull request.

#. Done!