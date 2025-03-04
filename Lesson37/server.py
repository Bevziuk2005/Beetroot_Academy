import socket
import threading

def handle_client(client_socket, client_name):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"{client_name}: {message}")
        except Exception as e:
            print("Error occurred:", e)
            break

    print(f"{client_name} disconnected")
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5555))
    server_socket.listen(5)
    print("Waiting for users to join the chat...")

    while True:
        client_socket, client_address = server_socket.accept()
        client_name = client_socket.recv(1024).decode('utf-8')
        print(client_name," joined the chat.")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_name))
        client_handler.start()

if __name__ == "__main__":
    start_server()
