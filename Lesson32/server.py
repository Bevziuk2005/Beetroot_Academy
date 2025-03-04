import socket
import json

HOST = '127.0.0.1'
PORT = 65438

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    while True:
        try:
            with conn:
                print('Connected by', addr)
                while True:
                    with open("file.json", "r") as file:
                        files = json.load(file)
                    data = conn.recv(1024).decode('utf-8')
                    for item in files:
                        if item["name"] == data:
                            res = str(item["age"])
                            conn.sendall(res.encode('utf-8'))
                        else:
                            non_res = "In this server no your name."
                            conn.sendall(non_res.encode('utf-8'))
        finally:
            conn.close()