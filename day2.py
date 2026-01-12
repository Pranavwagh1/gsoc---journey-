marks = [55,95,99,12,43,23,89,23,90]
passed = 0 ;

def is_pass(mark):
    if mark>=40:
        return True 
    else:
        return False
    
for mark in marks:
    if is_pass(mark):
       passed+=1 

print("Passed students =",passed)
