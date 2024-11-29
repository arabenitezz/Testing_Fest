import unittest
from socket_chat.username_validator import validar_username

class TestUsernameValidator(unittest.TestCase):
    def test_longitud_username(self):
        """
        Prueba la longitud válida del nombre de usuario.
        """
        self.assertFalse(validar_username("usr"))  # Muy corto
        self.assertFalse(validar_username("usuariovalidomuylargo"))  # Muy largo
        self.assertTrue(validar_username("usuario123"))  # Longitud válida


if __name__ == "__main__":
    unittest.main()
