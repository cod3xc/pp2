import pygame

pygame.init()
Width, Height = 800, 800
screen = pygame.display.set_mode((Width, Height))
clock = pygame.time.Clock()
red = (255, 0, 0)
white = (255, 255, 255)
x = Width
y = Height
step = 20
radius = 25
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 20
    if pressed[pygame.K_DOWN]: y += 20
    if pressed[pygame.K_LEFT]: x -= 20
    if pressed[pygame.K_RIGHT]: x += 20
    if x < radius:
        x = radius
    if x > Width - radius:
        x = Width - radius
    if y < radius:
        y = radius
    if y > Height - radius:
        y = Height - radius
    screen.fill(white)
    pygame.draw.circle(screen, red, (x, y), radius)
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
