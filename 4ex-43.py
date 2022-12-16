class Student():
	def __init__(self, name, age, marth_score, literature_score):
		self.name = name
		self.age = age
		self.marth_score = marth_score
		self.literature_score = literature_score
		self.teacher = "Phu Tam"

	def average_score(self):
		average_score = (self.marth_score + self.literature_score)/2
		return average_score

	def print_info(self):
		print("Student name", self.name, "study with", self.teacher, "have average score",self.average_score())

s1 = Student("Ronaldo", 37,9,10)
s2 = Student("Messi", 36,10,8)
s3 = Student("Son Heung Min", 30,9,9)

s2.teacher = "Tran Thuy"

students = []

students.append(s1)
students.append(s2)
students.append(s3)

for i in range(len(students)):
	students[i].print_info()


