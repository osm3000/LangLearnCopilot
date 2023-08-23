import yaml
import pathlib
import logging
from typing import List

from ..llm_calls import call_openai
from ..parsers import phrase_parser, word_parser


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

####################################################################################################
# Get the current directory path
# Load the prompt template
####################################################################################################
current_directory = str(pathlib.Path(__file__).parent.absolute())
with open(f"{current_directory}/configs/prompts.yml", "r") as f:
    PROMPT_TEMPLATE = yaml.safe_load(f)


def generate_unique_words(article: str):
    global PROMPT_TEMPLATE
    relevant_settings = PROMPT_TEMPLATE["generate_unique_words"]
    relevant_prompt = relevant_settings["prompt"]

    logging.info(f"Prompt to submit: {relevant_prompt.format(article=article)}")
    # Call OpenAI
    model_response = call_openai(prompt_to_send=relevant_prompt.format(article=article))

    # Parse the response
    parsed_model_response = word_parser(llm_output=model_response)

    # Print the response
    logging.info(f"Parsed response:\n{parsed_model_response}")

    return parsed_model_response


def generate_phrases(word: str):
    global PROMPT_TEMPLATE
    relevant_settings = PROMPT_TEMPLATE["generate_phrases"]
    relevant_prompt = relevant_settings["prompt"]

    logging.info(f"Prompt to submit: {relevant_prompt.format(word=word)}")

    # Call OpenAI
    model_response = call_openai(prompt_to_send=relevant_prompt.format(word=word))

    # Print the response

    # Parse the response
    parsed_model_response = phrase_parser(word=word, llm_output=model_response)

    # Print the parsed response
    logging.info(f"Parsed model response:\n{parsed_model_response}")

    return parsed_model_response


def generate_phrase_for_multiple_words(list_of_words: List[str], separator: str = None):
    """ """
    # Extract the actual words from the list of words - assume there is a translation for each word, separated by a ;
    if separator is not None:
        list_of_words = [word.split(separator)[0] for word in list_of_words]

    # Generate the phrases for each word
    phrases = []
    for word in list_of_words:
        phrases += generate_phrases(word=word)

    return phrases
