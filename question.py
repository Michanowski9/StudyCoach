from answer import *

class Question:
	def __init__(self):
		self.content = ""
		self.answers = []

	def addAnswer(self, answer):
		self.answers.append(answer)

	def __repr__(self):
		result = "{question: \'" + self.content + "\' answers: ["
		for answer in self.answers:
			result += str(answer) + ","	
		return result[:-1] + "]}"
		
	def __str__(self):
		return self.__repr__()


