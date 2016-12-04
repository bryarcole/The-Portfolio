print "You enter a dark room with two doors. Do you go thorugh door #1 or door # 2"

door = raw_input(">" )

if door == "1":
    print "Theres a giant bear here earting a cheescake. What do you do?"
    print "Option '1'. Take the cake"
    print "Option '2'. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bears eats your face off. Loser face! "
    elif bear == "2":
        print "The bear eats your legs off. Good job Legless face! "
    else: #haha error in the indentiuon in the book.
        print "Well, doing $s is pribably better. Bear runs way " % bear
elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina. "
    print "1. Blueberries."
    print "2. Yellow Hacket clothespins."
    print "3. Understanding revolvers yelling melodies. "

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of hjello. Greatness!"
    else:
        print "The insanity rots your eyes int a pool of muck. great!"

else:
    print "You stumble around and fall on a knife and die. You suck!"
