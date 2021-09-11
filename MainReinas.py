from tkinter import Tk, Canvas, Frame, BOTH
from Tablero import Tablero
from Reina import Reina


def main():

    pantalla = 700
    tamano = int(input("Introduce el tamaño del tablero: "))
    reinax = int(input("Introduce la columna de la reina inicial: "))
    reinay = int(input("Introduce la fila de la reina inicial: "))
    reina = Reina(reinax, reinay)
    reinas = []
    reinas.append(reina)
    ex = Tablero(tamano, pantalla, True, reinas, False, None)
    if len(ex.reinas) != tamano:
        print("No existe ninguna solucion")
    ex.mainloop()





if __name__ == '__main__':
    main()