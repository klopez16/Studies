#Juego de la serpiente

import turtle                                       #Libreria para construir la interfaz gráfica
import random                                       #Libreria para traer numeros aleatorios (en este caso lo utilizo para generar aleatoriamente las coordenadas del alimento)

# Configuración de la pantalla
window = turtle.Screen()                            #Pantalla a generarse
turtle.window_width()                               #Dimensiones de la pantalla (ancho)
900                                                 
turtle.window_height()                              #Dimensiones de la pantalla (alto)
900                                                 
turtle.delay()                                      #Establecer un retraso entre actualizaciones del lienzo
500
window.tracer(0)                                    #Establecer un mejor visual para la animacion

#Configuración de variables de la pantalla
window.title('Snake Game')                          #Título del juego que se visualiza en la pantalla  
window.bgcolor('gray')
Puntaje = 0                                         #El mensaje del puntaje de la partida actuale iniciará en 0

#Configuracion de la serpiente (cabeza)
head = turtle.Turtle()                              #Asignar una variable de un objeto creado en turtle en la pantalla (en este caso la cabeza)
head.speed(6)                                       #Establecer la velocidad de la animacion en turtle
head.shape('circle')                                #Establecer una forma geometrica para la cabeza de la serpiente
head.color('blue')                                  #Establecer un color para la cabeza de la serpiente
head.penup()                                        #Funcion para borrar el rastro de la cabeza en la pantalla
head.goto(0,0)                                      #Funcion aplicada para que la cabeza aparezce una parte aleatoria de la pantalla
head.direction = 'stop'                             #Variable para solicitar que la cabeza no se mueva automaticamente al iniciar la partida

#Configuracion del alimento
food = turtle.Turtle()                              #Asignar una variable de un objeto creado en turtle en la pantalla (en este caso el alimento)
food.speed(6)                                       #Establecer la velocidad de la animacion en turtle
food.shape('triangle')                              #Establecer una forma geometrica para el alimento de la serpiente
food.color('green')                                 #Establecer un color para el alimento de la serpiente
food.penup()                                        #Funcion para borrar el rastro de el alimento en la pantalla
food.goto(0,0)                                      #Funcion aplicada para que el alimento aparezce una parte aleatoria de la pantalla

#Configuracion del texto del puntaje
point = turtle.Turtle()                                                     #Asignar una variable de un objeto creado en turtle en la pantalla (en este caso el texto del puntaje)
point.speed(6)                                                              #Establecer la velocidad de la animacion en turtle
point.color('white')                                                        #Establecer un color para el alimento de la serpiente
point.penup()                                                               #Funcion para borrar el rastro de el alimento en la pantalla
point.hideturtle()                                                          #Funcion para ocultar el objeto cuando se dibuja otros
point.goto(0,800)                                                           #Funcion aplicada para que el alimento aparezce una parte aleatoria de la pantalla                                     
point.write('Puntaje:0', align='center', font=('Roboto', 20, 'normal'))     #Funcion para visualizar el texto en la pantalla

#Configuracion del cuerpo de la serpiente
body = []
color = [('green')]

#Configuracion de movimientos
def arriba ():
    head.direction = 'up'

def abajo ():
    head.direction = 'down'

def izquierda ():
    head.direction = 'left'

def derecha ():
    head.direction = 'right'