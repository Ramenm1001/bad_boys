import pygame
import  random
import Enemy
import sounds.sounds as sound
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image, win):
        super().__init__()
        self.image = image
        self.win = win
        self.rect = pygame.Rect(x, y, 100, 100)
        self.hp = 5
        self.speed = 5
        self.kd = 0

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
        if keys[pygame.K_SPACE]:
            if self.kd == 0:
                sound.sound("удар")
                Laser(player_laser, self.rect.x + 50, self.rect.y)
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
    pygame.display.set_caption(("Space invaders"))
    im = pygame.image.load("i.png")
    im = pygame.transform.scale(im, (100, 100))

    enemies = pygame.sprite.Group()

    player = Player(100, 100,im,win)
    player_laser = pygame.sprite.Group()
    Enemy.Enemies(100, 100, [[100, 100], [250, 400], [0, 0], [700, 250], [10, 350], [70, 200]], im, win, enemies)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.time.delay(50)
        win.fill((255,255,255))
        player.update()
        enemies.update()
        player_laser.update()
        for i in enemies:
            if pygame.sprite.spritecollideany(i, player_laser):
                i.hp -= 1
                pygame.sprite.spritecollideany(i, player_laser).kill()
        pygame.display.update()
    pygame.quit()

