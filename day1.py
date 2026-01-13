students = [
    {"name": "Pranav", "marks": 90},
    {"name": "Amit", "marks": 40},
    {"name": "Isha", "marks": 87}
]
passed_students = []

for student in students:
    if(student["marks"]>=75):
       passed_students.append(student)

print(passed_students)
