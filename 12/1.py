import json

name = input("Enter Your Name:")
age = input("Enter Your Age:")

courses = {}

for i in range(3):
    course = input("Enter your course:")
    course = course.split(",")
    courses[course[0]] = course[1]
    # courses.update({"math",12})
print(courses)

j = '{"name":"ali","age":10}'

j1 = [
    {
        "name":name,
        "age":age,
        "courses":courses
    }
]

y = json.loads(j)
y1 = json.dumps(j1)

print(type(y))
print(y1)