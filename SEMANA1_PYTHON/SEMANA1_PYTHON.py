def ejer1():
    nombre = input("Ingrese su nombre: ")
    carrera = input("Ingrese su carrera: ")

    print(f"\n{nombre}, bienvenido al curso de fudamentos de algoritmo de la carrera {carrera}")

def ejer2():
    print("\"Keila\"")

def ejer3():
    num1 = int (input("Ingrese número 1: "))
    num2 = int (input("Ingrese número 2: "))
    
    print("suma: ", (num1 + num2))
    print("Resta: ", (num1 - num2))
    print("Multiplicacón: ", (num1 * num2))
    print("División: ", (num1 / num2))

from ast import Num
import math #importado libreria math

def ejer4():
    num = float(iput("Ingrese número decimal:"))
    
    raiz = math.sqrt(num)
    redo = round(num,2)
    cubo = math.pow(num,3)
    cubica = num ** (1/3)

    print("Raiz cuadrada: " raiz)
    print("redondeado: " redo)
    print("al cubo: " cubo)
    print("Raiz cuadrada: ", cubica)


ejer4()

