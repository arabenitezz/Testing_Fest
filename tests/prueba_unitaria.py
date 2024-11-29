import unittest
from unittest.mock import MagicMock
from socket_chat.servidor import broadcast, clients



class TestBroadcast(unittest.TestCase):
    def setUp(self):
        clients.clear()

    def test_broadcast_happy_path(self):
        """Prueba que el mensaje se envíe correctamente a todos los clientes."""
        client1, client2 = MagicMock(), MagicMock()
        clients.extend([client1, client2])

        broadcast(b"Hola a todos")

        client1.send.assert_called_with(b"Hola a todos")
        client2.send.assert_called_with(b"Hola a todos")
        
    def test_broadcast_empty_message(self):
        """Prueba que no se envíe un mensaje vacío."""
        client1 = MagicMock()
        clients.append(client1)

        # Enviar un mensaje vacío
        broadcast(b"")

        # Verificar que no se haya enviado nada
        client1.send.assert_not_called()  # No se debe enviar nada


    def test_broadcast_error_in_client(self):
        """Prueba que el envío continúa si un cliente lanza un error."""
        client1 = MagicMock()
        client2 = MagicMock()
        client2.send.side_effect = Exception("Error al enviar")  # Simular fallo
        clients.extend([client1, client2])

        broadcast(b"Mensaje importante")

        client1.send.assert_called_with(b"Mensaje importante")
        client2.send.assert_called_with(b"Mensaje importante")  # Verifica que se intentó


if __name__ == "__main__":
    unittest.main()

