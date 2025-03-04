import socket
import threading
def send_message(client_socket, client_name):
    while True:
        message = input("Enter your message: ")
        client_socket.send(message.encode('utf-8'))

def start_client():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_name = input("Enter your name: ")
    client_socket.connect(('127.0.0.1', 5555))
    client_socket.send(client_name.encode('utf-8'))

    send_thread = threading.Thread(target=send_message, args=(client_socket, client_name))
    send_thread.start()


if __name__ == "__main__":
    start_client()