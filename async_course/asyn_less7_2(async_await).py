# #https://youtu.be/LO61F07s7gw?t=1991

##синхронный вариант
import requests
from time import time

url = 'https://loremflickr.com/320/240'

def get_file(url):
    r = requests.get(url, allow_redirects=True)
    return r

def write_file(responsne):
    filename = responsne.url.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(responsne.content)


def main():
    t0 = time()
    
    url = 'https://loremflickr.com/320/240'
    
    for i in range(10):
        write_file(get_file(url))
        
    print(time() - t0)


# if __name__ == "__main__":
#     main()

##################################################
##асинхронный вариант

import asyncio #предоставляет api for tcp and udp(for http not)
import aiohttp #библиотека для работы асинхронно с http

def write_image(data):
    filename = 'file-{}.jpeg'.format(int(time() * 1000))
    with open(filename, 'wb') as file:
        file.write(data)


async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True, ssl=False) as respsonse:
        data = await respsonse.read()
        write_image(data)

async def main2():
    url = 'https://loremflickr.com/320/240'
    tasks = []
    
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks) #gринимает распакованную последовательность

if __name__ == "__main__":
    t0 = time()
    asyncio.run(main2())
    print(time() - t0)