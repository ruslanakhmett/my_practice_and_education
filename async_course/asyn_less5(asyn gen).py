from asyncore import read
import socket
from select import select

tasks = []

to_read = {}
to_write = {}

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5001))
    server_socket.listen()

    while True:
        
        yield ('read', server_socket)
        client_socket, addr = server_socket.accept()  # read

        print('Connection from', addr)

        tasks.append(client(client_socket))


def client(client_socket):
    while True:
        
        yield ('read', client_socket) #первый элемент кортежа, который отдает генератор
        #это фильтрующий признак, который определяет, куда пойдет сокет(в какой словарь),
        #второй элемент кортежа
        request = client_socket.recv(4096)  # read

        if not request:
            break
        else:
            response = 'Hello world\n'.encode()

            yield ('write', client_socket)
            client_socket.send(response)  # write
    
    client_socket.close()

def event_loop():

    while any([tasks, to_read, to_write]):

        while not tasks:
            ready_to_read, ready_to_write, _ = select(to_read, to_write, []) # списки для мониторинга на готовность к чтению или к записи

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        try:
            task = tasks.pop(0) #получаем генератор

            reason, sock = next(task) # task это генератор, получаем ('write', client_socket)
            if reason == 'read': # наполняем словари данными ключь это сокет значение это таск
                to_read[sock] = task
            if reason == 'write':
                to_write[sock] = task
        except StopIteration:
            print('Done!')



tasks.append(server())
event_loop()