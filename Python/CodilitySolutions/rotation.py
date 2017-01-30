

def solution(A, K):
    if not A:
        return A

    if K > len(A):
        K = K % len(A)
    if not K:
        return A

    return A[len(A)-K:] + A[:len(A)-K]
Array = [0, 1 , 2 ,3 ,4 , 5 ,6 ,7 ,8 ,9 ]

print solution(Array, 4)