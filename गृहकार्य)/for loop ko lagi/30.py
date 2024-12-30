#29. Using a for loop and .append() method append each item with a Dr. prefix to the lst. Hint a=["ram","shyam"] expected output:  ['Dr.ram', 'Dr.shyam','Dr.1','Dr.2']
a = ["ram", "shyam"]
lst = []

for item in a:
    lst.append("Dr." + item)

lst.append("Dr." + str(1))
lst.append("Dr." + str(2))

print(lst)
