class Student:
	def __init__(self,name,age,math_score,literature_score):
		self.name = name
		self.age = age
		self.math_score = math_score
		self.literature_score = literature_score
		self.teacher = "Phu Tam"

	def average_score(self):
		self.ave_score = (self.math_score + self.literature_score)/2
		return self.ave_score

	def print_info(self):
		ave_score = str(self.average_score())
		print("Student name " + self.name + " study with " + self.teacher + " have average score " + ave_score)	

students = []

s1 = Student("Ronaldo", 21, 9, 7)
s2 = Student("Messi", 20, 8, 9)
s3 = Student("Neymar Jr", 19, 10,7)
s4 = Student("Son Heung Min",18,9,10 )

s2.teacher = "Tran Thuy"

students.append(s1)
students.append(s2)
students.append(s3)
students.append(s4)

for i in range(len(students)):
	students[i].print_info()