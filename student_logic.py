students = [
    {"name": "Pranav", "marks": 90},
    {"name": "Amit", "marks": 40},
    {"name": "Isha", "marks": 87},
    {"name": "Ishika", "marks": 45},
    {"name": "Rahul", "marks": 72},
    {"name": "Sneha", "marks": 95},
    {"name": "Vikram", "marks": 33},
    {"name": "Ananya", "marks": 68},
    {"name": "Rohan", "marks": 55},
    {"name": "Kavya", "marks": 82},
    {"name": "Arjun", "marks": 28},
    {"name": "Zoya", "marks": 91}
]

def has_passed(student):
    return student["marks"] >= 75


def separate_students(students):
    passed_students = [student for student in students if has_passed(student)]
    failed_students = [student for student in students if not has_passed(student)]

    return passed_students, failed_students
