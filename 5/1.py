a = ['a','b','c']
b = ['c','d','f']

final = []
for i in a:
    if i in b:
        final.append(i)
    else:
        pass
print(final)