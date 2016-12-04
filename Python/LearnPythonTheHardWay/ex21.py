def add(a, b):
    print "ADDING %d + %d" %(a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" %(a, b)
    return a - b

def multiply(a, b):
    print "MULTPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" %(a, b)
    return a / b

print "Let's do some math with just functuons!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Wight: %d, IQ: %d" %(age, height, weight, iq)

print "Here is a puzzle."

whatTHEF = add(age, subtract(height,multiply(age, subtract(divide(iq, -(age)), divide(iq, 2)))))#Do that math bi-atch.

print "AlL THAT MESS BECOMES::::. ",whatTHEF," Did it by hand, sucked balls, never doing it agian. "