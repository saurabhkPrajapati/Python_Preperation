from concurrent.futures import ProcessPoolExecutor, as_completed
import math
import os

def cpu_task(n):
    return sum(math.sqrt(i) for i in range(n))

# Python 3.13 default logic
default_max_workers = min(32, (os.process_cpu_count() or 1) + 4)
print(f"Default process pool max workers: {default_max_workers}")

# Using submit
with ProcessPoolExecutor(max_workers=default_max_workers) as executor:
    # Submit tasks individually
    futures = [executor.submit(cpu_task, n) for n in [1000000, 2000000, 3000000, 4000000]]
    
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
