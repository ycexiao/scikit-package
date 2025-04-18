.. _pre-commit-github-repo-setup:

Appendix 1. How to configure pre-commit CI via GitHub Apps
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``Pre-commit CI`` is available as a GitHub app that executes pre-commit hooks in each pull request. This GitHub app will automatically attempt to lint code and format docstrings according to the hooks provided in ``.pre-commit-config.yaml``. If all passes, it will give you a green checkmark as shown below.

.. image:: ./img/precommit-PR.png
   :alt: pre-commit-PR-automatic-check

To configure ``pre-commit CI``, follow the simple steps below:

#. Visit https://github.com/apps/pre-commit-ci and click "Configure".

#. Select the repository(s).

#. Done!



.. _codecov-token-setup:

Appendix 2. Codecov token setup for the repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For each PR, we use ``Codecov`` to report the test coverage percentage change as shown below.

.. image:: ./img/codecov-pr.png
   :alt: codecov-in-pr-comment

To do so, the repository owner needs to provide a ``CODECOV_TOKEN``.  Please follow the step-by-step guide below.

1. Visit https://app.codecov.io/

2. Connect your repository or organization with Codecov by clicking ``Configure Codecov's GitHub app``, shown below:

.. image:: ./img/codecov-configure.png
   :alt: codecov-configure-github-project-button

3. Scroll down, find your repository of interest, and click ``Configure``, shown below:

.. image:: ./img/codecov-projects.png
    :alt: codecov-list-github-projects

4. Scroll down again, copy ``CODECOV_TOKEN``, shown below:

.. image:: ./img/codecov-token.png
    :alt: codecov-list-github-projects

5. In your GitHub repository, go to ``Settings``, then click ``Actions`` under the ``Secrets and Variables`` tab.

6. Click ``New repository secret``.

7. Paste the token value and name it as ``CODECOV_TOKEN`` secret as shown below:

.. image:: ./img/codecov-github.png
    :alt: codecov-list-github-projects

8. Done. The Codecov token is now set up for the repository. A comment will be generated on each PR with the Codecov status automatically.
