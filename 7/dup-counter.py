#!/usr/local/bin/python3
import sys

# Quicky function to print dups
def print_dups(dup_list):
  print('duplicated arguments: ', *dup_list)

# checking to make sure i'm working with a list
#print(type(sys.argv))

# lets not mess with original argv.
args_list = sys.argv

# argv[0] is the program itself. Curious to see how this will be graded
# but assignment says cmd line args, so i'm deleting argv[0] from list.
del args_list[0]

# Use a dictionary to count the arguments
argscount_dict = dict()
for arg in args_list:
  argscount_dict[arg] = argscount_dict.get(arg, 0) + 1


# Use dup_counter and dup_list to count and store the duplicates
# Printing the duplicates wasn't specified in the assignment
# but it looks like there is some confusion on the discussion
# board about what constitutes a duplicate, so I printing mine out.
dup_counter = 0
dup_list = list()

# Count the dups and add the dups to a list
for arg in argscount_dict:
  if argscount_dict[arg] >= 2:
    dup_counter += 1
    dup_list.append(arg)

# Print output using  conditional
if dup_counter == 0:
  print('There are fewer than 1 duplicates (i.e. there are no duplicates).')
elif dup_counter == 1:
  print('There are exactly 1 duplicates.')
  print_dups(dup_list)
elif dup_counter >= 2:
  print('There are more than 1 duplicates.')
  print_dups(dup_list)

#args_list = list(argscount_dict.keys())
#args_list.sort()

#for arg in args_list:
#  print(arg, end =" ")

#print()
