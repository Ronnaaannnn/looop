"""12. Given list is [1,2,3,4,5] separate the elements into odd and even categories."""
a=[1,2,3,4,5]
for i in a :
    if i % 2 == 0:
        print(i,"is even")
    else:
        print(i,"is odd")