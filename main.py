import pygame
from math import acos, sin, cos
import  random
import Enemy
import sounds.sounds as sound
pygame.init()

class Shot(pygame.sprite.Sprite):
    def __init__(self, coord, group, target):
        pygame.sprite.Sprite.__init__(self)
        # gun_sounds[weapon_name].play()
        coord = list(coord)
        self.x_y = list((coord[0] + 30, coord[1] + 30))
        delta_x = coord[0] - target[0]
        delta_y = coord[1] - target[1]
        long = (delta_x ** 2 + delta_y ** 2) ** 0.5
        try:
            angle = acos(delta_x / long) * (1 if delta_y > 0 else -1)
        except ZeroDivisionError:
            angle = acos(delta_x / 1) * (1 if delta_y > 0 else -1)
        speed = 20
        self.speed_x = -cos(angle) * speed
        self.speed_y = -sin(angle) * speed
        self.rect = pygame.Rect(int(self.x_y[0]), int(self.x_y[1]), 20, 20)
        self.add(group)

    def update(self, *args):
        self.x_y[0] += self.speed_x
        self.x_y[1] += self.speed_y
        self.rect = pygame.Rect(int(self.x_y[0]), int(self.x_y[1]), 20, 20)
        pygame.draw.rect(win, (50, 50, 50), (*[int(j) for j in self.x_y], 10, 10))
        if not ((0 <= self.x_y[0] <= 1000) and (0 <= self.x_y[1] <= 700)):
            self.kill()

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, win, group, sprite=None):
        super().__init__()
        pygame.rect =  pygame.Rect(x, y, 100, 100)
        self.sprite = sprite
        self.win = win
        group.add(self)

    def draw(self):
        if self.sprite:
            self.win.blit(self.sprite, (self.rect.x, self.rect.y))
        else:
            pygame.draw.rect(self.win,(146,146,146), self.rect)
    def update(self):
        self.draw()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image, win):
        super().__init__()
        self.image = image
        self.win = win
        self.rect = pygame.Rect(x, y, 100, 100)
        self.hp = 5
        self.speed = 5
        self.kd = 0
        self.x_y = [x,y]

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect = self.rect.move(0, -self.speed)
        if keys[pygame.K_s]:
            self.rect = self.rect.move(0, self.speed)
        if keys[pygame.K_d]:
            self.rect = self.rect.move(self.speed, 0)
        if keys[pygame.K_a]:
            self.rect = self.rect.move(-self.speed, 0)
        pressed = pygame.mouse.get_pressed()
        if pressed[0] and self.kd == 0:
            sound.sound("удар")
            Shot(list((self.rect.x, self.rect.y)), shots, pygame.mouse.get_pos())
            self.kd = 30
        if self.kd:
            self.kd -= 1

    def draw(self):
        self.win.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.move()
        self.draw()


class Laser(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        super().__init__()
        self.rect = pygame.Rect(x,y, 5, 10)
        group.add(self)

    def move(self):
        self.rect = self.rect.move(0, -5)

    def draw(self):
        pygame.draw.rect(win,(0,255,0), self.rect)

    def update(self):
        self.move()
        self.draw()
        if not 0 < self.rect.y < 500:
            self.kill()


if __name__ == "__main__":
    pygame.init()
    win = pygame.display.set_mode((800, 500))
    pygame.display.set_caption(("Шутер"))
    im = pygame.image.load("i.png")
    im = pygame.transform.scale(im, (100, 100))

    enemies = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    player = Player(100, 100,im,win)
    player_laser = pygame.sprite().Group
    wall = pygame.sprite().Group
    Wall(400, 250, win,wall)
    Enemy.Enemies(100, 100, [[100, 100], [250, 400], [0, 0], [700, 250], [10, 350], [70, 200]], im, win, enemies)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.time.delay(50)
        win.fill((255,255,255))
        player.update()
        shots.update()
        enemies.update()
        wall.update()
        player_laser.update()
        for i in enemies:
            if pygame.sprite.spritecollideany(i, shots):
                i.hp -= 1
                pygame.sprite.spritecollideany(i, shots).kill()
        pygame.display.update()
    pygame.quit()

