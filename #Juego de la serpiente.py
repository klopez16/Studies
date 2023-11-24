#Juego de la serpiente

import turtle                                       #Usamos la libreria turtle para construir la interfaz gráfica
import time                                         #Usamos la libreria time para obtener el tiempo
import random                                       #Usamos la libreria random para usar numeros aleatorios

# Configuración de la ventana

WIDTH, HEIGHT = 900, 900                            #Dimensiones de la pantalla    
SCREEN_TITLE = "Juego de la Serpiente"              #Título de la pantalla o del juego
DELAY = 0.1                                         
PUNTAJE = 0                                         #El mensaje del puntaje de la partida actuale iniciará en 0
MAXPUNTAJE = 0                                      #El mensaje del puntaje máximo iniciará en 0
