
##Get number from user
number = int(input("Enter a number that is bigger than 2: "))

#assign variable to keep count of factors
counter = 2

#While the number is greater than the counter go to the next step
while number > counter :
	#if the number is divisble by the counter and the number is not the counter itself go to the next step
	if (number % counter) == 0 and counter != number:
		#Print the number is not a prime number
		print ('The number is not prime')
		break #Send loop back up until 'while' condition is exausted instead of the 'if' condition
	else: counter += 1

else: 
	print ('The number is Prime')


