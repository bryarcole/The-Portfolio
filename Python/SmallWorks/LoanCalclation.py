def LCP(principal, APR, numpay):
    
    rate = (APR/12)

    monpay = principal*((rate)*(1+ (rate)**(numpay)) / ((1 + rate)**(numpay) - 1))

    print (monpay)




def main():


    
    LoanCalc1 = LCP(principal=20000, APR=.04, numpay=36)
    LoanCalc2 = LCP(principal=20000, APR=.04, numpay=48)
    LoanCalc3 = LCP(principal=20000, APR=.04, numpay=60)
    LoanCalc4 = LCP(principal=20000, APR=.04, numpay=72)

    
