import os
import random
import sys

from question import *

databasesDir = "Databases/"


def getDatabases():
    return os.listdir(databasesDir)

def printDatabases():
    for i, database in enumerate(getDatabases()):
   	    print("[" + str(i) + "] " + database)	 
    
def chooseDatabase():
    databases = getDatabases()
    printDatabases()

    resultID = 0
    resultID = int(input("choose: "))

    return databases[resultID]
    
def getLoadedQuestion(file):
    result = Question()
    
    # load question content
    result.content = file.readline().strip()
    
    # load answers content
    answers_no = int(file.readline())
    for answer_id in range(answers_no):
        content = file.readline().strip()
        result.addAnswer(Answer(content))
    
    # set true to correct answers
    correct = file.readline().strip().split(",")
    for elem in correct:
        result.answers[(ord(elem)-ord('a'))].value = True
    
    return result	
    
def loadInput(databasePath):
    file = open(databasePath, 'r', errors="ignore", encoding='utf-8')
    
    questions = []
    while True:
        question = getLoadedQuestion(file)	
        questions.append(question)
        
        if not file.readline():
            break
    return questions
    
def shuffleQuestions(questions):
    random.shuffle(questions)
        
def getUserInput():
    return input("type answer: ")


totalScore = 0
userScore = 0

def printStatistics(questions):
    seenQuestions = 0
    totalQuestions = 0
    for elem in questions:
        totalQuestions += 1
        if elem.isNew == False:
            seenQuestions += 1
    if totalScore != 0:
        text = "\t" + str(int(userScore/totalScore*100)) + "%"
    else:
        text = "\t0%"
    print("correct: " + str(userScore) + "/" + str(totalScore) + text + "\t\tseen questions:" + str(seenQuestions) + "/" + str(totalQuestions))

    
if __name__ == '__main__':
    databaseName = chooseDatabase()
    questions = loadInput(databasesDir + databaseName)
    shuffleQuestions(questions)

    while True:
        if sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')
        questions[0].shuffle()

        printStatistics(questions)
        questions[0].print()
        questions[0].isNew = False

        correct = questions[0].getCorrectAnswers()
#        print(correct)
       
        userInput = sorted(getUserInput())
        print()

        if userInput == ['q']:
            break

        if userInput == correct:
            print("Correct answer")
            questions[0].points += 5
            userScore += 1
            questions.insert(random.randint(3,questions[0].points), questions[0])

        else:
            print("Wrong answer")
            print("Correct is: " + ','.join(correct).upper())
            questions[0].points = 0
            questions.insert(random.randint(3,10), questions[0])

        totalScore += 1
        questions.pop(0)
        input("press any key to continue... ")

        
