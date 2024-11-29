import unittest
import threading
import time
from socket_chat.servidor import manage, server, clients, usernames
import socket


class TestChatIntegration(unittest.TestCase):
    def setUp(self):
        """Iniciar el servidor en un hilo separado."""
        self.server_thread = threading.Thread(target=self.start_server, daemon=True)
        self.server_thread.start()
        time.sleep(1)  # Esperar que el servidor esté listo

    def start_server(self):
        """Ejecuta el servidor y acepta conexiones de clientes."""
        server.listen()
        while True:
            client, address = server.accept()
            print(f"Conectado desde {address}")
            
            # Simula la conexión de un cliente con un nombre de usuario
            client.send(b'NICK')  # El servidor envía 'NICK' para pedir el nombre
            username = client.recv(1024).decode('utf-8')  # Recibe el nombre del cliente
            print(f"Usuario: {username}")
            usernames.append(username)
            clients.append(client)

            # Inicia el manejo del cliente
            thread = threading.Thread(target=manage, args=(client,))
            thread.start()


    def create_client(self, username):
        """Crea un cliente y lo conecta al servidor."""
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('localhost', 3000))

        # Enviar el nombre de usuario directamente (sin encode() porque ya está en bytes)
        client.send(username)  # Se pasa `b'User1'` sin la necesidad de usar `.encode('utf-8')`
        return client


    def test_message_broadcast(self):
        """Validar que los mensajes se transmitan correctamente a todos los clientes."""
        client1 = self.create_client(b'User1')
        client2 = self.create_client(b'User2')

        # Esperar a que los clientes estén completamente conectados
        time.sleep(1)

        # Enviar mensaje desde el cliente 1
        client1.send(b'Hola desde User1')

        # Esperar que el mensaje llegue a todos los clientes
        time.sleep(1)

        # Verificar que el cliente 2 recibió el mensaje
        data = client2.recv(1024).decode('utf-8')
        self.assertIn('Hola desde User1', data)

    def test_disconnect_handling(self):
        """Validar que el servidor maneje desconexiones sin afectar a otros clientes."""
        client1 = self.create_client(b'User1')
        client2 = self.create_client(b'User2')

        # Desconectar el cliente 1
        client1.close()
        time.sleep(1)  # Esperar para que el servidor procese la desconexión

        # Verifica que el cliente 2 sigue recibiendo mensajes
        client2.send(b'User2 sigue conectado')
        data = client2.recv(1024).decode('utf-8')
        self.assertIn('User2 sigue conectado', data)

        # Verifica que el cliente 2 sigue recibiendo mensajes
        client2.send(b'User2 sigue conectado')
        data = client2.recv(1024).decode('utf-8')
        self.assertIn('User2 sigue conectado', data)

    def tearDown(self):
        """Limpiar clientes y detener el servidor."""
        for client in clients:
            client.close()
        clients.clear()
        usernames.clear()


if __name__ == "__main__":
    unittest.main()
