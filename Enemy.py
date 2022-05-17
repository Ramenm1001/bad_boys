import pygame
import random


class Enemies(pygame.sprite.Sprite):
    def __init__(self, x, y, waypoints, image, win, group):
        super().__init__()
        self.win = win
        self.rect = pygame.Rect(x, y, 100, 100)
        self.hp = 2
        self.image = image
        self.speed = 5
        self.n = 1
        self.waypoints = waypoints
        self.target = self.waypoints[self.n]
        group.add(self)

    def draw(self):
        self.win.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        if self.target[0] < self.rect.x:
            self.rect = self.rect.move(-self.speed, 0)
        if self.target[0] > self.rect.x:
            self.rect = self.rect.move(self.speed, 0)
        if self.target[1] < self.rect.y:
            self.rect = self.rect.move(0 ,-self.speed)
        if self.target[1] > self.rect.y:
            self.rect = self.rect.move(0 ,self.speed)
        if  self.target[0] == self.rect.x and self.target[1] == self.rect.y:
            self.n += 1
            if len(self.waypoints) <= self.n:
                self.n = 0
            self.target = self.waypoints[self.n]

    def update(self):
        self.move()
        self.draw()
        if self.hp <= 0:
            self.kill()


if __name__ == "__main__":
    pygame.init()
    win = pygame.display.set_mode((800, 500))
    pygame.display.set_caption(("Enemy"))
    enemies = pygame.sprite.Group()
    im = pygame.image.load("i.png")
    im = pygame.transform.scale(im, (100, 100))
    Enemies(100, 100, [[100,100], [250, 400], [0, 0], [700, 250], [10, 350], [70, 200]], im, win, enemies)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.time.delay(50)
        win.fill((255,255,255))
        enemies.update()
        pygame.display.update()
    pygame.quit()
