#Juego de la serpiente

import turtle                                       #Usamos la libreria turtle para construir la interfaz gráfica

# Configuración de la ventana
window = turtle.Screen()
turtle.window_width()                               #Dimensiones de la pantalla (ancho)
900                                                 
turtle.window_height()                              #Dimensiones de la pantalla (alto)
900                                                 
turtle.delay()                                      #Establecer un retraso entre actualizaciones del lienzo
500
window.tracer(0)

#Configuración de variables
window.title('Snake Game')                          #Título del juego que se visualiza en la pantalla  
window.bgcolor("black")
Puntaje = 0                                         #El mensaje del puntaje de la partida actuale iniciará en 0
MaxPuntaje = 0                                      #El mensaje del puntaje máximo iniciará en 0
