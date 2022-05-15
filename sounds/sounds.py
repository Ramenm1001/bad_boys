import pygame as pg
import sys

pg.init()
sc = pg.display.set_mode((1920,1080))


def sound(name):
    sounds[name].play()

sound_hit = pg.mixer.Sound('ударкулаком.ogg')     #sound_hit.play()
slowww = pg.mixer.Sound('ударножомдлявсех.ogg')  # slowww.play()
sounds = {"удар": sound_hit,
          }
sound("удар")

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

        elif i.type == pg.KEYUP:
            if i.key == pg.K_1:
                pg.mixer.music.pause()
                # pygame.mixer.music.stop()
            elif i.key == pg.K_2:
                pg.mixer.music.unpause()
                # pygame.mixer.music.play()
                pg.mixer.music.set_volume(0.5)
            elif i.key == pg.K_3:
                pg.mixer.music.unpause()
                # pygame.mixer.music.play()
                pg.mixer.music.set_volume(1)

        elif i.type == pg.MOUSEBUTTONUP:
            if i.button == 1:
                sound_hit.play()
            elif i.button == 3:
                slowww.play()

    pg.time.delay(20)