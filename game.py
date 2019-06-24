import board
from colorama import Fore, Back, Style
import os
import time
import sys
import random as r
import signal
import termios
import errno
from functools import wraps
import players
TERMIOS = termios
timeout_value = 0.1


def timeout(seconds, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise Exception(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.setitimer(signal.ITIMER_REAL, seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return wraps(func)(wrapper)
    return decorator


@timeout(0.05)
def getkey():
    start = time.time()
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c


def printing():
    time.sleep(0.05)
    os.system('clear')
    print("Mario Game")
    for i in range(0, 31):
        for j in range(0, 100):
            print (gamer.board_req.style[j][i] + gamer.board_req.arr[j][i], end='')
        print()
    print("Score:" + str(gamer.score))
    print("Lives:", gamer.Lives)
    print("Level:", gamer.Level)


def levelcomplete():
    print(Fore.CYAN + "Level Completed")
    print(Fore.RED + "Score:" + str(gamer.score))
    print(Fore.RED + "Lives Left:" + str(gamer.Lives))
    time.sleep(3)


def Gamecomplete():
    print(Fore.CYAN + "Game Completed")
    print(Fore.RED + "Score:" + str(gamer.score))
    print(Fore.MAGENTA + "Completed the game with Lives Left:" + str(gamer.Lives))
    time.sleep(3)
    sys.exit()

########Game class Contains Lives Levels########


class Game:
    def __init__(self):
        self.score = 0
        self.Lives = 3
        self.Time = 0
        self.end = 0
        self.Level = 1
        self.timer = 0
        self.pr = players.Player1(1, 24)
        self.board_req = board.board(self.Level)

    def reducelife(self):
        gamer.Lives = gamer.Lives - 1
        gamer.board_req = board.board(gamer.Level)
        gamer.board_req.mapstart(gamer.Level)
        if gamer.Lives == 0:
            gamer.end = 1
        gamer.board_req.resetposition(gamer.pr)
        gamer.pr = players.Player1(1, 24)
        gamer.board_req.maps = 0
        gamer.board_req.mapset()
        gamer.board_req.fillposition(gamer.pr)
        os.system('clear')
        print(Fore.RED + "You Lost a Life")
        print(Fore.RED + "You Have " + str(gamer.Lives) + " Left")
        time.sleep(1)


gamer = Game()
gamer.board_req.mapstart(gamer.Level)
gamer.board_req.mapset()
gamer.board_req.fillposition(gamer.pr)


printing()
x = 1


def keyget():
    try:
        k = getkey()
    except BaseException:
        k = None

    if k == b'd':
        gamer.board_req.resetposition(gamer.pr)
        cd = gamer.board_req.checkright(gamer.pr)
        if cd == 1:
            gamer.pr.moveright()

        elif cd == 2:
            gamer.pr.moveright()
            gamer.score += 1

        elif cd == 3:
            gamer.pr.moveright()
            gamer.pr = players.Player2(gamer.pr.pos[0][0], gamer.pr.pos[0][1])

        elif cd == 4:
            if gamer.pr.p == "p1":
                gamer.reducelife()
            else:
                gamer.pr = players.Player1(
                    gamer.pr.pos[0][0], gamer.pr.pos[0][1])
        elif cd == 6:
            if gamer.pr.p == "p2":
                gamer.pr.b = 1

        if gamer.pr.move == 1:
            gamer.board_req.mapreset()
            gamer.pr.move = 0
        gamer.board_req.fillposition(gamer.pr)

    elif k == b'a':
        gamer.board_req.resetposition(gamer.pr)
        cd = gamer.board_req.checkleft(gamer.pr)
        if cd == 1:
            gamer.pr.moveleft()
        elif cd == 2:
            gamer.pr.moveleft()
            gamer.score += 1
        elif cd == 3:
            gamer.pr.moveleft()
            gamer.pr = players.Player2(gamer.pr.pos[0][0], gamer.pr.pos[0][1])
        elif cd == 4:
            if gamer.pr.p == "p1":
                gamer.reducelife()
            else:
                gamer.pr = players.Player1(
                    gamer.pr.pos[0][0], gamer.pr.pos[0][1])
        elif cd == 6:
            if gamer.pr.p == "p2":
                gamer.pr.b = 1

        gamer.board_req.fillposition(gamer.pr)
        printing()

    elif k == b's':
        if gamer.pr.b == 1:
            gamer.board_req.makeBullets(
                gamer.pr.pos[0][0] + 1 + gamer.board_req.maps,
                gamer.pr.pos[2][1])

    elif k == b'q':
        gamer.end = 1

    elif k == b'w':
        gamer.board_req.resetposition(gamer.pr)
        if gamer.pr.j == 0 and not gamer.board_req.checkdown(gamer.pr):
            gamer.pr.jump()
        gamer.board_req.fillposition(gamer.pr)
        printing()


def mushroom():
    if gamer.board_req.Mrp is not None:
        gamer.board_req.mMushroom()
        gamer.board_req.fillposition(gamer.pr)


def enemies():
    if gamer.board_req.enemies != []:
        gamer.board_req.mEnemy()
        gamer.board_req.mBoss()
        gamer.board_req.fillposition(gamer.pr)


def Bullets():
    if gamer.board_req.bullets != []:
        gamer.board_req.mBullets()
        gamer.board_req.fillposition(gamer.pr)


def game():
    keyget()
    Bullets()
    enemies()
    cd = gamer.board_req.checkleft(gamer.pr)
    if cd == 2:
        gamer.score += 1

    if cd == 3:
        gamer.pr = players.Player2(gamer.pr.pos[0][0], gamer.pr.pos[0][1])
        gamer.board_req.fillposition(gamer.pr)

    if cd == 4:
        if gamer.pr.p == "p1":
            gamer.reducelife()
        else:
            gamer.pr = players.Player1(gamer.pr.pos[0][0], gamer.pr.pos[0][1])
            gamer.pr.moveleft()
            gamer.pr.moveleft()
    if cd == 6:
        if gamer.pr.p == "p2":
            gamer.pr.b = 1

    cd = gamer.board_req.checkright(gamer.pr)
    if cd == 2:
        gamer.score += 1

    if cd == 3:
        gamer.pr = players.Player2(gamer.pr.pos[0][0], gamer.pr.pos[0][1])
        gamer.board_req.fillposition(gamer.pr)

    if cd == 4:
        if gamer.pr.p == "p1":
            gamer.reducelife()
        else:
            gamer.pr = players.Player1(gamer.pr.pos[0][0], gamer.pr.pos[0][1])
            gamer.pr.moveright()
            gamer.pr.moveright()
    if cd == 5:
        gamer.board_req.resetposition(gamer.pr)
        gamer.pr.moveright()
        if gamer.pr.move == 1:
            gamer.board_req.mapreset()
            gamer.pr.move = 0

        gamer.pr.moveright()
        if gamer.pr.move == 1:
            gamer.board_req.mapreset()
            gamer.pr.move = 0

        gamer.pr.moveright()
        if gamer.pr.move == 1:
            gamer.board_req.mapreset()
            gamer.pr.move = 0

        gamer.board_req.fillposition(gamer.pr)

    if cd == 6:
        if gamer.pr.p == "p2":
            gamer.pr.b = 1

    cd = gamer.board_req.checkdown(gamer.pr)
    if gamer.pr.j == 0:
        if cd == 1:
            gamer.board_req.resetposition(gamer.pr)
            go = gamer.pr.movedown()
            if go == 1:
                gamer.reducelife()
                if gamer.Lives == 0:
                    gamer.end = 1
                return
            else:
                gamer.board_req.fillposition(gamer.pr)
                printing()

        elif cd == 2:
            gamer.board_req.resetposition(gamer.pr)
            gamer.pr.movedown()
            gamer.score += 1
            gamer.board_req.fillposition(gamer.pr)

        elif cd == 3:
            gamer.board_req.resetposition(gamer.pr)
            gamer.pr.movedown()
            pr = players.Player2(gamer.pr.pos[0][0], gamer.pr.pos[0][1])
            gamer.board_req.fillposition(gamer.pr)

    elif gamer.pr.j < 6:
        if gamer.board_req.checkup(gamer.pr):
            gamer.board_req.resetposition(gamer.pr)
            gamer.pr.jump()
            gamer.board_req.fillposition(gamer.pr)
        else:
            gamer.pr.j = 0
    elif gamer.pr.j == 6:
        gamer.pr.j = 0
        gamer.pr.count = 0

    mushroom()

    if gamer.pr.pos[0][0] + gamer.board_req.maps > 382 and gamer.pr.pos[0][0] + \
            gamer.board_req.maps < 399:
        gamer.board_req.resetposition(gamer.pr)
        gamer.pr.moveright()
        if gamer.pr.move == 1:
            gamer.board_req.mapreset()
            gamer.pr.move = 0
        gamer.board_req.fillposition(gamer.pr)

    if gamer.pr.pos[0][0] + gamer.board_req.maps == 399:
        if gamer.Level == 1:
            gamer.Level = 2
            os.system('clear')
            levelcomplete()
            gamer.board_req = board.board(gamer.Level)
            gamer.board_req.maps = 0
            gamer.board_req.mapstart(gamer.Level)
            gamer.board_req.mapset()
            if gamer.pr.p == "p1":
                gamer.pr = players.Player1(1, 24)
            else:
                if gamer.pr.b == 0:
                    gamer.pr = players.Player2(1, 24)
                else:
                    gamer.pr = players.Player2(1, 24)
            gamer.board_req.fillposition(gamer.pr)
        else:
            if gamer.board_req.boss == []:
                os.system('clear')
                Gamecomplete()

    printing()


while gamer.end == 0:
    if gamer.timer == 0:
        game()
    gamer.timer = (gamer.timer + 1) % 20
