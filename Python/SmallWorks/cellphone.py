# The CellPhone class holds data about a cell phone. 

class CellPhone:
	
	#the __init__ method initialize the attributes
	
	def __init__(self, manufact, model, price):
		self.__manufact = manufact
		self.__model = model
		self.__retail_price = price
	
	#The set_manufact method accepts an arugment for the
	# Phone's manufacturer
	
	def set_manufact(self, manufact):
		self.__manufact = manufact 
	
	#The set_model method acepts aan argument for
	#the phone's model number
	
	def set_model(self, model):
		self.__model = model
		
	#The set_retail_price method accepts an argument
	#for the phone's retail price.
	
	def set_retail_price(sale, price):
		self.__retail__price = price
		
	#the get_manufact method returns the phone's manufacturer
	
	def get_manufact(self):
		return self.__manufact
		
	#the get_model method returns the phone's model number
	
	def get_model(self):
		return self.__model
		
	#The get_retail_price method returns the phone's retail price. 
	
	def get_retail_price(self):
			return self.__retail_price
