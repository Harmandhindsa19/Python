# a=3
# if a<4:
#     a=a/(a-3)
# print(a)
#ZeroDivisionError
#to resolve this error
a=3
try:
    if a<4:
        a=a/(a-3)
        print(a)
except Exception:
    print("exception is existable here")
