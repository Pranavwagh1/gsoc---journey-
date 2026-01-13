def is_passed(student):
    return student["marks"] >= 75


students = [
    {"name": "Pranav", "marks": 90},
    {"name": "Amit", "marks": 40},
    {"name": "Isha", "marks": 87},
    {"name": "Rahul", "marks": 65}
]

passed_students = []
failed_students = []

for student in students:
    if is_passed(student):
        passed_students.append(student)
    else:
        failed_students.append(student)

print("Passed students:")
for student in passed_students:
    print(student["name"])

print("\nFailed students:")
for student in failed_students:
    print(student["name"])

print("\nTotal Passed:", len(passed_students))
print("Total Failed:", len(failed_students))
