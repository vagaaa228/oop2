class User:
	def set_age(self ,age):
		if age >= 0:
			self.age = age
		else:
			raise Exception('need age more 0')

class Employee:
	def set_age(self, age):
		if age >= 0 and age <= 120:
			self.age = age
		else:
			raise Exception('Age out of range')