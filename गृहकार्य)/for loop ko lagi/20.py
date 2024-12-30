"""Print multiplication table of  1,2,3,4,5,6,7,8 """
a = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(1, 11):
    for num in a:
        print(f"{num} X {i} = {num * i}")
