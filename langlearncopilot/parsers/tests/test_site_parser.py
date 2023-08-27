"""
Test the site parser module.
"""

import pytest
from unittest.mock import patch
from langlearncopilot.parsers.site_parser import clean_text, get_soup, get_text


def test_clean_text():
    """
    Test the clean_text function.
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

    assert clean_text(text) == expected


def test_get_soup():
    """
    Test the get_soup function.
    """
    url = "https://www.allendowney.com/wp/"
    soup = get_soup(url)
    assert soup.title.string == "Allen Downey"


def test_get_text():
    """
    Test the get_text function.
    """
    # Mock the get_soup function
    url = "https://www.python.org/"

    text = get_text(url)
    assert (
        "Python source code and installers are available for download for all versions!"
        in text
    )
