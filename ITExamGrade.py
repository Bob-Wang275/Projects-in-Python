# I write and run this python program to collect and calculate three types of exams, Multiple Choice exams, Technical
# Writing exams and Analytical Programming exams. I can fill the content of that object and Display all the exam
# contents.

from ITExam import ITExam
from MultipleChoiceExam import MultipleChoiceExam
from TechnicalWritingExam import TechnicalWritingExam
from AnalyticalProgrammingExam import AnalyticalProgrammingExam


def fillITExam(oneExam):  # Ask for the users to enter the valid score for this exam object.
    while True:
        title = input("Enter the Exam Title:")
        if oneExam.setExamTitle(title):  # Check and set the exam title.
            break
    if isinstance(oneExam, MultipleChoiceExam):
        while True:
            TotalNumber = input("Total Number of Multiple Choice's Questions:")
            if oneExam.setTotalNumOfMCQuestion(TotalNumber):  # Check and set the total number of questions
                break
        while True:
            CorrectNumber = input("Total Number of Correct Multiple Choice's Questions:")
            if oneExam.setCorrectNumOfMCQuestion(CorrectNumber):  # Check and set the total correct number of questions
                break
    elif isinstance(oneExam, TechnicalWritingExam):
        while True:
            GrammerScore = input("Score of Grammer Portion:")
            if oneExam.setGrammerScore(GrammerScore):  # Check and set the score for grammer.
                break
        while True:
            SentenceSturctureScore = input("Score of Sentence Structure Portion:")
            if oneExam.setSentenceStructureScore(SentenceSturctureScore):  # Check and set the score for Sentences
                break
        while True:
            ContentScore = input("Score of Content Portion:")
            if oneExam.setContentScore(ContentScore):
                break
    elif isinstance(oneExam, AnalyticalProgrammingExam):
        while True:
            ShortAnsScore = input("Score of Short Answer Section:")
            if oneExam.setShortAnswerScore(ShortAnsScore):
                break
        while True:
            ProgramScore = input("Score of Programming Section:")
            if oneExam.setProgrammingScore(ProgramScore):
                break
    oneExam.getExamGrade()
    exam_info = oneExam.toString()
    return exam_info


def displayResults(elist):  # Print the list of exams' information.
    for e in elist:
        print(e)


def main():
    exam_number = 0
    sum_scores = 0
    exam_list = []
    user_y_or_n = "Yes"
    while user_y_or_n == "Yes":
        print()
        print("IT Exam Type Menu:")
        print("1) Multiple Choice")
        print("2) Technical Writing")
        print("3) Analytical Programming")  # Print the Menu
        user_choice = input("Enter your choice: ")  # Ask the type of one exam
        if user_choice == "1" or user_choice == "2" or user_choice == "3":
            if user_choice == "1":  # Classify three kinds of exams. Object in different classes.
                exam = MultipleChoiceExam()
            elif user_choice == "2":
                exam = TechnicalWritingExam()
            elif user_choice == "3":
                exam = AnalyticalProgrammingExam()
            # exam = ITExam()
            exam_list.append(fillITExam(exam))
            exam_number = exam_number + 1  # Calculate the number of exams
            sum_scores = sum_scores + exam.ExamScore  # Calculate the sum score of exams
            user_y_or_n = input("More IT Exams (Yes/No)?")  # Ask if more exams
        else:
            print("\nSorry! No such choice. Please enter it again.")
            print()
    displayResults(exam_list)  # Display the results
    ave_scores = sum_scores / exam_number  # Calculate the average score.
    print()
    print("Total Score of All Exams:" + str(sum_scores))
    print("Average Score of All Exams:" + str(ave_scores))


if __name__ == "__main__":
    main()
