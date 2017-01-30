A = [2, 3, 1, 5,6, 7, 8]

def solution(a):
    
    #instructions like spanglish.
    """
    In plain english this challenge is asking you to find the missing element, which it gives you is 4.
    So basically, if you add up all the numbers in the array, and assume that 4 is missing so the goal is to find the formuala that will always be --
    4 away from the sum of the array you put into the function. 
    """
    n = len(a) +1
    print sum(a)
    return(n * (n+1) /2 - sum(a))



print solution(A)