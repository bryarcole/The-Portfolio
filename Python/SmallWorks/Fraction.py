
class fraction:
    def __init__(self):
        self.Numerator = 3
        self.Denominator = 9

    def __str__(self):
        return str(self.Numerator)+"/"+str(self.Denominator)

    def __repr__(self):
        return self.__str__()

    def ToFloat(self):
        return float(self.Numerator / self.Denominator)

    def ReduceMe(self):
        HCF = self.__HighestCommonFactor(self.Numerator,self.Denominator)
        if (HCF==1):
            return
        self.Numerator = self.Numerator // HCF
        self.Denominator = self.Denominator // HCF
        return

    def Reduce(self):
        temp = fraction()
        temp.Numerator = self.Numerator;
        temp.Denominator = self.Denominator;
        temp.ReduceMe()
        return temp

    def AddToMe(self,F):
        if (self.Denominator != F.Denominator):
            self.Numerator = (self.Numerator * F.Denominator) + (F.Numerator * self.Denominator)
            self.Denominator *= F.Denominator
        else:
            self.Numerator += F.Numerator

    def Add(self,F):
        NF = fraction()
        NF.Numerator = self.Numerator + F.Numerator
        NF.Denominator = self.Denominator
        if (self.Denominator != F.Denominator):
            NF.Numerator = (self.Numerator * F.Denominator) + (F.Numerator * self.Denominator)
            NF.Denominator = self.Denominator * F.Denominator
        return NF;

    def CompareToMe(self,F):
        x = self.ToFloat()
        y = F.ToFloat()
        if (x < y):
            return -1
        if (x > y):
            return 1
        return 0

    def __PrimeFactors(self,x):
        F = []
        Divisor = 2
        while (Divisor < x):
            if ((x % Divisor) == 0):
                F.append(Divisor)
                x = int(x / Divisor)
                Divisor = 2
            else:
                Divisor += 1
        F.append(x)
        return F

    def __HighestCommonFactor(self,x,y):
        HCF = 1
        XF = self.__PrimeFactors(x)
        for i in XF:
            if ((y % i) == 0):
                y = y // i
                HCF *= i
        return HCF

    def Reducible(self):
        if (self.__HighestCommonFactor(self.Numerator,self.Denominator)==1):
            return False
        return True


