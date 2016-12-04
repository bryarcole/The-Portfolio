def Monogram():
    name = input(str("What is the name you want to turn into a Monogram (Be sure to capitolize the first of each name)? "))

    mylist = []

    for index, item in enumerate(name):
        if item.isupper():
            mylist.append(item)

    return (str(mylist))

            
