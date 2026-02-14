import pygame
from pygame import display, init, quit, event, mouse

init()

display.set_caption("типа пеинт")
screen=display.set_mode((800, 800))

running =True
startDraw=False

while(running):
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            running=False
        if(pygame.mouse.get_pressed()[0]):
            print("Нажали кнопку")
            startDraw=True
        if (pygame.mouse.get_pressed()[0] and event.type==pygame.MOUSEMOTION):
            print("Рисуем")
pygame.quit()


