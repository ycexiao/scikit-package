.. _scikit-package-installation:

Install ``scikit-package``
--------------------------

Create a new environment named ``skpkg_env`` and install ``scikit-package`` at the same time: ::

    conda create -n skpkg_env scikit-package

Activate the environment: ::

    conda activate skpkg_env

Check the current Python version installed in the environment: ::

    python --version

Install other optional packages: ::

    conda install pre-commit
