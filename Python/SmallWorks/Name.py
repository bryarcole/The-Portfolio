name_list = ['Jon', 'David', 'Duke', 'Roy', 'Juan', 'Kate', 'Sara', 'Parker', 'Wendell', 'Kyle']
    
number_list = ['867-5309', '098-1234','583-3392', '435-0981', '821-4567', '143-4844', '813-0000', '747-9999', '398-5555']
    
    #Display members of the name list



def get_name_index(name_list):
        print ("Here are the names in the address book: ", name_list)
        name = input("Please enter the name of the person's number you would to see: ")
        return name_list.index(name)
                        
            
def __main__():
        index = get_name_index(name_list)
        print (number_list[index])
    
    
    
        
        

__main__()


