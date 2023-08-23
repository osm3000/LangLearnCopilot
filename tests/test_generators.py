from langlearncopilot.generators.main import generate_phrase_for_multiple_words
from unittest.mock import patch
from langlearncopilot.generators.main import (
    generate_unique_words,
    generate_phrase_for_multiple_words,
    generate_phrases,
    PROMPT_TEMPLATE,
)


def test_generate_unique_words():
    article = "Bonjour, je m'appelle Jean. Je suis un étudiant à l'université de Paris."
    relevant_settings = PROMPT_TEMPLATE["generate_unique_words"]
    relevant_prompt = relevant_settings["prompt"]
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

        mock_call_openai.return_value = "\n".join(example)
        unique_words = generate_unique_words(article)
        assert set(unique_words) == set(example)

        mock_call_openai.assert_called_once_with(
            prompt_to_send=relevant_prompt.format(article=article)
        )


def test_generate_phrases():
    word = "test"
    relevant_settings = PROMPT_TEMPLATE["generate_phrases"]
    relevant_prompt = relevant_settings["prompt"]
    with patch("langlearncopilot.generators.main.call_openai") as mock_call_openai:
        mock_call_openai.return_value = """
        French phrase here ; English translation here\n
        Another French phrase here ; Another English translation here\n
        Yet another French phrase here ; Yet another English translation here\n
        """
        phrases = generate_phrases(word)
        assert len(phrases) == 3
        assert word in phrases[0]
        assert word in phrases[1]
        assert word in phrases[2]
        # assert "This is a test phrase" in phrases
        # assert "Another test phrase" in phrases
        # assert "Yet another test phrase" in phrases

        mock_call_openai.assert_called_once_with(
            prompt_to_send=relevant_prompt.format(word=word)
        )


def test_generate_phrase_for_multiple_words():
    list_of_words = ["test", "word", "phrase"]
    with patch(
        "langlearncopilot.generators.main.generate_phrases"
    ) as mock_generate_phrases:
        mock_generate_phrases.return_value = [
            "This is a test phrase",
            "Another test phrase",
            "Yet another test phrase",
        ]
        phrases = generate_phrase_for_multiple_words(list_of_words)
        assert len(phrases) == 9
        assert "This is a test phrase" in phrases
        assert "Another test phrase" in phrases
        assert "Yet another test phrase" in phrases
        mock_generate_phrases.assert_any_call(word="test")
        mock_generate_phrases.assert_any_call(word="word")
        mock_generate_phrases.assert_any_call(word="phrase")
