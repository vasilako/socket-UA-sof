import socket

HOST = "127.0.0.1"
PORT = 6060

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

try:
    while True:
        data = client.recv(1024).decode("utf-8")
        if not data:
            break
        print("[RECIBIDO]", data)
except:
    print("[CONEXION FINALIZADA]")
finally:
    client.close()
