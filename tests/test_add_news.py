from types import SimpleNamespace

import pytest
import requests

from scikit_package.cli.add import news_item


def _setup_news_test_env(tmp_path, mocker):
    """Set up a temporary news directory and template file for
    testing."""
    test_news_dir = tmp_path / "news"
    test_news_dir.mkdir()
    # Locate the real TEMPLATE.rst file in the project root
    template_file_gh_url = (
        "https://raw.githubusercontent.com/scikit-package/"
        "scikit-package/main/news/TEMPLATE.rst"
    )
    response = requests.get(template_file_gh_url, timeout=(3.0, 5.0))
    response.raise_for_status()
    test_template_file = test_news_dir / "TEMPLATE.rst"
    test_template_file.write_text(response.text)
    # Mock the paths and the branch
    mocker.patch("scikit_package.cli.add.NEWS_DIR", str(test_news_dir))
    mocker.patch(
        "scikit_package.cli.add.TEMPLATE_PATH", str(test_template_file)
    )
    branch_name = "test-branch"
    mocker.patch(
        "scikit_package.utils.auth.get_current_branch",
        return_value=branch_name,
    )
    news_file = test_news_dir / f"{branch_name}.rst"
    return news_file


def test_add_news_item(tmp_path, mocker):
    """Test adding a news item to the news file."""
    try:
        news_file = _setup_news_test_env(tmp_path, mocker)
    except requests.RequestException as exc:
        pytest.skip(f"Cannot fetch `TEMPLATE.rst` from GitHub: {exc}")
    # Mimic `package add --add -m "Add first news."`
    args1 = SimpleNamespace(
        add=["Add first news."],
        change=None,
        deprecate=None,
        remove=None,
        fix=None,
        security=None,
        no_news=None,
    )
    news_item(args1)
    expected_content_1 = """**Added:**

* Add first news.

**Changed:**

* <news item>

**Deprecated:**

* <news item>

**Removed:**

* <news item>

**Fixed:**

* <news item>

**Security:**

* <news item>
"""
    content_1 = news_file.read_text()
    assert content_1.strip() == expected_content_1.strip()
    # Mimic `package add news --add "Add second news."`
    args2 = SimpleNamespace(
        add=["Add second news."],
        change=None,
        deprecate=None,
        remove=None,
        fix=None,
        security=None,
        no_news=None,
    )
    news_item(args2)
    expected_content_2 = """**Added:**

* Add second news.
* Add first news.

**Changed:**

* <news item>

**Deprecated:**

* <news item>

**Removed:**

* <news item>

**Fixed:**

* <news item>

**Security:**

* <news item>
"""
    content_2 = news_file.read_text()
    assert content_2.strip() == expected_content_2.strip()


def test_no_news_item(tmp_path, mocker):
    """Test adding "no news" item to the news file."""
    try:
        news_file = _setup_news_test_env(tmp_path, mocker)
    except requests.RequestException as exc:
        pytest.skip(f"Cannot fetch `TEMPLATE.rst` from GitHub: {exc}")
    # Mimic `package add --no-news "Fix small typo."`
    args = SimpleNamespace(
        add=None,
        change=None,
        deprecate=None,
        remove=None,
        fix=None,
        security=None,
        no_news=["Fix small typo."],
    )
    news_item(args)
    expected_content = """**Added:**

* No news added: Fix small typo.

**Changed:**

* <news item>

**Deprecated:**

* <news item>

**Removed:**

* <news item>

**Fixed:**

* <news item>

**Security:**

* <news item>
"""
    content = news_file.read_text()
    assert content.strip() == expected_content.strip()
