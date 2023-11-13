from utils import randbool
from utils import randcell
from utils import randcell2

# TODO выбор в зависимости от мода
#CELL_TYPES = ['🟫', '🌵', '⛲', '💊', '🛠', '🔥'] # * DESERT
#CELL_TYPES = ['🟩', '🌴', '🟦', '⛑', '🛠', '🔥'] # * TROPICA
#CELL_TYPES = ['⬜', '🎄', '🌊', '🏥', '🏦', '🔥'] # * WINTER
#CELL_TYPES = ['⬛', '🌲', '🌊', '🏥', '🏦', '🔥'] # * DEFAUT
CELL_TYPES = ['⚫', '🌳', '🌀', '🍄', '✨', '🔥']  #>* FANTASY

class Map:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]

    def check_bounds(self, x, y):
        if x < 0 or y < 0 or x >= self.h or y >= self.w:
            return False
        return True

#TODO  MAKET инфо панели
    def draw_info(self):
        print(f'╭{"─" * (self.w)*2}╮')
        print("│", end="")
        print(f'[L:{"💜" * (self.w//2-2)}][T:        ]', end="")
        print("│")
        print("│", end="")
        print(f'[W:{"💧" * (self.w//2-3)}  ][M:{"💲" * (self.w//2-3)}  ]', end="")
        print("│")
        print(f'╰{"─" * (self.w)*2}╯')

    def draw_map(self, helico):
        print(f'╭{"─" * (self.w)*2}╮')
        for ri in range(self.h):
            print("│", end="")
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if (helico.x == ri and helico.y == ci):
                    print("🚁", end="")
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
                if cell == 5:
                    self.cells[ri][ci] = 0
        for i in range(5):
            self.add_fire()
