"""
One of my favorite lessons on styling I found online, let me talk you through this.
This will help you prosper if you are having trouble understanding object oriented programming.
"""

class Bomb:
    def __init__(self):
        ""

    def talk(self):
        self.explode()

    def explode(self):
        print "BOOM!, The bomb explodes."

class Duck:
    def __init__(self):
        ""
    def talk(self):
        print "I am a duck, I will not blow up if you ask me to talk."    

class Kid:
    kids_duck = None

    def __init__(self):
        print "Kid comes around a corner and asks you for money so he could buy a duck."

    def takeDuck(self, duck):
        self.kids_duck = duck
        print "The kid accepts the duck, and happily skips along"

    def doYourThing(self):
        print "The kid tries to get the duck to talk"
        self.kids_duck.talk()


#Kid object initiated with an instance named myKid.
myKid = Kid()
# Bomb object initiated with instance namd myBomb.
myBomb = Bomb() 
#Run takeduck() method from Kid class on myKid obj. Will pass explode() method here to doYourThing() method as stated in the class
myKid.takeDuck(myBomb) 
# When this runs, this will access the "kids_duck" variable which will be assianed to a "mybomb" variable thats assigned ot  Bomb objet thats "talk()" method accesses the "explode()" method
myKid.doYourThing()
