def devolver_distintos(num1, num2, num3):
    '''
    Crea una función lamada devolver_distintos() que reciba 3 integers como parámetros.
    Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.
    Si la suma de los 3 numeros es menor a 10, va a devolver el número menor. Si la suma de los 3 números
    es un valor entre 10 y 15 (incluidos) va a devolver el número de valor intermedio
    '''
    suma = num1 + num2 + num3
    if suma>15:
        return max(num1, num2, num3)
    elif suma < 10:
        return min(num1, num2, num3)
    else:
        return num2


def palabraLista (palabra):
    '''
    Escribe una función(puedes ponerle cualquier nombre que quieras) que reciba
    cualquier palabra como parámetro, y que devuelva todas sus letras únicas(sin repetir) pero
    en orden alfabético. Por ejemplo si al invocar esta función pasamos la palabra "entretenido", debería
    devolver['d', 'e', 'i', 'n', 'o', 'r', 't']
    '''
    lista=[]
    for letra in palabra.lower():
        if letra not in lista:
            lista.append(letra)
    lista.sort()
    return lista

def numeroRepetido (*args):
    '''
    Escribe una función que requiera una cantidad indefinida de argumentos.Lo que hará esta función es
     devolver True si en algún momento se ha ingresado al numero cero repetido dos veces consecutivas.
    Por ejemplo:
    (5, 6, 1, 0, 0, 9, 3, 5) >> > True
    (6, 0, 5, 1, 0, 3, 0, 1) >> > False
    '''
    lista=list(args)
    for n in range(len(lista)):
        if lista[n] == 0 and lista[n+1] == 0:
            return True
    return False

def contar_primos(numero):
    '''
    Escribe una función llamada contar_primos() que requiera un solo argumento numérico. Esta función va a mostrar en pantalla todos
    los números primos existentes en el rango que va desde cero hasta ese número incluido, y va a devolver la cantidad de
    números primos que encontró. Aclaración, por convención el 0 y el 1 no se consideran primos.
    '''
    contador = 0
    for n in range(2, numero + 1):
        if es_primo(n):
            print(n)
            contador += 1
    return contador

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True