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
window.bgcolor('black')                             #Color del fondo de la pantalla

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
food.shape('circle')                                #Establecer una forma geometrica para el alimento de la serpiente
food.color('red')                                   #Establecer un color para el alimento de la serpiente
food.penup()                                        #Funcion para borrar el rastro de el alimento en la pantalla
food.goto(0,100)                                    #Funcion aplicada para que el alimento aparezce una parte aleatoria de la pantalla

bodies = []                                         #Funcion para crear una lista vacia para el cuerpo de la serpiente

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
    if head.direction != 'Left':                    #Definimos la variable con direccion hacia derecha
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
window.listen()                                     #Funcion donde la pantalla está esperando la accion
window.onkeypress(arriba, 'Up')                     #Funcion que ejecuta la reserva del bloque definido, en este caso hacia arriba
window.onkeypress(abajo, 'Down')                    #Funcion que ejecuta la reserva del bloque definido, en este caso hacia abajo
window.onkeypress(izquierda, 'Left')                #Funcion que ejecuta la reserva del bloque definido, en este caso hacia la izquierda
window.onkeypress(derecha, 'Right')                 #Funcion que ejecuta la reserva del bloque definido, en este caso hacia la derecha

#Configuracion del movimiento del Juego
while True:                                         #Funcion para crear un bucle infinito
    window.update()                                 #Funcion para que ejute constantemente la actualizacion de la pantalla, es decir que no la cierre

#Configuracion de choque contra los bordes
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:          #Funcion para verificar si las coordenadas X o Y de la cabeza exceden los valores determinados (en este caso 290 o -290) en cualquier dirección
        time.sleep(1)                               #Funcion para pausar el juego por el tiempo determinado (en este caso 1 segundo)
        head.goto(0, 0)                             #Funcion para mover la posicion de la cabea al centro (coordenadas 0, 0)
        head.direction = "Right"                    #Funcion para establecer el movimiento de la cabeza hacia una direccion especificada (en este caso hacia la derecha)

#Configuracion para ocultar los puntos que forman el cuerpo de la serpiente
        for body in bodies:                         #Funcion para asignar el valor de cada elemento de la lista "bodies" a la variable "body"  (en este caso ir alimentando el cuerpo)
            body.goto(1000, 1000)                   #Funcion para enviar los objetos que forman el cuerpo de la serpiente a un punto en el entorno gráfico no visible

#Configuracion para limpiar la lista de la variable new_body o es decir del cuerpo de la serpiente
        bodies.clear()

#Configuracion de Alimentacion (choque de la cabeza con la comida)
    if head.distance(food)<20:                      #Funcion IF para determinar una distancia entre la cabeza y la comida
        x = random.randint(-270, 270)               #Funcion para generar un numero aleatorio en el rango establecido para la coordenada X
        y = random.randint(-270, 270)               #Funcion para generar un numero aleatorio en el rango establecido para la coordenada Y
        food.goto(x,y)                              #Actualizacion del alimento de manera random

#Configuracion para crecimiento del cuerpo de la serpiente
        new_body = turtle.Turtle()                  #Asignar una variable de un objeto creado en turtle en la pantalla (en este caso el cuerpo de la serpiente)
        new_body.speed(0)                           #Establecer la velocidad de la animacion en turtle
        new_body.shape('square')                    #Establecer una forma geometrica para el cuerpo de la serpiente
        new_body.color('white')                     #Establecer un color para el cuerpo de la serpiente
        new_body.penup()                            #Funcion para borrar el rastro de el alimento en la pantalla
        bodies.append(new_body)                     #Funcion para agregar los nuevos objetos al final (en este caso ir adjuntando el cuerpo de la serpiente)

#Configuracion para mover el cuerpo de la serpiente
    for index in range(len(bodies) - 1, 0, -1):     #Funcion FOR para recorrer la lista "bodies" desde el penúltimo elemento (índice -1) hasta el primer elemento (índice 0), en orden decreciente
        x = bodies[index - 1].xcor()                #Funcion para almacenar la coordenada X del objeto anterior en la variable x
        y = bodies[index - 1].ycor()                #Funcion para almacenar la coordenada y del objeto anterior en la variable y
        bodies[index].goto(x, y)                    #Funcion para mover el objeto cuerpo de la serpiente, ubicado en el índice (en este caso la variable index) de la lista, a las coordenadas x e y obtenidas

#Configuracion para mover la cabeza de la serpiente
    if len(bodies) > 0:                             #Funcion IF para determinar si la lista del cuerpo (en este caso bodies) contiene al menos 1 elemento
        x = head.xcor()                             #Funcion para obtener la coordenada x de la cabeza de la serpiente (en este caso head)
        y = head.ycor()                             #Funcion para obtener la coordenada x de la cabeza de la serpiente (en este caso head)
        bodies[0].goto(x, y)                        #Funcion que mueve el primer elemento de la lista del cuerpo (en este caso bodies) a las coordenadas de la cabeza (obtenidas anteriormente)

    direction()                                     #Llamar a la funcion 'direction'

#Configuracion para el choque de la cabeza con el cuerpo de la serpiente
    for body in bodies:                             #Funcion FOR para iterar los elementos del cuerpo de la serpiente (en este caso la lista bodies) y asignarles a la variable body
        if head.distance(body) < 20:                #Funcion IF para verificar la distancia de la cabeza con el cuerpo de la serpiente
            time.sleep(1)                           #Funcion para pausar el juego por el tiempo determinado (en este caso 1 segundo) 
            head.goto(0, 0)                         #Funcion para mover la posicion de la cabea al centro (coordenadas 0, 0)
            head.direction = 'Right'                #Funcion para establecer el movimiento de la cabeza hacia una direccion especificada (en este caso hacia la derecha)
            for bod in bodies:                      #Funcion FOR para recorrer la lista del cuerpo de la serpiente y asignarles a una variable (en este caso bod)
                bod.goto(1000, 1000)                #Funcion para enviar los objetos que formaron el cuerpo de la serpiente a un punto en el entorno gráfico no visible
                bodies.clear()                      #Funcion para eliminar la lista de los objetos del cuerpo de la serpiente

    time.sleep(hold)                                #Funcion para que aplique el retraso del tiempo establecido inicialmente