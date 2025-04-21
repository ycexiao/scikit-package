We will use a script to automate the process of generating the API documentation. This script will create a new directory in your ``doc/source`` directory called ``api`` and generate the API documentation there.


#. Assume you have your project developed under ``dev``, here is the folder structure:

    .. code-block:: text

        dev/
        └── my-package
            ├── doc
            ├── src
            └── tests

#. Clone ``git clone https://github.com/Billingegroup/release-scripts.git`` in your folder outside of the package directory. Here is the folder structure:

    .. code-block:: text

        dev/
        ├── my-package
            ├── doc
            ├── src
            └── tests
        └── release-scripts
            └── auto_api.py

#. Run ``cd my-pacakge`` to enter the package directory.

#. Run ``python -m build`` to build the package. You may have to install ``python-build`` first.

#. Run the script. This is done by running ``python <path_to_auto_api_script> <package_name> <path_to_package_proper> <path_to_api_directory>``. Here is an example below:

    .. code-block:: bash

        # Regular Python package ex) package-name is regolith
        python ../release-scripts/auto_api.py regolith ./src/regolith ./doc/source/api/
        
        # Namespace Python package ex) package-name is diffpy.utils
        python ../release-scripts/auto_api.py diffpy.morph ./src/diffpy/pdfmorph ./doc/source/api


#. Check the newly created API documentation by runnning ``sphinx-reload doc``.

#. Add and commit the changes: ``git add doc && git commit -m skpkg: generate api doc with auto-api script``.

#. Push and create a PR to the branch you are working on.

.. note::

    If you see the the error "No module named" (``e.g. WARNING: autodoc: failed to import module 'tools' from module 'diffpy.pdfmorph'; the following exception was raised: No module named 'diffpy.utils'``), it can be resolved by adding ``autodoc_mock_imports = [<pkg>]`` to your ``conf.py`` right under imports. This file is located in ``/doc/source/conf.py``.    