##Fraction Assignment 

def reduceFrac():
    import Fraction
    F = Fraction.fraction()
    F.Numerator = 3
    F.Denominator = 9
    
    result = F.Reducible()

    if result == True:
        print ("The Fraction is reducible")
    else:
        print ("The Fraction is not reducible")

def displayFloat():
    import Fraction
    F = Fraction.fraction()
    F.Numerator = 3
    F.Denominator = 4

    realNum = F.ToFloat()

    print(realNum)

def mostReduce():
    import Fraction
    F = Fraction.fraction()
    F.Numerator = 15
    F.Denominator = 45

    reduce = F.Reduce()

    print (reduce)

def displayAddResult():
    import Fraction
    F1 = Fraction.fraction()
    F1.Numerator = 1
    F1.Denominator = 2

    F2 = Fraction.fraction()
    F2.Numerator = 1
    F2.Denominator = 4

    result = F1.Add(F2)

    print(result)

def compare():
    import Fraction
    F1 = Fraction.fraction()
    F1.Numerator = 7
    F1.Denominator = 9

    F2 = Fraction.fraction()
    F2.Numerator = 4
    F2.Denominator = 5

    compare = F1.CompareToMe(F2)

    print(compare)

def displayFloat():
    import Fraction
    F1 = Fraction.fraction()
    F1.Numerator = 1
    F1.Denominator = 5

    F2 = Fraction.fraction()
    F2.Numerator = 1
    F2.Denominator = 4

    float1 = F1.ToFloat()
    float2 = F2.ToFloat()
    float3 = float1 + float2
    print (float3)

def equal():
    import Fraction
    F1 = Fraction.fraction()
    F1.Numerator = 2
    F1.Denominator = 3

    F2 = Fraction.fraction()
    F2.Numerator = 6
    F2.Denominator = 9

    compare = F1.CompareToMe(F2)

    if compare == 0:
        print ("The fractions are equal")
    else:
        print ("The fractions are not equal")

def equal2():
    import Fraction
    F1 = Fraction.fraction()
    F1.Numerator = 1
    F1.Denominator = 2

    F2 = Fraction.fraction()
    F2.Numerator = 1
    F2.Denominator = 4

    F3 = Fraction.fraction()
    F3.Numerator = 6
    F3.Denominator = 8

    add = F1.Add(F2)


    compare = add.CompareToMe(F3)

    if compare == 0:
        print ("The fractions are equal")
    else:
        print ("The fractions are not equal")


def displayReduced():
    import Fraction
    F1 = Fraction.fraction()
    F1.Numerator = 6
    F1.Denominator = 8

    reduce = F1.Reduce()

    print ("The most reduced form of", F1, "is", reduce)

    

    
        

    

    
    

    
    

    


    

    

    

    
        
