import sys

sys.path.append("..")

# from langlearncopilot.generators import generate_unique_words
from langlearncopilot import generators


# generators.generate_unique_words(
#     article="Bonjour, je m'appelle Jean. Je suis un étudiant à l'université de Paris."
# )

# generators.generate_phrase_for_multiple_words(
#     list_of_words=["Paris", "étudiant", "université"]
# )

generators.generate_phrase_for_multiple_words(
    list_of_words=[
        "Bonjour; hello",
        "je; I",
        "m'appelle; am called",
        "suis; am",
        "un; a",
        "étudiant; student",
        "à; at",
        "l'; the",
        "université; university",
        "de; of",
    ],
    separator=";",
)
