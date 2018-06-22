#threading
import threading
from threading import Thread
import time
def display():
    time.sleep(5)
    print("angel thread")

t1=Thread(target=display)
t1.start()