Please follow the naming practices recommended by PyPI and GitHub:

.. important::

    Use lowercase letters with each space replaced by ``"-"``. The only instance where an underscore ``"_"`` is allowed is for ``package_dir_name``. Underscores are ONLY ALLOWED for importing the package in Python. For example, if you set the ``package_dir_name`` as ``diffpy.my_project``, you will be able to import the package using ``import diffpy.my_project``.

Do you want to import your package with the identifier (group name, organization name) attached, like in ``import <org-name>.<project-name>``.

.. note::

    If you want to be able to ``import diffpy.pdffit``, all you need to do is set the ``project_name`` as ``diffpy.pdffit`` when you create a new project by running the command ``package create system``.
