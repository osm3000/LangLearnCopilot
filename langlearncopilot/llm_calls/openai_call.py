import openai
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# API key handling: check if already set, if not, raise error
try:
    openai.api_key = os.getenv("OPENAI_API_KEY")
except ValueError:
    raise ValueError("OPENAI_API_KEY not set.")


# Wrap the prompt in the data-structure that OpenAI expects
def _wrap_prompt(prompt_to_send: str, language: str = "french"):
    """
    Wrap the prompt in the data-structure that OpenAI expects

    Example:
    prompt_to_send = "Hello, I am a"
    language = "french"
    _wrap_prompt(prompt_to_send=prompt_to_send, language=language)
    """
    return [
        {
            "role": "system",
            "content": f"You are an excellent {language} teacher",
        },
        {
            "role": "user",
            "content": prompt_to_send,
        },
    ]


# OpenAI API call
def call_openai(prompt_to_send):
    open_ai_data_struct = _wrap_prompt(prompt_to_send=prompt_to_send)

    model_works_fine: bool = False  # TODO: Unused for now
    model_response: str = None

    model_response = openai.ChatCompletion.create(
        model="gpt-4-0314",
        messages=open_ai_data_struct,
        temperature=0.7,
        max_tokens=512,
        # top_p=1,
        # frequency_penalty=0,
        # presence_penalty=0,
        # stop=["\n"]
    )["choices"][0]["message"]["content"]
    model_works_fine = True

    return model_response, model_works_fine
