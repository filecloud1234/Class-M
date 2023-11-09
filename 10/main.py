students = []

def insert(name, Family_Name):
    if search(name, Family_Name):
        return "Your name is existing"
    else:
        students.append(name)
        return "Your name added successfully"
    
def remove(name, Family_Name):
    if search(name = name) == True:
        students.remove(name)
    elif search(Family_Name = Family_Name) == True:
        return "Your name removed successfully"
    else:
        return "Your name not found"    

def search(name, Family_Name):
    return name,Family_Name in students

def courses(courses):
    for i in range(f):
        f = int(input("Enter your courses: "))
    


while True:
    user_n = input("Enter User's Name: ")
    user_f = input("Enter User's Family Name: ")
    sign = input("Enter Your Sign: ")

    if sign == "+":
        print(insert(user_n, user_f))

    elif sign == "-":
        print(remove(user_n, user_f))

    print(students)
    
    state = input("Do you want to continue: ")
    if state == "T":
        continue
    else:
        print("See you later")
        break