[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)

# LangLearnCopilot
LangLearnCopilot is a collection of functions and tools, to generate content in a proper format, to help you learn a new language.

For now, I am focusing on French (my personal interesting) and Spanish (for friends).

While this is a standalone library, my advice is, for the best results, to use its outcomes hand-in-hand with the awesome flashcards application, [Anki](https://apps.ankiweb.net/)

The main two applications at the moment

## Installation
`pip install langlearncopilot`

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
{
    'bonjour': 'hello',
    'je': 'i',
    "m'appelle": 'is called',
    'suis': 'am',
    'un': 'a',
    'étudiant': 'student',
    'à': 'at',
    "l'université": 'university',
    'de': 'of'
}
```

### Given a word, generate 3 phrases that are using these words
```python
from langlearncopilot import generators

generators.generate_phrases("combien")
```

returns
```python
[
    {'combien': {'phrase': 'Combien de personnes sont venues à la fête?', 'translation': ' How many people came to the party?'}},
    {'combien': {'phrase': 'Combien coûte ce sac à dos?', 'translation': ' How much does this backpack cost?'}},
    {'combien': {'phrase': "Il m'a demandé combien de temps cela prendrait.", 'translation': ' He asked me how long it would take.'}}
]
```

### Extract unique words from URL, with their translation
```python
from langlearncopilot.parsers import get_text_from_webpage
from langlearncopilot.generators import generate_unique_words


def main():
    # Get text from a webpage
    text = get_text_from_webpage(
        url="https://www.lemonde.fr/planete/article/2023/08/27/comment-les-parcs-nationaux-americains-tentent-de-faire-face-aux-effets-du-rechauffement-climatique_6186696_3244.html"
    )
    # Generate unique words from the text
    words = generate_unique_words(article=text, language="french")
    print(words)


if __name__ == "__main__":
    main()

```
returns
```python
{
    'comment': 'how',
    'les': 'the',
    'parcs': 'parks',
    'nationaux': 'national',
    'américains': 'american',
    'tentent': 'try',
    'de': 'of',
    ...
}
```
