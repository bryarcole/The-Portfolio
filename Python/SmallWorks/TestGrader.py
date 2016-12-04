def testGrader():
    mylist = ['B', 'D', 'A', 'A', 'C', 'A', 'B', 'A', 'C', 'D']
    correct = 0

    
    for letter in mylist:
        answer = input("What answer did the student putdown? ")
        if letter == answer:
            print ("That answer was correct")
            correct += 1

        else:
            print ("That answer is incorrect")

    print ("The student got", correct, "answers correct")
   
testGrader()
