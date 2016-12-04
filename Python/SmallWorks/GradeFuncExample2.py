def main():
    NumStud = int(input("How many students:"))

    StudNum = 0
    A = 0
    B = 0
    C = 0
    D = 0
    F = 0
    Total = 0
    HighestScore = 0
    LowestScore = 100

    for StudNum in range(1,NumStud+1):
        Name = input("Student #"+str(StudNum)+"'s name:")
        Score = int(input(Name+"'s score:"))
        while Score < 0 or Score > 100:
            print ("That is not a valid score.")
            Score = int(input(Name+"'s score:"))
        Grade = ScoreToGrade(Score)
        print (Name,"get's a grade of",Grade)
        if Grade == 'A':
            A += 1
        else:
            if Grade == 'B':
                B += 1
            else:
                if Grade == 'C':
                    C += 1
                else:
                    if Grade == 'D':
                        D += 1
                    else:
                        F += 1
        if Score < LowestScore:
            LowestScore = Score
        if Score > HighestScore:
            HighestScore = Score
        Total += Score
    
    print()
    print("The highest score was",HighestScore)
    print("The lowest  score was",LowestScore)
    print("The average score was",Total/NumStud)
    print("Number of A's:",A)
    print("Number of B's:",B)
    print("Number of C's:",C)
    print("Number of D's:",D)
    print("Number of F's:",F)


def ScoreToGrade(Score):
    if Score >= 90:
        return 'A'
    if Score >= 80:
        return 'B'
    if Score >= 70:
        return 'C'
    if Score >= 60:
        return 'D'
    return 'F'


main()

