import sqlite3

connection = sqlite3.connect("Universitys.db")
cursor = connection.cursor()

def show_students_of_teacher(teacher_name = "akbar"):
    cursor.execute("""
        SELECT Students.name 
        FROM Students
        JOIN student_teacher ON Students.id = student_teacher.student_id
        JOIN Teachers ON Teachers.id = student_teacher.teacher_id
        WHERE Teachers.name = ?
        """, (teacher_name,))
    
    students = cursor.fetchall()

    if students:
        for i in students:
            print(i[0])
    else:
        print("There's no students aviable")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_teacher (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        teacher_id INTEGER,
        student_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES Teachers(id),
        FOREIGN KEY (student_id) REFERENCES Students(id)
    )
""")

sname = input("Please enter the student's name: ")
cursor.execute("INSERT INTO Students (name) VALUES (?)", (sname,))

tname = input("Please enter the teacher's name: ")
cursor.execute("INSERT INTO Teachers (name) VALUES (?)", (tname,))

student_id = int(input("Please enter the student_id: "))
teacher_id = int(input("Please enter the teacher_id: "))

cursor.execute("INSERT INTO student_teacher (teacher_id, student_id) VALUES (?, ?)", (teacher_id, student_id))

teacher_name_to_search = input("Enter the teacher's name to show their students: ")
show_students_of_teacher(teacher_name_to_search)

connection.commit()
connection.close()
