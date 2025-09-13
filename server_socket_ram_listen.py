import socket
import time
import psutil

HOST = "0.0.0.0"
PORT = 6060

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"[LISTENING] Servidor en {HOST}:{PORT}")
conn, addr = server.accept()
print(f"[NUEVA CONEXION] {addr}")

last_used = None

try:
    while True:
        mem = psutil.virtual_memory()
        used = mem.percent  # % de RAM usada

        # Solo envía si hay cambio
        if used != last_used:
            mensaje = f"RAM usada: {used}%"
            conn.sendall(mensaje.encode("utf-8"))
            print("[ENVIADO]", mensaje)
            last_used = used

        time.sleep(1)
except:
    print("[CONEXION CERRADA]")
    conn.close()
