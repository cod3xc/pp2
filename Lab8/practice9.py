import pygame
import random
import sys
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
player_radius = 20
BLACK = (0, 0, 0)
font = pygame.font.SysFont("Verdana", 60)
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
player_x = WIDTH // 2
player_y = HEIGHT - 100
player_speed = 5
enemies = []
enemy_width = 50
enemy_height = 50
enemy_speed = 5
enemy_spawn_rate = 20
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x - player_radius > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + player_radius < WIDTH:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y - player_radius > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y + player_radius < HEIGHT:
        player_y += player_speed

    if random.randint(1, enemy_spawn_rate) == 1:
        enemy_x = random.randint(0, WIDTH - enemy_width)
        rect = pygame.Rect(enemy_x, -enemy_height, enemy_width, enemy_height)
        enemies.append(rect)
    for rect in enemies[:]: 
        rect.y += enemy_speed
        if rect.y > HEIGHT:
            enemies.remove(rect)

    player_rect = pygame.Rect(player_x - player_radius, player_y - player_radius, 
                              player_radius * 2, player_radius * 2)
    
    for rect in enemies:
        if player_rect.colliderect(rect):
            print("lose")
            running = False

    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (player_x, player_y), player_radius)
    

    for rect in enemies:
        pygame.draw.rect(screen, RED, rect)
    if pygame.sprite.spritecollideany(player_rect, enemies):
        SCORE += 1
    coin_text = font.render(f"Coins: {SCORE}", True, BLACK)
    coin_rect = coin_text.get_rect()
    coin_rect.topright = (WIDTH - 10, 10)
    DISPLAYSURF.blit(coin_text, coin_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()