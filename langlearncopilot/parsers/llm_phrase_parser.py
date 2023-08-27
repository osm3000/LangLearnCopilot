from ..datatypes import TEXT_TRANSLATION, MULTIPLE_PHRASES_TRANSLATION


def _insert_word_before_phrases_group(word: str, phrases_group: list):
    """
    Insert the word before each phrase in the phrases_group
    """
    return [f"{word.lower()} ; {phrase}" for phrase in phrases_group]


def _clean_one_phrases_group(phrases_group_str: str):
    """
    Remove empty lines, starting digits, and phrases that doesn't comply with the `;` separator
    """

    # Remove empty lines
    phrases_group = [line for line in phrases_group_str.split("\n") if len(line) > 0]
    # print(f"phrases_group: {phrases_group}")

    # Remove starting digits
    phrases_group = [line for line in phrases_group if not line[0].isdigit()]

    # Remove the starting - or . if present
    phrases_group = [
        line[1:] if line[0] in ["-", "."] else line for line in phrases_group
    ]
    # print(phrases_group)

    # Remove phrases_group that doesn't comply with the `;` separator
    phrases_group = [line for line in phrases_group if line.count(";") == 1]

    return phrases_group


def phrase_parser(word: str, llm_output: str) -> MULTIPLE_PHRASES_TRANSLATION:
    """
    Remove the artifacts from the LLM output.
    Convert the phrases generated by the LLM into a list of phrases.
    """
    # Remove the artifacts from the LLM output
    llm_output_clean = (
        llm_output.replace("b'", "").replace("\\n", "\n").replace("\\", "")
    )

    phrases_output = _clean_one_phrases_group(llm_output_clean)

    # Make a list of dictionaries: [{word: {phrase: ..., translation: ...}}, ...]
    phrases_dicts: MULTIPLE_PHRASES_TRANSLATION = []
    for i, line in enumerate(phrases_output):
        phrase, translation = line.split(";")
        phrases_dicts.append({word: {"phrase": phrase, "translation": translation}})

    # print(phrases_dicts)

    # Insert the word before each phrase in the phrases_group
    # phrases_output_final = _insert_word_before_phrases_group(word, phrases_output)

    # return phrases_output_final
    return phrases_dicts


def word_parser(llm_output: str) -> TEXT_TRANSLATION:
    """
    Remove the artifacts from the LLM output.
    Convert the words generated by the LLM into a list of words.
    """
    # Remove the artifacts from the LLM output
    llm_output_clean = (
        llm_output.replace("b'", "").replace("\\n", "\n").replace("\\", "")
    )

    words_output = _clean_one_phrases_group(llm_output_clean)

    # Build a dictionary of words and their translations
    words_dicts = {}
    for i, line in enumerate(words_output):
        word, translation = line.split(";")
        word = word.lower().strip()
        translation = translation.lower().strip()
        words_dicts[word] = translation

    # print(words_dicts)
    # return words_output
    return words_dicts
