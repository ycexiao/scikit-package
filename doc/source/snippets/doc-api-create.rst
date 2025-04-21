We will use a script to automate the process of generating the API documentation. This script will create a new directory in your ``doc/source`` directory called ``api`` and generate the API documentation there.

#. Assume you have your project developed under ``dev``. Here is the folder structure:

    .. code-block:: text

        dev/
        └── my-package
            ├── doc
            ├── src
            └── tests

#. Clone ``git clone https://github.com/Billingegroup/release-scripts.git`` into a folder outside of the package directory. Here is the folder structure:

    .. code-block:: text

        dev/
        ├── my-package
            ├── doc
            ├── src
            └── tests
        └── release-scripts
            └── auto_api.py

#. Run ``cd my-package`` to enter the package directory.

#. Run ``python -m build`` to build the package. You may have to install ``python-build`` first.

#. Run the ``auto_api.py`` script. This is done by running ``python <path_to_auto_api_script> <package_name> <path_to_package_proper> <path_to_api_directory>``. Here is an example below:

    .. code-block:: bash

        # Regular Python package, e.g., package name is regolith
        python ../release-scripts/auto_api.py regolith ./src/regolith ./doc/source/api/
        
        # Namespace Python package, e.g., package name is diffpy.utils
        python ../release-scripts/auto_api.py diffpy.morph ./src/diffpy/pdfmorph ./doc/source/api

#. Check the newly created API documentation by running ``sphinx-reload doc``.

#. Add and commit the changes: ``git add doc && git commit -m "skpkg: generate API doc with auto-api script"``.

#. Push and create a PR to the branch you are working on.

.. note::

    Here are some examples: https://www.diffpy.org/diffpy.utils/api/diffpy.utils.html
    The source code created by ``auto_api.py`` is provided in https://github.com/diffpy/diffpy.utils/tree/main/doc/source/api

    If you see the error "No module named" (e.g., ``WARNING: autodoc: failed to import module 'tools' from module 'diffpy.pdfmorph'; the following exception was raised: No module named 'diffpy.utils'``), it can be resolved by adding ``autodoc_mock_imports = [<pkg>]`` to your ``conf.py`` right under imports. This file is located in ``/doc/source/conf.py``.
