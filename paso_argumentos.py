import sys

# print(sys.argv)
# for argumento in sys.argv:
#     print(f'Argumento: {argumento}')

if len(sys.argv) > 2:
    if sys.argv[2].lower() == 'lower':
        print(sys.argv[1].lower())
    elif sys.argv[2].lower() == 'upper':
        print(sys.argv[1].upper())
    elif sys.argv[2].lower() == 'title':
        print(sys.argv[1].title())
    else:
        print(f'Accion ingresada incorrecta {sys.argv[2]}')
else:
    print(f'Uso: {sys.argv[0]} <nombre> <accion|lower-upper-title>')
    sys.exit()
# # if len(sys.argv) != 3:
# #     print(f'Uso: {sys.argv[0]} <nombre> <accion|lower-upper-title>')
# #     sys.exit()
# #
# # usr_nombre = sys.argv[1]
# # usr_accion = sys.argv[2] #lower-upper-title

# def cambiar_mayusculas(palabra):
#     '''
#     Función recibe una palabra y la pone todas en Mayusculas
#     :param palabra: cualquier palabra que va a cambiarse en mayusculas
#     :return: la palabra cambiada en mayusculas
#     '''
#     return palabra.upper()
#
# print(cambiar_mayusculas(input('Ingrese la palabra: ')))