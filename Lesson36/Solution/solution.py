"""
            Task 1
"""
"""
import asyncio
import time

async def func_1():
    start_time = time.time()
    await asyncio.sleep(1)
    print('Hello')
    end_time = time.time()
    f_time = end_time - start_time
    print("Час func_1:", f_time)

async def func_2():
    start_time = time.time()
    await asyncio.sleep(2)
    print('World')
    end_time = time.time()
    f_time = end_time - start_time
    print("Час func_2:", f_time)

async def func_3():
    start_time = time.time()
    await asyncio.sleep(3)
    print('!')
    end_time = time.time()
    f_time = end_time - start_time
    print("Час func_3:", f_time)

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(func_1())
    loop.run_until_complete(func_2())
    loop.run_until_complete(func_3())

if __name__ == '__main__':
    main()
"""
"""
            Task 2
"""
"""
import asyncio
import time

async def work_with_user():
    text = ""
    while True:
        try:
            inf = await asyncio.wait_for(get_user_input(), timeout=10)
            text += inf
        except asyncio.TimeoutError:
            print("Your time the end.")
            print("Your text:", text)
            break

async def get_user_input():
    start_time = time.time()
    text = input("Please print text: ")
    end_time = time.time()
    f_time = end_time - start_time
    await asyncio.sleep(int(f_time))
    return text

async def main():
    await work_with_user()

asyncio.run(main())
"""
"""
            Task 3
"""
"""
import aiohttp
import asyncio
import re

async def page(url):
    async with aiohttp.ClientSession() as ses:
        async with ses.get(url) as res:
            text = await res.text()
            txt = re.search(r"<title>(.*?)</title>", text)
            return txt.group(1)

async def main(urls):
    tasks = [page(url) for url in urls]
    results = await asyncio.gather(*tasks)

    for url in results:
        print(f"Title: {url}")

if __name__ == "__main__":
    urls = ["https://uk.wikipedia.org/wiki/Python", "https://uk.wikipedia.org/wiki/JavaScript"]
    asyncio.run(main(urls))
"""
"""
            Task 4
"""
import asyncio



























