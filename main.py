# File created by: JT Wilcox
# Agenda:
# gIT GITHUB    
# Build file and folder structures
# Create libraries
# testing github changes
# I changed something - I changed something else tooooo!

# This file was created by: JT Wilcox
# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
# Sources: 

# import libs
import pygame as pg
import random
import os
# import settings 
from settings import *
from sprites import *
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

def get_mouse_now():
    x,y = pg.mouse.get_pos()
    return (x,y)

# creates the window
pg.init()
# creates the sound
pg.mixer.init()
# creates the width and height of the screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
# title of the window
pg.display.set_caption("My first game...")
clock = pg.time.Clock() 

# sprites are a graphic element
all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()
player = Player()
# the width and height of all the enemies are the same
enemy1 = Mob(80,80)
enemy2 = Mob(80,80)
enemy3 = Mob(80,80)
enemy4 = Mob(80,80)
# holds and manages all the sprites
all_sprites.add(player)

for i in range(0,20):
    # creates random size and movement for each enemy 
    m = Mob(randint(30,90), randint(30,90))
    all_sprites.add(m)
    # enemies.add(m)

# game loop

while RUNNING:
    #  correct spped
    clock.tick(FPS)
    for event in pg.event.get():
        # closes window
        if event.type == pg.QUIT:
            RUNNING = False
            # break
    all_sprites.update()

    blocks_hit_list = pg.sprite.spritecollide(player, enemies, True)
    for block in blocks_hit_list:
        # print(enemies)
        pass
    # fills in the background blue
    screen.fill(BLUE)
    all_sprites.draw(screen)
    
    pg.display.flip()
    
pg.quit()