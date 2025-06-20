import subprocess

from scikit_package.utils.io import get_config_cmd


def run(repo_url):
    run_cmd = ["cookiecutter", repo_url]
    config_cmd = get_config_cmd()
    run_cmd.extend(config_cmd)

    try:
        subprocess.run(
            run_cmd,
            check=True,
        )

    except subprocess.CalledProcessError as e:
        print(f"Failed to run scikit-package for the following reason: {e}")
