
cardNumbers = ['4916-2600-1804-0530', '4779-252888-3972', '4252-278893-7978', '4556-4242-9283-2260']


def countCalc(A):
    count = 0
    for item in range(0, len(A)):
        for n in item:
            count += item[n]
    return count

print countCalc(cardNumbers)