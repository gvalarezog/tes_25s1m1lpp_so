import platform


archivo = None
try:
    archivo = open(str(platform.node()) + '.txt', 'a')
    archivo.write(f'Procesador: {platform.processor()}\n'
                  f'Arquitectura: {platform.architecture()}\n'
                  f'Plataforma: {platform.platform()}\n'
                  f'Sistema: {platform.system() + ' ' + platform.release()}\n'
                  f'Version de Python: {platform.python_version()}\n')

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
