import threading
from threading import Thread
import time
def display():
    print("elements in list are:")
    for i in l:
        print(i)
        time.sleep(1)
l=[1,2,3,4,5]

t=Thread(target=display)
t.start()
