import random
from dificultad import *
from categorias import *
from dibujo_ahorcado import *
import dificultad as dificultades


def elegir_dificultad():
    while True:
        dificultad = input("Elige una dificultad (1 = fácil, 2 = medio, 3 = difícil): ")
        if dificultad == "1" or dificultad == "2" or dificultad == "3":
            return int(dificultad)
        else:
            print("Por favor, elige un número entre 1, 2 o 3.")

def elegir_lista(dificultad):
    if dificultad == 1:
        lista = dificultades.facil
    elif dificultad == 2:
        lista = dificultades.medio
    else:
        lista = dificultades.dificil
    return lista

def elegir_categoria(lista):
    indice_categoria = random.randrange(len(lista))
    nombre_categoria, palabras = lista[indice_categoria]
    return nombre_categoria, palabras


def elegir_palabra(categoria):
    
    palabra = categoria[random.randrange(len(categoria))]
    return palabra

def mostrar_guiones(palabra):
    return "_ " * len(palabra)

def pedir_letra():
    while True:
        letra = input("Ingresa una letra: ").lower()
        if len(letra) == 1 and ('a' <= letra <= 'z' or 'A' <= letra <= 'Z'):
            return letra
        else:
            print("Por favor, ingrese una letra valida.")

def actualizar_guiones(guiones, palabra, letra):
    guiones_lista = list(guiones) 
    for i in range(len(palabra)):
        if palabra[i].lower() == letra:
            guiones_lista[i * 2] = palabra[i]
    return ''.join(guiones_lista)

def intentos_a_corazones(intentos):
    corazones=""
    while intentos>0:
        corazones=corazones + "❤ "
        intentos-= 1
    return corazones