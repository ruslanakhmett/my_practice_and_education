import socket
import selectors
from subprocess import call
#модуль для мониторинга, то же что и select
selector = selectors.DefaultSelector()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5001))
    server_socket.listen()

    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection) #регистрация объекта, за которым будет следить селектор



def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)

    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)



def send_message(client_socket):
    request = client_socket.recv(4096)
    if request:
        response = 'Hello world\n'.encode()
        client_socket.send(response)
    else:
        selector.unregister(client_socket) #перед закрытием надо снимать с регистрации
        client_socket.close()


def event_loop():
    while True:
        
        events = selector.select()  #возвращает список кортежей (key, events)

        for key, _ in events:
            callback = key.data
            callback(key.fileobj) # fileobj - здесь это сам сокет


if __name__ == '__main__':
    server()
    event_loop()
