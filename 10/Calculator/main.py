history = []

def Addition(x, y):
    history_handler(x, y, "+")
    return x + y

def Subtraction(x, y):
    history_handler(x, y, "-")
    return x - y

def multiplication(x, y):
    history_handler(x, y, "*")
    return x * y

def division(x, y):
    history_handler(x, y, "/")
    return x / y

def Exponentiation(x, y):
    history_handler(x, y, "**")
    return x ** y

def Modulus(x, y):
    history_handler(x, y, "%")
    return x % y

def	Floor_division(x, y):
    history_handler(x, y, "//")
    return x // y

def history_handler(x, y, z):
    result = []
    result.append(str(x) + z + str(y))
    history.append(result)

while True:
    a = input("Enter Your Action:")

    if a != "history" and a != "C":
        x = int(input("Enter Your Number:"))
        y = int(input("Enter Your Number:"))

    if a == "+":
        print(Addition(x, y))

    elif a == "-":
        print(Subtraction(x, y))

    elif a == "*":
        print(multiplication(x, y))

    elif a == "/":
        print(division(x, y))

    elif a == "**":
        print(Exponentiation(x, y))

    elif a == "%":
        print(Modulus(x, y))

    elif a == "//":
        print(Floor_division(x, y))
  
    elif a == "history":
        if not history:
            print("History is Empty")
        else:
            q = 1
            if len(history) >= 2:
                if len(history) % 2 == 0:
                    end = len(history) - 1
                elif len(history) % 2 != 0:
                    end = len(history)

                for i in range(0,end,2):
                    print(q)
                    q = q + 1
                    
                    for j in history[i:i+2]:
                        print(j[0])
                    
                    pagination = input("Do you want to continue?")
                    if pagination == "Y":
                        continue
                    else:
                        break

            else:
                for i in history:
                    print(q, i[0])
                    q = q + 1


    elif a == "C":
        history.clear()

    else:
        print("Invalid operator!")
        
    n = input("Do You Want To Continue?")
    if n == "Y":
        continue
    else:
        break

# list.clear()
# [[], [], []]
# list()
# public/private