.. _scikit-package-installation:

Install ``scikit-package`` with conda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Create a new environment named ``<project>_env``, e.g., ``skpkg_env``. Install ``scikit-package`` and ``pre-commit`` simultaneously by running the following command:

    .. code-block:: bash

        conda create -n <project>_env scikit-package pre-commit

#. Activate the environment:

    .. code-block:: bash

        conda activate <project>_env

#. Confirm that you have the latest version of ``scikit-package`` available on GitHub:

    .. code-block:: bash

        pip show scikit-package
