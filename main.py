import pygame
from pygame import display, init, quit, event, mouse, draw





init()

display.set_caption("типа пеинт")
screen=display.set_mode((800, 800))

draw_circle=False
draw_triangle=False
draw_rectangle=False
drawing=False
triangle_points=[]
rectangle_points=[]

running =True
first_pos=None
WHITE=(255,255,255)
BLACK=(0, 0, 0)
GRAY = (200, 200, 200) 
BLUE = (100, 150, 255)
screen.fill(WHITE)
button_circle=pygame.Surface((120, 40))
button_rectangle=pygame.Surface((120, 40))
button_triangle=pygame.Surface((120, 40))
save_button=pygame.Surface((60, 20))
main_surface=pygame.Surface((800, 55))
clear_button_surface=pygame.Surface((60, 20))
brush_button_surface=pygame.Surface((60, 20))
brush_button_surface.fill(GRAY)
clear_button_surface.fill(GRAY)
main_surface.fill(WHITE)
save_button.fill(GRAY)
button_triangle.fill(GRAY)
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
text3 = font.render("Triangle", True, BLACK)
text_button3 = text3.get_rect(
    center=(button_triangle.get_width() /2, 
            button_triangle.get_height()/2))
text4=font.render("Save", True, BLACK)
text_button4 = text4.get_rect(
    center=(save_button.get_width() /2, 
            save_button.get_height()/2))
text5=font.render("Clear", True, BLACK)
text_button5 = text5.get_rect(
    center=(clear_button_surface.get_width() /2, 
            clear_button_surface.get_height()/2))

text6 = font.render("Brush", True, BLACK)
text_button6 = text.get_rect(
    center=(brush_button_surface.get_width() /2, 
            brush_button_surface.get_height()/2))


main_surface_rect=pygame.Rect(1, 1, 150, 50)
button_rect = pygame.Rect(670, 10, 150, 50)
button_rect2 = pygame.Rect(520, 10, 150, 50)
button_rect3 = pygame.Rect(370, 10, 150, 50)
button_rect4 = pygame.Rect(20, 10, 100, 50)    # Save
button_rect5 = pygame.Rect(130, 10, 100, 50)   # Clear
button_rect6 = pygame.Rect(240, 10, 100, 50)   # Brush




button_circle.blit(text, text_button)
button_rectangle.blit(text2, text_button2)
button_triangle.blit(text3, text_button3)
save_button.blit(text4, text_button4)
clear_button_surface.blit(text5, text_button5)
brush_button_surface.blit(text6, text_button6)

pygame.draw.rect(main_surface, BLACK, main_surface.get_rect(), 2)
pygame.draw.rect(button_circle, BLACK, button_circle.get_rect(), 2)
pygame.draw.rect(button_rectangle, BLACK, button_rectangle.get_rect(), 2)
pygame.draw.rect(button_triangle, BLACK, button_triangle.get_rect(), 2)
pygame.draw.rect(save_button, BLACK, save_button.get_rect(), 2)
pygame.draw.rect(clear_button_surface, BLACK, clear_button_surface.get_rect(), 2)
pygame.draw.rect(brush_button_surface, BLACK, brush_button_surface.get_rect(), 2)


screen.blit(main_surface, (main_surface_rect.x, main_surface_rect.y))
screen.blit(button_circle, (button_rect.x, button_rect.y))
screen.blit(button_rectangle, (button_rect2.x, button_rect2.y))
screen.blit(button_triangle, (button_rect3.x, button_rect3.y))
screen.blit(save_button, (button_rect4.x, button_rect4.y))
screen.blit(clear_button_surface, (button_rect5.x, button_rect5.y))
screen.blit(brush_button_surface, (button_rect6.x, button_rect6.y))
pygame.display.update()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                draw_circle = True
                draw_rectangle = False
                draw_triangle = False
            elif button_rect2.collidepoint(event.pos):
                draw_circle = False
                draw_rectangle = True
                draw_triangle = False
            elif button_rect3.collidepoint(event.pos):
                draw_circle = False
                draw_rectangle = False
                draw_triangle = True
            elif button_rect5.collidepoint(event.pos):
                screen.fill(WHITE)
                screen.blit(main_surface, (main_surface_rect.x, main_surface_rect.y))
                screen.blit(button_circle, (button_rect.x, button_rect.y))
                screen.blit(button_rectangle, (button_rect2.x, button_rect2.y))
                screen.blit(button_triangle, (button_rect3.x, button_rect3.y))
                screen.blit(save_button, (button_rect4.x, button_rect4.y))
                screen.blit(clear_button_surface, (button_rect5.x, button_rect5.y))
                screen.blit(brush_button_surface, (button_rect6.x, button_rect6.y))
                pygame.display.update()
                print("Экран очищен")
            elif button_rect6.collidepoint(event.pos):
                drawing=True
                draw_circle=False
                draw_triangle=False
                draw_rectangle=False
        
        # Обработка рисовки
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Левая кнопка мыши
            if not (button_rect.collidepoint(event.pos) or 
                    button_rect2.collidepoint(event.pos) or 
                    button_rect3.collidepoint(event.pos) or
                    button_rect4.collidepoint(event.pos) or
                    button_rect5.collidepoint(event.pos)):
                
                first_pos = event.pos
                drawing = True
                if draw_circle:
                    center = event.pos
                    pygame.draw.circle(screen, BLACK, center, 50, 5)
                    pygame.display.update()
                    print("Нарисовали круг!")
                    drawing = False       
                if draw_triangle:
                    triangle_points.append(event.pos)
                    if len(triangle_points) == 3:
                        pygame.draw.polygon(screen, BLACK, triangle_points, 5)
                        pygame.display.update()
                        triangle_points = [] 
                if draw_rectangle:
                    rectangle_points.append(event.pos)
                    if len(rectangle_points)==2:
                        x1, y1 = rectangle_points[0]
                        x2, y2 = rectangle_points[1]
                        rect_x = min(x1, x2)
                        rect_y = min(y1, y2)
                        rect_width = abs(x2 - x1)
                        rect_height = abs(y2 - y1)
                        pygame.draw.rect(screen, BLACK, (rect_x, rect_y, rect_width, rect_height), 5)
                        pygame.display.update()
                        rectangle_points = [] 

                    
        if event.type == pygame.MOUSEMOTION and drawing and not draw_circle and not draw_rectangle and not draw_triangle:
            if first_pos:
                current_pos = event.pos
                pygame.draw.line(screen, BLACK, first_pos, current_pos, 10)
                first_pos = current_pos
                pygame.display.update()
        
        
        if event.type == pygame.MOUSEBUTTONUP:
            print("Прекращаем рисовать")
            first_pos = None
            drawing = False

pygame.quit()


