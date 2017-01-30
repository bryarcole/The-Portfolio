"""Let us consider a sequence a0, a1,...,an≠1. The leader of this sequence is the element whose
value occurs more than n
2 times.
a0 a1 a2 a3 a4 a5 a6
6 8 4 6 8 6 6
0 1 2 3 4 5 6
In the picture the leader is highlighted in gray. Notice that the sequence can have at most one
leader. If there were two leaders then their total occurrences would be more than 2 · n
2 = n,
but we only have n elements.

"""


def slowLeader(A):
    n = len(A)
    leader = -1
    for k in xrange(n):
        candidate = A[k]
        count = 0
        for i in xrange(n):
            if (A[i] == candidate):
                count += 1
            if (count > n / 2):
                leader = candidate
        return leader


def fastLeader(A):
    n = len(A)
    leader = -1
    sorted(A)
    candiate = A[n/2]
    count = 0
    for i in xrange(n):
        if (A[i] == candiate):
            count += 1
        if (count > n / 2):
            leader = candiate
        return leader

def goldenLeader(A):
        n = len(A)
        size = 0
        for k in xrange(n):
            if (size == 0):
                size += 1
                value = A[k]
            else:
                #If values not the same remove both from stack and move on the
                #third value
                if(value != A[k]):
                    size -= 1
                else:
                    size += 1
        candidate = -1
        if(size > 0):
            candidate = value
        leader = -1
        count = 0
        for k in xrange(n):
            if A[k] == candidate:
                count += 1
        if count > n / 2:
            leader = candidate
        return leader