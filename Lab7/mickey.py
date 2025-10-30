import pygame
import time

pygame.init()
Width, Height = 600, 600
CENTER = (Width // 2, Height // 2)
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Clock")
clock = pygame.time.Clock()
bg = pygame.image.load("Lab7/base_micky.jpg").convert()
minute_img = pygame.image.load("Lab7/minute.png").convert_alpha()
second_img = pygame.image.load("Lab7/second.png").convert_alpha()
bg = pygame.transform.scale(bg, (Width, Height))
x = CENTER[0]
y = CENTER[1]  
running = True
while running:
    for a in pygame.event.get():
        if a.type == pygame.QUIT:
            running = False
    t = time.localtime()
    sec = t.tm_sec
    minute = t.tm_min
    sec_angle = sec * 6      
    min_angle = minute * 6 + sec*0.1  
    rot_sec = pygame.transform.rotate(second_img, -sec_angle)
    rot_min = pygame.transform.rotate(minute_img, -min_angle)
    sec_rect = rot_sec.get_rect(center=(x, y))
    min_rect = rot_min.get_rect(center=(x, y))
    screen.blit(bg, (0, 0))
    screen.blit(rot_min, min_rect)
    screen.blit(rot_sec, sec_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
