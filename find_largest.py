grades = [85,97,78,95,88,70]

largest_grade = 0
print('Checking grades...')
for grade in grades:
    print(f"Currently checking grade: {grade}")
    if grade > largest_grade:
        largest_grade = grade

print(f"\nLargest grade is {largest_grade}")