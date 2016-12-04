from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file: \n"

print_all(current_file)

print "Now let's rewind, kind of alik ea tape."

rewind(current_file)

print "Let's print three lines: "



#lets play "FOLLOW THE VARIABLE::TARGET::;current_line;::##
#initiation = 1
current_line = 1
print_a_line(current_line, current_file)

#2nd declaration. now = (firstline)1 + (secondline)1
current_line += 1
print_a_line(current_line, current_file)

#3rd declaration. now = (firstline)1 + (secondline)1 + (thirdLine)1
current_line += 1
print_a_line(current_line, current_file)