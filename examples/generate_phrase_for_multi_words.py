from langlearncopilot import generators

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
    language="french",
)
