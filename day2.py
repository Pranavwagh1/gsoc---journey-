def grade_based_on_marks(marks):
    if marks >= 90 :
        return "Grade A"

    elif marks >= 75 :
       return "Grade B"

    elif marks >= 50 :
        return "Grade C"

    else : 
        return "Fail"


marks = int(input("Enter your marks = ")) 

print("You got",grade_based_on_marks(marks))
