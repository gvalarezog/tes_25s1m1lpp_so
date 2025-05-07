import sys
import argparse

parser = argparse.ArgumentParser(description='Cifra una palabra') #creando la variable con el funcionamiento de manejo de argumento
# parser.add_argument('palabra')
parser.add_argument('-p', dest='palabra', type=str, help='La palabra a cifrar', required=True)
parser.add_argument('-l', dest='llave', default='1', required=True)

args = parser.parse_args() #variable que me permite usar los argumentos
# print(args.palabra)
# print(args.llave)
# print(args)

lista = list(args.palabra)
lista.reverse()
for letra in lista:
    if letra == 'a':
        letra = args.llave
    print(letra, end='*')
