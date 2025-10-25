from scikit_package.cli.gh import _get_issue_content  # noqa: F401


def test_get_issue_content():
    # C1: a valid issue url. Expect the source_repo_url and
    #   issue content are returned.
    assert False


def test_get_issue_content_bad():
    # C1: a not valid issue url. Expect ValueError.
    assert False
