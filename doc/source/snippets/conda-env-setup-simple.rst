(Required) Use conda environment to run install pacakges and run Python code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Since we will be working across multiple projects, it is important to introduce the idea of \emph{virtual environments}. 

Virtual environments allow you to create isolated environments, each with their own software package versions installed. 
This is especially helpful when working with multiple different software programs that require conflicting versions of the same packages and is overall a good practice.

``conda`` is an open-source package and environment management software that allows you to create isolated environments to install software, including Python and its packages. The instructions for conda installation can be found at https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html.


If your code still does not run, we recommend setting up a conda environment. 

Once ``conda`` is install locally described in the above section, we need to inform where to download the packages from. The ``conda-forge`` channel hosts a colletion of packages including ``numpy``.

Add the ``conda-forge`` channel to your conda configuration by running the following command:

.. code-block:: bash

    conda config --add channels conda-forge

Now, let's create a new environment and install ``numpy`` in it.

.. code-block:: bash

    # Create a new environment and install numpy in the environment
    conda create -n <project-name>_env numpy

    # Activate the environment
    conda activate <project-name>_env

Let's check if the installation was successful. You can do this by running the following command:

.. code-block:: bash

    # Check Python version
    python --version

    # Run the script
    python <python_file_name>.py
