import map
import enemies
import sys
from colorama import Fore, Back, Style
map_req = map.map1()


class board:
    def __init__(self, level):
        self.arr = [[' ' for i in range(0, 31)] for j in range(0, 120)]
        self.style = [[Fore.YELLOW for i in range(
            0, 31)] for j in range(0, 120)]
        self.maps = 0
        self.Mrp = None
        self.enemies = []
        self.bullets = []
        self.flag = [382, 10]
        self.boss = []
        self.makeEnemies(level)
        self.bossEnemies(level)
        for i in range(self.maps, self.maps + 100):
            for j in range(0, 31):
                self.arr[i - self.maps][j] = map_req.arr[i][j].c
                self.style[i - self.maps][j] = map_req.arr[i][j].style
        for i in range(0, 100):
            self.arr[i][0] = "~"
        for i in range(0, 30):
            self.arr[0][i] = "|"
        for i in range(0, 100):
            self.arr[i][30] = "~"
        for i in range(0, 30):
            self.arr[99][i] = "|"

    def fillposition(self, player):
        x = player.pos[0][0]
        y = player.pos[0][1]

        if player.p == "p1":
            self.arr[x][y] = "O"
            self.arr[x][y + 1] = "i"
        elif player.p == "p2":
            self.arr[x][y] = "O"
            self.arr[x][y + 1] = "I"
            self.arr[x][y + 2] = "I"

    def resetposition(self, player):
        x = player.pos[0][0]
        y = player.pos[0][1]

        if player.p == "p1":
            self.arr[x][y] = " "
            self.arr[x][y + 1] = " "
            return 1
        elif player.p == "p2":
            self.arr[x][y] = " "
            self.arr[x][y + 1] = " "
            self.arr[x][y + 2] = " "
            return 0

    def checkdown(self, player):
        if player.p == "p1":
            x = player.pos[1][0]
            y = player.pos[1][1]
        else:
            x = player.pos[2][0]
            y = player.pos[2][1]

        if self.arr[x][y + 1] == " " or self.arr[x][y + 1] == "~":
            return 1
        elif self.arr[x][y + 1] == "$":
            map_req.resetblock(x, y + 1, self.maps)
            return 2
        elif self.arr[x][y + 1] == "M":
            self.rMushroom(x, y + 1)
            return 3
        elif self.arr[x][y + 1] == "e":
            for i in range(0, len(self.enemies)):
                if x + \
                        self.maps == self.enemies[i].pos[0] and y == self.enemies[i].pos[1] - 1:
                    map_req.resetenemy(
                        self.enemies[i].pos[0],
                        self.enemies[i].pos[1])
                    break
            self.rEnemy(i)
            return 2
        elif self.arr[x][y + 1] == "E":
            for i in range(0, len(self.boss)):
                if x + \
                        self.maps == self.boss[i].pos[0] and y == self.boss[i].pos[1] - 1:
                    self.boss[i].lives -= 1
                    if self.boss[i].lives == 0:
                        map_req.resetenemy(
                            self.boss[i].pos[0], self.boss[i].pos[1])
                        self.rBoss(i)
                    break
        elif self.arr[x][y + 1] == "B":
            return 6
        else:
            return 0

    def checkright(self, player):
        x = player.pos[0][0]
        y = player.pos[0][1]
        if player.p == "p1":
            if self.arr[x + 1][y] == " " and self.arr[x + 1][y + 1] == " ":
                return 1
            elif self.arr[x + 1][y + 1] == "$":
                map_req.resetblock(x + 1, y + 1, self.maps)
                return 2
            elif self.arr[x + 1][y + 1] == "M":
                self.rMushroom()
                return 3
            elif self.arr[x + 1][y + 1] == "e" or self.arr[x + 1][y + 1] == "E":
                if map_req.arr[x + 1 + self.maps][y + 1].d == 1:
                    return 4
                else:
                    return 1
            elif self.arr[x + 1][y + 1] == "*":
                if self.boss == []:
                    m = self.resetflag()
                    if m == 2:
                        return 5

            elif self.arr[x + 1][y + 1] == "B":
                map_req.resetblock(x + 1, y + 2, self.maps)
                return 6

        else:
            if self.arr[x + 1][y] == " " and self.arr[x + 1][y +
                                                             1] == " " and self.arr[x + 1][y + 2] == " ":
                return 1
            elif self.arr[x + 1][y + 2] == "$":
                map_req.resetblock(x + 1, y + 2, self.maps)
                return 2
            elif self.arr[x + 1][y + 2] == "M":
                self.rMushroom()
                return 3
            elif self.arr[x + 1][y + 2] == "e" or self.arr[x + 1][y + 2] == "E":
                if map_req.arr[x + 1 + self.maps][y + 2].d == 1:
                    return 4
                else:
                    return 1
            elif self.arr[x + 1][y + 2] == "*":
                if self.boss == []:
                    sys.exit()
                    m = self.resetflag()
                    if m == 2:
                        return 5

            elif self.arr[x + 1][y + 2] == "B":
                map_req.resetblock(x + 1, y + 2, self.maps)
                return 6

        return 0

    def checkleft(self, player):
        x = player.pos[0][0]
        y = player.pos[0][1]
        if player.p == "p1":
            if self.arr[x - 1][y] == " " and self.arr[x - 1][y + 1] == " ":
                return 1
            elif self.arr[x - 1][y + 1] == "$":
                map_req.resetblock(x - 1, y + 1, self.maps)
                return 2
            elif self.arr[x - 1][y + 1] == "M":
                self.rMushroom()
                return 3
            elif self.arr[x - 1][y + 1] == "e" or self.arr[x - 1][y + 1] == "E":
                if map_req.arr[x - 1 + self.maps][y + 1].d == 0:
                    return 4
                else:
                    return 1
            elif self.arr[x - 1][y + 1] == "B":
                map_req.resetblock(x - 1, y + 1, self.maps)
                return 6
        else:
            if self.arr[x - 1][y] == " " and self.arr[x - 1][y +
                                                             1] == " " and self.arr[x - 1][y + 2] == " ":
                return 1
            elif self.arr[x - 1][y + 2] == "$":
                map_req.resetblock(x - 1, y + 2, self.maps)
                return 2
            elif self.arr[x - 1][y + 2] == "M":
                self.rMushroom()
                return 3
            elif self.arr[x - 1][y + 2] == "e" or self.arr[x - 1][y + 2] == "E":
                if map_req.arr[x - 1 + self.maps][y + 2].d == 0:
                    return 4
                else:
                    return 1
            elif self.arr[x - 1][y + 2] == "B":
                map_req.resetblock(x - 1, y + 2, self.maps)
                return 6
        return 0

    def checkup(self, player):
        x = player.pos[0][0]
        y = player.pos[0][1]
        if self.arr[x][y - 1] == " ":
            self.req = 0
            return 1
        else:
            self.req += 1
            if self.arr[x][y - 1] == "o":
                map_req.resetblock(x, y - 1, self.maps)
                self.mapset()
            elif self.arr[x][y - 1] == "C":
                map_req.setcoin(x, y - 2, self.maps)
                self.mapset()
            elif self.arr[x][y - 1] == "?":
                if player.p == "p1":
                    self.Mrp = map_req.setmr(x + self.maps, y - 2)
                elif player.p == "p2":
                    map_req.setbb(x + self.maps, y - 2)
                map_req.setbr(x, y - 1, self.maps)
                self.mapset()
            return 0

    def mapreset(self):
        self.maps += 1
        for i in range(self.maps, 100 + self.maps):
            for j in range(0, 31):
                self.arr[i - self.maps][j] = map_req.arr[i][j].c
                self.style[i - self.maps][j] = map_req.arr[i][j].style

        for i in range(0, 100):
            self.arr[i][0] = "~"
        for i in range(0, 30):
            self.arr[0][i] = "|"
        for i in range(0, 100):
            self.arr[i][30] = "~"
        for i in range(0, 30):
            self.arr[99][i] = "|"

    def mapset(self):
        for i in range(self.maps, 100 + self.maps):
            for j in range(0, 31):
                self.arr[i - self.maps][j] = map_req.arr[i][j].c
                self.style[i - self.maps][j] = map_req.arr[i][j].style

        for i in range(0, 100):
            self.arr[i][0] = "~"
        for i in range(0, 30):
            self.arr[0][i] = "|"
        for i in range(0, 100):
            self.arr[i][30] = "~"
        for i in range(0, 30):
            self.arr[99][i] = "|"

    def mMushroom(self):
        if self.Mrp.count == 0:
            if map_req.arr[self.Mrp.pos[0]][self.Mrp.pos[1] + 1].c == " ":
                map_req.resetmushroom(self.Mrp.pos[0], self.Mrp.pos[1])
                if self.Mrp.pos[1] < 28:
                    self.Mrp = map_req.setmr(
                        self.Mrp.pos[0], self.Mrp.pos[1] + 1)
                else:
                    self.rMushroom()

            if self.Mrp.d == 0:
                if map_req.arr[self.Mrp.pos[0] + 1][self.Mrp.pos[1]].c == " ":
                    map_req.resetmushroom(self.Mrp.pos[0], self.Mrp.pos[1])
                    self.Mrp = map_req.setmr(
                        self.Mrp.pos[0] + 1, self.Mrp.pos[1])
                    self.Mrp.d = 0
                else:
                    self.Mrp.d = 1
            elif self.Mrp.d == 1:
                if map_req.arr[self.Mrp.pos[0] - 1][self.Mrp.pos[1]].c == " ":
                    map_req.resetmushroom(self.Mrp.pos[0], self.Mrp.pos[1])
                    self.Mrp = map_req.setmr(
                        self.Mrp.pos[0] - 1, self.Mrp.pos[1])
                    self.Mrp.d = 1
                else:
                    self.Mrp.d = 0
        self.Mrp.count = (self.Mrp.count + 1) % 2
        self.mapset()

    def rMushroom(self):
        if self.Mrp is not None:
            map_req.resetmushroom(self.Mrp.pos[0], self.Mrp.pos[1])
            self.Mrp = None
            self.mapset()

    def mEnemy(self):
        for i in range(0, len(self.enemies)):
            if self.enemies[i].count == 0:
                if map_req.arr[self.enemies[i].pos[0]
                               ][self.enemies[i].pos[1] + 1].c == " ":
                    map_req.resetenemy(
                        self.enemies[i].pos[0],
                        self.enemies[i].pos[1])
                    self.enemies[i] = map_req.setenemy(
                        self.enemies[i].pos[0], self.enemies[i].pos[1] + 1, self.enemies[i].vel)
                if self.enemies[i].d == 0:
                    if map_req.arr[self.enemies[i].pos[0] +
                                   1][self.enemies[i].pos[1]].c == " ":
                        map_req.resetenemy(
                            self.enemies[i].pos[0], self.enemies[i].pos[1])
                        self.enemies[i] = map_req.setenemy(
                            self.enemies[i].pos[0] + 1, self.enemies[i].pos[1], self.enemies[i].vel)
                        self.enemies[i].d = 0
                    else:
                        self.enemies[i].d = 1
                elif self.enemies[i].d == 1:
                    if map_req.arr[self.enemies[i].pos[0] -
                                   1][self.enemies[i].pos[1]].c == " ":
                        map_req.resetenemy(
                            self.enemies[i].pos[0], self.enemies[i].pos[1])
                        self.enemies[i] = map_req.setenemy(
                            self.enemies[i].pos[0] - 1, self.enemies[i].pos[1], self.enemies[i].vel)
                        self.enemies[i].d = 1
                    else:
                        self.enemies[i].d = 0
            self.enemies[i].count = (
                self.enemies[i].count + 1) % self.enemies[i].vel
        self.mapset()

    def rEnemy(self, i):
        self.enemies.pop(i)
        self.mapset()

    def makeEnemies(self, level):
        if level == 1:
            self.enemies.append(map_req.setenemy(80, 25, 4))
            self.enemies.append(map_req.setenemy(133, 25, 4))
            self.enemies.append(map_req.setenemy(145, 25, 2))
            self.enemies.append(map_req.setenemy(260, 25, 3))
            self.enemies.append(map_req.setenemy(311, 20, 1))
            self.mapset()
        if level == 2:
            self.enemies.append(map_req.setenemy(67, 25, 2))
            self.enemies.append(map_req.setenemy(80, 25, 1))
            self.enemies.append(map_req.setenemy(139, 25, 1))
            self.enemies.append(map_req.setenemy(208, 25, 2))
            self.enemies.append(map_req.setenemy(229, 20, 1))
            self.enemies.append(map_req.setenemy(210, 25, 1))
            self.enemies.append(map_req.setenemy(260, 25, 1))
            self.enemies.append(map_req.setenemy(265, 25, 2))
            self.enemies.append(map_req.setenemy(270, 25, 1))
        #    self.enemies.append(map_req.setenemy(139,25,1))

    def bossEnemies(self, level):
        if level == 2:
            self.boss.append(map_req.setboss(374, 25))

    def mBoss(self):
        for i in range(0, len(self.boss)):
            if map_req.arr[self.boss[i].pos[0]
                           ][self.boss[i].pos[1] + 1].c == " ":
                map_req.resetenemy(self.boss[i].pos[0], self.boss[i].pos[1])
                self.boss[i] = map_req.setboss(
                    self.boss[i].pos[0], self.boss[i].pos[1] + 1)
            if self.boss[i].d == 0:
                if map_req.arr[self.boss[i].pos[0] +
                               1][self.boss[i].pos[1]].c == " ":
                    map_req.resetenemy(
                        self.boss[i].pos[0], self.boss[i].pos[1])
                    self.boss[i] = map_req.setboss(
                        self.boss[i].pos[0] + 1, self.boss[i].pos[1])
                    self.boss[i].d = 0
                else:
                    self.boss[i].d = 1
            elif self.boss[i].d == 1:
                if map_req.arr[self.boss[i].pos[0] -
                               1][self.boss[i].pos[1]].c == " ":
                    map_req.resetenemy(
                        self.boss[i].pos[0], self.boss[i].pos[1])
                    self.boss[i] = map_req.setboss(
                        self.boss[i].pos[0] - 1, self.boss[i].pos[1])
                    self.boss[i].d = 1
                else:
                    self.boss[i].d = 0
        self.mapset()

    def mapstart(self, i):
        global map_req
        if i == 1:
            map_req = map.map1()
        elif i == 2:
            map_req = map.map2()

    def resetflag(self):
        map_req.resetflag(self.flag)
        if self.flag[1] < 25:
            self.flag[1] += 1
            return 1
        else:
            return 2
        self.mapset()

    def makeBullets(self, x, y):
        self.bullets.append(map_req.setbullet(x, y))
        self.mapset()

    def mBullets(self):
        f = 0
        rm = []
        for i in range(0, len(self.bullets)):
            if map_req.arr[self.bullets[i].pos[0] +
                           1][self.bullets[i].pos[1]].c == " ":
                map_req.resetenemy(
                    self.bullets[i].pos[0],
                    self.bullets[i].pos[1])
                self.bullets[i] = map_req.setbullet(
                    self.bullets[i].pos[0] + 1, self.bullets[i].pos[1])
            elif map_req.arr[self.bullets[i].pos[0] + 1][self.bullets[i].pos[1]].c == "e":
                for j in range(0, len(self.enemies)):
                    if self.bullets[i].pos[0] + \
                            1 == self.enemies[j].pos[0] and self.bullets[i].pos[1] == self.enemies[j].pos[1]:
                        map_req.resetenemy(
                            self.enemies[j].pos[0], self.enemies[j].pos[1])
                        f = 1
                        map_req.resetenemy(
                            self.bullets[i].pos[0], self.bullets[i].pos[1])
                        rm.append(i)
                        break
                if f == 1:
                    self.rEnemy(j)
            else:
                map_req.resetenemy(
                    self.bullets[i].pos[0],
                    self.bullets[i].pos[1])
                rm.append(i)
        for i in range(0, len(rm)):
            self.rBullets(rm[i])
        self.mapset()

    def rBullets(self, i):
        self.bullets.pop(i)
        self.mapset()

    def rBoss(self, i):
        self.boss.pop(i)
        self.mapset()
