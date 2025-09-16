age = -1
while age < 0 or age > 120:
    age_str = input("Please enter your age: ")
    try:
        age = int(age_str)
        if age < 0 or age > 120:
            print("Please enter a valid age, Age must be between 1 and 120.")
    except ValueError:
        print('invalid input, Please enter a number')

print(f"\n Your current age is {age}")
