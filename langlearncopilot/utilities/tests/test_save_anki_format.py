import os

import pytest

from langlearncopilot.utilities.save_anki_format import (
    save_multi_phrase,
    save_unique_words,
)


@pytest.fixture
def file_path(tmp_path):
    # Create a temporary file path
    file_path = os.path.join(tmp_path, "test.csv")
    yield file_path
    # Remove the file after the test is done
    os.remove(file_path)


def test_save_multi_phrase(file_path):
    # Define test data
    data = [
        {"word": "hello", "phrase": "hello world", "translation": "bonjour le monde"},
        {
            "word": "goodbye",
            "phrase": "goodbye world",
            "translation": "au revoir le monde",
        },
    ]

    # Call the function
    formatted_data = save_multi_phrase(data, file_path)

    # Check if the file was created and contains the expected data
    with open(file_path, "r") as f:
        assert (
            f.read()
            == "hello; hello world; bonjour le monde\ngoodbye; goodbye world; au revoir le monde"
        )

    assert isinstance(formatted_data, list)
    assert len(formatted_data) == 2


def test_save_unique_words(file_path):
    # Define test data
    data = {"hello": "bonjour", "world": "monde"}

    # Call the function
    formatted_data = save_unique_words(data, file_path)

    # Check if the file was created and contains the expected data
    with open(file_path, "r") as f:
        assert f.read() == "hello; bonjour\nworld; monde"

    assert isinstance(formatted_data, list)
    assert len(formatted_data) == 2


def test_save_unique_words_without_file():
    # Define test data
    data = {"hello": "bonjour", "world": "monde"}

    # Call the function
    formatted_data = save_unique_words(data)

    assert isinstance(formatted_data, list)
    assert len(formatted_data) == 2


def test_save_multi_phrase_without_file():
    # Define test data
    data = [
        {"word": "hello", "phrase": "hello world", "translation": "bonjour le monde"},
        {
            "word": "goodbye",
            "phrase": "goodbye world",
            "translation": "au revoir le monde",
        },
    ]

    # Call the function
    formatted_data = save_multi_phrase(data)

    assert isinstance(formatted_data, list)
    assert len(formatted_data) == 2
