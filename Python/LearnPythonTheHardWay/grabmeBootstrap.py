  from sys import argv
from urllib import urlopen
import sys

BOOT_URL ="http://s3.amazonaws.com/codecademy-content/courses/ltp/css/bootstrap.css"

page = urlopen(BOOT_URL).readlines()
target = open(filename, 'w')

target.write(page)
