#!/usr/local/bin/python3
import sys
import re

# lets not mess with original argv.
args_list = sys.argv
# delete program itself from the list
del args_list[0]

if args_list:
  filename=args_list[0]
else:
  filename='/users/abrick/resources/urantia.txt'

# pattern to match
pattern = r'\d+'
# list to store all the integers(as strings)
list_of_nums_as_str=list()

# open filehandle
with open(filename) as f:
#iterate over line, match ints and add them to the list.
  for line in f:
    match = re.findall(pattern, line)
    if match:
      list_of_nums_as_str.extend(match)

# convert list of strs to ints and print max
print(max(map(int, list_of_nums_as_str))) 
