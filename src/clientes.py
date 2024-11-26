import socket
import threading

# Input para que el cliente ingrese su nombre de usuario

username = input('Elija su nombre de usuario: ')

# Conectamos al usuario con el servidor

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 3000))

# Funcion para recibir el nombre de usuario del cliente

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break

# Enviar mensajes
def write():
    while True:
        message = '{}: {}'.format(username, input(''))
        client.send(message.encode('utf-8'))

# Hilos para las funciones recieve y write

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()