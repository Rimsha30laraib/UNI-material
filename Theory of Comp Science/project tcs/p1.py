import re

id_re = r'(a)+(b)+'

def match(text):
    if re. search (id_re, text):
        print ("valid cnic number")
    else:
        print ("invalid cnic number")

text=input ("enter cnic: ")

match(text)