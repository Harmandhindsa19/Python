# 1. Import Error
try:
    import cortana
    from cortana import cortu
    a=input("enter the value of x ")
    b=input("enter the value of y ")
    c=a/b
    if b>1:
        print(c)
except Exception as e:
    print(e)
    print("cortu is not present")
else:
    print("value")
#Value Error
try:
    a=int(input("enter the value of a"))
    b=int(input("enter the value of b"))
    c=a/b
    print(c)
except Exception as e:
    print(e)
else:
    print("value:")
#Index Error
l=[1,2,3]
print(l[5])


