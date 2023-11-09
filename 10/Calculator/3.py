a = [['2-3'], ['2-3'] , ['4-5'], ['1-8']]

[['2-3'], ['2-3']]

if len(a)%2 == 0:
    n = len(a)-1
elif len(a)%2 != 0:
    n = len(a)

q = 1

for i in range(0,n,2):
    print(q)
    q = q + 1
    for j in a[i:i+2]:
        print(j[0])