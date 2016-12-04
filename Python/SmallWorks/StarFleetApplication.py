#StarfleetAcademyProgram

minGPA = 2.0
minSAT = 800
minVulcAge = 16
minAge = 17

#Get the Name, age, GPA, SAT, and Race of the applicant
print("Welcome to the Starfleet Academy Online Application") 

appFirstName = input("What is the appliacants name?: ")
appGPA = (float(input("What is the applicants GPA? :")))
appAge = (int(input("What is the applicants age? :")))
appSAT = (float(input("What is the applicants SAT? :")))
appRace = input("What is the applicants Race? :")

#Print applicants results. 

print ("Applicant First name:", appFirstName)
print ("Age:", appAge)
print ("GPA:", appGPA)
print ("SAT:", appSAT)
print ("Race:", appRace)


##define the conditions to get into academy.

def GPA(appGPA):               
    return appGPA >= minGPA or appSAT >= 1100


def Age(appAge):
    return appAge >=minAge or appSAT >= 1500 or (appRace == "Vulcan" and appAge >= 16)
    
def SAT(appSAT):
    return appSAT > minSAT or appGPA > 3.5

def noRomulan(appRace):
    return appRace != "Romulan" or appRace == ("Human", "Vulcan", "Klingon")

	
     
def main():
        
    romulan_check = noRomulan(appRace)
    appAge_check = Age(appAge)
    appGPA_check = GPA(appGPA)
    appSAT_check = SAT(appSAT)
        
    if appGPA_check is True and appAge_check is True and appSAT_check is True and romulan_check:
        print ("Congradulations you meet the minimum requirements to join the Star Fleet Academy")
        
    else:
        print ("Sorry, but you did not meet out minimum requirments")
        



    

main()



