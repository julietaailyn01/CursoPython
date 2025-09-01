import random
nombre=input("Ingresa tu nombre: ")
numeroRandom=random.randint(1,100)
print(f"Bueno, {nombre}, he pensado un número entre el 1 y el 100 y tienes solo ocho intentos para adivinar cuál crees que es el número")

for i in range(1,9):
    numeroElegido=int(input("Elige un numero del 1 al 100: "))
    while numeroElegido<1 or numeroElegido>100:
        numeroElegido=input("Ha elegido un número que no está permitido, vuelve a intentarlo")
    if i == 8 and numeroElegido!=numeroRandom:
        print(f"Lo siento, no has podido encontrar el numero. El número secreto era {numeroRandom}")
    elif numeroRandom > numeroElegido:
        print("Lo siento, su respuesta es incorrecta, has elegido un número menor al número secreto, vuelve a intentarlo")
    elif numeroRandom < numeroElegido:
        print("Lo siento, su respuesta es incorrecta, has elegido un número mayor al número secreto, vuelve a intentarlo")
    else:
        print(f"Has ganado! el número secreto era {numeroRandom}, te ha llevado {i} intentos ")
        break