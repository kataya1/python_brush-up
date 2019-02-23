import sys
import random
import os
# pdb for debugging
import pdb

data_types = ['strings',
              'numbers',
              'lists',
              'tubles',
              'dictionaries']
# for debugging, after (pdb) appear in console n is for next and p followed
# by the variable to print the value of that specific variable.
# you can print multiple variables separated by a comma. q for quit and c for continue, l for list
# s to step into a subroutine(n doesn't do that) and r to return
# (Pdb)!b = "BBB" to assign a new value to a variable named b
# pdb.set_trace()

print(data_types)
word = "see what print() can do"
print("hello world", 123 ** 3 % 33, word)
# print("to end the new line that print puts between lines", end = "" )
quote = "\"he remembers that time when his father took him to see ice as he faced the firing squad\""
print(quote)
print("%s %s %s" % ('fromt the book that doesn\'t seem to end', quote, word))

num = [1, 2, 3]
num.insert(1, 4)
print(num)
num.sort()
print(num)
arithmatics = ("+", "-", "*", 1)
print(arithmatics)
