import requests
from bs4 import BeautifulSoup

from ..datatypes import TEXT, TEXT_SEQUENCE


def _clean_text(text: TEXT_SEQUENCE) -> TEXT_SEQUENCE:
    """
    Remove:
    1. Empty lines
    2. Starting digits
    3. The starting - or . if present
    4. Lines that has no letters
    5. Leading and trailing spaces
    6. Any URLs
    """
    # Remove empty lines
    text = [line for line in text if len(line) > 0]

    # Remove the starting - or . if present
    text = [line[1:] if line[0] in ["-", "."] else line for line in text]

    # Remove lines that has no letters
    text = [line for line in text if any(char.isalpha() for char in line)]

    # Remove leading and trailing spaces
    text = [line.strip() for line in text]

    return text


def _get_soup(url: TEXT) -> BeautifulSoup:
    """Returns a BeautifulSoup object from a given url."""
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def get_text_from_webpage(url: TEXT) -> TEXT:
    """Returns the text from a given url."""
    soup = _get_soup(url)
    text = soup.get_text()
    text_lines = text.split("\n")
    after_cleaning_text_lines = _clean_text(text_lines)
    after_cleaning_text = "\n".join(after_cleaning_text_lines)
    return after_cleaning_text


# def main():
#     url = "https://docs.python.org/3/library/html.parser.html#module-html.parser"
#     # print(use_html_parser(url))
#     print(get_text(url))

# if __name__ == "__main__":
#     main()
