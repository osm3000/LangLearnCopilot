import os


def set_openai_key(key: str):
    """
    Set OPENAI_API_KEY environment variable and initialize OpenAI object
    """
    os.environ["OPENAI_API_KEY"] = key
