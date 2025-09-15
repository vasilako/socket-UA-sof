import socket
import time
import psutil

print("=== SERVER CREDENCIALS SOCKET RAM ===")

# Pedir IP y puerto al usuario
HOST = input("Introduce la IP del servidor (ej: 127.0.0.1 o 192.168.x.x): ").strip()
PORT = int(input("Introduce el puerto del servidor (ej: 6060): ").strip())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Obtener la IP y puerto local asignados
ip_local, puerto_local = client.getsockname()
print(f"[CLIENTE INICIADO] IP {ip_local}, Puerto {puerto_local}")
change_used = 0

try:
    while True:
        # medir la RAM local del cliente
        mem = psutil.virtual_memory()
        used = mem.percent
        if used != change_used:
            # construir mensaje con IP y RAM
            # mensaje = f"Cliente {ip_local}:{puerto_local} → RAM usada del cliente: {used}%"
            mensaje = f"Mi → RAM usada es: {used}%"

            # enviar al servidor
            client.sendall(mensaje.encode("utf-8"))
            print("[yo como cliente envio]:", mensaje)

            # Esperar respuesta del servidor
            data = client.recv(1024).decode("utf-8")
            print(f"[CONFIRMACION del servidor.]: {data}")


            change_used = used


except KeyboardInterrupt:
    print("[CLIENTE] Finalizado por el usuario")

finally:
    client.close()
    print("[CLIENTE] Conexión cerrada")
