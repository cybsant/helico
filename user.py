from utils import randcell

class Helico:
    def __init__(self, w, h):
        rc = randcell(w, h)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.y = ry
        self.h = h
        self.w = w
        self.tank = 0
        self.mxtank = 1
        self.score = 0
        self.lives = 30

    def move(self, dx, dy):
        nx, ny = dx + self.x, dy + self.y
        if (0 <= nx < self.h and 0 <= ny < self.w):
            self.x, self.y = nx, ny

    def draw_info(self):
        print(f' │ 💧 {self.tank} / {self.mxtank} │ 💰 {self.score} | 💜 {self.lives} │')

    #TODO Причесать MAKET инфо панели
    #def draw_info(self):
    #    print(f'╭{"─" * (self.w)*2}╮')
    #    print("│", end="")
    #    print(f'[L:{"💜" * (self.w//2-2)}]', end="")
    #    print("│")
    #    print("│", end="")
    #    print(f'[W:{"💧" * (self.w//2-3)}  ][M:{"💰" * (self.w//2-3)}  ]', end="")
    #    print("│")
    #    print(f'╰{"─" * (self.w)*2}╯')

    def export_data(self):
        return {"score": self.score,
                "lives": self.lives,
                "x": self.x, "y": self.y,
                "tank": self.tank, "mxtank": self.mxtank,}
    
    def import_data(self, data):
        self.x, self.y = data["x"] or 0, data["y"] or 0
        self.tank, self.mxtank = data["tank"] or 0, data["mxtank"] or 1
        self.score = data["score"] or 0
        self.lives = data["lives"] or 3
        