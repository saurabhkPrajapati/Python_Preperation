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
