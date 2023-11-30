import math,heapq
import time

class timer:
    def __init__(self) -> None:
        self.start_time=None
    def start(self):
        self.start_time=time.perf_counter()
    def check(self):
        return time.perf_counter()-self.start_time
        
t=timer()
t.start()

time.sleep(1)
print(t.check())

