#https://codility.com/media/train/4-Sorting.pdf

Array = [1,4,6,4,3,7,8,2,1,5,0,9,11,10]



"""The idea: Find the minimal element and swap it with the first element of an array. Next,
just sort the rest of the array, without the first element, in the same way.
Notice that after k iterations (repetition of everything inside the loop) the first k elements
will be sorted in the right order (this type of a property is called the loop invariant).
"""

def selectionSort(A): #time complexity  =  O(n*2) 
    n = len(A)
    for k in xrange(n):
        minimal = k
        for j in xrange(k + 1, n):
            if A[j] < A[minimal]:
                minimal = j
            A[k], A[minimal] = A[minimal], A[k]
    return A

def countingSort(A, k):
    n = len(A)
    count = [0] * (k + 1)
    for i in xrange(n):
        count[A[i]] += 1
    p = 0
    for i in xrange(k + 1):
        for j in xrange(count[1]):
            A[p] = i
            p += 1
    return A

def distinct(A):
    n = len(A)
    A.sort()
    result = 1
    for k in xrange(1, n):
        if A[k] != A[k -1]:
            result += 1
    return result
    

print distinct(Array)
