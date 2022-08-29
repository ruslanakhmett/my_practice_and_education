#https://youtu.be/LO61F07s7gw
'''событийный цикл (event loop) - своего рода менеджер, планировщик задач
работает по приниципу: на событие А вызови функцию Б и т.д.
asyncio - фреймворк для создания событийных циклов'''
import asyncio

# @asyncio.coroutine #этот декоратор делает из функции корутину-генератор
# def print_numbs(): #эта функция просто выводит числа
#     num = 1
#     while True:
#         print(num)
#         num += 1
#         yield from asyncio.sleep(0.1) #создает задержку, но без блокировки как обычный sleep
async def print_numbs(): #эта функция просто выводит числа
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(0.1) #создает задержку, но без блокировки как 


# @asyncio.coroutine 
# def print_time(): #эта функция выводит время
#     count = 0
#     while True:
#         if count % 3 == 0: #каждые 3 секунды печатаем сообщение
#             print('{} seconds have passed'.format(count))
#         count += 1
#         yield from asyncio.sleep(1)
async def print_time(): #эта функция выводит время
    count = 0
    while True:
        if count % 3 == 0: #каждые 3 секунды печатаем сообщение
            print('{} seconds have passed'.format(count))
        count += 1
        await asyncio.sleep(1)

# @asyncio.coroutine
# def main():
#     task1 = asyncio.ensure_future(print_numbs())#ensure_future помещает функцию в очередь событийного цикла
#     task2 = asyncio.ensure_future(print_time())
    
#     yield from asyncio.gather(task1, task2)

async def main():
    task1 = asyncio.create_task(print_numbs())
    task2 = asyncio.create_task(print_time())
    
    await asyncio.gather(task1, task2)



if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()
    asyncio.run(main())