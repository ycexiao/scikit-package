def _get_issue_content(issue_url):
    """Get the source repo url and issue content form the issue url.

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
    source_repo_url = None
    issue_content = None
    return source_repo_url, issue_content
