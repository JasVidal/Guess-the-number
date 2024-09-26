[![Typing SVG](https://readme-typing-svg.demolab.com?font=Josefin+Sans&weight=500&size=45&pause=1000&color=0C2494&center=true&vCenter=true&multiline=true&width=800&height=200&lines=%C2%A1Hola!+Bienvenido+al+juego;Guess+the+Number+%F0%9F%A4%93)](https://git.io/typing-svg)

## Índice

- [1. Resumen del Proyecto](#1-resumen-del-proyecto)
- [2. Características Generales](#2-características-generales)
- [3. Objetivos de Aprendizaje](#3-objetivos-de-aprendizaje)
- [4. Lenguaje utilizado: Python 🐍](#4-lenguaje-utilizado-python-)
- [5. Hitos](#5-hitos)

---

<div align="center"><img width="900" align="center" src="https://www.educative.io/v2api/editorpage/6492381537894400/image/5954168597512192"></div>


## 1. Resumen del Proyecto

_Guess The Number_ es un juego interactivo desarrollado para ejecutarse en la terminal. En este juego, tanto el jugador como la computadora se turnan para intentar adivinar un número aleatorio entre 1 y 100. Durante el transcurso del juego, se proporcionan pistas sobre la validez de las suposiciones, indicando si estas son "muy altas" o "muy bajas".

![Demostración del juego](https://firebasestorage.googleapis.com/v0/b/laboratoria-945ea.appspot.com/o/guess-the-number-demo.gif?alt=media)

## 2. Características Generales

- **Turnos alternos entre jugador y computadora**: El juego permite que ambos alternen turnos para adivinar el número secreto, fomentando la interacción y competitividad.

- **Visualización de información**: Después de cada intento, se muestra el nombre del jugador, la suposición realizada y el resultado, con mensajes que indican si la suposición fue "muy alta", "muy baja" o correcta.

- **Finalización del juego**: El juego concluye al adivinar correctamente el número secreto, mostrando un mensaje final y una lista de todos los intentos realizados durante la partida.
  

## 3. Objetivos de Aprendizaje

- Comprendí y apliqué conceptos básicos de programación en Python.
- Implementé estructuras de control, bucles y condiciones en el desarrollo del juego.
- Creé pruebas unitarias y manejé errores para asegurar la funcionalidad del código.
- Mejoré mis habilidades de resolución de problemas a través del desarrollo de un juego interactivo.

## 4. Lenguaje utilizado: Python 🐍

### 1. Preámbulo

Python es un lenguaje de programación popular por su simplicidad y legibilidad, ideal para principiantes. Su naturaleza multiparadigma permite resolver problemas con distintos estilos de programación. Este proyecto busca introducir a los usuarios en Python a través de un juego sencillo y entretenido.

### 2. Consideraciones Específicas

- **Lenguaje de programación**: El juego se implementa en Python, utilizando pytest como única dependencia externa permitida para pruebas unitarias.
  
- **Ejecutabilidad**: El juego se ejecuta en la terminal y las pruebas se pueden realizar tanto en la terminal como en un IDE, siendo Visual Studio Code el recomendado.

- **Número secreto**: Se utiliza un número aleatorio entre 1 y 100 como el número que se debe adivinar.

- **Turnos de juego**: El jugador y la computadora se alternan para intentar adivinar el número secreto.

- **Visualización de suposiciones**: Se muestra información sobre cada suposición realizada por el jugador y la computadora.

- **Finalización del juego**: El juego concluye cuando se adivina correctamente el número secreto, mostrando una lista de todas las tentativas realizadas.

### 3. Consideraciones Técnicas

El juego se lleva a cabo en la terminal usando Python. La lógica del juego incluye estructuras de control como bucles, condicionales y colecciones. Se mantiene el código modular y legible. Se utiliza la biblioteca de utilidades de Python para generar números aleatorios y se realizan pruebas unitarias con PyTest.

## 5. Hitos

### 5.1 Entorno de desarrollo

- Se instaló Python 3 desde el [sitio oficial de Python](https://www.python.org/downloads/).
- Se eligió un editor de texto o IDE, como [PyCharm](https://www.jetbrains.com/pycharm/), [Visual Studio Code](https://code.visualstudio.com/) o [Sublime Text](https://www.sublimetext.com/).
- Se configuró el editor o IDE para utilizar Python 3.

### 5.2 Creación de un script de Python

- Se creó un archivo llamado `main.py`.
- Se ejecutó `main.py`.

### 5.3 Implementación del juego

- Se generó un número aleatorio entre 1 y 100 utilizando `randint`.
- Se implementó un bucle que solicita al jugador adivinar el número mediante `input`.
- Se comparó la entrada del jugador con el número secreto, proporcionando pistas al respecto.
- Se desarrolló la lógica para el turno de la computadora.
- Se continuó el juego hasta que alguien adivinara el número.
- Se añadieron pruebas unitarias usando `unittest`.

### 5.4 Mejoras del juego

- Se llevó un registro de las suposiciones realizadas y se mostraron al final del juego.
- Se agregó una opción para jugar de nuevo.
- Se añadieron comentarios para mejorar la legibilidad del código.
