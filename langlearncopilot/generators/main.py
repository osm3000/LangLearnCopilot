import yaml
import pathlib
from ..llm_calls import call_openai

# Get the current directory path
current_directory = str(pathlib.Path(__file__).parent.absolute())

# Load the prompt template
with open(f"{current_directory}/configs/prompts.yml", "r") as f:
    PROMPT_TEMPLATE = yaml.safe_load(f)

def generate_phrases(word:str):
    global PROMPT_TEMPLATE
    relevant_settings = PROMPT_TEMPLATE["generate_phrases"]
    relevant_prompt = relevant_settings["prompt"]
    
    print("Prompt to submit: ", relevant_prompt.format(word=word))
    # Call OpenAI
    model_response, model_works_fine = call_openai(prompt_to_send=relevant_prompt.format(word=word))

    # Print the response
    print("Model response: ", model_response)