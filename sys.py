import os
import platform


archivo = None
try:
    env = os.environ
    archivo = open(str(platform.node()) + '.txt', 'w')
    archivo.write(f'Procesador: {platform.processor()}\n'
                  f'Arquitectura: {platform.architecture()}\n'
                  f'Plataforma: {platform.platform()}\n'
                  f'Sistema: {platform.system() + ' ' + platform.release()}\n'
                  f'Version de Python: {platform.python_version()}\n')
    for llave, valor in env.items():
        archivo.write(f'{llave}: {valor}\n')

    print(f'Procesador: {platform.processor()}')
    print(f'Arquitectura: {platform.architecture()}')
    print(f'Plataforma: {platform.platform()}')
    print(f'Sistema: {platform.system()}')
    print(f'Version de Python: {platform.python_version()}')
    print(f'Nombre Maquina: {platform.node()}')
    print(f'Release: {platform.release()}')
except Exception as e:
    print(e)
else:
    print('Informacion almacenada con exito')
finally:
    if archivo:
        archivo.close()
