

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" %cheese_count
    print "Youb have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "WE can just give thje functions numbers directly: "
cheese_and_crackers(20, 30)

print "OR, we can use varibles from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can ever do math inside too: "
cheese_and_crackers(10 + 43, 4 + 56)

print " And we cand ombin the two, variable and math, duh.: "
cheese_and_crackers(amount_of_crackers + 14, amount_of_crackers + 256)