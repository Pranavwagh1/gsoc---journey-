marks = [55,95,99,12,43,23,89,23,90]
new_marks = []

def is_valid_distinction(mark):
      return mark>=75 and mark<=100

for mark in marks:
    if is_valid_distinction(mark):
        new_marks.append(mark)

print(new_marks)
