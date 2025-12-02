import re

pattern = r'\b[+-]?[0-9]+\b'

def match(text):
    if re.search(pattern, text):
        print("valid integer number")
    else:
        print("invalid integer number")

text = input("enter integer number: ")
match(text)
