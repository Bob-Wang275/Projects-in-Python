from ITExam import ITExam


class TechnicalWritingExam(ITExam):  # Assign the initial value
    GRAMMER_PERCENT = 0.3
    SENTENCE_PERCENT = 0.3
    CONTENT_PERCENT = 0.4

    def __init__(self):
        ITExam.__init__(self)
        self.GrammerScore = 0
        self.SentenceStructureScore = 0
        self.ContentScore = 0

    def setGrammerScore(self,GrammerS):
        GrammerS = float(GrammerS)
        if 0 <= GrammerS <= self.MAX_SCORE:
            self.GrammerScore = GrammerS
            return True
        else:
            print()
            print("Sorry! The score is not valid. Please enter it again.")
            return False

    def getGrammerScore(self):
        return self.GrammerScore

    def setSentenceStructureScore(self, SentenceStructureS):
        SentenceStructureS = float(SentenceStructureS)
        if 0 <= SentenceStructureS <= self.MAX_SCORE:
            self.SentenceStructureScore = SentenceStructureS
            return True
        else:
            print()
            print("Sorry! The score is not valid. Please enter it again.")
            return False

    def getSentenceStructureScore(self):
        return self.SentenceStructureScore

    def setContentScore(self,ContentS):
        ContentS = float(ContentS)
        if 0 <= ContentS <= self.MAX_SCORE:
            self.ContentScore = ContentS
            return True
        else:
            print()
            print("Sorry! The score is not valid. Please enter it again.")
            return False

    def getContentScore(self):
        return self.ContentScore

    def getExamGrade(self):
        self.setExamScore(self.GrammerScore*self.GRAMMER_PERCENT + self.SentenceStructureScore*self.SENTENCE_PERCENT + self.ContentScore*self.CONTENT_PERCENT)
        # Compute the score according the rule.
        self.ExamGrade = ITExam.getExamGrade(self)
        return self.ExamGrade

    def toString(self):  # Return the information of exams
        e = ITExam.toString(self)
        e += "\nScore of Grammer Portion:" + str(self.getGrammerScore())
        e += "\nScore of Sentence Structure Portion: " + str(self.getSentenceStructureScore())
        e += "\nScore of Content Portion: " + str(self.getContentScore())
        e += "\nFinal Grade: " + self.getExamGrade()
        return e