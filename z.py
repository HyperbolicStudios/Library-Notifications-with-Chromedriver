import os
from inspect import getsourcefile
from os.path import abspath

directory = abspath(getsourcefile(lambda:0))
newDirectory = directory[:(directory.rfind("\\")+1)]
os.chdir(newDirectory)

file = open('logs.txt', 'r')
print(file.read())
