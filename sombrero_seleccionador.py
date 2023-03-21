""""
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts:
 *   (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas
 *   y crear el algoritmo seleccionador:
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 """


#PREGUNTAS
preg1 = int(input("Ves que una persona está siendo atacada por un dementor ¿que harías? \n 1-peleo con dementor \n 2-dejo que ataquen a la persona para escapar \n 3-ayudo persona para q me ayuder a enfrentarlo\n 4-casteo hechizo como teletransportación\nRespuesta: ")) 
preg2 = int(input("ves a una persona llorando \n 1-le digo q le pasa y ayudo a resolver el preblema \n 2-no hago nada \n 3-le doy apoyo emocional \n 4-le doy una respues para aliviar su tristeza\nRespuesta: ") )
preg3 = int(input("ves un animal en la calle \n 1-trato de encontrar de quien es \n 2-no hago nada \n 3-lo llevo a casa y cuido hasta que se mejore \n 4-hago una publicidad para encontrar al dueño más facilmente\nRespuesta: ")) 
preg4 = int(input("¿qué animal te gusta más? \n 1-un grifo \n 2-una serpiente \n 3-un oso panda \n 4-un cuervo\nRespuesta: "))
preg5 = int(input("describite a ti mismo \n 1-soy valiente \n 2-soy ambicionso \n 3-soy amable \n 4-me gusta estudiar\nRespuesta: "))


#SOMBRERO SELECCIONADOR
lista_de_preguntas = [preg1,preg2,preg3,preg4,preg5]
contador = 0    
casa_ganadora = 0

for i in [1,2,3,4]:

    if contador < lista_de_preguntas.count(i):
        contador = lista_de_preguntas.count(i)  
        casa_ganadora = i

print(contador)
print(casa_ganadora)
#elijo casa
 

if   casa_ganadora==1:  
    print("Tu casa será Griffindor")
elif casa_ganadora==2:
    print("Tu casa será Slytherin")
elif casa_ganadora==3:  
    print("Tu casa será Hufflepuff")
elif casa_ganadora==4 : 
    print("Tu casa será Ravenclaw")