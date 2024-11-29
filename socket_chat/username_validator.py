def validar_username(username):
    """
    Valida que el nombre de usuario tenga una longitud entre 4 y 20 caracteres.
    """
    return 4 <= len(username) <= 20
