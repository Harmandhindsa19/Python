import threading
from threading import Thread
import time
def display():
    for x in range(10):
        time.sleep(1)
        print("value of x is:" , x)
t=Thread(target=display)
t.start()

