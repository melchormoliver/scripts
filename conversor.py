import re

def detect_os(command):
    # Esta función analiza el comando y devuelve 'windows' o 'linux' según la detección.
    
    # Verificamos si el comando contiene un carácter de barra invertida ('\').
    if '\\' in command:
        return 'windows'
    
    # Verificamos si el comando contiene una barra diagonal ('/').
    if '/' in command:
        return 'linux'
    
    # Si no se detecta ninguno de los caracteres anteriores, se asume 'linux' de manera predeterminada.
    return 'linux'

def windows_to_linux(command):
    # Reemplazar barras invertidas por barras diagonales en rutas de archivo
    command = command.replace("\\", "/")

    # Reemplazar variables de entorno de Windows por variables de Linux
    command = re.sub(r'%(\w+)%', r'$\1', command)

    return command

def linux_to_windows(command):
    # Reemplazar barras diagonales por barras invertidas en rutas de archivo
    command = command.replace("/", "\\")

    # Reemplazar variables de entorno de Linux por variables de Windows
    command = re.sub(r'\$(\w+)', r'%\1%', command)

    return command

# Ejemplo de uso
command = 'dir C:\\Users\\Usuario\\Documentos'

# Detectar el sistema operativo
os_type = detect_os(command)

# Convertir el comando en función del sistema operativo detectado
if os_type == 'windows':
    converted_command = windows_to_linux(command)
    print(f'Comando Windows: {command}')
    print(f'Comando Linux: {converted_command}')
elif os_type == 'linux':
    converted_command = linux_to_windows(command)
    print(f'Comando Linux: {command}')
    print(f'Comando Windows: {converted_command}')
else:
    print('No se pudo detectar el sistema operativo.')
