import asyncio
from async_tasks import (
    delay_2_seconds,
    delay_5_seconds,
    random_delay_and_count,
    check_and_square,
    write_to_file,
)

async def main():
    print("\n--- Task 1 ---")
    t1 = asyncio.create_task(delay_2_seconds())
    t2 = asyncio.create_task(delay_5_seconds())
    await asyncio.gather(t1, t2)

    print("\n--- Task 2 ---")
    await random_delay_and_count()

    print("\n--- Task 3 ---")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    await check_and_square(numbers)

    print("\n--- Task 4 ---")
    tasks = [
        write_to_file("file1.txt", "Content for file 1"),
        write_to_file("file2.txt", "Content for file 2"),
        write_to_file("file3.txt", "Content for file 3"),
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
