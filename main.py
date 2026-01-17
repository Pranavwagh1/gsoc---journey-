from student_logic import students, separate_students

def generate_report(students):
    passed, failed = separate_students(students)

    print("📘 STUDENT RESULT REPORT\n")

    print("✅ Passed Students:")
    for student in passed:
        print("-", student["name"])

    print("\n❌ Failed Students:")
    for student in failed:
        print("-", student["name"])

    print("\n🏆 Top Performers (90+):")
    top_performer = [i for i in passed if i['marks']>=90]
    for i in top_performer:
        print("-", i["name"])

    pass_percentage = (len(passed) / len(students)) * 100

    print("\n📊 Summary:")
    print("Total Students:", len(students))
    print("Passed:", len(passed))
    print("Failed:", len(failed))
    print(f"Pass Percentage: {pass_percentage:.2f}%")


generate_report(students)
