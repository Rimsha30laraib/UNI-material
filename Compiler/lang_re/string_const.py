import re

# Pattern to match exactly the newline character '\n'
pattern = r'^\"(\\?[a-zA-Z_])*\"|\"(\\[\\|\'|\"])*\"$'
A = r"[\\|'|\"]"

    # B: Set of characters that represent special sequences and cannot occur without a backslash
B = r"[bntro]"

    # C: Set of characters that do not require a backslash
C = r"[@+]"

    # D: Set of alphabetic characters and underscores (a-z, A-Z, _)
D = r"[a-zA-Z\s+_]"

char_const = rf"(\\{A}|\\{B}|{B}|{C}|{D})"

strchar_pattern = rf"^\"({char_const})*\"$"
def match(text):
    if re.fullmatch(strchar_pattern, text):
        print("Valid character")
    else:
        print("Invalid character")

text = input("Enter a character: ")
match(text)
