import socket
import threading

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))  # conecta para saber interfaz
        return s.getsockname()[0]
    finally:
        s.close()

# función para atender a cada cliente
def handle_client(conn, addr):
    print(f"[NUEVA CONEXION] {addr}")
    try:
        while True:
            data = conn.recv(1024).decode("utf-8")
            if not data:  # cliente cerró
                print(f"[DESCONECTADO] {addr}")
                break
            print(f"[RECIBIDO desde cliente {addr}], [MENSAJE]: {data}")

            # Responder confirmación al cliente
            respuesta = f"Ok, Cliente {addr[0]}:{addr[1]}, he recido tu mensaje: {data}%"
            conn.sendall(respuesta.encode("utf-8"))
    except Exception as e:
        print(f"[ERROR {addr}] {e}")
    finally:
        conn.close()
        print(f"[CERRADA CONEXION] {addr}")


HOST = get_local_ip()
PORT = 6060

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"[LISTENING] Servidor escuchando en {HOST}:{PORT}")

# aceptar múltiples clientes
while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
    thread.start()
    print(f"[CONEXIONES ACTIVAS] {threading.active_count()-1}")
