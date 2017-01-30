# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    holder = len(A)
    size = 0
    #For loop gets element to test
    for item in xrange(holder):
        if (size == 0):
            size += 1
            val = A[item]
        else:
            if val != A[item]:
                size -=1
            else:
                size += size
    possible = -1
    if (size > 0):
        possible = val
    lead = -1
    count = 0
    for item in xrange(holder):
        if A[item] == possible:
            count += 1
    if count > holder / 2:
        lead = A.index(possible)
    return lead