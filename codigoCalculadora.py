import numpy as np
import math as ma
import matplotlib.pyplot as plt

seleccion = 0
while seleccion != 8:
    print("\n")
    mylist = ['CALCULADORA', '1) Sumar', '2) Restar', '3) Multiplicar', '4) Dividir', '5) Raiz n', '6) Exponente n',
              '7) Seno', '8) SALIR']
    for x in mylist:
        print(x)
    seleccion = int(input("\nIndica la operación que requieres: "))

    if seleccion == 1:
        numeroUno = int(input("\nTeclea el primer numero: "))
        numeroDos = int(input("Teclea el segundo numero: "))
        print(f"\nLa suma de: {numeroUno} + {numeroDos} es = {numeroUno+numeroDos}")
    elif seleccion == 2:
        numeroUno = int(input("\nTeclea el primer numero: "))
        numeroDos = int(input("Teclea el segundo numero: "))
        print(f"\nLa resta de: {numeroUno} - {numeroDos} es = {numeroUno - numeroDos}")
    elif seleccion ==3:
        numeroUno = int(input("\nTeclea el primer numero: "))
        numeroDos = int(input("Teclea el segundo numero: "))
        print(f"\nLa multiplicacion de: {numeroUno} * {numeroDos} es = {numeroUno * numeroDos}")
    elif seleccion == 4:
        numeroUno = int(input("\nTeclea el primer numero: "))
        numeroDos = int(input("Teclea el segundo numero: "))
        print(f"\nLa division de: {numeroUno} / {numeroDos} es = {numeroUno / numeroDos}")
    elif seleccion == 5:
        numeroUno = int(input("\nTeclea un numero: "))
        resultado = pow(numeroUno, 1 / 2)
        resultado = numeroUno ** (0.5)
        np.sqrt(numeroUno)
        ma.sqrt(numeroUno)
        print(f"\nLa raiz cuadrada de: {numeroUno} es = {resultado} ")
    elif seleccion == 6:
        numeroUno = int(input("\nTeclea un numero: "))
        exponente = int(input("Indica que exponente quieres: "))
        print(f"\n{numeroUno} elevado a la {exponente} es = {numeroUno**exponente}")
    elif seleccion == 7:
        numeroUno = int(input("\nTeclea el primer numero: "))
        numeroDos = int(input("Teclea el segundo numero: "))

        def seno(valor):
            return np.sin(valor)

        a = numeroDos * np.pi
        espaciamiento = 15
        x = np.linspace(numeroUno, a, int(360 / espaciamiento + 1))
        f = seno(x)
        plt.plot(x, f)
        plt.plot(x, f, "o")  # Grafica los puntos
        plt.grid(True)  # Para la cuadricula
        plt.show()

    elif seleccion == 8:
       print("\n¡TERMINAMOS GRACIAS!")
       break