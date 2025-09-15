# 🖧 Proyecto: Monitor RAM con Sockets Concurrentes

Este proyecto implementa un sistema **cliente-servidor con Python y sockets TCP**.\
El **servidor** acepta múltiples conexiones concurrentes y muestra el estado de la RAM enviado por los clientes.\
Cada **cliente** mide periódicamente su propia memoria RAM (con `psutil`) y la envía al servidor, que responde con una confirmación.

---

## 📂 Archivos del proyecto

- ``\
  Servidor concurrente que escucha en un puerto (por defecto `6060`), acepta múltiples clientes y muestra sus mensajes.

- ``\
  Cliente que pide por `input` la IP y puerto del servidor. Envía periódicamente el uso de su RAM local y recibe confirmación del servidor.

- ``\
  Imagen mínima basada en Python 3.11 para ejecutar el cliente dentro de un contenedor.

- ``\
  Variante de configuración Docker para lanzar el cliente.

---

## 🛠️ Requisitos previos

- Python **3.11+**
- `pip`
- `venv` para entorno virtual
- Docker (opcional, para ejecución en contenedor)

---

## 📦 Instalación con entorno virtual

1. **Clonar el repositorio**

   ```bash
   git clone <URL_DEL_REPO>
   cd <CARPETA_DEL_PROYECTO>
   ```

2. **Crear entorno virtual**

   ```bash
   python3 -m venv .venv
   ```

3. **Activar entorno virtual**

   - Linux/macOS:
     ```bash
     source .venv/bin/activate
     ```
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```

4. **Instalar dependencias**

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Ejecución sin Docker

### 1. Iniciar el servidor

```bash
python server_Concurente_socket_ram_listen.py
```

Ejemplo de salida:

```
[LISTENING] Servidor escuchando en 192.168.100.183:6060
```

### 2. Iniciar el cliente

```bash
python client_socket_ram.py
```

El cliente pedirá los datos:

```
=== SERVER CREDENCIALS SOCKET RAM ===
Introduce la IP del servidor (ej: 127.0.0.1 o 192.168.x.x): 192.168.100.183
Introduce el puerto del servidor (ej: 6060): 6060
```

Ejemplo de salida en cliente:

```
[CLIENTE INICIADO] IP 172.17.0.2, Puerto 54321
[yo como cliente envio]: Mi → RAM usada es: 14%
[CONFIRMACION del servidor.]: OK 192.168.100.183:6060 recibido
```

Ejemplo de salida en servidor:

```
[NUEVA CONEXION] ('172.17.0.2', 54321)
[RECIBIDO de ('172.17.0.2', 54321)] Mi → RAM usada es: 14%
```

---

## 🐳 Ejecución con Docker (Cliente)

1. **Construir la imagen**

   ```bash
   docker build -t cliente-ram-img .
   ```

2. **Ejecutar cliente en segundo plano**

   ```bash
   docker run -it --rm --name cliente1 cliente-ram-img
   ```

   ⚠️ El cliente pedirá la IP y el puerto del servidor. Como el contenedor no tiene interacción directa con tu terminal principal, puedes entrar en él con `docker exec`:

   ```bash
   docker exec -it cliente1 python client_socket_ram.py
   ```

   Allí introduces manualmente:

   ```
   === SERVER CREDENCIALS SOCKET RAM ===
   Introduce la IP del servidor (ej: 127.0.0.1 o 192.168.x.x): 192.168.100.183
   Introduce el puerto del servidor (ej: 6060): 6060
   ```

📌 Notas según sistema:

- En **Docker Desktop (Mac/Windows)** usar:
  ```python
  HOST = "host.docker.internal"
  ```
- En **Linux** usar la IP real del host (ej: `192.168.x.x`), o lanzar con red host:
  ```bash
  docker run --rm --network host --name cliente1 cliente-ram-img
  ```

---

## 📖 Flujo de comunicación

- **Cliente → Servidor**:

  ```
  Mi → RAM usada es: 15%
  ```

- **Servidor → Cliente (confirmación)**:

  ```
  OK 192.168.100.183:6060 recibido
  ```

---

## 🔍 Diagrama de arquitectura

```text
         ┌───────────────┐             ┌───────────────┐
         │   Cliente 1   │             │   Cliente N   │
         │ RAM: 14%      │             │ RAM: 27%      │
         └──────┬────────┘             └──────┬────────┘
                │                             │
                ▼                             ▼
          ┌─────────────────────────────────────────┐
          │        Servidor Concurrente             │
          │  - Escucha en IP:PUERTO (ej. 6060)      │
          │  - Recibe RAM de múltiples clientes     │
          │  - Envía confirmación a cada cliente   │
          └─────────────────────────────────────────┘
```

---

## ✨ Mejoras futuras

- Guardar histórico de RAM por cliente en logs o base de datos.
- Añadir métricas extra (`CPU`, disco, red).
- Dashboard web para visualizar clientes conectados.
- Autenticación básica (credenciales).

