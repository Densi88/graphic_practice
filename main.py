import pygame
from pygame import display, init, quit, event, mouse, draw

init()

display.set_caption("типа пеинт")
screen=display.set_mode((800, 800))

running =True
startDraw=False
first_pos=None
WHITE=(255,255,255)
BLACK=(0, 0, 0)
screen.fill(WHITE)
pygame.display.update()
while(running):
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            running=False
        if(pygame.mouse.get_pressed()[0]):
            print("Нажали кнопку")
            startDraw=True
            first_pos=event.pos
        if (pygame.mouse.get_pressed()[0] and event.type==pygame.MOUSEMOTION):
            print("Рисуем")
            pygame.draw.line(screen, BLACK, first_pos, event.pos, 10)
            pygame.display.update()
        if (event.type==pygame.MOUSEBUTTONUP):
            print("Прекращаем рисовать")
            first_pos=event.pos

            startDraw=False
pygame.quit()


