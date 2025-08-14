"""
Returns: A Future object for each task.

Execution order: Tasks are submitted to the pool and may complete in any order.

Result order: You have to explicitly call future.result() for each Future. 
              The results come in the order you call .result(), not necessarily in the order tasks completed. 
              Use reversed(futures) for getting results in reverse input order 

Flexibility: You can cancel, check status, or handle exceptions for each task individually.

"""

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
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
    futures = [executor.submit(task, i) for i in range(10)]

    # Get results in submission order
    print("Results in submission order:")
    for future in futures:
        print(future.result())

    # Get results in reverse submission order 
    print("Results in reverse submission order:")
    for future in reversed(futures):
        print(future.result())

    # Get results in completion order
    print("\nResults in completion order:")
    for future in as_completed(futures):
        print(future.result())
