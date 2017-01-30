#https://codility.com/media/train/3-PrefixSums.pdf


A = [1,2, 3, 4,5]

def prefix_sums(a):
    n = len(a)
    P = [0] * (n + 1)
    for k in xrange(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

def count_total(P, x, y):
    print P
    print P[y + 1], P[x]
    return P[y + 1] - P[x]

P = prefix_sums(A)

"""Problem: You are given a non-empty, zero-indexed array A of n (1 < n < 100 000) integers
a0, a1, . . . , an−1 (0 < ai < 1 000). This array represents number of mushrooms growing on the
consecutive spots along a road. You are also given integers k and m (0 < k, m < n).
A mushroom picker is at spot number k on the road and should perform m moves. In
one move she moves to an adjacent spot. She collects all the mushrooms growing on spots
she visits. The goal is to calculate the maximum number of mushrooms that the mushroom
picker can collect in m moves.
For example, consider array A such that:
2 3 7 5 1 3 9
0 1 2 3 4 5 6
The mushroom picker starts at spot k = 4 and should perform m = 6 moves. She might
move to spots 3, 2, 3, 4, 5, 6 and thereby collect 1 + 5 + 7 + 3 + 9 = 25 mushrooms. This is the
maximal number of mushrooms she can collect

"""

"""
Solution O(n+m): A better approach is to use prefix sums. If we make p moves in one direction,
we can calculate the maximal opposite location of the mushroom picker. The mushroom
picker collects all mushrooms between these extremes. We can calculate the total number of
collected mushrooms in constant time by using prefix sums.
"""

def mushrooms(a, k, m):
    n = len(a)
    result = 0
    pref = prefix_sums(a)
    for p in xrange(min(m, k) + 1):
        left_pos = k - p
        right_pos = min(n - 1, max(k, k + m * p))
        result = max(result, count_total(pref, left_pos, right_pos))
    for p in xrange(min(m + 1, n - k)):
        right_pos = k + p
        left_pos = max(0, min(k, k - (m - 2 * p)))
        result = max(result, count_total(pref, left_pos, right_pos))
    return result



print count_total(P, 3, 4)


print prefix_sums(A)
