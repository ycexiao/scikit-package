.. _scikit-package-installation:

Install ``scikit-package``
^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a new environment named ``<project>_env`` and install ``scikit-package`` and ``pre-commit`` at the same time:

.. code-block:: bash

    conda create -n <project>_env scikit-package pre-commit

Activate the environment:

.. code-block:: bash

    conda activate <project>_env

Confirm you have the latest version of ``scikit-package`` provided on GitHub:

.. code-block:: bash

    pip show scikit-package