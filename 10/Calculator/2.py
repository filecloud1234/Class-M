a = [0,1,2,3]

if len(a)%2 == 0:
    n = len(a)-1
elif len(a)%2 != 0:
    n = len(a)

for i in range(0,n,2):
    print(i)
    print(a[i:i+2])