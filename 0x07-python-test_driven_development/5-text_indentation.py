#!/usr/bin/python3
"""module prints text with 2 new lines after each ".", "?", and ":"""""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: .?:
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    list_lines = [lines.strip() for lines in text.split('\n')]
    new_text = "\n".join(list_lines)
    print(new_text, end="")
