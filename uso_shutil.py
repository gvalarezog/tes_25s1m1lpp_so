import os
import shutil

# try:
#     src = 'C:\\Proyectos\\Python\\Scripting\\Unidad3\\src\\'
#     dst = 'C:\\Proyectos\\Python\\Scripting\\Unidad3\\dst\\'
#
#     print(os.listdir(src))
#
#     # shutil.copyfile(src + 'prueba1.txt', dst + 'prueba1.txt')
#     # shutil.copy(src + 'prueba2.txt', dst + 'prueba2.txt')
#     # shutil.copy2(src + 'prueba3.txt', dst + 'prueba3.txt')
#     shutil.copymode(src + 'prueba4.txt', dst + 'prueba4.txt')
# except Exception as e:
#     print(e)
dst = 'C:\\Proyectos\\Python\\Scripting\\Unidad3\\dst\\'
ruta_host = 'C:\\Windows\\System32\\drivers\\etc\\'
try:
    print(os.listdir(ruta_host))
    os.chdir(dst) # change directory
    os.mkdir('respaldo')
    for archivo in os.listdir(ruta_host):
        print(archivo)
        shutil.copyfile(ruta_host + archivo, dst + '\\respaldo\\' + archivo )
except Exception as e:
    print(e)
