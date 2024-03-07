#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    space = 0
    while space < len(text) and space == " ":
        space += 1

    while space < len(text):
        print(text[space], end="")
        if text[space] == "\n" or text[space] in ":.?":
            if text[space] in ":.?":
                print("\n")
            space += 1
            while space < len(text) and text[space] == " ":
                space += 1
            continue
        space += 1