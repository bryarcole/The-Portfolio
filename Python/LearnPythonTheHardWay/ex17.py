from sys import argv
from os.path import exists

#input args
script, from_file, to_file = argv

#explaining that you're copying from one to the other
print "Copying from %s to %s" % (from_file, to_file)

#Apparerntly you can use the semicolon (;) to make
#one liners in python
#---> Remove comment hash in line 13 to see<----
in_file = open(from_file) #; indata = in_file.read()
#read data to varible "indata"
indata = in_file.read()

#check to see how long indata is
print "The inpurt file is %d bytes long" % len(indata)

#test to see if the file exist
print "Does the oiutput file exist? %r" % exists(to_file)
print "Ready, hit RETURN to contiune, CTRL-C to abort."

#Get confirmation from the user
raw_input()

#open the out file
out_file = open(to_file, 'w')
#Write the '.read()' data from the "indata" variable
#to the "out_file" variable.
out_file.write(indata)

print "Alrigh, all done."


#close both opened files.
out_file.close()
in_file.close()

