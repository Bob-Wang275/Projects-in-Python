from ITExam import ITExam


class AnalyticalProgrammingExam(ITExam):
    SHORT_ANSWER_PERCENT = 0.3
    PROGRAMMING_PERCENT = 0.7

    def __init__(self):  # Assign the initial value
        ITExam.__init__(self)
        self.ShortAnswerScore = 0
        self.ProgrammingScore = 0

    def setShortAnswerScore(self, ShortAnswerS):
        ShortAnswerS = float(ShortAnswerS)
        if 0<= ShortAnswerS <= self.MAX_SCORE:
            self.ShortAnswerScore = ShortAnswerS
            return True
        else:
            print()
            print("Sorry! The score is not valid. Please enter it again.")
            return False

    def getShortAnswerScore(self):
        return self.ShortAnswerScore

    def setProgrammingScore(self, ProgrammingS):
        ProgrammingS = float(ProgrammingS)
        if 0 <= ProgrammingS <= self.MAX_SCORE:
            self.ProgrammingScore = ProgrammingS
            return True
        else:
            print()
            print("Sorry! The score is not valid. Please enter it again.")
            return False

    def getProgrammingScore(self):
        return self.ProgrammingScore

    def getExamGrade(self):
        self.setExamScore(self.ShortAnswerScore*self.SHORT_ANSWER_PERCENT+self.ProgrammingScore*self.PROGRAMMING_PERCENT)
        # Compute the score according the rule.
        self.ExamGrade = ITExam.getExamGrade(self)
        return self.ExamGrade

    def toString(self):
        e = ITExam.toString(self)
        e += "\nScore of Short Answer Section: " + str(self.getShortAnswerScore())
        e += "\nScore of Programming Section: " + str(self.getProgrammingScore())
        e += "\nFinal Grade: " + self.getExamGrade()
        return e