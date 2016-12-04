def main():
    try:
        option = 0
        while (option != 4):
                print()
                print("1 - Divide by zero")
                print("2 - Open a nonexistent file")
                print("3 - Bad list index")
                print("4 - Quit")
                print()
                option = int(input("Choose an option (1-4)"))

                if (option==1):
                        print (1/0)
                if (option==2):
                        f = open("IDONTEXIST")
                if (option==3):
                        l = []
                        print (l[100])
                if (option==4):
                        print ("Thanks for playing")
    except IndexError:
            print("Can't assign a list to a integer Doc")
    except ZeroDivisionError:
            print("You can't divide by zero Doc")
    except FileNotFoundError:
            print("That files not found Doc")
    except ValueError:
            print("You gotta input one of the numbers one through four, Doc")
                        

main()
