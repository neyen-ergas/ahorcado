# Juego del Ahorcado

¡Bienvenido al clásico juego del Ahorcado! Este proyecto permite al jugador adivinar palabras pertenecientes a distintas categorías y niveles de dificultad. A medida que se cometen errores, el dibujo del ahorcado se completa. ¡Adivina antes de perder todas tus vidas!

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Requisitos](#requisitos)
- [Ejecución](#ejecución)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Descripción

El juego presenta una palabra oculta que pertenece a una categoría elegida al azar. El jugador tiene 6 intentos para adivinarla correctamente antes de "ser ahorcado". Con cada error, se dibuja una parte del ahorcado.

### Mecánica del Juego

1. Selecciona un nivel de dificultad (Fácil, Medio, Difícil).
2. Una categoría se elige al azar dentro del nivel de dificultad.
3. Adivina la palabra letra por letra.
4. Cada error reducirá tus intentos y actualizará el dibujo del ahorcado.
5. ¡Adivina la palabra completa antes de quedarte sin intentos!

## Características

- Selección de dificultad: Fácil, Medio, Difícil.
- Diversas categorías temáticas: Cine, Deportes, Geografía, Animales, etc.
- Representación gráfica del ahorcado que se actualiza con cada intento incorrecto.
- Indicador visual de vidas restantes con corazones.

## Requisitos

Para ejecutar este proyecto, necesitas:

- **Python 3.7+**
- Módulos estándar de Python (`random`)

## Ejecución

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu_usuario/juego-ahorcado.git
