import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image, win):
        super().__init__()
        self.image = imagew
        self.win = win
        self.rect = pygame.Rect(x, y, 100, 100)
        self.hp = 5
        self.speed = 5

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
    def draw(self):
        self.win.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        self.move()
        self.draw()

if __name__ == "__main__":
    pygame.init()
    win = pygame.display.set_mode((800, 500))
    pygame.display.set_caption(("Space invaders"))
    im = pygame.image.load("i.png")
    im = pygame.transform.scale(im, (100, 100))
    player = Player(100, 100,im,win)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.time.delay(50)
        win.fill((255,255,255))
        player.update()
        pygame.display.update()
    pygame.quit()

