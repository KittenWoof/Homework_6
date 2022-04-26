class Student:
	def __init__(self, name, surname, gender):
		self.name = name
		self.surname = surname
		self.gender = gender
		self.finished_courses = []
		self.courses_in_progress = []
		self.grades = {}

	def rate_lecturer(self, lecturer, course, grade):
		if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
			if course in lecturer.grades:
				lecturer.grades[course] += [grade]
			else:
				lecturer.grades[course] = [grade]
		else:
			return 'Ошибка'	
	
	def avg_grade(self):
		sum_grade = 0
		len_grade = 0
		for list in self.grades.values():
			for item in list:
				sum_grade += item
				len_grade += 1
		return sum_grade / len_grade
	def __str__(self):
		return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self.avg_grade(), 1)}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

	def __gt__(self, other):
		if isinstance(other, Student):
			return self.avg_grade > other.avg_grade
		return 'Ошибка'	
	def __lt__(self, other):
		if isinstance(other, Student):
			return self.avg_grade < other.avg_grade
		return 'Ошибка'
	def __ge__(self, other):
		if isinstance(other, Student):
			return self.avg_grade >= other.avg_grade
		return 'Ошибка'
	def __le__(self, other):
		if isinstance(other, Student):
			return self.avg_grade <= other.avg_grade
		return 'Ошибка'


class Mentor:
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname
		self.courses_attached = []

class Lecturer(Mentor):
	def __init__(self, name, surname):
		super().__init__(name, surname)
		self.grades = {}
		self.courses_attached = []
	def avg_grade(self):
		sum_grade = 0
		len_grade = 0
		for list in self.grades.values():
			for item in list:
				sum_grade += item
				len_grade += 1
		return sum_grade / len_grade
	def __str__(self):
		return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self.avg_grade(), 1)}'
	
	def __gt__(self, other):
		if isinstance(other, Lecturer):
			return self.avg_grade > other.avg_grade
		return 'Ошибка'	
	def __lt__(self, other):
		if isinstance(other, Lecturer):
			return self.avg_grade < other.avg_grade
		return 'Ошибка'
	def __ge__(self, other):
		if isinstance(other, Lecturer):
			return self.avg_grade >= other.avg_grade
		return 'Ошибка'
	def __le__(self, other):
		if isinstance(other, Lecturer):
			return self.avg_grade <= other.avg_grade
		return 'Ошибка'
		
class Reviewer(Mentor):
	def __init__(self, name, surname):
		super().__init__(name, surname)
	def rate_hw(self, student, course, grade):
		if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
			if course in student.grades:
				student.grades[course] += [grade]
			else:
				student.grades[course] = [grade]
		else:
			return 'Ошибка'
	def __str__(self):
		return f'Имя: {self.name}\nФамилия: {self.surname} '




def avg_grade_all_students(name_course, list_students):
	sum_grades = 0
	count_grades = 0
	for item in list_students:
		for grade in item.grades[name_course]:
			sum_grades += grade
			count_grades += 1
	return sum_grades / count_grades

def avg_grade_all_lecturers(name_course, list_lecturers):
	sum_grades = 0
	count_grades = 0
	for item in list_lecturers:
		for grade in item.grades[name_course]:
			sum_grades += grade
			count_grades += 1
	return sum_grades / count_grades

