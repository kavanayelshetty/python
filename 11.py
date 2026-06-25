from time import strftime
import time

for _ in range(10):
    current_time = strftime("%H:%M:%S")
    print("Current Time:", current_time)
    time.sleep(1)