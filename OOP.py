""" OOP and Design Patterns """

 
# class Node:
#     def __init__(self):
#         self.value = 0
#         self.left = None
#         self.right = None
#     def toString(self):
#         print(self, "\t", self.value, "\t", self.left, "\t",  self.right)

# root = Node()
# root.value = 3
# root.left = Node()

# print(root.value)
# root.toString()
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
'''Class methods are the third and final OOP method type to know. Class methods know about their class. They can’t access specific instance data, but they can call other static methods.
Class methods don’t need self as an argument, but they do need a parameter called cls. This stands for class, and like self, gets automatically passed in by Python.
Class methods are created using the @classmethod decorator.Class methods are possibly the more confusing method types of the three, but they do have their uses. Class methods can manipulate the class itself, which is useful when you’re working on larger, more complex projects.'''
class DecoratorExample:
  """ Example Class """
  def __init__(self):
    """ Example Setup """
    print('Hello, World!') 

  @classmethod
  def example_function(cls):
    """ This method is a class method! """
    print('I\'m a class method!')
    cls.some_other_function()

  @staticmethod
  def some_other_function():
    print('Hello!')
 
de = DecoratorExample()
de.example_function()