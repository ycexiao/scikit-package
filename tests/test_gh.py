from types import SimpleNamespace

import pytest

from scikit_package.cli.gh import _broadcast_issue_to_urls  # noqa: F401
from scikit_package.cli.gh import _get_issue_content


def test_get_issue_content(mocker):
    # C1: a valid issue url. Expect the source_repo_url and
    #   issue content are returned.
    get_issue_mocker = mocker.patch(
        "requests.get",
        return_value=SimpleNamespace(
            status_code=200,
            json=lambda: {"title": "issue-title", "body": "issue-body"},
        ),
    )
    issue_url = "https://github.com/user-or-orgname/reponame/issues/1"
    expected_issue_content = {"title": "issue-title", "body": "issue-body"}
    expected_source_repo_url = "https://github.com/user-or-orgname/reponame"
    actual_source_repo_url, actual_issue_content = _get_issue_content(
        issue_url
    )
    get_issue_mocker.assert_called_once()
    assert actual_source_repo_url == expected_source_repo_url
    assert actual_issue_content == expected_issue_content


def test_get_issue_content_bad(mocker):
    # C1: a not valid url. Expect ValueError.
    issue_url = "non-valid-url"
    with pytest.raises(
        ValueError,
        match=(
            f"{issue_url} is not a valid url to be parsed. "
            "Please ensure the input url is with a format like "
            "https://github.com/username/reponame/issues/issue-number"
        ),
    ):
        source_repo_url, issue_content = _get_issue_content(issue_url)

    # C2: a valid url but can not find the corresponding issue.
    #   Expect ValueError.
    get_issue_fail_mocker = mocker.patch(
        "requests.get",
        return_value=SimpleNamespace(
            status_code=404,
            json=lambda: {"message": "Not Found"},
        ),
    )
    issue_url = "https://github.com/nonexisting/nonexisting/issues/0"
    with pytest.raises(
        ValueError,
        match=(
            f"Can not find the corresponding issue from {issue_url}. "
            "Please ensure the input url is with a format like "
            "https://github.com/username/reponame/issues/issue-number"
        ),
    ):
        source_repo_url, issue_content = _get_issue_content(issue_url)
    get_issue_fail_mocker.assert_called_once()


def test_broadcast_issue_to_urls(mocker):
    # C1: complete issue_content, a list of target repo urls and
    #   dry_run is True.
    #   Expect failed_urls to be empty. Issues are not created in the
    #   target repos.
    mocker.patch(
        "rich.prompt.Confirm.ask",
        return_value=True,
    )
    create_issue_mocker = mocker.patch(
        "requests.post",
        return_value=SimpleNamespace(status_code=201),
    )
    issue_content = {"title": "issue-title", "body": "issue-body"}
    broadcast_urls = [
        "https://github.com/user-or-orgname/reponame1",
        "https://github.com/user-or-orgname/reponame2",
    ]
    actual_failed_urls = _broadcast_issue_to_urls(
        issue_content, broadcast_urls, gh_token="dummy_token", dry_run=True
    )
    create_issue_mocker.assert_not_called()
    expected_failed_urls = broadcast_urls
    assert set(actual_failed_urls) == set(expected_failed_urls)
    # C2: complete issue_content, a list of target repo urls, and
    #   dry_run is False.
    #   Expect failed_urls to be empty. Issues are created in the target
    #   repos.
    actual_failed_urls = _broadcast_issue_to_urls(
        issue_content, broadcast_urls, gh_token="dummy_token", dry_run=False
    )
    create_issue_mocker.assert_called()
    expected_failed_urls = []
    assert actual_failed_urls == expected_failed_urls
    # C3: complete issue_content, all urls are invalid.
    #   Expect non empty failed_urls.
    create_issue_failed_mocker = mocker.patch(
        "requests.post",
        return_value=SimpleNamespace(status_code=404),
    )
    broadcast_urls = [
        "https://github.com/user-or-orgname/invalid-repo1",
        "https://github.com/user-or-orgname/invalid-repo2",
    ]
    actual_failed_urls = _broadcast_issue_to_urls(
        issue_content, broadcast_urls, gh_token="dummy_token"
    )
    create_issue_failed_mocker.assert_called()
    expected_failed_urls = broadcast_urls
    assert set(actual_failed_urls) == set(expected_failed_urls)
