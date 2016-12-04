#Define Function
def Get_pay():
    file = open ('C:\Python34\InputA.txt', 'r')
    name = file.readline()
#While loop to iterate through
    while True:
        #assign first line to variable, worker
        worker = file.readline()
        #if the line is empty, break the loop
        if not worker:
            break
        #assign the wage and hours from the next two lines to variables
        wage = file.readline()
        hours = file.readline()
        #Strip the extra space
        worker = worker.rstrip('\n')
        wage = wage.rstrip('\n')
        hours = hours.rstrip('\n')
        #calculate the total pay
        pay = float(wage) * float(hours)
        #print the result
        print (worker, "$", pay, sep=' ')

        

    file.close()
        
Get_pay()
