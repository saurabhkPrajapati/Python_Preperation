from concurrent.futures import ProcessPoolExecutor
import math
import os

def cpu_task(n):
    return sum(math.sqrt(i) for i in range(n))

# Python 3.13 default logic
default_max_workers = min(32, (os.process_cpu_count() or 1) + 4)
print(f"Default process pool max workers: {default_max_workers}")

with ProcessPoolExecutor(max_workers=default_max_workers) as executor:
    results = executor.map(cpu_task, [1000000, 2000000, 3000000, 4000000])
    print(list(results))
