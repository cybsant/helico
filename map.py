from utils import randbool
from utils import randcell
from utils import randcell2

# TODO выбор в зависимости от мода
#CELL_TYPES = ['🟫', '🌵', '⛲', '💊', '🛠', '🔥'] # * DESERT
#CELL_TYPES = ['🟩', '🌴', '🟦', '⛑', '🛠', '🔥'] # * TROPICA
#CELL_TYPES = ['⬜', '🎄', '🌊', '🏥', '🏦', '🔥'] # * WINTER
#CELL_TYPES = ['⬛', '🌲', '🌊', '🏥', '🏦', '🔥'] # * DEFAUT
CELL_TYPES = [' ⬛', '🌳', '🌀', '🏥', '🏦', '🔥']
# >>>>>>>>>>    0     1     2     3     4     5
#INFO_TYPES = ['💰','💧','💜']
#DYN_TYPES = ['🌧 ','🌩 ','🚒']

#TODO !!! игровой баланс !!! 
TREE_BOUNS = 100
UPGRADE_COST = 500
LIFE_COST = 500

class Map:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]
        self.gen_forest(3, 10)
        self.gen_river(10)
        self.gen_river(9)
        self.gen_water(7)
        self.gen_water(5)
        self.gen_upgrade()
        self.gen_medic()

    def check_bounds(self, x, y):
        if x < 0 or y < 0 or x >= self.h or y >= self.w:
            return False
        return True

    def draw_map(self, helico, clouds):
        print(f'╭{"─" * (self.w)*2}╮')
        for ri in range(self.h):
            print("│", end="")
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if (clouds.cells[ri][ci] == 1):
                    print("🌧 ", end="")
                elif (clouds.cells[ri][ci] == 2):
                    print("🌩 ", end="")
                elif (helico.x == ri and helico.y == ci):
                    print("🚒", end="")
                elif 0 <= cell < len(CELL_TYPES):
                    print(CELL_TYPES[cell], end="")
            print("│")
        print(f'╰{"─" * (self.w)*2}╯')

    def gen_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1

    def gen_river(self, l):  # TODO переделать в реки
        rc = randcell(self.w, self.h)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if (self.check_bounds(rx2, ry2)): #? and (randbool(l, l * 2)):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1

    def gen_water(self, l):  # TODO переделать в озера
        rc = randcell(self.w, self.h)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if (self.check_bounds(rx2, ry2)): #? and (randbool(l, l * 6)):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1

    def gen_upgrade(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 4

    def gen_medic(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.cells[cx][cy] != 4):
            self.cells[cx][cy] = 3
        else:
            self.gen_medic()

    def add_tree(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.cells[cx][cy] == 0):
            self.cells[cx][cy] = 1

    def add_fire(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 1:
            self.cells[cx][cy] = 5

    def update_fires(self):
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if (cell == 5):
                    self.cells[ri][ci] = 0
        for i in range(5):
            self.add_fire()

    def proc_helico(self, helico, clouds):
        c = self.cells[helico.x][helico.y]
        d = clouds.cells[helico.x][helico.y]
        if (c == 2):
            helico.tank = helico.mxtank
        if (c == 5 and helico.tank > 0):
            helico.tank -= 1
            helico.score += TREE_BOUNS
            self.cells[helico.x][helico.y] = 1
        if (c == 4 and helico.score >= UPGRADE_COST):
            helico.score -= UPGRADE_COST
            helico.mxtank += 1
        if (c == 3 and helico.score >= LIFE_COST):
            helico.score -= LIFE_COST
            helico.lives += 10
        if (d == 2):
            helico.lives -= 1