from urllib.parse import urlparse

import requests
from rich.prompt import Confirm, Console


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


def _broadcast_issue_to_urls(
    issue_content, broadcast_urls, gh_token, dry_run=False
):
    """Broadcast issue to the repos pointed by the urls in the
    broadcast_urls.

    Parameters
    ----------
    issue_content : dict
        The issue_content needed to create issues in each repo.
    broadcast_urls : list of str
        The urls to the target repos.
    gh_token : str
        GitHub token for authentication.

    Returns
    -------
    failed_urls: list of str
        The list of repo urls where the issue creation failed.
    """

    failed_urls = []
    console = Console()
    for repo_url in broadcast_urls:
        if Confirm.ask(f"Broadcast to {repo_url}?"):
            console.print(f"Broadcasting to {repo_url}...")
            try:
                success_status = _broadcast_issue_to_one(
                    issue_content, repo_url, gh_token, dry_run
                )
            except Exception:
                failed_urls.append(repo_url)
                console.print(f"Failed to broadcast to {repo_url}.")
                console.print_exception()
            if not success_status:
                failed_urls.append(repo_url)
                console.print(f"Failed to broadcast to {repo_url}.")
        else:
            console.print(f"Skipped broadcasting to {repo_url}.")
            continue
    return failed_urls


def _broadcast_issue_to_one(issue_content, repo_url, gh_token, dry_run=False):
    """Broadcast a issue to a single GitHub repository.

     Parameters
    ----------
    issue_content : dict
        The issue_content needed to create issues in each repo.
    repo_url : str
        The url to the target repo.
    gh_token : str
        GitHub token for authentication.

    Returns
    """
    parsed = urlparse(repo_url)
    path_parts = parsed.path.strip("/").split("/")
    try:
        owner = path_parts[0]
        repo = path_parts[1]
    except IndexError:
        raise ValueError(
            f"{repo_url} is not a valid repository URL. "
            "Please check your JSON files and "
            "ensure the repo URL is with a format like https://"
            "github.com/username/reponame"
        )
    api_url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    headers = {
        "Authorization": f"token {gh_token}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {
        "title": issue_content["title"],
        "body": issue_content["body"],
    }
    if dry_run:
        return False
    else:
        response = requests.post(api_url, headers=headers, json=data)
        return response.status_code == 201
