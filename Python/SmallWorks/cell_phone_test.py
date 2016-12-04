import cellphone

def main():
	
	#get the phone data
	
	man = input('Enter the manufacturer: ')
	mod = input('Enter the model number: ')
	retail = float(input('Enter the retail price: '))
	
	#creat an instance in the cellphone class
	
	phone = cellphone.CellPhone(man, mod, retail)
	
	#Display the data that was entered. 
	
	print('Here is the data that you entered: ')
	print('Manufacturer:', phone.get_manufact())
	print('Model Number:', phone.get_model())
	print('Retail Prince:$', format(phone.get_retail_price(), ',.2f'), sep='')
	
main()

	
