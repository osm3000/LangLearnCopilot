import openai
import os
import logging
import dotenv

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def _configure_openai_key():
    """
    Set OPENAI_API_KEY environment variable and initialize OpenAI object
    """
    openai_key = os.getenv("OPENAI_API_KEY", None)
    if openai_key is None:
        logger.info(
            "Can't find OPENAI_API_KEY environment variable. Checking the .env file."
        )
        dotenv.load_dotenv()
        openai_key = os.getenv("OPENAI_API_KEY", None)
        if openai_key is None:
            raise ValueError(
                """
                             OPENAI_API_KEY not set. Can't find it in the .env file either.\n
                             You can also set the key by call langlearncopilot.llm_calls.set_openai_key(key="YOUR_KEY")
                             """
            )

    openai.api_key = openai_key


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
    # Setup the OpenAI API key
    _configure_openai_key()

    open_ai_data_struct = _wrap_prompt(prompt_to_send=prompt_to_send)

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

    return model_response
