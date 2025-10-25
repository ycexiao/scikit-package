def _broadcast_issue_to_urls(issue_content, broadcast_urls, dry_run=False):
    """Broadcast issue to the repos pointed by the urls in the
    broadcast_urls.

    Parameters
    ----------
    issue_content : dict
        issue_content needed to create issues in each repo.
    broadcast_urls : list of str
        urls to the target repos.

    Returns
    -------
    status_flag : int
        0 if the issue is successfully broadcast to other urls.
        1 if dry_run is enabled and no other errors exist.
        <0 if there are errors.
    """
    return
