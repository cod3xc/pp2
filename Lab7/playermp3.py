import pygame
import os

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((500, 200))
pygame.display.set_caption("Player: SPACE=Play/Pause, Arrowleft/Arrowright=Prev/Next")
musicpath = "./Lab7"
tracks = [a for a in os.listdir(musicpath)
          if a.lower().endswith((".mp3"))]
clock = pygame.time.Clock()
b = 0              
playing = False    
paused = False
running = True
while running:
    for music in pygame.event.get():
        if music.type == pygame.QUIT:
            running = False
        elif music.type == pygame.KEYDOWN:
            if music.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                    playing = True
                elif playing:
                    pygame.mixer.music.pause()
                    paused = True
                    playing = False
                else:
                    pygame.mixer.music.load(os.path.join(musicpath, tracks[b]))
                    pygame.mixer.music.play()
                    playing = True
                    paused = False
            elif music.key == pygame.K_RIGHT:
                b = (b+1) % len(tracks)
                pygame.mixer.music.load(os.path.join(musicpath, tracks[b]))
                pygame.mixer.music.play()
                playing = True
                paused = False
            elif music.key == pygame.K_LEFT:
                b = (b-1) % len(tracks)
                pygame.mixer.music.load(os.path.join(musicpath, tracks[b]))
                pygame.mixer.music.play()
                playing = True
                paused = False
    screen.fill((240, 240, 240))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
