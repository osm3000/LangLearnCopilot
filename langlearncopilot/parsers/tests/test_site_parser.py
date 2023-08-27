"""
Test the site parser module.
"""

from langlearncopilot.parsers.site_parser import (
    _clean_text,
    _get_soup,
    get_text_from_webpage,
)


def test_clean_text():
    """
    Test the _clean_text function.
    """
    text = [
        "1. This is a line",
        "" "2. This is another line",
        "\n",
        "Hello this is me indeed    ",
        "   It is me again    ",
    ]
    expected = [
        "1. This is a line",
        "2. This is another line",
        "Hello this is me indeed",
        "It is me again",
    ]

    assert _clean_text(text) == expected


def test_get_soup():
    """
    Test the _get_soup function.
    """
    url = "https://www.allendowney.com/wp/"
    soup = _get_soup(url)
    assert soup.title.string == "Allen Downey"


def test_get_text_from_webpage():
    """
    Test the get_text_from_webpage function.
    """
    # Mock the _get_soup function
    url = "https://www.python.org/"

    text = get_text_from_webpage(url)
    assert (
        "Python source code and installers are available for download for all versions!"
        in text
    )
