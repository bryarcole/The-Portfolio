def purify(x):
    
    final = []
    if type(x) == int:
        if x % 2 == 0:
            final.append(x)
    elif type(x) == list:
        for item in x:
            if item % 2 == 0:
                final.append(item)
    print final

purify([88])