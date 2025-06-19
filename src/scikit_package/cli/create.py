from scikit_package.utils import cookie

# SKPKG_GITHUB_URL = "https://github.com/scikit-package/scikit-package"
SKPKG_GITHUB_URL = "https://github.com/ycexiao/scikit-package"


def package(args):
    subcmd = args.subcommand
    if subcmd == "workspace":
        cookie.run(f"{SKPKG_GITHUB_URL}-workspace")
    elif subcmd == "system":
        cookie.run(f"{SKPKG_GITHUB_URL}-system")
    elif subcmd == "public":
        cookie.run(SKPKG_GITHUB_URL)
    elif subcmd == "conda-forge":
        cookie.run(f"{SKPKG_GITHUB_URL}-conda-forge")
    elif subcmd == "manuscript":
        cookie.run(f"{SKPKG_GITHUB_URL}-manuscript")
