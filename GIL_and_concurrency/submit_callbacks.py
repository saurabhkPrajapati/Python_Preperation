"""
In concurrent.futures a callback is a function that is attached to future object and is intended to be called automatically after future object/task completes.
Are used only with executor.submit() not executor.map() 

Callbacks are automatic: You don’t call them manually after attaching to future object.
Receive the Future object: The callback gets the Future as an argument, so you can get the result or check status.
Runs in the thread that completed the task: Not necessarily the main thread.

"""


from concurrent.futures import ThreadPoolExecutor
import time
import threading

def task(n):
    print(f"{threading.current_thread().name} running task {n}")
    time.sleep(2)
    return n * n

def callback_func(future):
    print(f"Callback: result={future.result()}")

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = []
    
    # Submit tasks and attach callbacks
    for i in range(5):
        future = executor.submit(task, i)
        # call callback will run automatically once the future/task completes
        future.add_done_callback(callback_func) # immediately attach callback
        futures.append(future)

    # Wait for all tasks to complete
    for future in futures:
        future.result()


# ____________________________________________________________________________________________________________________

from concurrent.futures import ThreadPoolExecutor
import time
import threading

def task(n):
    print(f"{threading.current_thread().name} running task {n}")
    time.sleep(2)
    return n * n

def callback_func(future):
    print(f"Callback: result={future.result()}")

with ThreadPoolExecutor(max_workers=3) as executor:
    # List comprehension to submit tasks and attach callbacks
    futures = [executor.submit(task, i) for i in range(5)]
    # Each callback will run right after its future/task completes, not after all tasks are done.
    [f.add_done_callback(callback_func) for f in futures] # attach callback once all task are submitted

    # Wait for all tasks to complete
    for future in futures:
        future.result()
