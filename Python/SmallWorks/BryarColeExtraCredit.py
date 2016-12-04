def FarhToCels():
    number = int(input('Please enter the degrees in Fahrenheit: '))

    cels = ((5/9)*(number - 32))
    print("The current degrees in Celcius is", cels)

def MilesToKilos():
    number = int(input('Please enter the number of miles: '))

    kilos = number * 1.609

    print(number,'miles is equivalent to', kilos, 'Kilometers',)

def RaceResults():
    name1 = str(input('Input the name of the first runner: '))
    time1 = int(input('How many seconds did it take the first runner to finish the race?: '))
    name2 = str(input('Input the name of the second runner: '))
    time2 = int(input('How many seconds did it take the second runner to finish the race?: '))
    name3 = str(input('Input the name of the third runner: '))
    time3 = int(input('How many seconds did it take the third runner to finish the race?: '))


    if time1 > time2 and time3:
        print ('1st Place', name1)

        if time2 > time3:
            print('2nd Place', name2)
            print('3rd Place', name3)

        else:
            print('2nd Place', name3)
            print('3rd Place', name2)

    elif time2 > time3 and time1:
        print ('1st Place', name2)

        if time1 > time3:
            print('2nd Place', name1)
            print('3rd Place', name3)

        else:
            print('2nd Place', name3)
            print('3rd Place', name1)

    else:
        print ('1st Place', name3)

        if time1 > time2:
            print('2nd Place', name1)
            print('3rd Place', name2)

        else:
            print('2nd Place', name2)
            print('3rd Place', name1)


            
def MixingColors():
    FirstColor = str(input("What is the first color?: "))
    SecondColor = str(input("What is the second color?: "))

    red = 'red' or 'Red'
    blue = 'blue' or 'Blue'
    yellow = 'yellow' or 'Yellow'
    
    if FirstColor == red and SecondColor == blue or FirstColor == blue and SecondColor == red:
        print("When you mix those you get Purple")
    elif FirstColor == yellow and SecondColor == red or FirstColor == red and SecondColor == yellow:
        print("When you mix those you get Orange")
    elif FirstColor == yellow and SecondColor == blue or FirstColor == blue and SecondColor == yellow:
        print("When you mix those you get Green")

def QuickBudgetLoop():
    SB = int(input("What is your starting budget?: "))
    TE = 0
    while True:
        expenses = int(input("Enter expense amount, entering zero will show you your result: "))
        TE += expenses
        if expenses == 0:
            break
        result = SB - TE
 
    if result > 0:
        print ("You are", result, "dollars under budget")
    else:
        print ("You are", result, "dollars over budget")
                       
    
def LoanPaymentCalculation(principal, APR, numpay):
    monpay = principal((APR /12)*(1+ (APR/12)**(numpay)) / ((1 + (APR/12)**(numpay)) - 1))
    print (monpay)





    
        


            
