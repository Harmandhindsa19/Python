class AgeTooSmallError(Exception):
    pass
a=0
while a<18:
    try:
        a=int(input("enter your age"))
        if a<18:
            print("you have enter a number that defines an underage person and thats not valid ")
            raise AgeTooSmallError("age too small error is raised")

    except Exception as e:
        print(e)
    else:
        print("age is:" , a)