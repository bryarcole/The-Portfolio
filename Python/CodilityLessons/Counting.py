#https://codility.com/media/train/2-CountingElements.pdf

"""Problem: You are given an integer m (1 ¬ m ¬ 1 000 000) and two non-empty, zero-indexed
arrays A and B of n integers, a0, a1, . . . , an−1 and b0, b1, . . . , bn−1 respectively (0 ¬ ai
, bi ¬ m).
The goal is to check whether there is a swap operation which can be performed on these
arrays in such a way that the sum of elements in array A equals the sum of elements in
array B after the swap. By swap operation we mean picking one element from array A and
one element from array B and exchanging them."""


def counting(A, m):
    n = len(A)
    count = [0] * (m + 1)
    for k in xrange(n):
        count[A[k]] += 1
    return count

def slow_solution(A, B, m):
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    for i in xrange(n):
        for j in xrange(n):
            change = B[j] - A[i]
            sum_a += change
            sum_b -= change
            if sum_a == sum_b:
                return True
            sum_a -= change
            sum_b += change
    return False


"""
The best approach is to count the elements of array A and calculate
the difference d between the sums of the elements of array A and B.

For every element of array B, we assume that we will swap it with some element from
array A. The difference d tells us the value from array A that we are interested in swapping,
because only one value will cause the two totals to be equal. The occurrence of this value can
be found in constant time from the array used for counting
"""
def fast_solution(A, B, m):
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    d = sum_b - sum_a
    if d % 2 == 1:
        return False
    d /= 2
    count = counting(A, m)
    for i in xrange(n):
        if 0 <= B[i] - d and B[i] - d <= m and count[B[i] - d] > 0:
            return True
        return False
    
