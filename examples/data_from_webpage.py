from langlearncopilot.generators import generate_unique_words
from langlearncopilot.parsers import get_text_from_webpage


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
