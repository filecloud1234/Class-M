names = ["ali", "gholi", "sadra", "nazanin", "mohammad", "simin", "soroosh", "sima"]

f = open("output.txt", "+a")

for i in names:
    f.write(i + "\n")

f.close()
