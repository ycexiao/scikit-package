.. _scikit-package-manuscript-tutorials:

Create your manuscript with ``scikit-package-manuscript``
=========================================================

Overview
--------

This is a tutorial for using ``scikit-package-manuscript`` template, which provides the command

.. code-block:: bash

	package create manuscript

in ``scikit-package`` to create a manuscript directory with a customized LaTeX repository.

The tutorial is divided into two steps.

- You will learn how to create an environment for ``scikit-package`` in :ref:`manuscript-create-the-environment`.
- You will try the command ``package create manuscript`` and learn the prompt interface in :ref:`manuscript-run-the-command`.

We strongly recommend that you read through :ref:`manuscript-customize-latex-repo` to unleash the full potential of ``scikit-package-mansucript``.


How does ``scikit-package-manuscript`` benefit the manuscript writing process?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``scikit-package-manuscript`` provides a systematic way to organize your these LaTeX snippets and simplifies finding and copying the reusable LaTeX snippets into choosing from pre-defined journal template and GitHub repository.

Prerequisites
^^^^^^^^^^^^^^

To proceed with the following steps, we assume that you

#. know how to use ``conda`` to create an environment and install ``scikit-package`` in the environment. Please see :ref:`conda-env-setup-simple` for more information.
#. know how to manage repositories on GitHub. Please see the GitHub tutorial `GitHub Hello World <https://docs.github.com/en/get-started/start-your-journey/hello-world>`_ for more information.


.. _manuscript-create-the-environment:

Step 1. Create an environment and install ``scikit-package``
------------------------------------------------------------

#. Make sure ``conda`` is installed. Please see :ref:`conda-env-setup-simple` for more information.

   .. code-block:: bash

	conda --version

#. Create a new environment and activate it.

   .. code-block:: bash

	conda create -n skpkg-manuscript
	conda activate skpkg-manuscript


#. Install ``scikit-package`` in the environment.

   .. code-block:: bash

	conda install scikit-package


.. _manuscript-run-the-command:

Step 2. Run ``package create manuscript`` without customization
---------------------------------------------------------------

After Step 1, ``scikit-package-manuscript`` is enabled with a minimal setup.

1. Run ``scikit-package-manuscript``.

   .. code-block:: bash

	package create manuscript

2. Answer the following questions:

    .. include:: ../snippets/user-input-manuscript.rst

    .. note::

        You may press the "Enter" key to accept the default values for the questions.


3. Done! A manuscript folder named ``project_name`` is created in your working directory.


.. _manuscript-customize-latex-repo:

(Recommended) How to customize the LaTeX repositories
-----------------------------------------------------

The flexibility of ``scikit-package-manuscript`` is mainly attributed to that LaTeX repositories can be customized for different manuscripts. The following steps will help you create a LaTeX repository to be used by ``package create manuscript``

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
	cp my-latex-file.tex <latex-repo-dir>/
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
	git commit -m 'skpkg: initialize a LaTeX repository'
	git push origin main

#. Done! You can now run ``package create manuscript`` using this GitHub repository's URL as the input for ``latex_headers_repo_url`` to test it.

A manuscript folder will be created in the working directory. Files from the GitHub repository will be copied into the manuscript folder. Packages and commands in ``usepackages.txt`` and ``newcommands.txt`` will be inserted after ``\documentclass`` in the main LaTeX file (``manuscript.tex`` by default) in the manuscript folder. The names of all ``.bib``  will be added to the ``\bibliography`` entry in the main LaTeX file.


How to contribute
-----------------

Please make an issue on `scikit-package-manuscript <https://github.com/scikit-package/scikit-package-manuscript>`_ if you have any new features.
