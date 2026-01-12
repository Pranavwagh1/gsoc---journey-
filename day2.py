ages = [12,16,18,39,67,87,11,1,72,15]
filtered_ages = []

def is_special(age):
      return age<13 or age>=60

for age in ages:
    if is_special(age):
        filtered_ages.append(age)

print(filtered_ages)
