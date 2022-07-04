#!/usr/bin/python3
def text_indentation(text):
    """Prints text with 2 new lines after '.', '?' and ':'"""
    char = ['.', '?', ':']
    if type(text) != str:
        raise TypeError("text must be a string")
    for x in text:
        print(x, end='')
        if x in char:
            print('\n\n', end='')
