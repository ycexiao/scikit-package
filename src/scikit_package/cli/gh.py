import json
import os
import subprocess
import warnings
from collections import defaultdict
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.parse import urlparse

import requests
from rich.console import Console
from rich.prompt import Confirm, Prompt

from scikit_package.utils.io import read_skpkg_config


def broadcast_issue(args):
    issue_content = _get_issue_content(args.issue_url)
    (
        broadcast_target_candidates_from_repo,
        broadcast_target_candidates_from_config,
    ) = _get_broadcast_target_candidates()
    target_repos_url = _get_broadcast_target_url(
        broadcast_target_candidates_from_repo,
        broadcast_target_candidates_from_config,
    )
    _broadcast_issue(issue_content, target_repos_url)


def _get_issue_content(issue_url):
    api_url, (owner, repo, issue_number) = _get_get_issue_api_from_issue_url(
        issue_url
    )
    response = requests.get(api_url)
    issue_content = None
    if response.status_code == 200:
        issue_content = response.json()

    if issue_content is None:
        raise ValueError(
            f"Failed to fetch issue from {issue_url}. "
            "Please ensure the following content generated "
            "from the URL is correct: "
            f"Owner: {owner}, Repo: {repo}, Issue Number: {issue_number} "
        )

    return issue_content


def _get_broadcast_target_candidates(json_name="broadcast_candidates.json"):
    """Get target repositories from (1) a JSON file in a Github
    repository whose URL is specified in config file or prompt and (2)
    local config file ~/.skpkgrc.

    Parameters
    ----------
    json_name : str, optional
        The name of the JSON file in the GitHub repo containing broadcast
        target candidates. Default "broadcast_candidates.json".
        The file content is expected to be:
        {
            <group1-name>: {
                <repo1-name> : <repo1-URL>,
                <repo2-name> : <repo2-URL>
                ...
            },
            <group2-name>: {
                <repo1-name> : <repo1-URL>,
                <repo2-name> : <repo2-URL>
                ...
            },
            <group2-name>: {
                <repo1-name> : <repo1-URL>,
                <repo2-name> : <repo2-URL>
                ...
            },
            ...
        }
        scikit-package can recognize all <group-name> and <repo-name>.
        <repo-name> and <group-name> should all be unique across groups.
    """
    try:
        config = read_skpkg_config()
        candidates_from_config = config.get(
            "broadcast_target_candidates", None
        )
        candidates_repo_url = config.get(
            "broadcast_target_candidates_repo_url", None
        )
    except FileNotFoundError:
        candidates_from_config = None
    candidates_repo_url = Prompt.ask(
        "Please enter the url to the json file containing the information of "
        "target repositories",
        default=candidates_repo_url,
    )
    candidates_from_repo = None
    if candidates_repo_url:
        with TemporaryDirectory() as tmpdir:
            subprocess.run(
                [
                    "git",
                    "clone",
                    candidates_repo_url,
                ],
                cwd=tmpdir,
                check=True,
                capture_output=True,
            )
            for file in Path(tmpdir).glob("*.json"):
                if file.name == json_name:
                    with file.open() as f:
                        candidates_from_repo = json.load(f)
    if candidates_from_repo and candidates_from_config:
        # candidates found in both places
        return (
            candidates_from_repo,
            candidates_from_config,
        )
    elif candidates_from_repo and (not candidates_from_config):
        # candidates found in repo only.
        # Don't warn the user since candidates in config are optional.
        return candidates_from_repo, None
    elif (not candidates_from_repo) and candidates_from_config:
        # candidates found in config only.
        if candidates_repo_url:
            warnings.warn(
                f"\nNo json file found in {candidates_repo_url}. "
                "Please ensure the URL is correct and the file exists. "
                "broadcast_candidates from ~/.skpkgrc will be used.\n",
                UserWarning,
            )
        else:
            warnings.warn(
                "\nNo URL provided to fetch the json file. "
                "broadcast_candidates from ~/.skpkgrc will be used.\n",
                UserWarning,
            )
        return None, candidates_from_config
    else:
        # no candidates found in both places
        raise FileNotFoundError(
            "No broadcast candidates found. "
            f"Please ensure the URL is correct and {json_name} exists. "
            "Or set broadcast_candidates in your ~/.skpkgrc file."
        )


