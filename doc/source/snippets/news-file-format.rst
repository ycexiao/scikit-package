.. _news-file-guide:

We require that each PR includes a news item of ``<branch-name>.rst`` file under the ``news`` directory.

Here is an example PR containing the news file: https://github.com/Billingegroup/scikit-package/pull/299/files

How are the new files used?
^^^^^^^^^^^^^^^^^^^^^^^^^^^

``.rst`` files under the ``news`` directory are used to compile and update the ``CHANGELOG.rst`` file during releases. These news items are of interest to both developers and technical users looking for specific keywords.

Here an example ``CHANGELOG.rst``: https://github.com/Billingegroup/scikit-package/blob/main/CHANGELOG.rst

Guidelines for writing news
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Do not remove ``news/TEMPLATE.rst``. Make a copy called ``<branch-name>.rst``.
- Do not modify other section headers in the rst file. Replace ``* <news item>``
- Begin with "No news", "no news", or "no news added" for trivial changes with the following format:
- For consistency, start with a capital letter and a verb. End with a period. Ex) ``Add automatic linting of .md, .yml, .rst files via prettier hook in pre-commit.``

.. code-block:: text

    **Added:**

    * No news: <brief reason>

Where to place the news item in ``<branch-name>.rst``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``**Added:**`` includes features or functionality of interest to users and developers, such as support for a new Python version or the addition of a useful feature.
- ``**Changed:**`` includes modifications that affect end-users or developers, such as API changes or dependencies replaced.
- ``**Fixed:**`` includes bug fixes or refactoring.
- ``**Deprecated:**`` includes methods, classes, or workflows that are no longer supported in the future release.
- ``**Removed:**`` includes the opposite of the "Added" section, referring to features or functionality that have been removed.

.. _codecov-token-setup:
