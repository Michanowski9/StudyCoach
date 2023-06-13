import os

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
	file = open(databasePath)
	
	questions = []
	while True:
		question = getLoadedQuestion(file)	
		questions.append(question)

		if not file.readline():
			break
	return questions

if __name__ == '__main__':
	databaseName = chooseDatabase()
	temp = loadInput(databasesDir + databaseName)
	print(temp)
	
