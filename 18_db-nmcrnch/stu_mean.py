# Moududur "Moody" Rahman & David Lupea
#SoftDev
# STUDENT MEAN
#Oct 13 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O
import sys
import os

DB_FILE="discobandit.db"

try:
	os.remove(DB_FILE)
except Exception as e:
	pass

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

studf = open("students.csv", "r")
coursesf = open("courses.csv", "r")

stud = csv.DictReader(studf)
courses = csv.DictReader(coursesf)


c.execute("CREATE TABLE students(name STRING, age INTEGER, id INTEGER);")
c.execute("CREATE TABLE courses(code STRING, mark INTEGER, id INTEGER);")

for row in stud:
    command = "INSERT INTO students VALUES('{}', '{}', '{}')".format(row["name"], row["age"], row["id"])
    c.execute(command)

for row in courses:
    command = "INSERT INTO courses VALUES('{}', '{}', '{}')".format(row["code"], row["mark"], row["id"])
    c.execute(command)

def run():
	command = "SELECT * FROM students"
	allstudents = c.execute(command).fetchall()
	for stud in allstudents:
		command = "SELECT * FROM courses WHERE id = {};".format(stud[2])
		classes = c.execute(command).fetchall()
		s = ("HELLO I AM {}, OF ID {} AND I AM TAKING {}").format(stud[0], stud[2], [x[0] for x in classes])
		print(s)
		# for z in classes:
		cumsum = 0
		for cl in classes:
			cumsum += cl[1]
		sss = ("MY AVERAGE IS {}").format(round(cumsum / len(classes), 2))
		print(sss)
		print("")



	command = ""          # test SQL stmt in sqlite3 shell, save as string
	c.execute(command)    # run SQL statement

def lookup(student):
	command = "SELECT * FROM students WHERE name = '{}'".format(student)
	c.execute(command)
	stud = c.fetchall()
	if len(stud) == 0:
		print("student not found")
		return
	command = "SELECT * FROM courses WHERE id = {}".format(stud[0][2])
	allcourses = c.execute(command).fetchall()

	cumsum = 0
	for x in allcourses:
		cumsum += x[1]
	# print(cumsum / len(allcourses))
	s =  ''' HELLO I AM {}, OF ID {}, MY AVERAGE IS {}'''.format(stud[0][0], stud[0][2], cumsum / len(allcourses))
	print(s)

if __name__ == '__main__':
	while True:
		z = input("what u want: ")
		z = z.split(" ")
		if z[0] == "allstudents":
			run()
			break
		elif z[0] == "lookup":
			lookup(z[1])
			break
	db.commit() #save changes
	db.close()  #close database
