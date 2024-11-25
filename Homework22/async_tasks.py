import asyncio
import random
from datetime import datetime

async def delay_2_seconds():
    print(f"Task 1 (2s) started at {datetime.now()}")
    await asyncio.sleep(2)
    print(f"Task 1 (2s) ended at {datetime.now()}")


async def delay_5_seconds():
    print(f"Task 2 (5s) started at {datetime.now()}")
    await asyncio.sleep(5)
    print(f"Task 2 (5s) ended at {datetime.now()}")


async def random_delay_and_count():
    delay = random.randint(1, 5)
    print(f"Random delay task started with delay of {delay} seconds.")
    await asyncio.sleep(delay)
    for i in range(1, 11):
        print(i)
    print("Random delay task completed.")


async def calculate_square(number):
    if number % 2 == 0:
        print(f"Number {number} is even, calculating square.")
        return number ** 2
    else:
        print(f"Number {number} is odd, skipping square.")
        return None


async def is_even(number):
    return number % 2 == 0


async def check_and_square(numbers):
    tasks = [calculate_square(num) for num in numbers]
    results = await asyncio.gather(*tasks)
    print("Squares of even numbers:", [res for res in results if res is not None])


async def write_to_file(file_name, value):
    print(f"Iwereba failshi {file_name} ")
    await asyncio.sleep(random.randint(1, 3))
    with open(file_name, 'w') as f:
        f.write(value)
    print(f"Dasrulda failshi chawera - {file_name} ")
