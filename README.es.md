# Aplicación de Chat por Socket - Suite de Pruebas

## Descripción de Pruebas

Este proyecto se centra en pruebas exhaustivas para una aplicación de chat basada en sockets, demostrando diferentes enfoques de testing:

### Archivos de Pruebas

1. **Pruebas Unitarias** (`prueba_unitaria.py`):
   - Prueba funcionalidad de difusión de mensajes
   - Verifica envío de mensajes a múltiples clientes
   - Maneja casos extremos como mensajes vacíos
   - Utiliza `unittest.mock` para simular interacciones de clientes

2. **Pruebas de Validación de Nombre de Usuario** (`prueba_tdd.py`):
   - Implementa enfoque de Desarrollo Guiado por Pruebas (TDD)
   - Valida restricciones de longitud de nombre de usuario
   - Asegura que los nombres de usuario cumplan criterios específicos

3. **Pruebas de Integración** (`prueba_integracion.py`):
   - Pruebas de extremo a extremo de interacciones cliente-servidor
   - Valida difusión de mensajes entre múltiples clientes
   - Verifica capacidad del servidor para manejar desconexiones de clientes

## Ejecución de Pruebas

```bash
python -m unittest discover
```

### Casos de Prueba Cubiertos

#### Funcionalidad de Difusión
- Envío de mensajes a múltiples clientes
- Manejo de errores durante transmisión de mensajes
- Prevención de difusión de mensajes vacíos

#### Validación de Nombre de Usuario
- Validación de longitud mínima
- Validación de longitud máxima
- Restricciones de tipos de caracteres

#### Interacción Cliente-Servidor
- Conexión exitosa de clientes
- Transmisión de mensajes entre clientes
- Manejo elegante de desconexiones de clientes

## Técnicas de Pruebas

- Pruebas Unitarias
- Objetos Mock
- Pruebas de Integración
- Validación de Manejo de Errores

## Tecnologías Utilizadas

- Framework de pruebas `unittest` de Python
- Programación de sockets
- Multiproceso (Threading)
- Objetos Mock

## Contribución

Se agradecen contribuciones para expandir la cobertura de pruebas. Por favor, envía pull requests con casos de prueba adicionales o mejoras a las pruebas existentes.