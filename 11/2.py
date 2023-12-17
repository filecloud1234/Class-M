
def search(name):
    f = open("output.txt", "r")
    for i in range(8):
        if name == f.readline():
            print(name)

search("ali")

# f.close()
