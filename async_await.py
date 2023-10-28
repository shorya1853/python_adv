import asyncio

async def long_operation(n):
    print(f"Starting operation {n}")
    await asyncio.sleep(n)
    print(f"Finished operation {n}")

async def main():
    task1 = asyncio.create_task(long_operation(5))
    task2 = asyncio.create_task(long_operation(2)W

    # Wait for tasks to complete
    await task1
    await task2

if __name__ == "__main__":
    asyncio.run(main())


# import time

# def my_function():
#     # Your function's code here

#     print("hello wordl")

# start_time = time.time()  # Get the current time before calling the function
# my_function()             # Call your function
# end_time = time.time()    # Get the current time after the function has completed

# execution_time = end_time - start_time  # Calculate the execution time
# print(f"Execution time: {execution_time} seconds")