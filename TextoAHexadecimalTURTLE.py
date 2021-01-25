'''
Programa que emula la transmisión en hexadecimal de un código binario arremedando
a la película «Marte»

En esa película se muestra una cámara que, en nuestro caso será Turtle que se
desplaza angularmente para ir seleccionando los caracteres hexadecimales que
conforman el mensaje proveniente de la Tierra que recibe el astronauta.
'''

import turtle

def mensajeAhexadecimal(cadena): #Función que traduce una cadena en ASCII decimal a su correspondiente hexadecimal.
    cadenaHexadecimal = "" #Esta cadena será la que devolverá esta función
    
    if len(cadena)==0:
        return cadenaHexadecimal
    
    for caracter in cadena:
        
        cadenaHexadecimal = cadenaHexadecimal + hex(ord(caracter)).partition("x")[2]
    
    return cadenaHexadecimal

def ponerLeyenda(texto,coordX,coordY):
    tortuga.penup() #Se levanta el lápiz
    #Se traslada la tortuga al punto cuya coordenada es (coordX,coordY)
    tortuga.setx(coordX) 
    tortuga.sety(coordY)
    tortuga.pendown() #Se baja la pluma para dejar huella
    tortuga.write(texto) #Se escribe el texto
    

def marcoOriginal(): #Función que dibuja los 16 radiovectores en que queda dividido el plano
    PASO = 60 #Cantidad de pasos que avanzará o retrocederá la tortuga
    caracteres=('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f')
    #Se debe dibujar el centro y la circunferencia
    tortuga.penup()
    tortuga.home()
    tortuga.pendown()
    tortuga.setheading(0)
    
    for i in range(16):
        tortuga.forward(PASO)
        tortuga.write(caracteres[i])
        tortuga.backward(PASO)
        tortuga.setheading((i+1)*22.5)
   
def mensajeUsandoCamara(texto): #Función que dibuja el código
    #El siguiente diccionario contiene los ángulos que debe rotar la cámara
    digitoBinario={'0':0,'1':22.5,'2':45,'3':67.5,'4':90,'5':112.5,'6':135,'7':157.5,
                   '8':180,'9':202.5,'a':225,'b':247.5,'c':270,'d':292.5,'e':315,'f':337.5}
    tortuga.pencolor("red") #Se establece el color
    PASO=70
    contador=1 #El contador aparecerá como el nominal justo en la punta del vector
    tortuga.speed(1)
    
    for caracter in texto:
        tortuga.setheading(digitoBinario[caracter])
        tortuga.forward(PASO)
        tortuga.write(str(contador)+'o')
        tortuga.backward(PASO)
        PASO += 10
        contador +=1
#<<< FIN DE DEFINICION DE FUNCIONES            

mensajeAscii = input("Dame mensaje a transmitir a Marte: ")
txtHexadecimal = mensajeAhexadecimal(mensajeAscii)
tortuga = turtle.Turtle() #Constructor de la tortuga

ponerLeyenda("Mensaje original: "+mensajeAscii,-300,250)
ponerLeyenda("Mensaje hexadecimal: "+txtHexadecimal,-300,230) 

marcoOriginal() #Se dibujan los 16 radios correspondientes a los 16 dígitos hexadecimales
mensajeUsandoCamara(txtHexadecimal)