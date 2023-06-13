import random

from answer import *

class Question:
    questionID = 0
    def __init__(self):
        self.id = Question.questionID
        Question.questionID += 1
        self.content = ""
        self.answers = []
        self.points = 0
        self.isNew = True
        
    def addAnswer(self, answer):
        self.answers.append(answer)
        
    def shuffle(self):
        random.shuffle(self.answers)
        
    def print(self):
        print(str(self.id) + ". " + self.content)
        for i, answer in enumerate(self.answers):
            print(chr(i + ord('a')).upper() + ") " + answer.content)

    def getCorrectAnswers(self):
        result = []
        for i, answer in enumerate(self.answers):
            if answer.value == True:
                result.append(chr(i + ord('a')))
        return result

    def __repr__(self):
        result = "{question: \'" + self.content + "\' answers: ["
        for answer in self.answers:
            result += str(answer) + ","	
        return result[:-1] + "]}"
        
    def __str__(self):
        return self.__repr__()
        
        
