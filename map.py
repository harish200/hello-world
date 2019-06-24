import bricks
import enemies


class maps:
    def __init__(self):
        self.arr = [[bricks.iBricks(i, j) for i in range(0, 31)]
                    for j in range(0, 500)]
        self.k = 0

    def makemap(self, x, y, i):
        for j in range(x, y):
            self.makeblocks(j, i)

    def resetblock(self, x, y, l):
        self.l = x + l
        br = bricks.iBricks(x + l, y)
        self.arr[x + l][y] = br

    def makeblocks(self, x, i):

        if i == 1:
            self.makeuB(x)

        if i == 2:
            self.makeiB(x)

        if i == 3:
            self.maken0uB(x)

        if i == 4:
            self.maken0uB(x)
            self.maken1uB(x)

        if i == 5:
            self.makeupuB(x)

        if i == 6:
            self.makeup1uB(x)

        if i == 7:
            self.makeupbB(x)

        if i == 8:
            self.makeup1bB(x)

        if i == 9:
            self.makeupcB(x)

        if i == 10:
            self.makeuppB(x)

        if i == 11:
            self.maken0uB(x)
            self.maken1uB(x)
            self.maken2uB(x)

        if i == 12:
            self.maken0uB(x)
            self.maken1uB(x)
            self.maken2uB(x)
            self.maken3uB(x)

        if i == 13:
            self.makeupcB(x)
            self.makeup1pB(x)

        if i == 14:
            self.makeup0uB(x)

        if i == 15:
            self.maken0uB(x)
            self.maken1uB(x)
            self.maken2uB(x)
            self.maken3uB(x)
            self.maken4uB(x)

        if i == 16:
            self.maken0uB(x)
            self.maken1uB(x)
            self.maken2uB(x)
            self.maken3uB(x)
            self.maken4uB(x)
            self.maken5uB(x)

        if i == 17:
            self.makeuB(x + 1)
            self.makeuB(x + 2)
            self.makeflag(x + 1)
            self.maken0uB(x)
            self.maken0uB(x + 1)
            self.maken0uB(x + 2)

    def makeuB(self, x):
        for j in range(0, 4):
            br = bricks.uBricks(x, 29 - j)
            self.arr[x][29 - j] = br

    def makeupuB(self, x):
        self.arr[x][21] = bricks.uBricks(x, 21)

    def makeup1uB(self, x):
        self.arr[x][16] = bricks.uBricks(x, 16)

    def maken0uB(self, x):
        self.arr[x][25] = bricks.uBricks(x, 25)

    def maken1uB(self, x):
        self.arr[x][24] = bricks.uBricks(x, 24)

    def maken2uB(self, x):
        self.arr[x][23] = bricks.uBricks(x, 23)

    def maken3uB(self, x):
        self.arr[x][22] = bricks.uBricks(x, 22)

    def maken4uB(self, x):
        self.arr[x][21] = bricks.uBricks(x, 21)

    def maken5uB(self, x):
        self.arr[x][20] = bricks.uBricks(x, 20)

    def makeiB(self, x):
        for j in range(0, 4):
            self.arr[x][29 - j] = bricks.iBricks(x, 29 - j)

    def makeupiB(self, x):
        self.arr[x][21] = bricks.iBricks(x, 21)

    def makeup1iB(self, x):
        self.arr[x][16] = bricks.iBricks(x, 16)

    def makeup0uB(self, x):
        for i in range(0, 11):
            self.makeupuB(x + i)
            self.arr[x + i][16] = bricks.cBricks(x + i, 16)
        self.arr[x][20] = bricks.uBricks(x, 20)
        self.arr[x + i][20] = bricks.uBricks(x + i, 20)

    def makeupbB(self, x):
        self.arr[x][21] = bricks.bBricks(x, 21)

    def makeup1bB(self, x):
        self.arr[x][16] = bricks.bBricks(x, 16)

    def makeupcB(self, x):
        self.arr[x][21] = bricks.cBricks(x, 21)

    def makeuppB(self, x):
        self.arr[x][21] = bricks.pBricks(x, 21)

    def makeup1pB(self, x):
        self.arr[x][16] = bricks.pBricks(x, 16)

    def setcoin(self, x, y, i):
        self.arr[x + i][y] = bricks.Coins(x + i, y)
        self.arr[x + i][y + 1] = bricks.uBricks(x + i, y + 1)

    def setmr(self, x, y):
        br = bricks.Mushrooms(x, y)
        self.arr[x][y] = br
        return br

    def setbr(self, x, y, i):
        self.arr[x + i][y] = bricks.uBricks(x + i, y)

    def resetmushroom(self, x, y):
        self.arr[x][y] = bricks.iBricks(x, y)

    def setenemy(self, x, y, v):
        br = enemies.Enemy(x, y, v)
        self.arr[x][y] = br
        return br

    def resetenemy(self, x, y):
        self.arr[x][y] = bricks.iBricks(x, y)

    def makeflag(self, x):
        for i in range(10, 25):
            self.arr[x][i] = bricks.flag(x, i)
        br = bricks.cloth(x + 1, 10)
        self.arr[x + 1][10] = br
        return br

    def resetflag(self, ob):
        if ob[1] < 24:
            self.arr[ob[0]][ob[1]] = bricks.iBricks(ob[0], ob[1])
            self.arr[ob[0]][ob[1] + 1] = bricks.cloth(ob[0], ob[1] + 1)

    def setBr(self, x, y):
        self.arr[x][y] = bricks.uBricks(x, y)

    def makebBr(self, x1, x2, y):
        for i in range(x1, x2):
            self.arr[i][y] = bricks.bBricks(i, y)

    def makepBr(self, x1, x2, y):
        for i in range(x1, x2):
            self.arr[i][y] = bricks.pBricks(i, y)

    def setbb(self, x, y):
        self.arr[x][y] = bricks.bulletBricks(x, y)

    def setbullet(self, x, y):
        br = enemies.bullet(x, y)
        self.arr[x][y] = br
        return br

    def setboss(self, x, y):
        br = enemies.Boss(x, y)
        self.arr[x][y] = br
        return br

    def makecastle(self, x):
        self.makemap(x, x + 2, 16)
        self.makemap(x + 2, x + 4, 4)
        self.makemap(x + 4, x + 6, 16)
        self.makemap(x + 10, x + 12, 16)
        self.makemap(x + 12, x + 14, 4)
        self.makemap(x + 14, x + 16, 16)
        self.setBr(x + 2, 20)
        self.setBr(x + 2, 21)
        self.setBr(x + 3, 21)
        self.setBr(x + 3, 20)
        self.setBr(x + 12, 20)
        self.setBr(x + 12, 21)
        self.setBr(x + 13, 21)
        self.setBr(x + 13, 20)
        self.makebBr(x, x + 16, 19)
        self.makebBr(x + 2, x + 4, 18)
        self.makebBr(x + 2, x + 4, 17)
        self.makebBr(x + 2, x + 4, 16)
        self.makebBr(x + 12, x + 14, 18)
        self.makebBr(x + 12, x + 14, 17)
        self.makebBr(x + 12, x + 14, 16)
        self.makepBr(x + 2, x + 14, 15)
        self.makepBr(x + 4, x + 12, 14)
        self.makepBr(x + 6, x + 10, 13)


