import nltk
import re

# Download NLTK resources if not already downloaded
nltk.download('punkt')

# Define the regular expressions
arithmetic_operators_regex = r'\*|\-|\/|\+|\^'
digit_re = r'([+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?)'
rel_op_re = r'\>|\<|\>=|\<=|\=='
equal_re=r'='
log_op_re=r'and|or|not'
sp_sym_re = r'\{|\}|\[|\]|\;|\(|\)|\_'
conditional_re=r'if|else|elif'
loop_re = r'iter'
print_re = r'print'
input_re = r'input'
data_type_re = r'num'
id_re=r'^#[a-zA-Z]+[0-9]*([_]?[a-zA-Z0-9])*|\S+'
# Test string containing arithmetic operators, digits, and other symbols
test_string = "iter(num #i = 0; #i < 0.99e45 ; #i = #i + 1) elif or input print"

# Tokenize the test string using NLTK
tokens = nltk.word_tokenize(test_string)

# Classify each token based on the regular expressions
for token in tokens:
    if re.match(arithmetic_operators_regex, token):
        print(f"'{token}'  : {token}")
    elif re.match(digit_re, token):
        print(f"'{token}': VALUE")
    elif re.match(conditional_re, token):
        print(f"'{token}' : {token.upper()}")
    elif re.match(rel_op_re, token):
        print(f"'{token}': {token}")
    elif re.match(equal_re, token):
        print(f"'{token}': {token}")
    elif re.match(log_op_re, token):
        print(f"'{token}': {token.upper()}")
    elif re.match(sp_sym_re, token):
        print(f"'{token}' : {token}")
    elif re.match(data_type_re, token):
        print(f"'{token}' : DT")
    elif re.match(loop_re, token):
        print(f"'{token}' : LOOP ")
    elif re.match(input_re, token):
        print(f"'{token}' : KEYWORD")
    elif re.match(print_re, token):
        print(f"'{token}' : KEYWORD")
    elif re.match(id_re, token):
        print(f"'{token}' : ID")
    else:
        print(f"'{token}' does not belong to any defined class.")
