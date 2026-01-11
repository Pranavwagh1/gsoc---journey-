marks = [55,95,99,12,43,23,89,23,90]

passed = 0 

for mark in marks:
    if(mark>=40):
        passed += 1 
    else:
        continue

print(passed)
