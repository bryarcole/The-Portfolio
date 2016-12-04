def monogram():
    name = input(str("What is the name you want to turn into a Monogram? "))
    names = name.split()
    empty = ""

    for stuff in names:
        initial = stuff[0]
        empty += initial
    print (empty)

monogram()


