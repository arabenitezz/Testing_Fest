import unittest
from unittest.mock import MagicMock, patch
from src.servidor import broadcast, manage, receive, clients, usernames
import socket

class TestServidor(unittest.TestCase):
    def setUp(self):
        # Configuración inicial antes de cada prueba
        self.fake_client = MagicMock()
        self.fake_client.recv = MagicMock(side_effect=[
            b"Mensaje de prueba",
            socket.error("Simulando error de conexión")
        ])
        clients.clear()
        usernames.clear()

    def test_broadcast(self):
        # Simular dos clientes
        client1 = MagicMock()
        client2 = MagicMock()
        clients.extend([client1, client2])

        message = b"Hola a todos"
        broadcast(message)

        # Verificar que ambos clientes recibieron el mensaje
        client1.send.assert_called_with(message)
        client2.send.assert_called_with(message)

    @patch("src.servidor.broadcast")  # Updated import path
    def test_manage(self, mock_broadcast):
        # Probar la gestión de mensajes y desconexiones
        clients.append(self.fake_client)
        usernames.append("UsuarioPrueba")

        manage(self.fake_client)

        # Verificar que el cliente fue eliminado tras el error
        self.assertNotIn(self.fake_client, clients)
        self.assertNotIn("UsuarioPrueba", usernames)

        # Verificar que se notificó a los demás usuarios
        mock_broadcast.assert_called_with(b"UsuarioPrueba sali\xc3\xb3 del chat")

    @patch("socket.socket")  # Simular sockets
    def test_receive(self, mock_socket):
        # Crear un cliente falso
        fake_client = MagicMock()
        fake_client.recv = MagicMock(side_effect=[
            b"UsuarioPrueba",  # Devuelve un nombre de usuario
            OSError("Simulando error de conexión")  # Luego lanza un error
        ])
        fake_client.send = MagicMock()  # Simular envío sin errores

        # Configurar el servidor simulado
        mock_server = MagicMock()
        mock_server.accept = MagicMock(return_value=(fake_client, ("127.0.0.1", 12345)))

        # Parchear el servidor real en la función a probar
        with patch("src.servidor.server", mock_server):
            with patch("threading.Thread") as mock_thread:  # Simular creación de hilos
                try:
                    receive()  # Llamar a la función de recepción
                except Exception as e:
                    self.fail(f"El servidor no debería lanzar excepciones: {e}")

                # Verificar que el cliente se agregó correctamente a las listas
                self.assertIn(fake_client, clients)
                self.assertIn("UsuarioPrueba", usernames)

                # Verificar que se intentó crear un hilo para gestionar el cliente
                mock_thread.assert_called_once()




if __name__ == "__main__":
    unittest.main()