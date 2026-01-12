marks = [55,95,99,12,43,23,89,23,90]
distinction = []

def is_distinction(mark):
    if mark >= 75 : 
        return True
    else:
        return False 

for mark in marks:
    if is_distinction(mark):
        distinction.append(mark)

print(distinction)
