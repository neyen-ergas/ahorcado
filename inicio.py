import random



# Cine
cine_facil = ["Titanic", "Avatar", "Alien", "Matrix", "Amelie"]
cine_medio = ["Gladiator", "Casablanca", "Inception", "Jumanji", "Interestelar"]
cine_dificil = ["Godfather", "Schindler", "Apocalypse", "Reservoir", "Interstellar"]

# Deporte
deporte_facil = ["Fútbol", "Tenis", "Rugby", "Esgrima", "Golf"]
deporte_medio = ["Atletismo", "Natación", "Ciclismo", "Baloncesto", "Voleibol"]
deporte_dificil = ["Halterofilia", "Taekwondo", "Snowboarding", "Badminton", "Pentatlón"]

# Cultura General
cultura_general_facil = ["Historia", "Física", "Geografía", "Economía", "Cultura"]
cultura_general_medio = ["Matemáticas", "Astronomía", "Política", "Filosofía", "Biología"]
cultura_general_dificil = ["Antropología", "Sociología", "Arquitectura", "Epistemología", "Etnografía"]

# Animales
animales_facil = ["Elefante", "Tigre", "Jirafa", "Delfín", "Pingüino"]
animales_medio = ["Cocodrilo", "Colibrí", "Camaleón", "Rinoceronte", "Hipopótamo"]
animales_dificil = ["Ornitorrinco", "Avestruz", "Peregrino", "Dragón de Komodo", "Caracal"]

# Países
paises_facil = ["España", "Japón", "Brasil", "Francia", "Egipto"]
paises_medio = ["Argentina", "Australia", "Alemania", "Canadá", "Nueva Zelanda"]
paises_dificil = ["Kazajistán", "Madagascar", "Uzbekistán", "Liechtenstein", "Azerbaiyán"]

# Ciencia
ciencia_facil = ["Átomo", "ADN", "Química", "Genética", "Energía"]
ciencia_medio = ["Fotosíntesis", "Neurona", "Gravedad", "Evolución", "Mitosis"]
ciencia_dificil = ["Electromagnetismo", "Tectónica", "Termodinámica", "Biotecnología", "Criptografía"]

# Entretenimiento
entretenimiento_facil = ["Netflix", "Cómic", "Magia", "Karaoke", "Música"]
entretenimiento_medio = ["Televisión", "Concierto", "Espectáculo", "Musical", "Festival"]
entretenimiento_dificil = ["Videojuego", "Streaming", "Cinematografía", "Stand-up", "Audiovisual"]

# Geografía
geografia_facil = ["Montaña", "Océano", "Desierto", "Río", "Lago"]
geografia_medio = ["Península", "Archipiélago", "Delta", "Estrecho", "Volcán"]
geografia_dificil = ["Catarata", "Fjord", "Cenote", "Cordillera", "Meseta"]

# Fácil
facil = [
    "cine_facil",
    "deporte_facil",
    "cultura_general_facil",
    "animales_facil",
    "paises_facil",
    "ciencia_facil",
    "entretenimiento_facil",
    "geografia_facil"
]

# Medio
medio = [
    "cine_medio",
    "deporte_medio",
    "cultura_general_medio",
    "animales_medio",
    "paises_medio",
    "ciencia_medio",
    "entretenimiento_medio",
    "geografia_medio"
]

# Difícil
dificil = [
    "cine_dificil",
    "deporte_dificil",
    "cultura_general_dificil",
    "animales_dificil",
    "paises_dificil",
    "ciencia_dificil",
    "entretenimiento_dificil",
    "geografia_dificil"
]




def definir_dificultad():
    dificultad = int (input ("Bienvenido al juego del ahorcado, elegí una dificultad entre 1, 2 o 3. Luego de eso se te asignará un tema aleatorio: "))

    while dificultad < 1 or dificultad > 3:

     dificultad = int(input ("El valor ingresado es erróneo, por favor, ingresá un número entre 1, 2 o 3: "))

    if dificultad == 1:
        return facil

    elif dificultad == 2:
        return medio

    elif dificultad == 3:
        return dificil

def definir_categoria(dificultad):

    categoria = random.choice(list(dificultad))

    return categoria

def definir_palabra(categoria):
    
    palabra = random.choice(globals()[categoria])

    return palabra

def palabra_guiones(palabra):

    return '_ ' * len(palabra)

def mostrar_letra(guiones, palabra):

    letra=input("Ingrese una letra:")

    for i in range(len(palabra)):
        if palabra[i] == letra:
            guiones.replace(guiones[i], letra)
            return guiones
        




    

def juego():
    dificultad=definir_dificultad()

    categoria=definir_categoria(dificultad)

    palabra=definir_palabra(categoria)

    guiones=palabra_guiones(palabra)
    print(palabra)
    print("Se te ha asignado una palabra, a JUGAR!💪🎮", guiones)