class map1(maps):
    def __init__(self):
        maps.__init__(self)
        self.makemap(0, 48, 1)
        self.makemap(51, 60, 1)
        self.makemap(60, 61, 3)
        self.makemap(62, 63, 4)
        self.makemap(64, 65, 4)
        self.makemap(66, 67, 3)
        self.makemap(80, 82, 5)
        self.makemap(82, 85, 9)
        self.makemap(85, 87, 10)
        self.makemap(87, 89, 7)
        self.makemap(89, 90, 8)
        self.makemap(96, 97, 3)
        self.makemap(98, 99, 4)
        self.makemap(100, 101, 4)
        self.makemap(102, 103, 3)
        self.makemap(51, 120, 1)
        self.makemap(120, 123, 2)
        self.makemap(130, 132, 4)
        self.makemap(140, 142, 11)
        self.makemap(150, 152, 12)
        self.makemap(160, 161, 9)
        self.makemap(166, 167, 13)
        self.makemap(172, 173, 9)
        self.makemap(180, 182, 4)
        self.makemap(190, 192, 11)
        self.makemap(200, 202, 12)
        self.makemap(210, 212, 11)
        self.makemap(220, 222, 4)
        self.makemap(228, 231, 5)
        self.makemap(232, 233, 9)
        self.makemap(234, 237, 5)
        self.makemap(250, 251, 7)
        self.makemap(251, 252, 9)
        self.makemap(252, 253, 7)
        self.makemap(253, 254, 9)
        self.makemap(254, 255, 7)
        self.makemap(270, 274, 12)
        self.makemap(274, 290, 1)
        self.makemap(290, 295, 5)
        self.makemap(295, 300, 6)
        self.makemap(123, 307, 1)
        self.makemap(307, 308, 14)
        self.makemap(330, 334, 11)
        self.makemap(320, 500, 1)
        self.makemap(350, 352, 3)
        self.makemap(352, 354, 4)
        self.makemap(354, 356, 11)
        self.makemap(356, 358, 12)
        self.makemap(358, 360, 15)
        self.makemap(360, 362, 16)
        self.makemap(380, 381, 17)
        self.makecastle(400)


class map2(maps):
    def __init__(self):
        maps.__init__(self)
        self.makemap(40, 45, 2)
        self.makemap(120, 125, 2)
        self.makemap(180, 185, 2)
        self.makemap(230, 235, 2)
        self.makemap(300, 305, 2)
        self.makemap(1, 40, 1)
        self.makemap(45, 120, 1)
        self.makemap(50, 54, 12)
        self.makemap(70, 74, 12)
        self.makemap(58, 59, 5)
        self.makemap(60, 61, 7)
        self.makemap(62, 63, 9)
        self.makemap(64, 65, 7)
        self.makemap(66, 67, 5)
        self.makemap(80, 85, 9)
        self.makemap(90, 93, 11)
        self.makemap(100, 103, 12)
        self.makemap(110, 113, 11)
        self.makemap(128, 130, 3)
        self.makemap(135, 137, 5)
        self.makemap(139, 140, 10)
        self.makemap(142, 144, 5)
        self.makemap(148, 150, 3)
        self.makemap(190, 193, 7)
        self.makemap(197, 198, 13)
        self.makemap(201, 204, 11)
        self.makemap(208, 217, 9)
        self.makemap(220, 223, 11)
        self.makemap(221, 226, 6)
        self.makemap(227, 228, 14)
        self.makemap(310, 312, 3)
        self.makemap(312, 314, 4)
        self.makemap(314, 316, 11)
        self.makemap(316, 318, 12)
        self.makemap(318, 320, 15)
        self.makemap(320, 322, 16)
        self.makemap(250, 253, 11)
        self.makemap(280, 283, 11)

        # self.makemap(80,)
        self.makemap(125, 180, 1)
        self.makemap(185, 230, 1)
        self.makemap(235, 300, 1)
        self.makemap(305, 500, 1)
        self.makemap(380, 381, 17)
        self.makecastle(400)
