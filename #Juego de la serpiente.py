#Juego de la serpiente

import turtle                                       #Libreria para construir la interfaz gráfica
import random                                       #Libreria para traer numeros aleatorios (en este caso lo utilizo para generar aleatoriamente las coordenadas del alimento)
import time                                         #Libreria para acceder a funciones relacionadas con el tiempo

#Configuracion pantalla
hold = 0.1                                          #Variable asignada para determinar un tiempo, en este caso un retraso 

# Configuración de la pantalla
window = turtle.Screen()                            #Pantalla a generarse
turtle.window_width()                               #Dimensiones de la pantalla (ancho)
200                                                 
turtle.window_height()                              #Dimensiones de la pantalla (alto)
200                                                 
turtle.delay()                                      #Establecer un retraso entre actualizaciones del lienzo
500
window.tracer(0)                                    #Establecer un mejor visual para la animacion
window.title('Snake Game')                          #Título del juego que se visualiza en la pantalla  
window.bgcolor('white')

#Configuracion de la serpiente (cabeza)
head = turtle.Turtle()                              #Asignar una variable de un objeto creado en turtle en la pantalla (en este caso la cabeza)
head.speed(0)                                       #Establecer la velocidad de la animacion en turtle
head.shape('circle')                                #Establecer una forma geometrica para la cabeza de la serpiente
head.color('blue')                                  #Establecer un color para la cabeza de la serpiente
head.penup()                                        #Funcion para borrar el rastro de la cabeza en la pantalla
head.goto(0,0)                                      #Funcion aplicada para que la cabeza aparezce una parte aleatoria de la pantalla
head.direction = 'stop'                             #Variable para solicitar que la cabeza no se mueva automaticamente al iniciar la partida

#Configuracion del alimento
food = turtle.Turtle()                              #Asignar una variable de un objeto creado en turtle en la pantalla (en este caso el alimento)
food.speed(0)                                       #Establecer la velocidad de la animacion en turtle
food.shape('triangle')                              #Establecer una forma geometrica para el alimento de la serpiente
food.color('green')                                 #Establecer un color para el alimento de la serpiente
food.penup()                                        #Funcion para borrar el rastro de el alimento en la pantalla
food.goto(0,100)                                      #Funcion aplicada para que el alimento aparezce una parte aleatoria de la pantalla

segments = []

#Definicion de movimientos
def arriba ():                                      #Funcion para reservar un bloque de codigo definiendo el nombre asignado al bloque
    if head.direction != 'Down':                    #Definimos la variable con direccion hacia arriba
        head.direction = 'Up'

def abajo ():                                       #Funcion para reservar un bloque de codigo definiendo el nombre asignado al bloque
    if head.direction != 'Up':                      #Definimos la variable con direccion hacia abajo
        head.direction = "Down"

def izquierda ():                                   #Funcion para reservar un bloque de codigo definiendo el nombre asignado al bloque
    if head.direction != 'right':                   #Definimos la variable con direccion hacia izquierda
        head.direction = 'left'

def derecha ():                                     #Funcion para reservar un bloque de codigo definiendo el nombre asignado al bloque
    if head.direction != 'left':                     #Definimos la variable con direccion hacia derecha
        head.direction = 'right'

#Configuracion para ejecucion de movimiento
def direction():                                    #Funcion para reservar un bloque de codigo definiendo el nombre asignado al bloque
    if head.direction == "up":                      #Funcion IF para determinar hacia donde se presenta la direccion
        y =  head.ycor()                            #Definimos a Y como la variable que determina el movimiento vertical de la serpiente 
        head.sety(y + 20)                           #Funcion para actualizar (mover) la posicion de cabeza de la serpiente en la coordenada Y

    elif head.direction == "down":                  #Funcion ELIF para determinar hacia donde se presenta la direccion
        y =  head.ycor()                            #Definimos a Y como la variable que determina el movimiento vertical de la serpiente 
        head.sety(y - 20)                           #Funcion para actualizar (mover) la posicion de cabeza de la serpiente en la coordenada Y

    elif head.direction == "left":                  #Funcion ELIF para determinar hacia donde se presenta la direccion
        x =  head.xcor()                            #Definimos a X como la variable que determina el movimiento horizontal de la serpiente 
        head.setx(x - 20)                           #Funcion para actualizar (mover) la posicion de cabeza de la serpiente en la coordenada X

    elif head.direction == "right":                 #Funcion ELIF para determinar hacia donde se presenta la direccion
        x =  head.xcor()                            #Definimos a X como la variable que determina el movimiento horizontal de la serpiente 
        head.setx(x + 20)                           #Funcion para actualizar (mover) la posicion de cabeza de la serpiente en la coordenada X

#Configuracion para conexion de la pantalla con el teclado
    window.listen()                                     #Funcion donde la pantalla está esperando la accion
    window.onkeypress(arriba,'Up')                      #Funcion que ejecuta la reserva del bloque definido, en este caso hacia arriba
    window.onkeypress(abajo,'Down')                     #Funcion que ejecuta la reserva del bloque definido, en este caso hacia abajo
    window.onkeypress(izquierda,'Left')                 #Funcion que ejecuta la reserva del bloque definido, en este caso hacia la izquierda
    window.onkeypress(derecha,'Right')                  #Funcion que ejecuta la reserva del bloque definido, en este caso hacia la derecha

#Configuracion para movimiento del cuerpo
def movementBody():                                 #Funcion para reservar un bloque de codigo definiendo el nombre asignado al bloque
    totalBody = len(body)                           #Funcion para devolver la longitud del objeto en este caso el cuerpo
    
    for body in range(totalBody-1,0,-1):            #Funcion en bucle para iterar 
        x = body[body-1].xcor()                     #Método para obtener la coordenada X del objeto
        y = body[body-1].ycor()                     #Método para obtener la coordenada Y del objeto
        body[body].goto(x,y)                        #Método para mover el objeto a las coordenadas X,Y obtenidas en las dos líneas anteriores

    if totalBody >0:                                #Funcion IF para determinar hacia donde se presenta la direccion
        x = head.xcor()                             #Definimos a X como la variable que determina el movimiento horizontal de la serpiente
        y = head.ycor()                             #Definimos a Y como la variable que determina el movimiento vertical de la serpiente
        body[0].goto(x,y)                           #Método para mover el objeto a las coordenadas X,Y

#Configuracion de Alimentacion (choque de la cabeza con la comida)
def feeding():                                      #Funcion para reservar un bloque de codigo definiendo el nombre asignado al bloque
    if head.distance(food)<25:                      #Funcion IF para determinar la distancia entre la cabeza y la comida
        x = random.randint(-500, 500)               #Funcion para generar un numero aleatorio en el rango establecido para la coordenada X
        y = random.randint(-500, 500)               #Funcion para generar un numero aleatorio en el rango establecido para la coordenada Y
        food.goto(x,y)                              #Actualizacion del alimento de manera random

#Configuracion de la pantalla para que sea continua
while True:                                         #Funcion para crear un bucle infinito en este caso utilizada para que la pantalla se mantenga activa
    window.update()                                 #Funcion para que ejute constantemente la actualizacion de la pantalla, es decir que no la cierre
    time.sleep(hold)                                #Funcion para que aplique el retraso del tiempo establecido inicialmente