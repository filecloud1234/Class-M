history = []

def sum(x, y):
    history_handler(x, y, "+")
    return x + y

def minus(x, y):
    history_handler(x, y, "-")
    return x - y

def multiple(x, y):
    history_handler(x, y, "*")
    return x * y

def division(x, y):
    history_handler(x, y, "/")
    return x / y

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
        print(sum(x, y))

    elif a == "-":
        print(minus(x, y))

    elif a == "*":
        print(multiple(x, y))

    elif a == "/":
        print(division(x, y))

    elif a == "history":
        if not history:
            print("History is Empty")
        else:
            q = 1
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