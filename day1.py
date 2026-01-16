"""
Student Result Processing System
--------------------------------
Features:
- Separate passed and failed students
- Show top performers (90+)
- Display summary statistics

Author: Pranav Wagh
"""

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
     return student['marks']>=75


def separate_students(students):
       passed_students = []
       falied_students=[]
       for student in students:
          if has_passed(student):
               passed_students.append(student)
          else:
               falied_students.append(student)
        
       return passed_students , falied_students


def generate_report(students) : 
    passed , failed = separate_students(students) 

    print("📘 STUDENT RESULT REPORT\n")
    print("✅ Passed Students:")
    for i in passed :
        print("--",i['name'])

    print("\n❌ Failed Students:")
    for i in failed:
        print("-", i["name"])

    print("\n🏆 Top Performers (90+):")
    for student in passed:
        if student["marks"] >= 90:
                print("-", student["name"])


    total = len(students)
    passed_count = len(passed)
    failed_count = len(failed)

    pass_percentage = (passed_count / total) * 100

    print("\n📊 Summary:")
    print("Total Students:", total)
    print("Passed:", passed_count)
    print("Failed:", failed_count)
    print("Pass Percentage:", pass_percentage, "%")


generate_report(students)



