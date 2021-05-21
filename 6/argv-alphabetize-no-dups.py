#!/usr/local/bin/python3
import sys

# checking to make sure i'm working with a list
#print(type(sys.argv))

# lets not mess with original argv.
args_list = sys.argv

# argv[0] is the program itself. Curious to see how this will be graded
# but assignment says cmd line args, so i'm deleting argv[0] from list.
del args_list[0]

# Ok, so there are potentially easier...and more elegant(?) 
# ways to alphabetize and remove duplicates w/out going from list -> dict -> list.
# In the spirit of the assignment, I am going to convert a list into
# the keys of a dictionary, which will remove duplicates...value for each key is NULL 

args_dict = dict()
for args in args_list:
  args_dict[args] = args_dict.get(args)

# Fortunately, sorting keys in the dict is straightforward (as opposed to vals)
# by convert keys back to a list and sorting

args_list = list(args_dict.keys())
args_list.sort()

for arg in args_list:
  print(arg, end =" ")

print()
