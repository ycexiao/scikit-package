from scikit_package.cli.gh import _broadcast_issue_to_urls  # noqa: F401


def test_broadcast_issue_to_urls():
    # C1: complete issue_content, a list of target repo urls and
    #   dry_run is True.
    #   Expect status_flag to be 1. Issues are not created in the
    #   target repos.
    # C2: complete issue_content, a list of target repo urls, and
    #   dry_run -s False.
    #   Expect status_flag to be 0. Issues are created in the target
    #   repos.
    assert False


def test_broadcast_issue_to_urls_bad():
    # C1: no "title" or "body" key found in the issue_content.
    #   Expect KeyError.
    # C2: empty broadcast_urls. Expect ValueError.
    assert False
