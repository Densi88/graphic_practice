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
save_button=pygame.Surface((60, 20))
main_surface=pygame.Surface((800, 55))
main_surface.fill(WHITE)
save_button.fill(GRAY)
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
text4=font.render("Save", True, BLACK)
text_button4 = text4.get_rect(
    center=(save_button.get_width() /2, 
            save_button.get_height()/2))

main_surface_rect=pygame.Rect(1, 1, 150, 50)
button_rect = pygame.Rect(670, 10, 150, 50)
button_rect2 = pygame.Rect(520, 10, 150, 50)
button_rect3 = pygame.Rect(370, 10, 150, 50)
button_rect4 = pygame.Rect(20, 10, 150, 50)



button_circle.blit(text, text_button)
button_rectangle.blit(text2, text_button2)
button_polygon.blit(text3, text_button3)
save_button.blit(text4, text_button4)

pygame.draw.rect(main_surface, BLACK, main_surface.get_rect(), 2)
pygame.draw.rect(button_circle, BLACK, button_circle.get_rect(), 2)
pygame.draw.rect(button_rectangle, BLACK, button_rectangle.get_rect(), 2)
pygame.draw.rect(button_polygon, BLACK, button_polygon.get_rect(), 2)
pygame.draw.rect(save_button, BLACK, save_button.get_rect(), 2)

screen.blit(main_surface, (main_surface_rect.x, main_surface_rect.y))
screen.blit(button_circle, (button_rect.x, button_rect.y))
screen.blit(button_rectangle, (button_rect2.x, button_rect2.y))
screen.blit(button_polygon, (button_rect3.x, button_rect3.y))
screen.blit(save_button, (button_rect4.x, button_rect4.y))
pygame.display.update()
while(running):
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            running=False
        if(pygame.mouse.get_pressed()[0]):
            first_pos=event.pos
        if (pygame.mouse.get_pressed()[0] and event.type==pygame.MOUSEMOTION):
            current_pos=event.pos
            pygame.draw.line(screen, BLACK, first_pos, event.pos, 10)
            first_pos=current_pos
            pygame.display.update()
        if (event.type==pygame.MOUSEBUTTONUP):
            print("Прекращаем рисовать")
            first_pos=event.pos
pygame.quit()


