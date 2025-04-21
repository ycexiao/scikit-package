
``/doc`` is the the Sphinx documentation folder. The documentation will be built locally first and then automatically built and hosted on GitHub Pages when a new release is created.

#. Build the documentation locally by running:

    .. code-block:: bash

        conda install --file requirements/docs.txt

#. Then we will use an external tool called ``sphinx-reload`` to automatically reload the documentation when you make changes to ``.rst`` files.

    .. code-block:: bash

        pip install sphinx-reload

    .. note::

        ``sphinx-reload`` is only available via pip install.

#. A HTML will appear automatically in your browser by running the following command:

    .. code-block:: bash

        sphinx-reload doc

#. Done! Later, you will learn to host this documentation on GitHub Pages via public URL.
