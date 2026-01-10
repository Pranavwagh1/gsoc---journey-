def Category_acording_to_your_age(age):
    if age < 13:
        return "Child"
    elif age >=13 and age <= 19:
        return "Teenager"
    elif age >= 20 and age <= 59 :
        return "Adult"
    else : 
        return "Senior Citizen"
    
age = int(input("Enter your age = "))

print("Your category according to your age is",Category_acording_to_your_age(age))
