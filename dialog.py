import pygame
import random

pygame.init()
win = pygame.display.set_mode((500, 500))
font1 = pygame.font.SysFont("#название шрифта", #размер шрифта)

scenes = {1: ["Text1", pygame.image.load("#спрайт.png")],
          2: ["Text2", pygame.image.load("#спрайт.png")]}

def dialog(person, font, win):
    pygame.draw.rect(win, (120, 120, 120), (0, 400, 500, 100))
    text = font1.render(person[0], True, (255,255,255))
    win.blit(text, (125, 410))
    win.blit(person[1], (0, 380))

def slowtext(text, n):
    return text[:n]

num = 1
phase = 0
run = True
while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False
        if eve.type == pygame.MOUSEBUTTONDOWN:
            num += 1
            phase = 0
            
    pygame.time.delay(50)
    
    win.fill((0,0,0))
    if num in scenes:
        if phase <= len(scenes[num][0]):
            phase += 1
            text = [slowtext(scenes[num][0], phase), scenes[num][1]]
        dialog(text, font1, win)
    pygame.display.update()
    
pygame.quit()
