# LangLearnCopilot
LangLearnCopilot is a collection of functions and tools, to generate content in a proper format, to help you learn a new language.

For now, I am focusing on French (my personal interesting) and Spanish (for friends).

While this is a standalone library, my advice is, for the best results, to use its outcomes hand-in-hand with the awesome flashcards application, [Anki](https://apps.ankiweb.net/)

The main two applications at the moment

## Installation
Soon, pretty simple: `pip install langlearncopilot`

## Usage
You can find examples in the `./examples` folder

Note: you need to set your OpenAI key first. If the `OPENAI_API_KEY` is declared already as an environment variable, or exisiting in the current folder in a `.env` file, then the package will find it.

Other wise, you can set it manually by calling
```python
from langlearncopilot.llm_calls import set_openai_key

set_openai_key("ENTER KEY VALUE HERE")
```

### Given a text, extract all the unique words and its translation from that text
```python
from langlearncopilot import generators

generators.generate_unique_words(
    article="Bonjour, je m'appelle Jean. Je suis un étudiant à l'université de Paris."
)
```
returns
```
[
    'Bonjour; Hello',
    'je; I',
    "m'appelle; call myself",
    'suis; am',
    'un; a',
    'étudiant; student',
    'à; at',
    "l'université; the university",
    'de; of'
]
```

### Given a word, generate 3 phrases that are using these words
```python
from langlearncopilot import generators

generators.generate_phrases("combien")
```

returns
```
[
    'combien ; Combien de pommes voulez-vous acheter ? ; How many apples do you want to buy?',
    'combien ; Combien coûte cette robe ? ; How much does this dress cost?',
    'combien ; Combien de temps dure le film ? ; How long does the movie last?'
]
```

### Extract unique words from URL, with their translation
TBD
