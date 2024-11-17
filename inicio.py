import random
from dificultad import *
from categorias import *
import dificultad as dificultades

def elegir_dificultad():
    while True:
        dificultad = input("Elige una dificultad (1 = fácil, 2 = medio, 3 = difícil): ")
        if dificultad == "1" or dificultad == "2" or dificultad == "3":
            return int(dificultad)
        else:
            print("Por favor, elige un número entre 1, 2 o 3.")

def elegir_palabra(dificultad):
    if dificultad == 1:
        lista = dificultades.facil
    elif dificultad == 2:
        lista = dificultades.medio
    else:
        lista = dificultades.dificil

    categoria = lista[random.randrange(0,len(lista))]
    palabra = categoria[random.randrange(0,len(categoria))]
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
        corazones=corazones + "♥ "
        intentos-= 1
    return corazones



def juego():
    print("Bienvenido al juego del ahorcado")
    
    dificultad = elegir_dificultad()
    palabra = elegir_palabra(dificultad)
    guiones = mostrar_guiones(palabra)
    intentos = 5 
    letras_adivinadas = []
    
    print(f"Palabra a adivinar: {guiones}")
    
    while intentos > 0:
        letra = pedir_letra()

        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra, intenta con otra.")
            continue

        letras_adivinadas.append(letra)
        
        if letra in palabra.lower():
            print(f"¡Correcto! La letra {letra} está en la palabra.")
            guiones = actualizar_guiones(guiones, palabra, letra)
            print(f"Palabra actual: {guiones}")
        else:
            intentos -= 1
            corazones=intentos_a_corazones(intentos)

            print(f"¡Letra incorrecta! Te quedan {corazones} vidas.")
        
        if "_ " not in guiones:
            print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
            break
    else:
        print(f"¡Perdiste! La palabra era: {palabra}")

juego()

#TODO: Mensajes en otro archivo, cuerpito del tipito, readme, play again?, clases en otro archivo, tu categoria es.