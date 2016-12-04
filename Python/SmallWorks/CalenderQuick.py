Months = {'Jan':31,'Feb':28,'Mar':31,'Apr':30,'May':31,'Jun':30,\
'Jul':31,'Aug':31,'Sep':30,'Oct':31,'Nov':30,'Dec':31 }

def cal():
    #Prompt for month
    month = input("Enter a Month: ")

    if month in Months:
            result = (Months[month])
            print (month, "has", result, "days in it.")
    else:
        print ("please enter a valid month")


cal()
