Initiate a new package by running the following command in the terminal:

.. code-block:: bash

    package create public

Enter values for the following prompts:

``proj`` stands for "project" and ``gh`` for "GitHub".

:proj_owner_name: e.g., ``Simon J. L. Billinge``.

:proj_owner_email: e.g., ``sbillinge@columbia.edu``.

:proj_owner_gh_username: e.g., ``sbillinge``.

:contributors: e.g., ``Billinge Group members and community contributors``.

:license_holders: e.g., ``The Trustees of Columbia University in the City of New York``.

:project_name: e.g., ``my-package``. For a namespace package, use e.g., ``diffpy.my-package``.

:github_org: The GitHub organization name or owner's GitHub username. e.g., ``diffpy`` or ``sbillinge``.

:github_repo_name: e.g., ``my-package``. The repository name of the project displayed on GitHub.

:package_dist_name: The name in the package distribution in PyPI and conda-forge. If your package name contains ``_``, replace it with ``-``. e.g., ``my-package``. For a namespace package, use e.g., ``diffpy.my-package``.

:package_dir_name: The name of the package directory under ``src``. Unlike ``project_name``, it must be lowercase so that it can be imported as ``import my_package``.

:proj_short_description: e.g., ``Python package for doing science.``

:keywords: Each word is separated by a comma and a space. e.g., ``pdf, diffraction, neutron, x-ray``. The keywords may be found in ``pyproject.toml`` or ``setup.py``.

:min_python_version: The minimum Python version for package distribution.

:max_python_version: The maximum Python version for package distribution.

:needs_c_code_compiled: Whether the package requires C/C++ code that requires building the package. For pure Python packages, type ``1`` to select ``No``.

:has_gui_tests: Whether the package runs headless testing in GitHub CI. If your package does not contain a GUI, type ``1`` to select ``No``.

``cd`` into the newly created folder by running the command:

.. code-block:: bash

    cd <project-name>

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








