from unittest.mock import patch

from langlearncopilot.generators.main import (
    PROMPT_TEMPLATE,
    generate_phrase_for_multiple_words,
    generate_phrases,
    generate_unique_words,
)


def test_generate_unique_words():
    article = "Bonjour, je m'appelle Jean. Je suis un étudiant à l'université de Paris."
    relevant_settings = PROMPT_TEMPLATE["generate_unique_words"]
    relevant_prompt = relevant_settings["prompt"].format(
        article=article, language="french"
    )
    with patch("langlearncopilot.generators.main.call_openai") as mock_call_openai:
        example = [
            "Bonjour; Hello",
            "je; I",
            "m'appelle; am called",
            "suis; am",
            "un; a",
            "étudiant; student",
            "à; at",
            "l'université; the university",
            "de; of",
        ]
        output = {
            "bonjour": "hello",
            "je": "i",
            "m'appelle": "am called",
            "suis": "am",
            "un": "a",
            "étudiant": "student",
            "à": "at",
            "l'université": "the university",
            "de": "of",
        }

        mock_call_openai.return_value = "\n".join(example)
        unique_words = generate_unique_words(article=article, language="french")
        assert unique_words == output

        mock_call_openai.assert_called_once_with(prompt_to_send=relevant_prompt)


def test_generate_phrases():
    word = "test"
    relevant_settings = PROMPT_TEMPLATE["generate_phrases"]
    relevant_prompt = relevant_settings["prompt"].format(word=word, language="french")
    with patch("langlearncopilot.generators.main.call_openai") as mock_call_openai:
        mock_call_openai.return_value = """
        French phrase here ; English translation here\n
        Another French phrase here ; Another English translation here\n
        Yet another French phrase here ; Yet another English translation here\n
        """
        phrases = generate_phrases(word=word, language="french")
        assert len(phrases) == 3
        assert word == phrases[0]["word"]
        assert word == phrases[1]["word"]
        assert word == phrases[2]["word"]

        mock_call_openai.assert_called_once_with(prompt_to_send=relevant_prompt)


def test_generate_phrase_for_multiple_words():
    list_of_words = ["test", "word", "phrase"]
    with patch("langlearncopilot.generators.main.call_openai") as mock_call_openai:
        mock_call_openai.return_value = """
        French phrase here ; English translation here\n
        Another French phrase here ; Another English translation here\n
        Yet another French phrase here ; Yet another English translation here\n
        """

        phrases = generate_phrase_for_multiple_words(
            list_of_words=list_of_words, language="french"
        )

        assert len(phrases) == 9
        assert list_of_words[0] == phrases[0]["word"]
        assert list_of_words[1] == phrases[3]["word"]
        assert list_of_words[2] == phrases[6]["word"]
        # mock_generate_phrases.assert_any_call(word="test", language="french")
        # mock_generate_phrases.assert_any_call(word="word", language="french")
        # mock_generate_phrases.assert_any_call(word="phrase", language="french")
