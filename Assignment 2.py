#Task 1

n = int(input("Enter a number:"))

if n % 2 == 0:
    print(f"{n} is an even number.")
else:
    print(f"{n} is an odd number.")


# Task 2

n = range(1,51)

sum = 0

for i in n:
    sum = sum + i

print(f"The sum of from 1 to 50 is: {sum}")