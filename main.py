from os import system, name
from time import sleep
from map import Map
from user import Helicopter as Helico

TICK_SLEEP = 0.06
TREE_UPD = 25
FIRE_UPD = 50

# TODO выбор размера карты юзером и умолчания на основе размера экрана(терминала).
#? Sml
#MAP_W, MAP_H = 16, 8
#? Med
##MAP_W, MAP_H = 24, 16
#? Big
#MAP_W, MAP_H = 32, 24
#? Gig
#MAP_W, MAP_H = 48, 32
#? Mobile (мне так удобнее отлаживать на моем устройстве)
MAP_W, MAP_H = 12, 24

# !--------------------------
# TODO(?) Menu > Select Theme
# TODO(?) HowTo set background color

field = Map(MAP_W, MAP_H)
field.gen_forest(3, 10)
field.gen_river(10)
field.gen_river(9)
#field.gen_water(7)
#field.gen_water(5)

#field.draw_map()

helico = Helico(MAP_W, MAP_H)

tick = 1

while True:
    system('cls' if name == 'nt' else 'clear')
    #field.draw_info()
    field.draw_map(helico)
    tick += 1
    sleep(TICK_SLEEP)
    if (tick % TREE_UPD == 0):
        field.add_tree()
    if (tick % FIRE_UPD == 0):
        field.update_fires()
