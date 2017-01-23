"""
Making a command line celandar to show the for/while loops in python along with 
if/elif/else statements

"""

from time import sleep, strftime


USERNAME = 'Bryar'

calendar = {}

def welcome():
  print "Welcome" + USERNAME + "!"
  print strftime("%A %B %d, %Y")
  print strftime("%H:%M:%S")
  
  print "What would you like to do?"
 
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("A to add, U to update, V to view, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == 'V':
      if len(calendar.keys()) < 1:
        print "Calendar empty."
      else:
        print calendar
        
        
    elif user_choice == 'U':
      date = raw_input("What date? ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      
    elif user_choice == 'A':
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
        print "That is not a valid address"
        try_again = "Try Again? Y for Yes, N for No: "
        try_again = try_again.upper()
        if try_again == 'Y':
          continue
        else:
          start = False
        
      else:
        if len(calendar[date]) > 0:
          print "There is already something there"
        else:  
        	calendar[date] = event
        
    elif user_choice == 'D':
      if len(calendar.keys()) < 1:
        print "The Calendar is empty"
      else:
        event = raw_input("What event would youlike ot delete: ")
        for date in calendar.keys():
          if event == calendar[date]:
            del(caldnar[date])
            print "Deletion successful"
            print calendar
          else:
            print "Wrong event"
      
    elif user_choice == 'X':
      start = False
    else:
      print "Invalid command!"
      start = False
      
 

start_calendar()