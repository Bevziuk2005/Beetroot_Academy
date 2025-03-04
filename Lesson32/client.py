import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT1 = 65438        # The port used by the server
PORT2 = 65439

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT1))
    name_search = input("Enter name for search: ")
    s.sendall(name_search.encode("utf-8"))
    data = s.recv(2056)
    if data.decode("utf-8") == "In this server no your name.":
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
            s2.connect((HOST, PORT2))
            s2.sendall(name_search.encode("utf-8"))
            data2 = s2.recv(2056)
            print(data2.decode("utf-8"))
    else:
        print('Received', repr(data.decode("utf-8")))