from colorama import Fore, Back, Style


class bricks:
    def __init__(self, x, y):
        self.type = "brick"
        self.pos = [x, y]


class uBricks(bricks):
    def __init__(self, x, y):
        self.brick = "ub"
        self.c = "x"
        self.style = Fore.WHITE
        bricks.__init__(self, x, y)


class bBricks(bricks):
    def __init__(self, x, y):
        self.style = Fore.CYAN
        self.brick = "b"
        self.c = "o"
        bricks.__init__(self, x, y)


class pBricks(bricks):
    def __init__(self, x, y):
        self.brick = "p"
        self.c = "?"
        self.style = Fore.BLUE
        bricks.__init__(self, x, y)


class iBricks(bricks):
    def __init__(self, x, y):
        self.brick = "i"
        self.c = " "
        self.style = Fore.YELLOW
        bricks.__init__(self, x, y)


class cBricks(bricks):
    def __init__(self, x, y):
        self.brick = "b"
        self.c = "C"
        self.style = Fore.YELLOW
        bricks.__init__(self, x, y)


class Mushrooms(bricks):
    def __init__(self, x, y):
        self.c = "M"
        self.d = 1
        self.count = 0
        self.style = Fore.GREEN
        bricks.__init__(self, x, y)


class Coins(bricks):
    def __init__(self, x, y):
        self.c = "$"
        self.style = Fore.YELLOW
        bricks.__init__(self, x, y)


class flag(bricks):
    def __init__(self, x, y):
        self.c = "*"
        self.style = Fore.MAGENTA
        bricks.__init__(self, x, y)


class cloth(bricks):
    def __init__(self, x, y):
        self.c = ")"
        self.style = Fore.RED
        self.d = 0
        bricks.__init__(self, x, y)


class bulletBricks(bricks):
    def __init__(self, x, y):
        self.c = "B"
        self.style = Fore.GREEN
        bricks.__init__(self, x, y)
