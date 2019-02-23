import os
import sys
import pdb
import random

class Node:
    def __init__(self):
        self.value = 0
        self.left = None
        self.right = None
    def toString(self):
        print(self, "\t", self.value, "\t", self.left, "\t",  self.right)

root = Node()
root.value = 3
root.left = Node()

print(root.value)
root.toString()

