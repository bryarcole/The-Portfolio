from sys import argv

#Set arguments, the script and the file you want read

script, filename = argv

#Get file.

file = open(filename)

#Read file, must use ->print<- here to get python to read it. 

print file.read()