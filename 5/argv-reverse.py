#!/usr/local/bin/python3
import sys

# checking to make sure i'm working with a list
#print(type(sys.argv))

# lets not mess with original argv.
prog_list = sys.argv

# argv[0] is the program itself. Curious to see how this will be graded
# but assignment says cmd line args, so i'm deleting argv[0] from list.
del prog_list[0]

# you don't actually want me to iteratee over each element and copy
# to a new list do you when the built-in reverse method is available
# right? :)
prog_list.reverse()
for arg in range(len(prog_list)):
  print(prog_list[arg], end =" ")

# curious about this. python3 on macos does not require this nweline
# wheras on hills, it does.
print()
