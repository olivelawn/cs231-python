#!/usr/local/bin/python3
import sys
import statistics

# functions at top of prog! I could use  statistics module for mode, but lets do this the hard way.
def my_mode(param_list):
  #create a dictionary where key is the argument, val is number of occurrences
  argscount_dict = dict()
  for arg in param_list:
    argscount_dict[arg] = argscount_dict.get(arg, 0) + 1 
  #sort the dictionary by value and return a list of keys
  sorted_param_list=sorted(argscount_dict, key=argscount_dict.get, reverse=True)
  return sorted_param_list[0]

# Not proud of this logic neccesarily, BUT assignment sez "non-numerical" needs to be treated as a string
# So, I'm gonna try for an int...and then try for a float, and then finally assume a string
def if_int(string):
  try:
    return(int(string))
  except:
    return False

def if_float(string):
  try:
    return(float(string))
  except:
    return False

def get_str_len(string):
  return(len(string))

# lets not mess with original argv.
args_list = sys.argv
# delete program itself from the list
del args_list[0]

# create a new list to store arguments as either a int, float, or len of string
newlist=list()

if args_list: #make sure list not empty. if no cmd line args, just exit quietly.
  # Ok, so. check if int and then a float. Must be in that order!
  for arg in args_list:
    if if_int(arg):
      newlist.append(if_int(arg))
    elif if_float(arg):
      newlist.append(if_float(arg))
    else:
      newlist.append(get_str_len(arg))

  print('Cmdline args converted to ints, floats, or len(str):', newlist)
  print('Median of cmdline arguments is:', statistics.median(newlist)) 
  print('Mode of cmdline arguments is:', my_mode(newlist))
