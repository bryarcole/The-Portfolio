def scoretograde(score):
    if score >= 90 and score <= 100:
        return ("A")
    elif score >= 80 and score < 90:
        return ("B")
    elif score >= 70 and score < 80:
        return ("C")
    elif score >= 60 and score < 70:
        return ("D")
    


def main():
     score = int(input("Enter the numeric score (-1 to quit): "))
     while (score >= 0):
         print (score,"get's a grade of",scoretograde(score))
         score = int(input("Enter the numeric score (-1 to quit): "))
     print()
     print("Thank's for playing!")
main()

