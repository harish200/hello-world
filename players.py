from colorama import Fore, Back, Style


class Player:
    def __init__(self):
        self.type = "player"
        self.move = 0
        self.j = 0
        self.b = 0
        self.count = 0
        self.style = Fore.YELLOW


class Player1(Player):
    def __init__(self, x, y):
        self.p = "p1"
        self.c = ["O", "i"]
        self.pos = [[x, y], [x, y + 1]]
        Player.__init__(self)

    def moveright(self):
        if self.pos[0][0] < 50:
            self.pos[0][0] += 1
            self.pos[1][0] += 1
        else:
            self.move = 1

    def moveleft(self):
        if self.pos[0][0] > 1:
            self.pos[0][0] -= 1
            self.pos[1][0] -= 1

    def movedown(self):
        if self.pos[1][1] < 29:
            self.pos[0][1] += 1
            self.pos[1][1] += 1
            return 0
        else:
            return 1

    def jump(self):
        self.pos[0][1] -= 1
        self.pos[1][1] -= 1
        self.j += 1


class Player2(Player):
    def __init__(self, x, y):
        self.p = "p2"
        self.c = ["O", "I", "I"]
        self.style = Fore.YELLOW
        self.b = 0
        self.pos = [[x, y - 1], [x, y], [x, y + 1]]
        Player.__init__(self)

    def moveright(self):
        if self.pos[0][0] < 50:
            self.pos[0][0] += 1
            self.pos[1][0] += 1
            self.pos[2][0] += 1
        else:
            self.move = 1

    def moveleft(self):
        if self.pos[0][0] > 1:
            self.pos[0][0] -= 1
            self.pos[1][0] -= 1
            self.pos[2][0] -= 1

    def movedown(self):
        if self.pos[2][1] < 29:
            self.pos[0][1] += 1
            self.pos[1][1] += 1
            self.pos[2][1] += 1
            return 0
        else:
            return 1

    def jump(self):
        self.pos[0][1] -= 1
        self.pos[1][1] -= 1
        self.pos[2][1] -= 1
        self.j += 1
