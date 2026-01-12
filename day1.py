student_marks = {
    "Pranav" : 90,
    "Amit" : 40,
    "Isha" : 87
}
passed_students = {}

def is_passed(mark):
    return mark >= 75

for name , mark in student_marks.items():
   if is_passed(mark):
    passed_students[name]=mark

print(passed_students)
