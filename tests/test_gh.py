import json
import warnings
from pathlib import Path

import pytest

from scikit_package.cli.gh import (
    _get_broadcast_target_candidates,
    _get_broadcast_target_url,
)

dict_with_broadcast_candidates = {
    "scikit-package": {
        "public": "https://github.com/scikit-package/scikit-package",
        "system": "https://github.com/scikit-package/scikit-package-system",
        "manuscript": (
            "https://github.com/scikit-package/scikit-package-manuscript"
        ),
    }
}
dict_without_broadcast_candidates = {
    "some-key": "some-value",
}
config_with_broadcast_candidates = {
    "broadcast_target_candidates": dict_with_broadcast_candidates
}
config_without_broadcast_candidates = dict_without_broadcast_candidates


@pytest.mark.parametrize(
    "dict_from_repo, dict_from_config,  expected",
    [
        # Candidates are provided both in config and url repo.
        #     Expect two dicts.
        (
            dict_with_broadcast_candidates,
            config_with_broadcast_candidates,
            (
                dict_with_broadcast_candidates,
                dict_with_broadcast_candidates,
            ),
        ),
        # only candidates from URL is provided.
        #     Expect one  dict and None.
        (
            dict_with_broadcast_candidates,
            config_without_broadcast_candidates,
            (dict_with_broadcast_candidates, None),
        ),
    ],
)
def test_get_broadcast_candidates_dict(
    dict_from_repo, dict_from_config, expected, mocker
):
    def fake_clone_repo(*args, **kwargs):
        file_path = Path(kwargs["cwd"]) / "broadcast_candidates.json"
        with open(file_path, "w") as f:
            json.dump(dict_from_repo, f)

    mock_get_candidates_from_url = mocker.patch(
        "subprocess.run", side_effect=fake_clone_repo
    )
    mock_prompt = mocker.patch(
        "rich.prompt.Prompt.ask", return_value="some-url"
    )
    mock_get_candidates_from_config = mocker.patch(
        "scikit_package.cli.gh.read_skpkg_config",
        return_value=dict_from_config,
    )
    out = _get_broadcast_target_candidates()
    assert out == expected
    mock_get_candidates_from_url.assert_called_once()
    mock_prompt.assert_called_once()
    mock_get_candidates_from_config.assert_called_once()


def test_get_broadcast_candidates_dict_bad(mocker):
    # case 1: URL is not valid. Skipped since it is with subprocess.
    # case 2: broadcast_candidates.json found in config but not in the cloned
    #  repo. Expect warning.
    expected_error_msg = (
        "\nNo json file found in some-url. "
        "Please ensure the URL is correct and the file exists. "
        "broadcast_candidates from ~/.skpkgrc will be used.\n"
    )
    mock_prompt = mocker.patch(
        "rich.prompt.Prompt.ask", return_value="some-url"
    )

    def fake_clone_empty_repo(*args, **kwargs):
        # do not create broadcast_candidates.json
        return

    mock_get_no_candidates_from_repo = mocker.patch(
        "subprocess.run", side_effect=fake_clone_empty_repo
    )
    mock_get_candidates_from_config = mocker.patch(
        "scikit_package.cli.gh.read_skpkg_config",
        return_value=config_with_broadcast_candidates,
    )
    with warnings.catch_warnings(record=True) as w:
        _get_broadcast_target_candidates()
    has_warning_msg = False
    for warning in w:
        if expected_error_msg in str(warning.message):
            has_warning_msg = True
    assert has_warning_msg
    mock_get_no_candidates_from_repo.assert_called_once()
    mock_prompt.assert_called_once()
    mock_get_candidates_from_config.assert_called_once()

    # case 3: broadcast_candidates.json not found in both places.
    #  Expect FileNotFoundError.
    mock_get_no_candidates_from_config = mocker.patch(
        "scikit_package.cli.gh.read_skpkg_config",
        return_value=config_without_broadcast_candidates,
    )
    # Re-patch subprocess.run for the second case
    mocker.patch("subprocess.run", side_effect=fake_clone_empty_repo)
    with pytest.raises(
        FileNotFoundError,
        match=(
            "No broadcast candidates found. "
            "Please ensure the URL is correct and "
            "broadcast_candidates.json exists. "
            "Or set broadcast_candidates in your ~/.skpkgrc file."
        ),
    ):
        _get_broadcast_target_candidates()
    mock_get_no_candidates_from_config.assert_called_once()


@pytest.mark.parametrize(
    "candidates_from_url, candidates_from_config, expected_target_urls",
    [
        # Two groups found in the candidates_from_url, select one group and
        # one repo in another group. candidates_from_url also has one group
        # with the same name.
        # Expect only get repos from candidates_from_url and all
        # corresponding repo urls are returned.
        (
            {
                "scikit-package": {
                    "public": (
                        "https://github.com/scikit-package/scikit-package"
                    ),
                    "system": (
                        "https://github.com/scikit-package/"
                        "scikit-package-system"
                    ),
                    "manuscript": (
                        "https://github.com/scikit-package/"
                        "scikit-package-manuscript"
                    ),
                },
                "another-group": {
                    "repo-a": "some-url-a",
                    "workspace": (
                        "https://github.com/scikit-package/"
                        "scikit-package-workspace"
                    ),
                },
            },
            {
                "scikit-package": {
                    "outdated-local-group-repo": "some-url",
                }
            },
            [
                "https://github.com/scikit-package/scikit-package",
                "https://github.com/scikit-package/scikit-package-system",
                "https://github.com/scikit-package/scikit-package-manuscript",
                "https://github.com/scikit-package/scikit-package-workspace",
            ],
        )
    ],
)
def test_process_broadcast_candidates(
    candidates_from_url, candidates_from_config, expected_target_urls, mocker
):
    mock_prompt = mocker.patch(
        "rich.prompt.Prompt.ask", return_value="scikit-package, workspace"
    )
    target_urls = _get_broadcast_target_url(
        candidates_from_url, candidates_from_config
    )
    assert set(target_urls) == set(expected_target_urls)
    mock_prompt.assert_called_once()
