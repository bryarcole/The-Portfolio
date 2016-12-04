#create a mapping of stae to abbreaviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'

}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'JacksonVille'

}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

#print some sates

print '-' * 10
print "Michigans's abbreaviation is: ", states['Michigan']
print "Flordia's abbreviation is: ", states['Florida']

print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" %(state, abbrev)

print '-' * 10
for abbrev, city in cities.items():
    print "%s is has the city %s" %(abbrev, city)

print '-' * 10
for state, abbrev in states.items():
    print "%s sate is abbreviated %s and has city %s" %(state, abbrev, cities[abbrev])

print '-' * 10

state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

city = cities.get('TX', 'Does not exist')
print "The city for the state of 'TX' is: %s" %city