"""Python program to calculate the sum of all the odd numbers within the given range."""
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

total = 0

for num in range(start, end + 1):
    if num % 2 != 0:
        total += num

print(f"The sum of odd numbers between {start} and {end} is: {total}")