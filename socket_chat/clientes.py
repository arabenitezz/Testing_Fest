import socket
import threading
from socket_chat.username_validator import validar_username

def obtener_username_valido():
    while True:
        username = input('Elija su nombre de usuario: ')
        if validar_username(username):
            return username
        else:
            print("Nombre de usuario inválido. Debe tener entre 4 y 20 caracteres.")


def receive(client, username):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print("Ocurrió un error al recibir el mensaje!")
            client.close()
            break

def write(client, username):
    while True:
        message = '{}: {}'.format(username, input(''))
        client.send(message.encode('utf-8'))

def main():
    # Obtener username válido
    username = obtener_username_valido()

    # Conectamos al usuario con el servidor
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 3000))

    # Hilos para las funciones receive y write
    receive_thread = threading.Thread(target=receive, args=(client, username))
    receive_thread.start()

    write_thread = threading.Thread(target=write, args=(client, username))
    write_thread.start()

if __name__ == "__main__":
    main()