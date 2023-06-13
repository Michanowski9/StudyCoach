

class Answer:
	def __init__(self, text):			
		self.content = text
		self.value = False

	def __repr__(self):
		return "\'" + self.content + "\' <" + str(self.value) + ">"
		
	def __str__(self):
		return self.__repr__()


