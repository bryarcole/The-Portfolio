#Random Module Example 

def lottery():
    import random
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    random.shuffle(mylist)

    print ("The winning ACC lotto numbers are:", mylist[0],",", mylist[1],"," ,mylist[2],"and the Powerball number is", mylist[3])

lottery()

    
        

    
    
