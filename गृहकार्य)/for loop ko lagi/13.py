"""11. Given list is [1,2,3,4] but expected output is [1,"a",2,4]"""
numbers = [1, 2, 3, 4]
for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        numbers[i] = "a"
print(numbers)
