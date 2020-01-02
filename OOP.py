""" OOP and Design Patterns """

# # Built-In Class Attributes
# Every Python class keeps following built-in attributes and they can be accessed using dot operator like any other attribute −
# __dict__ − Dictionary containing the class's namespace.
# __doc__ − Class documentation string or none, if undefined.
# __name__ − Class name.
# __module__ − Module name in which the class is defined. This attribute is "__main__" in interactive mode.
# __bases__ − A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.
 
class Node:
  # this is a class comment you can access through [classname].__doc__
  'node in a tree' 
  #these are class atributes (like a static attributes)
  middleL = None
  middleR = None
  nodecount = 0

  def __init__(self):
    # there are object attiributes
      self.value = 0
      self.left = None
      self.right = None
      Node.nodecount += 1
  def toString(self):
      print(self, "\n", self.value, "\n", self.left, "\n",  self.left.value, "\n", self.right, "\n", self.middleL, "\n", self.middleR)

root = Node()
root.value = 3
root.left = Node()

print(root.value)
root.toString()

# Instead of using the normal statements to access attributes, you can use the following functions −
# The getattr(obj, name[, default]) − to access the attribute of object.
# The hasattr(obj,name) − to check if an attribute exists or not.
# The setattr(obj,name,value) − to set an attribute. If attribute does not exist, then it would be created.
# The delattr(obj, name) − to delete an attribute.

'''DECORATOR'''
# class DecoratorExample:
#   """ Example Class """
#   def __init__(self):
#     """ Example Setup """
#     print('Hello, World!')

#   @staticmethod
#   def example_function():
#     """ This method is decorated! """
#     print('I\'m a decorated function!')
# de = DecoratorExample()
# de.example_function()

''' Instance Methods in Python'''
# class DecoratorExample:
#   """ Example Class """
#   def __init__(self):
#     """ Example Setup """
#     print('Hello, World!')
#     self.name = 'Decorator_Example'

#   def example_function(self):
#     """ This method is an instance method! """
#     print('I\'m an instance method!')
#     print('My name is ' + self.name)
 
# de = DecoratorExample()
# de.example_function()

''' static method '''
# class DecoratorExample:
#   """ Example Class """
#   def __init__(self):
#     """ Example Setup """
#     print('Hello, World!') 

#   @staticmethod
#   def example_function():
#     """ This method is a static method! """
#     print('I\'m a static method!')
# de = DecoratorExample.example_function()
# print(type(de))

'''class method'''
'''Class methods are the third and final OOP method type to know. 
Class methods know about their class. They can’t access specific instance data,
but they can call other static methods.
Class methods don’t need self as an argument,
but they do need a parameter called cls.
This stands for class, and like self, gets automatically passed in by Python.
Class methods are created using the @classmethod decorator.
Class methods are possibly the more confusing method types of the three,
 but they do have their uses. Class methods can manipulate the class itself,
which is useful when you’re working on larger, more complex projects.'''
# class DecoratorExample:
#   """ Example Class """
#   def __init__(self):
#     """ Example Setup """
#     print('Hello, World!') 
#   @classmethod
#   def example_function(cls):
#     """ This method is a class method! """
#     print('I\'m a class method!')
#     cls.some_other_function()
#   @staticmethod
#   def some_other_function():
#     print('Hello!')

# de = DecoratorExample()
# de.example_function()

# #into 😐
# class person:
#   #hard codded class every one is named kataya
#   def getName(self):
#     print("kataya")
#   def getAge(self):
#     print("22")
# p = person()
# p.getAge()
# class person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def getName(self):
#     return f'the name is {self.name}'
#   def getAge(self):
#     print(f'{self.name} is {self.age} years old')

# p = person("sasuke",21)
# k = person("naruto",31)
# print(p,k)
# print(p.getName(),k.getName())

'operator overloading' 😊
# Suppose you have created a Vector class to represent two-dimensional vectors, what happens when you use the plus operator to add them? Most likely Python will yell at you.
# You could, however, define the __add__ method in your class to perform vector addition and then the plus operator would behave as per expectation −
# class Vector:
#    def __init__(self, a, b):
#       self.a = a
#       self.b = b

#    def __str__(self):
#       return 'Vector (%d, %d)' % (self.a, self.b)
   
#    def __add__(self,other):
#       return Vector(self.a + other.a, self.b + other.b)

# v1 = Vector(2,10)
# v2 = Vector(5,-2)
# print v1 + v2

# ouptup: Vector(7,8)