"""
asyncio.gather() is used to run multiple coroutines concurrently
asyncio.gather() waits for all coroutines to finish.
Returns results in order of arguments, not execution time
"""
import asyncio


async def func1():
    print("Function 1 started..")
    await asyncio.sleep(1)
    print("Function 1 Ended")
    return "Result from Function 1"


async def func2():
    print("Function 2 started..")
    await asyncio.sleep(3)
    print("Function 2 Ended")
    return "Result from Function 2"


async def func3():
    print("Function 3 started..")
    await asyncio.sleep(1)
    print("Function 3 Ended")
    return "Result from Function 3"


async def main():
    results = await asyncio.gather(func1(), func2(), func3())
    print(results)

    print("Main Ended..")


asyncio.run(main())
