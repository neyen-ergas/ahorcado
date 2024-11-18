from logica.logica import *


def juego():
    print("Bienvenido al juego del ahorcado!")

    while True:
        dificultad = elegir_dificultad()
        lista= elegir_lista(dificultad)
        nombre_categoria, categoria = elegir_categoria(lista)
        palabra = elegir_palabra(categoria)
        guiones = mostrar_guiones(palabra)
        
        intentos = 6
        letras_adivinadas = []

        mostrar_ahorcado(intentos)
        print(f"¡A jugar!🎮\nLa categoría es: {nombre_categoria} \nPalabra a adivinar: {guiones}")


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
                mostrar_ahorcado(intentos)
                print(f"¡Letra incorrecta! Te quedan {intentos} vidas.")
                print(f"Palabra actual: {guiones}")


            if "_ " not in guiones:
                print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
                break
        else:
            mostrar_ahorcado(intentos) 
            print(f"¡Perdiste!💀 La palabra era: {palabra}")

        jugar_otra_vez = input("\nPresiona Enter para jugar de nuevo o escribe 'salir' para terminar: ")
        if jugar_otra_vez.lower() == 'salir':
            print("¡Gracias por jugar! 😊")
            break  

    

juego()
