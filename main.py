from os import system, name
from time import sleep
from pynput import keyboard
from clouds import Clouds

from map import Map
from user import Helico

TICK_SLEEP = 0.2
TREE_UPD = 25
CLOUDS_UPD = 100
FIRE_UPD = 50

# TODO Выбор размера карты юзером и 
# TODO Умолчания на основе размера экрана(терминала) например.
#? Sml
#MAP_W, MAP_H = 16, 8
#? Med
MAP_W, MAP_H = 24, 16
#? Big
#MAP_W, MAP_H = 32, 24
#? Mobile
#MAP_W, MAP_H = 12, 24

# TODO Menu > Select Theme
# TODO HowTo set background color

field = Map(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)
helico = Helico(MAP_W, MAP_H)

MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}

def pres_key(key):
    global helico
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)

listener = keyboard.Listener(
    on_press=None,
    on_release=pres_key)
listener.start()

tick = 1

while True:
    system('cls' if name == 'nt' else 'clear')
    field.proc_helico(helico, clouds)
    field.draw_map(helico, clouds)
    helico.draw_info() 
    tick += 1
    sleep(TICK_SLEEP)
    if (tick % TREE_UPD == 0):
        field.add_tree()
    if (tick % FIRE_UPD == 0):
        field.update_fires()
    if (tick % CLOUDS_UPD == 0):
        clouds.update()
    
    