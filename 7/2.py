list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3 = []
list4 = []

for i in list1:
    if i % 2 != 0:
        list3.append(i)

for i in list2:
    if i % 2 != 0:
        list3.append(i)
    
print(list3)


###################

for i in range(len(list1)):
    if list1[i] % 2 != 0:
        list4.append(list1[i])
    if list2[i] % 2 != 0:
        list4.append(list2[i])

print(list4)

###################

# i = 1
# print(i)
# i = 2
# print(i)