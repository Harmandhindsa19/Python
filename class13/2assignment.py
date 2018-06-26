l=[1,2,3]
try:
    print(l[3])
except Exception as e:
    print("exception is handled")
    print(e)
#exception name is: list index out of range