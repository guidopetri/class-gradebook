#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#python 3.6.4

"""Student Gradebook Application – Keep track of students (with a student class that has their name, average, and scores) in a class and their grades. Assign their scores on tests and assignments to the students and figure out their average and grade for the class. For added complexity put the students on a bell curve."""

import random

random.seed(9)
studentCount = 10

class Grade():
	def __init__(self,gradeNum):
		self.students = []
		self.gradeNum = gradeNum
		self.size = len(self.students)
		self.calcAverage()
		self.calcMedian()
		return

	def addStudent(self,student):
		self.students.append(student)
		self.size += 1
		self.calcAverage()
		self.calcMedian()
		return

	def calcAverage(self):
		if len(self.students) > 0:
			self.average = round(sum([x.average for x in self.students])/len(self.students),2)
			self.valedictorian = tuple([(x.name,x.average) for x in self.students if x.average == max([y.average for y in self.students])])
			self.classclown = tuple([(x.name,x.average) for x in self.students if x.average == min([y.average for y in self.students])])
		else:
			self.average = 0
			self.valedictorian = 0
			self.classclown = 0
		return

	def calcMedian(self):
		if len(self.students) > 0:
			halflen = len(self.students)/2 - 1
			if halflen.is_integer():
				self.median = sum([y.average for y in sorted(self.students,key=lambda x:x.average)[int(halflen):int(halflen+2)]])/2
			else:
				self.median = sorted(self.students,key=lambda x:x.average)[int(halflen+0.5)].average
		else:
			self.median = 0
		return

class Student():
	def __init__(self,name,age):
		self.name = name
		self.age = age
		self.scores = []
		self.average = 0
		self.updateAverage()
		return

	def addGrade(self,grade,weight):
		self.scores.append((grade,weight))
		self.updateAverage()
		return

	def updateAverage(self):
		if len(self.scores) > 0:
			self.average = round(sum([x*y for (x,y) in self.scores])/sum([y for (x,y) in self.scores]),2)
		else:
			self.average = -1
		return

students = {}
studentNames = ['Sally','Joe','Bill','Pete','Aaron','Diana','Camilla']
lastNames = ['Bo','West','Cook','Bauer','Rogan','Stu','Oak']
gradeWeights = [random.randrange(1,5) for x in range(0,10)]

grade1 = Grade(1)

for i in range(0,studentCount):
	students[i] = Student(random.choice(studentNames)+" "+random.choice(lastNames),13)
	for j in range(0,10):
		students[i].addGrade(random.randrange(0,101),gradeWeights[j])
	grade1.addStudent(students[i])

printJob = sorted([(fulano.name,str(fulano.average)) for fulano in students.values()],key=lambda x:x[1],reverse=True)
for item in printJob:
	print(item[0]+",\t",item[1])
print("\nClass average: %s"%grade1.average)
print("\nClass median: %s"%grade1.median)
print("\nValedictorian: %s"%grade1.valedictorian)
print("\nClass clown: %s"%grade1.classclown)