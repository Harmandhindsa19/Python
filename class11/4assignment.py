import threading
from threading import Thread
import math
def factorial():
    n=int(input("enter any number :"))
    fact=1
    for x in range(1,n+1):
        fact=fact*x
    print(fact)
t2=Thread(target=factorial)
t2.start()







    