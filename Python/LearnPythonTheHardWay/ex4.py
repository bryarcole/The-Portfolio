#assigning the int 100 to "cars"
cars = 100
#assiging the int 4.0 to "space_in_a_car
space_in_a_car = 4.0
#assigning drivers to the int 30
drivers = 30
#assigning passangers to the int 90
passengers = 90
#assigning cars_not_driver to (cars-drivers)
cars_not_driven = cars - drivers
#assigning cars_driven to drivers
cars_driven = drivers
#assigning carpool_capacity to (cars_driven * space_in_a_car)
carpool_capacity = cars_driven * space_in_a_car
#assiging the average of passengers per car to passanegers divided by cars driven
average_passengers_per_car = passengers / cars_driven

#printing results. 

print "The are ", cars, "cars available."
print "There are only ", drivers, "drivers available."
print "There will be ", cars_not_driven, "empty cars today."
print "We can transport ", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about ", average_passengers_per_car, "in each car."

