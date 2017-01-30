#https://codility.com/media/train/0-Arrays.pdf

Array = []

def negative(A):
    total = 0
    for item in A:
        if item < 0:
            total += 1
    return total
