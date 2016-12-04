
def main():
	start = int(input("Enter the start of the search range: "))
	end = int(input("ENter the end of the search range: "))
	
	print ("Here are the prime numbers in the range!")
	for each in range(start, end):
		prime = getprimenumber(each)
		print (prime)	





def getprimenumber(number):


#assign variable to keep count of factors
	counter = 2

#While the number is greater than the counter go to the next step
	while number > counter :
	#if the number is divisble by the counter and the number is not the counter itself go to the next step
		if (number % counter) == 0 and counter != number:
			break #Send loop back up until 'while' condition is exausted instead of the 'if' condition
		else: counter += 1

	else: 
		return (number)

main()

