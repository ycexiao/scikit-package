.. _scikit-package-manuscript-tutorials:

Creating your manuscript with ``scikit-package-manuscript``
===========================================================

Overview
--------

This is a tutorial for using ``scikit-package-manuscript``. The following steps can help you to learn to use

.. code-block:: bash

		package create manuscript

to create a manuscript directory with a customized LaTeX repository.


How does ``scikit-package-manuscript`` benefit the manuscript writing process?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A common way of managing reusable LaTeX files is to do it manually. For users who maintain a large amount of reusable LaTeX files, finding and copying the correct LaTeX snippets into the newly created manuscript can be a tiresome task, especially when different manuscripts need quite different LaTeX snippets and when users have to do it frequently.


``scikit-package-manuscript`` is a template in the ``scikit-package`` project which provides a systematic way to organize your reusable LaTeX snippets and simplifies selecting and copying the reusable LaTeX snippets into choosing from pre-defined ``journal_template`` and ``latex_headers_repo_url`` options.


Prerequisites
^^^^^^^^^^^^^^
To proceed with the following steps, we assume that you

#. Know how to use ``conda`` to create an environment and install ``scikit-package`` in the environment. Please see :ref:`conda-env-setup-simple` for more information.
#. Know how to manage repositories on GitHub. Please see the GitHub tutorial `GitHub hello world <https://docs.github.com/en/get-started/start-your-journey/hello-world>`_ for more information.


Table of contents
^^^^^^^^^^^^^^^^^

1. :ref:`create-environment-with-scikit-package`
2. :ref:`try-package-create-manuscript`
3. :ref:`customize-latex-repo`


.. _create-environment-with-scikit-package:

Step 1. Create an environment and install ``scikit-package``
------------------------------------------------------------

#. Make sure ``conda`` is installed.

   .. code-block:: bash

	conda --version

#. Create a new environment and activate it.

   .. code-block:: bash

	conda create -n skpkg-manuscript
	conda activate skpkg-manuscript


#. Install ``scikit-package`` in the environment.

   .. code-block:: bash

	conda install scikit-package


.. _try-package-create-manuscript:

Step 2. Try ``package create manuscript`` without customization
---------------------------------------------------------------

After Step 1, ``scikit-package-manuscript`` is enabled with a minimal setup.

1. Invoke ``scikit-package-manuscript``

   .. code-block:: bash

	package create manuscript

2. Answer the following questions

    .. include:: ../snippets/user-input-manuscript.rst

    .. note::

        You may press the "Enter" key to accept the default values for the questions.


3. Done! A manuscript folder named ``project_name`` is created in your working directory.

You can use a different LaTeX repository URL as the input for ``latex_headers_repo_url`` during the process. The flexibility of ``scikit-package-manuscript`` is mainly attributed to that LaTeX repositories can be customized for different manuscripts.


.. _customize-latex-repo:

Step 3. Customize the LaTeX repositories
-----------------------------------------

#. Create a GitHub repository and copy the repository URL. Please see :ref:`create-new-github-repo` for more information.

#. Create a directory ``<latex-repo-dir>`` to store the LaTeX files and associate the directory with the GitHub repository.

   .. code-block:: bash

	mkdir <latex-repo-dir>
	cd <latex-repo-dir>
	git init
	git remote add origin <coppied-repository-URL>

#. Copy the files that you want to include in the manuscript folder into the ``<latex-repo-dir>`` directory. During ``package create manuscript``, these files will be copied into the manuscript folder without modifications.

   e.g.

   .. code-block:: bash

	cp my-class-file.cls <latex-repo-dir>/
	cp my-style-file.bst <latex-repo-dir>/
	cp my-bib-file-1.bib <latex-repo-dir>/
	cp my-bib-file-2.bib <latex-repo-dir>/
	cp another-latex-file.tex <latex-repo-dir>/
	cp other-file.txt <latex-repo-dir>/


#. Create ``usepackages.txt`` and ``newcommands.txt`` in the ``<latex-repo-dir>`` directory.

   ``usepackages.txt`` is used to add commands like ``\usepackage{graphicx}`` into the main LaTeX file. ``newcommands.txt`` is used to add commands like ``\newcommand{\a_command}[1]{\mathrm{#1}}`` into the main LaTeX file. The main LaTeX file is ``manuscript.tex`` in the manuscript folder by default.

   .. note::
      No LaTeX syntax check is executed during ``package create manuscript``. The content in ``usepackages.txt`` is what will be inserted after ``\documentclass`` and the content in ``newcommands.txt`` is what will be inserted after all ``\usepackage``.


   Example of ``usepackages.txt``

   .. code-block:: text

	\usepackage{mathtools}
	\usepackage{amsmath}
	\usepackage{mathtools}
	...

   Example of ``newcommands.txt``

   .. code-block:: text

	\newcommand{\command_1}[1]{\mathrm{#1}}
	\newcommand{\command_2}[1]{\mathbb{#1}}
	\newcommand{\command_3}[1]{\mathcal{#1}}
	...


#. Commit the change and sync the repository with the one in GitHub.

   .. code-block:: bash

	git add .
	git commit -m '<your-commit-message>'
	git push origin main

#. Done! You can now run ``package create manuscript`` using this GitHub repository's URL as the input for ``latex_headers_repo_url`` to test it.

   A manuscript folder will be created in the working directory. Files from the GitHub repository will be copied into the manuscript folder. Packages and commands in ``usepackages.txt`` and ``newcommands.txt`` will be inserted after ``\documentclass`` in the main LaTeX file (``manuscript.tex`` by default) in the manuscript folder. The names of all ``.bib``  will be added to the ``\bibliography`` entry in the main LaTeX file.


How to contribute
-----------------

Please make an issue on `scikit-package-manuscript <https://github.com/scikit-package/scikit-package-manuscript>`_ if you have any new features.
