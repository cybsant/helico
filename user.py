# 🚁 - вертолет 🚒🚁🛩
from utils import randcell

class Helicopter:
    def __int__(self, w, h):
        rc = randcell(w, h)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.y = ry