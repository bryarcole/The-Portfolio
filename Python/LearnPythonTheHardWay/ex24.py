#General practice from Learn Python the Hard Way

print "Let's practice everything. "
print "You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs."

#assign string to variable
poem = """
\tThe lovely world
with logic so firmly planted 
cannot discern \n the needs of love
nor comprehend passion from intuation
and requires an explanation
\n\t\twhere there is none. 
"""


#print variable
print "_____________"
print poem
print "_____________"

#do math, get the number five
five = 10 - 2 + 3 - 6
#print the number five as as a string. = %s
print "This should be five: %s" %five

#define function with one argument, "started"

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    #notice here: Returns THREE things
    return jelly_beans, jars, crates

start_point = 10000
#the varibles are delcared and then assigned to the
# results of the function call.
beans, jars, crates = secret_formula(start_point) #start_point aka: '10000' is the starting number

#display start point
print "WIth a starting point of: %d" % start_point
#display the variables assigned ot the results (or return) of the function
print "We'd have %d beans, %d jars, and %d crates." %(beans, jars, crates)

#just divide everything by 10
start_point = start_point / 10

print "We can also do that this way: "
#this time, each 'return' is assigned to a %d, so
# the first %d = jelly_beans from functon secret_formula()
# the second %d = jars fro the function secret_formulaS()
# the third %d = crates from the funrtion secret_formual()
print "We'd have %d beans, %d jars, and %d crates. " %secret_formula(start_point)

