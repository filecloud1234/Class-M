students = []

def insert(name):
    if search(name):
        return "Your name is existing"
    else:
        students.append(name)
        return "Your name added successfully"
    
def remove(name):
    if search(name = name) == True:
        students.remove(name)
        return "Your name removed successfully"
    else:
        return "Your name not found"

def search(name):
    return name in students
 
while True:
    user = input("Enter User's Name: ")
    sign = input("Enter Your Sign: ")

    if sign == "+":
        print(insert(user))

    elif sign == "-":
        print(remove(user))

    print(students)
    
    state = input("Do you want to continue: ")
    if state == "T":
        continue
    else:
        break