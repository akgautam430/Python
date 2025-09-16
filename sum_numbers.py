num_str = int(input('Enter the number to be summed: '))
total_sum = 0

print(f"Calculating sum from 1 to {num_str}")

for i in range(1,num_str+1):
    total_sum = total_sum + i
    print(f"Adding {i}. Current sum: {total_sum}")
print(f"\nThe final sum of numbers  from 1 to {num_str} is {total_sum}")