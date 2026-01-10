def Check_even_odd(user_input):

     if(user_input%2 == 0):
       return "Even Number"
     else:
        return "Odd Number"



user_input = int(input("Enter a numbe to check its even or odd = ")) 


print(Check_even_odd(user_input))
