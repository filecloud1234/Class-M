# Write a Python program that takes a list of numbers as input and prints all the even numbers in the list.

n = int(input("Enter Your Iteration:"))
numbers = []
for i in range(n):
    number = int(input("Enter Your Numbers:"))
    if number%2 == 0 :
        numbers.append(number)
    else:
        pass
print(numbers)