def _get_broadcast_target_url(candidates_from_url, candidates_from_config):
    """Prompt the user to select target repositories or groups.

    Multiple groups and repositories can be selected by separating names
    with commas.
    """

    def process_single(candidates):
        repo_dict = defaultdict(list)
        dict_to_print = defaultdict(list)
        if candidates:
            for group_name, group_repos in candidates.items():
                for repo_name, repo_url in group_repos.items():
                    repo_dict[group_name].append(repo_url)
                    dict_to_print[group_name].append(repo_name)
                    if repo_name not in repo_dict:
                        repo_dict[repo_name].append(repo_url)
            return repo_dict, dict_to_print
        else:
            return {}, {}

    def save_update_dict(dict1, dict2):
        """Update dict1 with dict2 without overwriting existing keys."""
        for key in dict2:
            if key not in dict1:
                dict1[key] = dict2[key]
        return dict1

    repos_from_url, print_dict_from_url = process_single(candidates_from_url)
    repos_from_config, print_dict_from_config = process_single(
        candidates_from_config
    )
    repos_dict = save_update_dict(repos_from_url, repos_from_config)
    dict_to_print = save_update_dict(
        print_dict_from_url, print_dict_from_config
    )
    print_list = list(dict_to_print.items())
    print_content = (
        "The broadcast candidates are:\n"
        "|---------------|--------------------|\n"
        "|  Group Name   |   Repository Names |\n"
        "|---------------|--------------------|\n"
        + "".join(
            [
                f"|{group_name.center(15) if i == 0 else " "*15}"
                f"|{repo_names.center(20)}|\n"
                for group_name, repo_names in print_list
                for (i, repo_names) in enumerate(repo_names)
            ]
        )
        + "|---------------|--------------------|\n"
    )
    target_repos = Prompt.ask(
        print_content + "\n"
        "Please enter the targeted group names and repo names.\n"
        "(Each name should be separated by a comma)"
    )
    target_repos = [
        repo.strip() for repo in target_repos.split(",") if repo.strip() != ""
    ]
    try:
        target_urls = []
        for name in target_repos:
            target_urls.extend(repos_dict[name])
    except KeyError as e:
        raise KeyError(
            f"{e} not found in broadcast candidates. "
            "Please ensure the name is correct."
        ) from e
    target_urls = list(set(target_urls))
    return target_urls


def _broadcast_issue(issue_content, target_urls):
    token = os.environ.get("GITHUB_TOKEN", None)
    if not token:
        raise ValueError(
            "No 'GITHUB_TOKEN' found in your environment variables. "
            "Please set it as instructed in the documentation."
        )
    console = Console()
    for url in target_urls:
        api_url, (owner, repo) = _get_post_issue_api_from_repo_url(url)
        confirm = Confirm.ask(
            f"Do you want to broadcast the issue to {owner}/{repo}?",
            default=True,
        )
        if confirm:
            console.print(f"Broadcasting issue to {owner}/{repo}...")
            headers = {
                "Authorization": f"token {token}",
                "Accept": "application/vnd.github.v3+json",
            }
            data = {
                "title": issue_content["title"],
                "body": issue_content["body"],
            }
            response = requests.post(api_url, headers=headers, json=data)
            if response.status_code == 201:
                console.print(
                    f"[green]Successfully broadcasted issue to "
                    f"{owner}/{repo}.[/green]"
                )
            else:
                console.print(
                    f"[red]Failed to broadcast issue to {owner}/{repo}. "
                    f"Status code: {response.status_code}. "
                    f"Response: {response.text}[/red]"
                    f"Broadcasting continues..."
                )
        else:
            console.print(
                f"[yellow]Skipped broadcasting issue to {owner}/{repo}."
                "[/yellow]"
            )
            continue
    console.print("[bold green]Broadcasting completed.[/bold green]")


def _parse_repo_url(url):
    parsed = urlparse(url)
    path_parts = parsed.path.strip("/").split("/")
    if len(path_parts) < 2:
        raise ValueError(f"Invalid GitHub repository URL: {url}")
    owner = path_parts[0]
    repo = path_parts[1]
    return path_parts, owner, repo


def _get_get_issue_api_from_issue_url(issue_url):
    path_parts, owner, repo = _parse_repo_url(issue_url)
    issue_number = int(path_parts[3])
    api_url = (
        f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
    )
    return api_url, (owner, repo, issue_number)


def _get_post_issue_api_from_repo_url(repo_url):
    path_parts, owner, repo = _parse_repo_url(repo_url)
    api_url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    return api_url, (owner, repo)
