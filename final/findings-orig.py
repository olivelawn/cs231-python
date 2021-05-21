#!/usr/local/bin/python3

# CS131B final exam: Send in a plain text file that describes how and why
#  this program produces the output that it does.
#
# about Counter: https://docs.python.org/3/library/collections.html
# about Urantia: https://en.wikipedia.org/wiki/The_Urantia_Book
#


#
# 0. tools
from re import split
from urllib.request import urlopen as access
from collections import Counter


#
# 1. resources
terms = set(open('/users/abrick/resources/english').read().split('\n'))
material = access('http://hills.ccsf.edu/~abrick/urantia').read().decode()
#material = open('urantia').read()
parts = Counter(split(r',?[\s.:"-]+',material))


#
# 2. interpretations
def digits(text):
 try:
  return int(text.strip().replace(',',''))
 except ValueError:
  return 0

def appearance(text):
 return parts.get(text)

def surprise_appearance(text):
 return 0 if digits(text) or text.lower() in terms else parts.get(text)


#
# 3. analysis
findings = []
import pdb; pdb.set_trace()
for concern in [appearance,len,digits,str,surprise_appearance]:
 findings.append(str(max(parts,key=concern)))
print(' '.join(findings)+'.')


