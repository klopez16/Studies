#Juego de la serpiente

import turtle                                       #Libreria para construir la interfaz gráfica
import random                                       #Libreria para traer numeros aleatorios (en este caso lo utilizo para generar aleatoriamente las coordenadas del alimento)
import time                                         #Libreria para acceder a funciones relacionadas con el tiempo

#Configuracion retraso de la pantalla
hold = 0.1                                          #Variable asignada para determinar un tiempo, en este caso un retraso 

# Configuración de la pantalla
window = turtle.Screen()                            #Pantalla a generarse
window.setup(width=600, height=700)                 #Dimensiones de la pantalla
window.tracer(0)                                    #Establecer un mejor visual para la animacion
window.title('Snake Game')                          #Título del juego que se visualiza en la pantalla  
window.bgcolor('black')

#Configuracion de la serpiente (cabeza)
head = turtle.Turtle()                              #Asignar una variable de un objeto creado en turtle en la pantalla (en este caso la cabeza)
head.speed(0)                                       #Establecer la velocidad de la animacion en turtle
head.shape('circle')                                #Establecer una forma geometrica para la cabeza de la serpiente
head.color('navy')                                  #Establecer un color para la cabeza de la serpiente
head.penup()                                        #Funcion para borrar el rastro de la cabeza en la pantalla
head.goto(0,0)                                      #Funcion aplicada para que la cabeza aparezce una parte aleatoria de la pantalla
head.direction = 'Stop'                             #Variable para solicitar que la cabeza no se mueva automaticamente al iniciar la partida

#Configuracion del alimento
food = turtle.Turtle()                              #Asignar una variable de un objeto creado en turtle en la pantalla (en este caso el alimento)
food.speed(0)                                       #Establecer la velocidad de la animacion en turtle
food.shape('triangle')                              #Establecer una forma geometrica para el alimento de la serpiente
food.color('green')                                 #Establecer un color para el alimento de la serpiente
food.penup()                                        #Funcion para borrar el rastro de el alimento en la pantalla
food.goto(0,100)                                    #Funcion aplicada para que el alimento aparezce una parte aleatoria de la pantalla

bodies = []

#Definicion de movimientos
def arriba ():                                      #Funcion para reservar un bloque de codigo definiendo el nombre asignado al bloque
    if head.direction != 'Down':                    #Definimos la variable con direccion hacia arriba
        head.direction = 'Up'

def abajo ():                                       #Funcion para reservar un bloque de codigo definiendo el nombre asignado al bloque
    if head.direction != 'Up':                      #Definimos la variable con direccion hacia abajo
        head.direction = "Down"

def izquierda ():                                   #Funcion para reservar un bloque de codigo definiendo el nombre asignado al bloque
    if head.direction != 'Right':                   #Definimos la variable con direccion hacia izquierda
        head.direction = 'Left'

def derecha ():                                     #Funcion para reservar un bloque de codigo definiendo el nombre asignado al bloque
    if head.direction != 'Left':                     #Definimos la variable con direccion hacia derecha
        head.direction = 'Right'

#Configuracion para ejecucion de movimiento
def direction():                                    #Funcion para reservar un bloque de codigo definiendo el nombre asignado al bloque
    if head.direction == "Up":                      #Funcion IF para determinar hacia donde se presenta la direccion
        y =  head.ycor()                            #Definimos a Y como la variable que determina el movimiento vertical de la serpiente 
        head.sety(y + 20)                           #Funcion para actualizar (mover) la posicion de cabeza de la serpiente en la coordenada Y

    elif head.direction == "Down":                  #Funcion ELIF para determinar hacia donde se presenta la direccion
        y =  head.ycor()                            #Definimos a Y como la variable que determina el movimiento vertical de la serpiente 
        head.sety(y - 20)                           #Funcion para actualizar (mover) la posicion de cabeza de la serpiente en la coordenada Y

    elif head.direction == "Left":                  #Funcion ELIF para determinar hacia donde se presenta la direccion
        x =  head.xcor()                            #Definimos a X como la variable que determina el movimiento horizontal de la serpiente 
        head.setx(x - 20)                           #Funcion para actualizar (mover) la posicion de cabeza de la serpiente en la coordenada X

    elif head.direction == "Right":                 #Funcion ELIF para determinar hacia donde se presenta la direccion
        x =  head.xcor()                            #Definimos a X como la variable que determina el movimiento horizontal de la serpiente 
        head.setx(x + 20)                           #Funcion para actualizar (mover) la posicion de cabeza de la serpiente en la coordenada X

#Configuracion para conexion de la pantalla con el teclado
window.listen()                                 #Funcion donde la pantalla está esperando la accion
window.onkeypress(arriba, 'Up')                 #Funcion que ejecuta la reserva del bloque definido, en este caso hacia arriba
window.onkeypress(abajo, 'Down')                #Funcion que ejecuta la reserva del bloque definido, en este caso hacia abajo
window.onkeypress(izquierda, 'Left')            #Funcion que ejecuta la reserva del bloque definido, en este caso hacia la izquierda
window.onkeypress(derecha, 'Right')             #Funcion que ejecuta la reserva del bloque definido, en este caso hacia la derecha

#Configuracion del movimiento del Juego
while True:                                         #Funcion para crear un bucle infinito
    window.update()                                 #Funcion para que ejute constantemente la actualizacion de la pantalla, es decir que no la cierre

#Configuracion de choque contra los bordes
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Right"

#Configuracion para ocultar los puntos que forman el cuerpo de la serpiente
        for body in bodies:
            body.goto(1000, 1000)

#Configuracion para limpiar la lista de la variable new_body o es decir del cuerpo de la serpiente
        bodies.clear()

#Configuracion de Alimentacion (choque de la cabeza con la comida)
    if head.distance(food)<20:                  #Funcion IF para determinar la distancia entre la cabeza y la comida
        x = random.randint(-270, 270)           #Funcion para generar un numero aleatorio en el rango establecido para la coordenada X
        y = random.randint(-270, 270)           #Funcion para generar un numero aleatorio en el rango establecido para la coordenada Y
        food.goto(x,y)                          #Actualizacion del alimento de manera random

#Configuracion para crecimiento del cuerpo de la serpiente
        new_body = turtle.Turtle()              #Asignar una variable de un objeto creado en turtle en la pantalla (en este caso el cuerpo de la serpiente)
        new_body.speed(0)                       #Establecer la velocidad de la animacion en turtle
        new_body.shape('square')                #Establecer una forma geometrica para el cuerpo de la serpiente
        new_body.color('white')                 #Establecer un color para el cuerpo de la serpiente
        new_body.penup()                        #Funcion para borrar el rastro de el alimento en la pantalla
        bodies.append(new_body)                 #Funcion para agregar los nuevos objetos al final (en este caso ir adjuntando el cuerpo de la serpiente)

#Configuracion para mover el cuerpo de la serpiente
    for index in range(len(bodies) - 1, 0, -1):
        x = bodies[index - 1].xcor()
        y = bodies[index - 1].ycor()
        bodies[index].goto(x, y)

#Configuracion para mover la cabeza de la serpiente
    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    direction()

#configuracion para el choque de la cabeza con el cuerpo de la serpiente
    for body in bodies:
        if head.distance(body) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'Right'


            for bod in bodies:
                bod.goto(1000, 1000)


                bodies.clear()

    
    time.sleep(hold)                                #Funcion para que aplique el retraso del tiempo establecido inicialmente