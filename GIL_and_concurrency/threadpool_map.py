from concurrent.futures import ThreadPoolExecutor
import time
import threading
import os

def task(name):
    print(f"Thread {threading.current_thread().name} is running task {name}")
    time.sleep(2)
    return f"Task {name} done"

# Python 3.13 default logic
default_max_workers = min(32, (os.process_cpu_count() or 1) + 4)
print(f"Default thread pool max workers: {default_max_workers}")

with ThreadPoolExecutor(max_workers=default_max_workers) as executor:
    # map runs the tasks and returns results in order
    results = executor.map(task, range(10))
    
    # results is an iterator, we can loop to get each result
    for result in results:
        print(result)
