"""
Now if you want the program to be actually asynchronous, In the actual order of execution we’ll need to make tasks
in order to accomplish this. This means that the other function will begin to run anytime if there is any free time
using asyncio.create_task(fn2())
"""


import asyncio


async def fn():
    # other function will begin to run anytime if there is any free time comes(asyncio.sleep)
    task = asyncio.create_task(fn2())
    print("one")
    # await asyncio.sleep(0)
    # await fn2()
    print('four')
    await asyncio.sleep(1)
    print('five')
    await asyncio.sleep(1)


async def fn2():
    # await asyncio.sleep(1)
    print("two")
    await asyncio.sleep(1)
    print("three")


asyncio.run(fn())


# If you want fn2() to begin immediately after scheduling it, insert await asyncio.sleep(0):

# task = asyncio.create_task(fn2())
# await asyncio.sleep(0)  # give fn2() a chance to start