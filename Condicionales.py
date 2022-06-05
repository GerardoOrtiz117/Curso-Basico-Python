#Declaramos la variable
calificacion = input ("Introduce tu calificacion de la AZ-900: ")
#Todo lo que entra de teclado por el usuario es de tipo String por lo que en este caso queremos Int (enteros)

calificacion = int(calificacion)#Cambio ed tipo de variable


#Preguntamos si la calidficacion es menos de 700
if calificacion < 700 :
    print ("VEESSS, por no estudiar") #Si es menor a 700 muestra este mensaje
elif calificacion > 1000:
    print ("Mientes....El maximo son 1000")
else :
    print ("Felicidades.....Pasa por tu certificado prru :v") #si no se cumple el if anterior o cualquiera de los anteriores se ejecuta esta linea


#Verificador de edad
edad = input("Introduce tu edad ")
edad = int (edad)

if edad >= 18 and edad<= 100 :
        print("Bienvanido al Mamitas....")
elif edad >100 :
        print ("Si vienes acompañado de tus abuelitos, si te podemos fiar")
elif edad < 0 :
        print ("Ni que fueras viajero en el tiempo")
else :
        print("Tu no puedes ingresar")

#En Python no existe el switch case...
