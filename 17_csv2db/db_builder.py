#Devin Lin, David Lupea
#StraightOuttaSoftDev
#SoftDev pd 2
#K17 - No Trouble
#10/10/19

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db

# reads from the courses file and creates a new table
c.execute("DROP TABLE courses")
c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)")
courses = open("courses.csv","r")
reader = csv.DictReader(courses)
for row in reader:
    code = str(row["code"])
    mark = int(row["mark"])
    id = int(row["id"])
    c.execute("INSERT INTO courses VALUES(?,?,?)",(code,mark,id))
courses.close()

# reads from the students file and creates a new table
c.execute("DROP TABLE students")
c.execute("CREATE TABLE students(name TEXT, age INTEGER, id INTEGER)")
students = open("students.csv","r")
reader = csv.DictReader(students)
for row in reader:
    name = str(row["name"])
    age = int(row["age"])
    id = int(row["id"])
    c.execute("INSERT INTO courses VALUES(?,?,?)",(name,age,id))
students.close()

command = "SELECT name, students.id, courses.id, mark FROM students, courses WHERE students.id = courses.id;"          # test SQL stmt in sqlite3 shell, save as string
test = c.execute(command)    # run SQL statement
print(test)

for row in test:
    print(row)
#==========================================================

db.commit() #save changes
db.close()  #close database
