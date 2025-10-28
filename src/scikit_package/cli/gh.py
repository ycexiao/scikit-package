from urllib.parse import urlparse

import requests


def _get_issue_content(issue_url):
    """Fetch the contents of the issue that will be broadcast.

    Parameters
    ----------
    issue_url: str
      url to the issue to be broadcast. Currently it takes the form:
      https://github.com/{user-or-org-name}/{repo-name}/issues/{issue-number}

    Returns
    -------
    source_repo_url: str
        used to exclude source repo from the broadcasting target list.
    issue_content: dict
        issue-title and issue-body to be broadcast.
    """
    parsed = urlparse(issue_url)
    path_parts = parsed.path.strip("/").split("/")
    try:
        owner = path_parts[0]
        repo = path_parts[1]
        issue_number = int(path_parts[3])
    except (IndexError, ValueError):
        raise ValueError(
            f"{issue_url} is not a valid url to be parsed. "
            "Please ensure the input url is with a format like "
            "https://github.com/username/reponame/issues/issue-number"
        )
    api_url = (
        f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
    )
    source_repo_url = f"https://github.com/{owner}/{repo}"
    try:
        response = requests.get(api_url)
        assert response.status_code == 200
        issue_content = response.json()
    except (AssertionError, requests.JSONDecodeError):
        raise ValueError(
            f"Can not find the corresponding issue from {issue_url}. "
            "Please ensure the input url is with a format like https://"
            "github.com/username/reponame/issues/issue-number"
        )
    return source_repo_url, issue_content


def _broadcast_issue_to_urls(issue_content, repo_urls, gh_token, dry_run=True):
    """Broadcast a issue to multiple GitHub repositories.

     Parameters
    ----------
    issue_content : dict
        The issue_content needed to create issues in each repo.
    repo_urls : list of str
        The urls to the target repos.
    gh_token : str
        GitHub token for authentication.

    Returns
    -------
    failed_urls: list of str
        The list of repo urls where the issue creation failed.
    """
    data = {
        "title": issue_content["title"],
        "body": issue_content["body"],
    }
    headers = {
        "Authorization": f"token {gh_token}",
        "Accept": "application/vnd.github.v3+json",
    }
    non_gh_urls = []
    failed_gh_urls = []
    for i in range(len(repo_urls)):
        try:
            api_url = _get_post_api_url(repo_urls[i])
        except (IndexError, AssertionError):
            non_gh_urls.append(repo_urls[i])
            continue
        if not dry_run:
            response = requests.post(api_url, json=data, headers=headers)
            if (
                response.status_code != 201
                and repo_urls[i] not in failed_gh_urls
            ):
                failed_gh_urls.append(repo_urls[i])
    if dry_run:
        _print_dry_run_message(non_gh_urls)
    return non_gh_urls, failed_gh_urls, dry_run


def _get_post_api_url(repo_url):
    """Get the GitHub API URL for posting issues to a repository.

    Parameters
    ----------
    repo_url : str
        The URL of the target GitHub repository.

    Returns
    -------
    api_url : str
        The GitHub API URL for posting issues.
    owner : str
        The user name or organization name of the repository.
    repo : str
        The name of the repository.
    """
    assert repo_url.startswith("https://github.com/")
    parsed = urlparse(repo_url)
    path_parts = parsed.path.strip("/").split("/")
    owner = path_parts[0]
    repo = path_parts[1]
    api_url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    return api_url


def _print_dry_run_message(none_gh_urls=[]):
    pass
