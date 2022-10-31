class ITExam:
    MAX_SCORE = 100

    def __init__(self):  # Assign the initial value
        self.ExamTitle = "None"
        self.ExamScore = 0
        self.ExamGrade = ""

    def setExamTitle(self, title):
        if title == "":
            print("Sorry! The exam title is not valid. Please enter it again.")
            print()
            return False
        else:
            self.ExamTitle = title
            return True

    def getExamTitle(self):
        return self.ExamTitle

    def setExamScore(self, score):
        score = float(score)
        if 0 <= score <= self.MAX_SCORE:
            self.ExamScore = score
            return True
        else:
            print("Sorry! The score is not valid. Please enter it again.")
            return False

    def getExamScore(self):
        return self.ExamScore

    def getExamGrade(self):  # Transfer score to grade.
        if self.ExamScore >= 90:
            self.ExamGrade = "A"
        elif 80 <= self.ExamScore < 90:
            self.ExamGrade = "B"
        elif 70 <= self.ExamScore < 80:
            self.ExamGrade = "C"
        elif 60 <= self.ExamScore < 70:
            self.ExamGrade = "D"
        elif self.ExamScore < 60:
            self.ExamGrade = "F"
        return self.ExamGrade

    def toString(self):  # Return the information of exams
        e = "\nExam Title:" + self.getExamTitle()
        e += "\nExam Score:" + str(self.getExamScore())
        return e


