import pygame
from pygame import display, init, quit, event, mouse, draw

init()

display.set_caption("типа пеинт")
screen=display.set_mode((800, 800))

running =True
first_pos=None
WHITE=(255,255,255)
BLACK=(0, 0, 0)
GRAY = (200, 200, 200) 
BLUE = (100, 150, 255)
screen.fill(WHITE)
button_circle=pygame.Surface((120, 40))
button_rectangle=pygame.Surface((120, 40))
button_polygon=pygame.Surface((120, 40))
button_polygon.fill(GRAY)
button_circle.fill(GRAY)
button_rectangle.fill(GRAY)
font=pygame.font.Font(None, 14)

text = font.render("Circle", True, BLACK)
text_button = text.get_rect(
    center=(button_circle.get_width() /2, 
            button_circle.get_height()/2))

text2 = font.render("Rectangle", True, BLACK)
text_button2 = text2.get_rect(
    center=(button_circle.get_width() /2, 
            button_circle.get_height()/2))

text3 = font.render("Polygone", True, BLACK)
text_button3 = text3.get_rect(
    center=(button_polygon.get_width() /2, 
            button_polygon.get_height()/2))

button_rect = pygame.Rect(25, 10, 150, 50)
button_rect2 = pygame.Rect(175, 10, 150, 50)
button_rect3 = pygame.Rect(325, 10, 150, 50)


button_circle.blit(text, text_button)
button_rectangle.blit(text2, text_button2)
button_polygon.blit(text3, text_button3)

pygame.draw.rect(button_circle, BLACK, button_circle.get_rect(), 2)
pygame.draw.rect(button_rectangle, BLACK, button_rectangle.get_rect(), 2)
pygame.draw.rect(button_polygon, BLACK, button_polygon.get_rect(), 2)

screen.blit(button_circle, (button_rect.x, button_rect.y))
screen.blit(button_rectangle, (button_rect2.x, button_rect2.y))
screen.blit(button_polygon, (button_rect3.x, button_rect3.y))
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
pygame.quit()


