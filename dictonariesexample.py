def studentInfo(data, **kwargs):
    for student in data:
        match = True

        for key in kwargs:
            if student[key] != kwargs[key]:
                match = False
                break

        if match:
            return student

    return None


students = []
n = int(input('Enter the students no: '))

for i in range(n):
    name = input("Enter the name: ")
    age = int(input("Enter Age: "))
    grade = input("Enter Grade: ")     

    student = {
        "name": name,
        "age": age,
        "grade": grade
    }

    students.append(student)


key = input("Filter by (name, age, grade): ")
value = input("Enter value: ")

if key == "age":
    value = int(value)

result = studentInfo(students, **{key: value})

if result:
    print("Result:", result)
else:
    print("No student found")