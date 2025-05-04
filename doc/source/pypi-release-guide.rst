:tocdepth: -1

.. index:: pypi-release-guide

.. _pypi-release-guide:

==================================
Release package to GitHub and PyPI
==================================

Overview
~~~~~~~~~

In this guide, you will learn to release your source code to GitHub and PyPI so that by the end of the guide, you can install your package via ``pip install <package-name>``.

Initiate a release process with GitHub issue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _release-instructions-contributor:

.. important::  Make sure you have your project is standarlized with scikit-package up to Level 5. Otherwise, please start from the Getting started page :ref:`here <getting-started>`.

#. In the repository, create an issue on GitHub with the "Release" option as shown below:

   .. image:: ./img/release-issue.png
      :alt: add-personal-access-token
      :width: 600px

#. Check off all items in the first checklist for PyPI/GitHub release.

#. Proceed to the next section.

Start pre-release
~~~~~~~~~~~~~~~~~

.. _release-instructions-project-maintainer:

#. Review the release GitHub issue created in the previous step.

#. Set ``PYPI_TOKEN`` and ``PAT_TOKEN`` are configured at the organization or repository level by following the instructions in Appendix :ref:`1 <pypi-token-setup>`, :ref:`2 <pat-token-setup>`, respectively.

#. Setup GitHub pages at the repository level by following the instructions in Appendix :ref:`3 <gh-pages-setup>`.

#. Confirm the ``github_admin_username`` section in ``.github/workflows/build-wheel-release-upload.yml`` is that of the project maintainer.

#. In your terminal, run ``git checkout main && git pull upstream main`` to sync with the main branch.

#. Run the following:

   .. code-block:: bash

      # For pre-release, use *.*.*-rc.* e.g., 1.0.0-rc.0
      # rc stands for release candidate
      git checkout -b <version>-rc.<rc-number>
      git push upstream <version>-rc.<rc-number>

#. Done! Once the tag is pushed, visit the ``Actions`` tab in the repository to monitor the CI progress.

#. You will see that the GitHub Actions workflow is triggered and the package is built and uploaded to PyPI and GitHub.

#. For ``pre-release``, it will not update the documentation on GitHub Pages. It will also not update the changelog. See the next section for the full release process.

Full release after pre-release
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. In your terminal, run ``git checkout main && git pull upstream main`` to sync with the main branch.

#. Run the following::

    # For release, use *.*.* e.g., 1.0.0
    git tag <version>
    git push upstream <version>

#. Notice that the documentation is deployed. It will also update the ``CHANGELOG.rst``.

#. Now that you have your source code uploaded to ``PyPI``, we will then now provide a conda package as well.

Release conda-forge package
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To support ``conda install <package-name>``, for your package, follow the instructions :ref:`here<conda-forge-release-guide>`.

.. _pypi-token-setup:

Appendix 1. Setup ``PYPI_TOKEN`` to allow GitHub Actions to upload to PyPI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generate a PyPI API token from ``pypi.org``:

#. Visit https://pypi.org/manage/account/ and log in.

#. Scroll down to the ``API tokens`` section and click ``Add API token``.

#. Set the ``Token name`` to ``PYPI_TOKEN``.

#. Choose the appropriate ``Scope`` for the token.

#. Click ``Create token`` and copy the generated token.

Add the generated token to GitHub:

#. Navigate to the ``Settings`` page of the org (or repository).

#. Click the ``Actions`` tab under ``Secrets and variables``.

#. Click ``New org secret``, name it ``PYPI_TOKEN``, and paste the token value.

#. Done!

.. image:: ./img/add-pypi-secret.png
   :alt: add-pypi-secret
   :width: 600px

.. _pat-token-setup:

Appendix 2. Setup ``PAT_TOKEN`` to allow GitHub Actions to compile ``CHANGELOG.rst``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Recall that dring a release (not pre-release) process, the GitHub Actions workflow compiles the news items in the ``CHANGELOG.rst`` file in the ``main`` branch. Hence, the GitHub workflow needs to link with this privilege through a personal access token (PAT) of the project maintainer.

1. Visit https://github.com/settings/tokens

2. Click ``Generate new token`` and choose the classic option.

3. Under ``Note``, write, "GitHub CI release"

4. Set the Expiration date of the token.

5. Under ``Select scopes``, check ``repo`` and ``user``.

6. Scroll down, click ``Generate token``.

7. Done!

.. image:: ./img/add-personal-access-token.png
   :alt: add-personal-access-token
   :width: 600px

Copy and paste the ``PAT_TOKEN`` to your GitHub organization:

1. Visit ``Settings`` in the organization.

2. Click the ``Actions`` tab under ``Secrets and variables``.

3. Click ``New organization secret`` and add a new secret and name it as ``PAT_TOKEN``.

4. Done!

.. _gh-pages-setup:

Appendix 3. Host documentation online with GitHub Pages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The goal is to host the official documentation online i.g., ``https://diffpy.github.io/diffpy.utils`` using GitHub Pages.

#. Visit the ``Settings`` page in your repository and and click ``pages`` under ``Code and automation``.
#. Click ``Deploy from a branch`` under ``Source``. Below, choose ``gh-pages`` branch and ``/(root)`` and click ``Save``. See the image below.

   .. image:: ./img/github-pages.png
      :alt: setup-github-pages-from-branch

#. Done! Wait a few minutes and visit your GitHub Pages URL!
