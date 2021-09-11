class Reina:

    def __init__(self, x, y):
        self.posicio=[0,0]
        self.posicio[0] = x
        self.posicio[1] = y

    def getPosicio(self):
        return self.posicio

    def mata(self, reina2):
        pos1 = self.getPosicio()
        pos2 = reina2.getPosicio()
        if pos1[0] == pos2[0] or pos1[1] == pos2[1] or self.mismaDiagonal(reina2):
            return True
        else:
            return False

    def mismaDiagonal(self, reina2):
        pos1 = self.getPosicio()
        pos2 = reina2.getPosicio()

        return abs(pos1[1]-pos2[1]) == abs(pos1[0] - pos2[0])

    def mostrarReina(self, sizeTablero, sizePantalla, canvas):
        prop = sizePantalla/sizeTablero

        canvas.create_oval((self.posicio[0])*prop, (self.posicio[1])*prop, (self.posicio[0]+1)*prop,
                           (self.posicio[1]+1)*prop, outline="#000000", fill="#f000f0")

    def __str__(self):
        return "Reina[" + str(self.posicio[0]) + ", " + str(self.posicio[1]) + "]"
