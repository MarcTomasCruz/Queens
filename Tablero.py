from tkinter import Tk, Canvas, Frame, BOTH
from Casilla import Casilla
from Reina import Reina


class Tablero(Frame):

    solucionsTrobades=0

    def __init__(self, n, pantalla, reinas, reinaInicial):
        super().__init__()
        self.size = n
        self.solucions = []
        self.sizePantalla = pantalla
        self.casillas=[]
        self.canvas = Canvas(self)
        for i in range(1, self.size+1):
            for j in range(1, self.size+1):
                casilla = Casilla(i, j)
                self.casillas.append(casilla)
        if reinas:
            self.reinas = self.backtrackingReinas(0, reinaInicial)

        self.initUI(reinas)


    def initUI(self, reinas):
        self.master.title("Tablero")
        self.pack(fill=BOTH, expand=1)
        for casilla in self.casillas:
            relleno = "#000000"

            i = casilla.getX()
            j = casilla.getY()
            if (i + j) % 2 == 1:
                relleno = "#ffffff"
            casilla.mostraCasilla(self.size, self.sizePantalla, relleno, self.canvas)

            if reinas:
                for reina in self.reinas:
                    reina.mostrarReina(self.size, self.sizePantalla, self.canvas)

        self.canvas.pack(fill=BOTH, expand=1)

   

    def backtrackingReinas(self, fila, reinas):

        if len(reinas) == self.size:
            return reinas

        else:
            if self.tieneReina(fila, reinas):
                self.backtrackingReinas(fila + 1, reinas)
            else:
                for i in range(0, self.size):
                        reinaNueva = Reina(fila, i)

                        if self.reinaColocable(reinaNueva, reinas):

                            reinas.append(reinaNueva)

                            reinasNuevas=self.backtrackingReinas(fila+1, reinas)

                            if len(reinasNuevas) != self.size:
                                reinasNuevas.pop(-1)

        return reinas


    def reinaColocable(self, reinaNueva, reinas):
        colocable = True
        i = 0

        while colocable and i < len(reinas):

            if reinas[i].mata(reinaNueva):
                colocable = False

            i += 1

        return colocable

    def tieneReina(self, fila, reinas):
        i = 0
        ocupado = False

        while not ocupado and i < len(reinas):
            ocupado = reinas[i].getPosicio()[0] == fila
            i += 1

        return ocupado

    def getCasilla(self, x, y):
        return Casilla(x, y)
