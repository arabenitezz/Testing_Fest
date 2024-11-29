import socket
import threading

host = 'localhost'
port = 3000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
usernames = []

def broadcast(message):
    if not message:  # No enviar mensajes vacíos
        return
    for client in clients:
        try:
            client.send(message)
        except Exception as e:
            print(f"Error al enviar mensaje a {client}: {e}")
            continue  # Ignorar el cliente que no pudo recibir el mensaje


def manage(client):
    while True:
        try:
            message = client.recv(1024)
            if message:  # Si hay un mensaje
                broadcast(message)
            else:  # Si no hay mensaje, el cliente se ha desconectado
                break
        except (ConnectionAbortedError, ConnectionResetError):
            print(f"Cliente {client} desconectado.")
            break  # Si el cliente se desconectó, salir del bucle
        except Exception as e:
            print(f"Error al recibir mensaje: {e}")
            break
    
    # Eliminar el cliente de las listas
    if client in clients:
        clients.remove(client)
    if client in usernames:
        usernames.remove(client)
    client.close()



def receive():
    while True:
        try:
            client, address = server.accept()
            print(f"Conectado desde {address}")

            # Enviar 'NICK' para pedir nombre de usuario
            client.send(b'NICK')
            username = client.recv(1024).decode('utf-8')
            print(f"Usuario: {username}")
            usernames.append(username)
            clients.append(client)

            # Notificar a otros clientes sobre la conexión
            broadcast(f"{username} se ha unido al chat".encode('utf-8'))
            client.send('Te has conectado exitosamente'.encode('utf-8'))

            # Iniciar el manejo del cliente
            thread = threading.Thread(target=manage, args=(client,))
            thread.start()
        except Exception as e:
            print(f"Error al aceptar o gestionar cliente: {e}")
            break


if __name__ == "__main__":
    print("Servidor activo :)")
    receive()
