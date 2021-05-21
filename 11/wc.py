#!/usr/local/bin/python3
import sys

# lets not mess with original argv.
args_list = sys.argv
# delete program itself from the list
del args_list[0]

# handle this like the unix wc util where file is the 1st arg. If no arg default to urantia
#[pjohnso9@hills 11]$ wc /users/abrick/resources/urantia.txt | awk '{print $2}'
#1112604
#[pjohnso9@hills 11]$ ./wc.py /users/abrick/resources/urantia.txt
#1112604

if args_list:
  filename=args_list[0]
else:
  filename='/users/abrick/resources/urantia.txt'

# wc will be our word counter
wc=int()

# again modeling after the unix wc util which counts something like "34:6.13" as a word :)
# open filehandle
with open(filename) as f:
#iterate over line, split, count, and add to counter
  for line in f:
    wc += len(line.split())
  
print(wc)
 
