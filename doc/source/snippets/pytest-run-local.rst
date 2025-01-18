.. _test-package-locally:

Appendix 1. How to test your package locally
--------------------------------------------

Ensure your package has been scikit-packaged. We will use the ``diffpy.utils`` package as an example. In the package directory, follow these instructions:

.. code-block:: bash

    # Create a new environment, specify the Python version and install packages
    conda create -n diffpy_utils_env python=3.13 \
        --file requirements/test.txt \
        --file requirements/conda.txt \
        --file requirements/build.txt

    # Activate the environment
    conda activate diffpy_utils_env

    # Install your package locally
    # `--no-deps` to NOT install packages again from `requirements.pip.txt`
    pip install -e . --no-deps

    # Run pytest locally
    pytest

    # ... run example tutorials

.. _build-documentation-locally:

=
