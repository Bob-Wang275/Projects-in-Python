# I write and run this python program that can input any number of students
# and their any number of exam scores to compute each of their average, highest,
# and lowest scores among all the scores entered for those students。
def isNum(value):  # Whether the string consist of numbers
    try:
        f = float(value)
    except ValueError:
        print("The score entered is not a number. Please enter it again.")
        print()
        return False
    else:
        return True
def main():
    n = 0  # variable with the number of student
    b = "yes"  # yes or no
    average = []  # Create a list with the average of scores for each student
    high = []   # Create a list with the highest scores for each student
    low = []   # Create a list with the lowest scores for each student
    ne = []   # Create a list with the number of exams for each student
    while (b=="yes" or b=="Yes"):
        n = n+1
        m = 0  # variable with the number of exams for one student
        s = 0.0  # variable with the sum of scores for one student
        max = 0.0  # variable with the highest score for one student. Its initial value should be small
        min = 10000.0  # variable with the lowest score for one student. Its initial value should be large
        a = input("Please enter Student {}'s score (-1: Exit): ".format(n))
        while (True):
            while(not isNum(a)):   # We can't calculate if the score entered is not a number
                a = input("Please enter Student {}'s score (-1: Exit): ".format(n))  # I need to enter again.
            a = float(a)  # Until I enter a number. Convert it.
            if a == -1:
                print()
                break    # -1 means exit
            else:
                if (a > max):
                    max = a       # Finding the highest score
                if (a < min):
                    min = a       # Finding the lowest score
                s = s + a    # Adding the score
                m = m + 1    # Counting how many exams
                a = input("Please enter Student {}'s score (-1: Exit): ".format(n))   # I enter next score or exit.
        if (m==0):
            ave = max = min = 0   # If zero exam is taken, every value about score are zero.
        else:
            ave = s/m  # Sum of scores divided by number of exams equals average score
        average.append(ave)
        ne.append(m)
        high.append(max)
        low.append(min)  # Appending every data to the list it should be in.
        b = input("Any more student?(Yes or No)")  # I enter if any more student.
        print()
        while (b != "yes") and (b != "no") and (b != "Yes") and (b != "No"):  # Checking if valid
            print()
            b = input("Any more student?(Yes or No)")
            print()
    i=1
    while (i <= n):  # Output students with serial numbers from 1 to n.
        print("Student", i, "took", ne[i-1], "exams")  # Output which student and how many exams are taken by the student.
        print("Average Score:", round(average[i-1], 2))  # Output the average score of the student, just 2 decimal places.
        print("Highest Score:", high[i-1])  # Output the highest score of the student
        print("Lowest Score:", low[i-1])  # Output the lowest score of the student
        print()
        i = i+1  # Moving to the next student
if __name__ == "__main__":
    main()