student_marks = {
    "Pranav" : 90,
    "Amit" : 40,
    "Isha" : 87
}
passed_students = {}

for name , mark in student_marks.items():
   if mark>=75:
    passed_students[name]=mark

print(passed_students)
