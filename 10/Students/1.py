name = "ali" #input("Enter your Name: ")
f_name = "alizadeh" #input("Enter your Family Name: ")
age = 12 #int(input("Enter your Family Age: "))
n = 2 #int(input("Enter your course numbers: "))

courses = []

for i in range(0, n):
    course_name = input("Enter your Course: ")
    course_score = input("Enter your Score: ")
    final = [course_name,course_score]
    courses.append(final)

f = open("output.txt", "+a")
f.write(f"{name},{f_name},{age},{str(courses)}"+"\n")
f.close()