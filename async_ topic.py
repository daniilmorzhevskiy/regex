import asyncio

async def task(number):
    print(f'Starting task {number}')
    await asyncio.sleep(1)
    print(f'Finished task {number}')
    return number

async def task123(number):
    while True:
        print("///")
async def main():
    results = await asyncio.gather(task(1), task123(2), task(3))
    print(f'Task results: {results}')

asyncio.run(main())