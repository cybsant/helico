from utils import randcell

class Helicopter:
    def __init__(self, w, h):
        rc = randcell(w, h)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.y = ry
        self.h = h
        self.w = w
        self.tank = 0
        self.mxtank = 1


    def move(self, dx, dy):
        nx, ny = dx + self.x, dy + self.y
        if (0 <= nx < self.h and 0 <= ny < self.w):
            self.x, self.y = nx, ny

