import re

# Updated pattern to ensure the identifier ends with an alphabet or digit
pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*[a-zA-Z0-9]$'

def match(text):
    if re.fullmatch(pattern, text):
        print("valid identifier")
    else:
        print("invalid identifier")

text = input("Enter identifier: ")
match(text)
