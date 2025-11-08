import pygame
import random
#writing variables and initializing pygame
pygame.init()
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
blue = (50, 150, 213)
bgcolor = (25, 25, 25)
displaywidth = 800
displayheight = 600
display = pygame.display.set_mode((displaywidth, displayheight))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
snake_block = 20 
base_snake_speed = 10    
speed_increase = 3     
foods_per_level = 3  
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
#function to show score and level
def show_stats(score, level): 
    score_value = score_font.render("Score: " + str(score), True, yellow)
    display.blit(score_value, [10, 10])
    level_value = score_font.render("Level: " + str(level), True, yellow)
    display.blit(level_value, [10, 50])
#function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, blue, [x[0], x[1], snake_block, snake_block])
#function to display messages
def message(msg, color, y_displace=0):
    mesg = font_style.render(msg, True, color)
    text_rect = mesg.get_rect(center=(displaywidth / 2, displayheight / 2 + y_displace))
    display.blit(mesg, text_rect)
#function to generate food
def generate_food(snake_list):
    while True:
        foodx = round(random.randrange(0, displaywidth - snake_block) / snake_block) * snake_block
        foody = round(random.randrange(0, displayheight - snake_block) / snake_block) * snake_block
        if [foodx, foody] not in snake_list:
            return foodx, foody
#main game loop
def gameLoop():
    game_over = False
    game_close = False
    x1 = displaywidth / 2
    y1 = displayheight / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    level = 1                
    current_speed = base_snake_speed 
    food_eaten_this_level = 0   
    foodx, foody = generate_food(snake_List) 
#main game loop
    while not game_over:
        while game_close:
            display.fill(bgcolor)
            message("Game Over", red, y_displace=-50)
            message("Press Q to Quit or C to Play Again", white, y_displace=50)
            show_stats(Length_of_snake - 1, level)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
#main game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0
#move the snake
        if x1 >= displaywidth or x1 < 0 or y1 >= displayheight or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.fill(bgcolor)
        pygame.draw.rect(display, red, [foodx, foody, snake_block, snake_block])
#draw snake
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
#draw everything
        our_snake(snake_block, snake_List)
        show_stats(Length_of_snake - 1, level)
        pygame.display.update()
#check if snake has eaten the food
        if x1 == foodx and y1 == foody:
            foodx, foody = generate_food(snake_List)
            Length_of_snake += 1
            food_eaten_this_level += 1 
            if food_eaten_this_level >= foods_per_level:
                level += 1
                current_speed += speed_increase
                food_eaten_this_level = 0
        clock.tick(current_speed)
    pygame.quit()
    quit()
gameLoop()
