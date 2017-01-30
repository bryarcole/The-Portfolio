
def solution(A):
    # write your code in Python 2.7
    hold = len(A)
    stack = 0 #create stack to pile variable
    eqCount = 0 #create eqcount
    #iter through list
    for item in range(len(A)):
        if stack == 0:
            stack += 1
            leadVal = A[item]
            if leadVal != A[item +1]:
                eqCount += 1
                stack -= 1
                newList = A.pop(item)
            else:
                if A.count(item) >= (len(A)) / 2:
                    eqCount += 1
                    stack -= 1
                else:
                    stack -= 1
    return eqCount
    
A = [1,2,3,4,5,5,5,5,6,7,7,7,7,7,4,4,4,4]
print solution(A)