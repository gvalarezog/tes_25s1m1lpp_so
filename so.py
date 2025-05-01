import os
#
# print(os.path.isfile('C:\\Proyectos\\Python\\Scripting\\Unidad3\\GEVG-Laptop2.txt'))
# print(os.path.isfile('C:\\Proyectos\\Python\\Scripting\\Unidad3'))
#
# print(os.path.isdir('C:\\Proyectos\\Python\\Scripting\\Unidad3'))
# print(os.path.isdir('C:\\Proyectos\\Python\\Scripting\\Unidad3\\GEVG-Laptop2.txt'))
#
# print(os.path.sep)
#
# ruta = 'C:\\Proyectos\\Python'
#
# print(os.path.getsize('C:\\Proyectos\\Python\\Scripting\\Unidad3\\GEVG-Laptop2.txt'))
# print(os.path.getatime(ruta))
# print(os.path.getctime(ruta))
# print(os.path.getmtime(ruta))
#
# print(os.getcwd())
# os.chdir(path=ruta)
# print(os.getcwd())

# try:
#
#     ruta_host = 'C:\\Windows\\System32\\drivers\\etc'
#     print(os.listdir(ruta_host))
#     os.chdir(ruta_host)
#     for archivo in os.listdir(ruta_host):
#         print(archivo)
#         print(os.path.isfile(archivo))
#         with open(archivo, 'r') as a:
#            print(a.read())
#         print('Fin de archivo')
#         print('*'.center(80, '*'))
# except Exception as e:
#     print(e)

comando = input('Ingrese el comando a ejecutar: ')
rt = None
try:
    rt = os.system(comando)
except Exception as e:
    print(e)
if rt == 0:
    print('La ejecución fue correcta')
else:
    print('La ejecución no fue correcta')