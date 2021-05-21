#!/usr/local/bin/python3
import sys
import statistics

# functions at top of prog! I could use  statistics module for mode, but lets do this the hard way.
# We are treating both numbers and words as strings!
def my_mode(param_list):
  #create a dictionary where key is the argument, val is number of occurrences
  argscount_dict = dict()
  for arg in param_list:
    argscount_dict[arg] = argscount_dict.get(arg, 0) + 1 
  #sort the dictionary by value and return a list of keys
  sorted_param_list=sorted(argscount_dict, key=argscount_dict.get, reverse=True)
  return sorted_param_list[0]

# taking the easy route for median
def my_median(param_list):
  try:
    return statistics.median(map(int, param_list))
  except:
    print("My median function isn't that smart, please enter integers on the command line...attempting mode on non-integers...") 
    return False

# lets not mess with original argv.
args_list = sys.argv
# delete program itself from the list
del args_list[0]

#x=statistics.median(map(int, args_list))

if args_list: #make sure list not empty
  med=my_median(args_list)
  if med:
    print('Median of cmdline arguments is:', med)
  print('Mode of cmdline arguments is:', my_mode(args_list))
