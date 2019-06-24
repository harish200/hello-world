from bricks import bricks
from colorama import Fore, Back, Style


class Enemy(bricks):
    def __init__(self, x, y, v):
        self.c = "e"
        self.d = 1
        self.count = 0
        self.vel = v
        self.style = Fore.RED
        bricks.__init__(self, x, y)


class Boss(bricks):
    def __init__(self, x, y):
        self.c = "E"
        self.d = 1
        self.style = Fore.GREEN
        self.lives = 3
        bricks.__init__(self, x, y)


class bullet(bricks):
    def __init__(self, x, y):
        self.c = "-"
        self.style = Fore.GREEN
        bricks.__init__(self, x, y)
