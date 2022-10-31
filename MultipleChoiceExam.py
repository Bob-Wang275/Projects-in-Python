from ITExam import ITExam


class MultipleChoiceExam(ITExam):
    POINTS_PER_QUESTION = 2
    MAX_NQUESTIONS = ITExam.MAX_SCORE / POINTS_PER_QUESTION

    def __init__(self):  # Assign the initial value
        ITExam.__init__(self)
        self.TotalNumOfMCQ = 0
        self.CorrectNumofMCQ = 0

    def setTotalNumOfMCQuestion(self, TNumOfMCQ):
        TNumOfMCQ = float(TNumOfMCQ)
        if 0 <= TNumOfMCQ <= self.MAX_NQUESTIONS:
            self.TotalNumOfMCQ = TNumOfMCQ
            return True
        else:
            print()
            print("Sorry! The number is not valid. Please enter it again.")
            return False

    def getTotalNumofMCQuestion(self):
        return self.TotalNumOfMCQ

    def setCorrectNumOfMCQuestion(self, CNumOfMCQ):
        CNumOfMCQ = float(CNumOfMCQ)
        if 0 <= CNumOfMCQ <= self.TotalNumOfMCQ:
            self.CorrectNumofMCQ = CNumOfMCQ
            return True
        else:
            print()
            print("Sorry! The number is not valid. Please enter it again.")
            return False

    def getCorrectNumOfMCQuestion(self):
        return self.CorrectNumofMCQ

    def getExamGrade(self):
        self.setExamScore(self.CorrectNumofMCQ * self.POINTS_PER_QUESTION)
        # Compute the score according the rule.
        self.ExamGrade = ITExam.getExamGrade(self)
        return self.ExamGrade

    def toString(self):  # Return the information of exams
        e = ITExam.toString(self)
        e += "\nTotal Number of MC Questions: " + str(self.getTotalNumofMCQuestion())
        e += "\nTotal Number of Correct MC Questions: " + str(self.getCorrectNumOfMCQuestion())
        e += "\nFinal Grade: " + self.getExamGrade()
        return e



