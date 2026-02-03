import asyncio

async def main():
    task1 = asyncio.create_task(job(1))
    task2 = asyncio.create_task(job(2))

    print("Tasks started")   # doesn't wait

    await task1              # wait later
    await task2

async def job(n):
    print(f"job {n} started")
    await asyncio.sleep(1)
    print(f"job {n} done")

asyncio.run(main())
