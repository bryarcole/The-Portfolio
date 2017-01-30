def logrithimic(n):
    result = 0
    while n > 1:
        n //= 2
        result += 1
    return result

print logrithimic(666)