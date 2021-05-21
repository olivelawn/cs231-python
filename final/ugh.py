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

def appearance(text):
 return parts.get(text)

parts=Counter({'of': 4, 'the': 3, 'great': 3, '': 2, 'Urantia': 2, '0': 2, 'The': 1, 'Book': 1, '1': 1, 'IN': 1, 'THE': 1, 'MINDS': 1, 'mortals': 1, 'that': 1, 'being': 1, 'name': 1, 'your': 1, 'world': 1, 'there': 1, 'exists': 1, 'confusion': 1, 'respecting': 1, 'meaning': 1, 'such': 1})

#import pdb; pdb.set_trace()
print(max(parts,key=appearance))
