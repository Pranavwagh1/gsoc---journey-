students = [
    {"name": "Pranav", "marks": 90},
    {"name": "Amit", "marks": 40},
    {"name": "Isha", "marks": 87}
]
passed_students = []

def is_passed(student):
     return student['marks']>=75

for student in students:
    if is_passed(student):
       passed_students.append(student)

print(passed_students)
