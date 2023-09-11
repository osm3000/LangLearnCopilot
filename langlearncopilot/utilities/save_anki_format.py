from ..datatypes import (
    MULTIPLE_PHRASES_TRANSLATION,
    TEXT_TRANSLATION,
    OPTIONAL_TEXT,
)


def save_multi_phrase(
    data: MULTIPLE_PHRASES_TRANSLATION,
    file_path: OPTIONAL_TEXT = None,
):
    # Check if the data is a TEXT_TRANSLATION or MULTIPLE_PHRASES_TRANSLATION
    final_data = []
    for item in data:
        final_data.append(f"{item['word']}; {item['phrase']}; {item['translation']}")

    # Save the data to a csv file
    if file_path is not None:
        with open(file_path, "w") as f:
            f.write("\n".join(final_data))

    return final_data


def save_unique_words(
    data: TEXT_TRANSLATION,
    file_path: OPTIONAL_TEXT = None,
):
    # Check if the data is a TEXT_TRANSLATION or MULTIPLE_PHRASES_TRANSLATION
    final_data = []
    for key, value in data.items():
        final_data.append(f"{key}; {value}")

    # Save the data to a csv file
    if file_path is not None:
        with open(file_path, "w") as f:
            f.write("\n".join(final_data))

    return final_data
