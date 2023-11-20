from os import system, name
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
        #print(f' │ 💧 {self.tank} / {self.mxtank} │ 💰 {self.score} | 💜 {self.lives} │')
        print(f' Water: {self.tank} / {self.mxtank} Score: {self.score} Lives: {self.lives} ')

    def draw_score(self):
        print(self.score)

    #TODO Причесать MAKET инфо панели
    #def draw_info(self):
    #    print(f'╭{"─" * (self.w)*2}╮')
    #    print("│", end="")
    #    print(f'[L:{"💜" * (self.w//2-2)}][T:        ]', end="")
    #    print("│")
    #    print("│", end="")
    #    print(f'[W:{"💧" * (self.w//2-3)}  ][M:{"💰" * (self.w//2-3)}  ]', end="")
    #    print("│")
    #    print(f'╰{"─" * (self.w)*2}╯')

    def game_over(self):
        system('cls' if name == 'nt' else 'clear')
        print(f' :. GAME OVER .:. YOUR SCORE: {Helico.draw_score} .: ')
        #print(f'╭─────────────────────────────────────────╮')
        #print(f'│ :. GAME OVER .:. YOUR SCORE: {Helico.draw_score} .: │')
        #print(f'╰─────────────────────────────────────────╯')