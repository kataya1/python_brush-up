import sys
import random
import os
# pdb for debugging
import pdb
import collections
# print this li
data_types = ['strings',
              'numbers',
              'lists',
              'tubles',
              'dictionaries']
            
'''sitn'''
# for debugging, after (pdb) appear in console n is for next and p followed
# by the variable to print the value of that specific variable.
# you can print multiple variables separated by a comma. q for quit and c for continue, l for list
# s to step into a subroutine(n doesn't do that) and r to return
# (Pdb)!b = "BBB" to assign a new value to a variable named b
# pdb.set_trace()

# print(data_types)
# word = "see what print() can do"
# print("hello world", 123 ** 3 % 33, word)
# # print("to end the new line that print puts between lines", end = "" )
# quote = "\"he remembers that time when his father took him to see ice as he faced the firing squad\""
# print(quote)
# print("%s %s %s" % ('fromt the book that doesn\'t seem to end', quote, word))
 
# num = [1, 2, 3]
# num.insert(1, 4)
# print(num)
# num.sort()
# print(num)
# arithmatics = ("+", "-", "*", 1)
# print(arithmatics)

# #lambda expresion
# lambda x: 3*x + 1

# def build_quadratic_function(a, b, c):
#     return lambda x: a*x**2 + b*x + c

# # f becomes of type functi

# f = build_quadratic_function(2, 4, 5)
# f(3)
# f(6)

# build_quadratic_function(2 ,0, 9)(3)
# help(num.sort())

# #reading file
# # opening the input file #r+ is for reading and writing
# f = open('example.in','r')
# #loopr over the file for line in f:
# first_line = f.readline()
# second_line = f.readline()
# #setting the input variables and splitting input like 2 3 1 5 into variables
# row, column, min, max = tuple(map(int,first_line.split(' ')))

# #dont forget to close the file
# f.close()

#i just added code runner extension to visual studio code but you can run code in the terminal by      <filename>.py, to run using runner ctrl + alt + n  to stop ctrl + alt + m 
#<<<< LIST Comprehension >>>>
# nums = [1,2,3,4,5,6,7,8,99,9,0]
# func = []
# # -------------------------------
# # # for n in nums:
# # #     func.append(n*n)
# # func = [n*n for n in nums]
# # -------------------------------
# # func = [n for n in nums if n%2 == 0]
# # func = [(letter,num) for letter in 'abcd' for num in range(4)]
# numss = [1,2,3,4,2,1,2,1,1,1,3,4,5,6,7]
# myset = { n for n in numss}
# print(myset)
# print("heldddlo",func)

# #positional arguments 👌
# def familyfirst(first_name,last_name):
#     # print("hello", last_name, first_name)
#     # a new way to format print
#     print(f'hi {last_name} {first_name}!')
#
# familyfirst("naruto","uzumaki")
# # you can call the parameter name from the function
# familyfirst(last_name="uzumaki", first_name="naruto")

# #exceptions 😊
# try:
#     age = int(input('Age: '))
#     print(f'you are {age} years old')
#     risk = 2000/age
# except ValueError:
#     print('type a number !!!')
# except ZeroDivisionError:
#     print('age cannot be 0. !!')
# maybe you can add (except :)  just like that

# modules 😁
# you put functions in othre <file>.py and import them for usebility
# import KgtoLbs
# KgtoLbs.convertKgtoLbs(30)  #convert is a function in the KgtoLbs module
# you could import functions directly  # from KgtoLbs import convertKgtoLbs  # you don't need to use KgtoLbs.convertKgtoLbs just call the function normaaly
# from KgtoLbs import convertKgtoLbs as conv # to rename the function

# data passing
# python doesn't pass by reference or by value. is passes by something called "object-reference-pass-by-value"
# ex x = 3 , x is a var assigned to a reference of an object of value 3, you can reassign x to a d differenct referenece of an object or change the object itself which you will see in other vars that are assigned to a reference to that object  use id(x) to check unique id of the object 
