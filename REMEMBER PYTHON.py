import sys
import random
import os
# pdb for debugging
import pdb

import collections

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

#lambda expresion
lambda x: 3*x + 1

def build_quadratic_function(a, b, c):
    return lambda x: a*x**2 + b*x + c

# f becomes of type function

f = build_quadratic_function(2, 4, 5)
f(3)
f(6)

build_quadratic_function(2 ,0, 9)(3)
help(num.sort())

#reading file
# opening the input file #r+ is for reading and writing
f = open('example.in','r')
#loopr over the file for line in f:
first_line = f.readline()
second_line = f.readline()
#setting the input variables and splitting input like 2 3 1 5 into variables
row, column, min, max = tuple(map(int,first_line.split(' ')))

#dont forget to close the file
f.close()