import requests

from scikit_package.utils import cookie

SKPKG_GITHUB_URL = "https://github.com/scikit-package/scikit-package"


def _get_latest_tag(repo_url):
    api_url = (
        repo_url.replace(
            "https://github.com/", "https://api.github.com/repos/"
        )
        + "/tags"
    )
    response = requests.get(api_url)
    tags = response.json()
    return tags[0]["name"]


def package(args):
    subcmd = args.subcommand
    url_base = SKPKG_GITHUB_URL
    if subcmd == "workspace":
        cookie.run(f"{url_base}-workspace")
    elif subcmd == "system":
        cookie.run(f"{url_base}-system")
    elif subcmd == "public":
        cookie.run(url_base)
    elif subcmd == "conda-forge":
        cookie.run(f"{url_base}-conda-forge")
    elif subcmd == "manuscript":
        latest_tag = _get_latest_tag(SKPKG_GITHUB_URL)
        cookie.run(f"{url_base}-manuscript", latest_tag)
