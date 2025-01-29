import pygame
from pygame.locals import *
import time

pygame.init()
pygame.display.set_caption('hawk vs mouse')
screen_width=900
screen_height=700
screen = pygame.display.set_mode([screen_width,screen_height])

background = pygame.image.load('hawk hunt bg.jpg')
bg = pygame.transform.scale(background, (screen_width,screen_height))
screen.blit(bg, (0,0))

class hawk(pygame.sprite.Sprite):
   def __init__(self):
      super().__init__()
      self.image = pygame.image.load('hawk.png').convert_alpha()
      self.image = pygame.transform.scale(self.image, (200,100))
      self.rect = self.image.get_rect()

class mouse(pygame.sprite.Sprite):
    def __init__(self):
       super().__init__()
       self.image = pygame.image.load('mouse.png').convert_alpha()
       self.image = pygame.transform.scale(self.image, (150,75))
       self.rect = self.image.get_rect()

Hawk_list = pygame.sprite.Group()
Mouse_list = pygame.sprite.Group()

hawk = hawk()
mouse = mouse()

Hawk_list.add(hawk)
Mouse_list.add(mouse)

hawk.x = 700
hawk.y = -200

mouse.x = 200
mouse.y = -500

RED=(255,0,0)
BLACK=(0,0,0)
WHITE=(255, 255, 255)

playing=True
clock=pygame.time.Clock
start_time = time.time()
timingFont=pygame.font.SysFont("Times New Roman", 22,True,WHITE)

while playing:
    #clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing=False

    timeElapsed=time.time()-start_time
    if timeElapsed >=90:
        text=myFont.render("Mouse Wins!",True,BLACK)

    elif pygame.sprite.spritecollide(Hawk_list, Mouse_list, True):
        text=myFont.render("Hawk Wins!",True,RED)
            
    Keys = pygame.key.get_pressed()
    if Keys[pygame.K_UP]:
        if hawk.rect.y>0:
            hawk.rect.y -=5
    if Keys[pygame.K_DOWN]:
        if hawk.rect.y<800:
            hawk.rect.y +=5
    if Keys[pygame.K_LEFT]:
        if hawk.rect.x> 0:
            hawk.rect.x -=5
    if Keys[pygame.K_RIGHT]:
        if hawk.rect.x <670:
            hawk.rect.x +=5
    if Keys[pygame.K_a]:
        if mouse.rect.x>0:
            mouse.rect.x -=5
    if Keys[pygame.K_s]:
        if mouse.rect.x<670:
            mouse.rect.x +=5

    #draw(screen)
    Hawk_list.draw(screen)
    Mouse_list.draw(screen)

    pygame.display.update()

pygame.quit()
