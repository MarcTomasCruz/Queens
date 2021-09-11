

class Casilla:

    def __init__(self, x, y):
        self.posx = x
        self.posy = y

    def getX(self):
        return self.posx

    def getY(self):
        return self.posy

    def mostraCasilla(self, sizeTablero, sizePantalla, relleno, canvas):
        prop = sizePantalla/sizeTablero
        canvas.create_rectangle((self.posx-1)*prop, (self.posy-1)*prop, self.posx*prop, self.posy*prop,
                                outline="#000000", fill=relleno)

    def __eq__(self, other):
        return (self.posx == other.getX()) and (self.posy == other.getY())

    def __str__(self):
        return "[" + str(self.posx) + ", " + str(self.posy) + "]"
