l=[]
l.append(int(input("enter any number for first set:")))
l.append(int(input("enter any number for first set:")))
l.append(int(input("enter any number for first set:")))
l2=[]
l2.append(int(input("enter any number for second set:")))
l2.append(int(input("enter any number for second set:")))
l2.append(int(input("enter any number for second set:")))
s1=set(l)
s2=set(l2)
print(s1)
print(s2)
if(s2-s1==set()):
    print('there is no difference in set')
else:
    print("difference is:" , s2-s1)
if(s1==s2):
    print("sets are equal")
else:
    print("sets are not equal")
print("intersection is:" , s1&s2)