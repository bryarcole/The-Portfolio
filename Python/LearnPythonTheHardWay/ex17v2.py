from sys import argv
from os.path import exists
#Trying to do this section in one line, have not figured it out yet.

s, ff, tf = argv

in_file = open(ff).read ; of = open(tf, 'w'); of.write(in_file)