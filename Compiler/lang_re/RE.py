import re

# Updated pattern to ensure the identifier ends with an alphabet or digit
pattern = r'^[a-zA-Z][a-zA-Z0-9_]*[a-zA-Z0-9]$' #identifier re
# number_pattern=r'([+-]?[0-9]*(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?)'
pattern3 = r'^\"(\\?[a-zA-Z_])*\"|\"(\\[\\|\'|\"])*\"$' #StrChar re
# number_pattern = r'^[+-]?(\d*\.\d+|\d+\.\d*|\d+)([eE][+-]?\d+)?$'
identifier_pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'  # Corrected identifier pattern
number_pattern = r'^[+-]?(\d*\.\d+|\d+\.\d*|\d+)([eE][+-]?\d+)?$'  # Corrected number pattern
strchar_pattern = r'^\"(\\?[a-zA-Z_])*\"|\"(\\[\\|\'|\"])*\"$'  # StrChar re
def match(text):
    if re.match(number_pattern, text):
        print("valid identifier")
    else:
        print("invalid identifier")

text = input("Enter identifier: ")
match(text)

