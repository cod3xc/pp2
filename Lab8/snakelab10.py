import pygame
import random
import psycopg2 

# Database settings
DB_CONFIG = {
    'dbname': 'lab10',
    'user': 'postgres',
    'password': '1234', 
    'host': 'localhost'
}

# Database
def get_user_data(username):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        
        cur.execute("SELECT user_id FROM user_snake WHERE username = %s", (username,))
        row = cur.fetchone()
        
        if row:
            user_id = row[0]
            cur.execute("SELECT level, score FROM user_score WHERE user_id = %s", (user_id,))
            data = cur.fetchone()
            conn.close()
            if data: return data[0], data[1]
            else: return 1, 0
        else:
            cur.execute("INSERT INTO user_snake (username) VALUES (%s) RETURNING user_id", (username,))
            uid = cur.fetchone()[0]
            cur.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, 1, 0)", (uid,))
            conn.commit()
            conn.close()
            return 1, 0
    except Exception as e:
        print("DB Error:", e)
        return 1, 0

def save_game(username, level, score):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        query = "UPDATE user_score SET level=%s, score=%s WHERE user_id=(SELECT user_id FROM user_snake WHERE username=%s)"
        cur.execute(query, (level, score, username))
        conn.commit()
        conn.close()
        print(f"-> Saved: {username} | Level: {level} | Score: {score}")
    except Exception as e:
        print("Save Error:", e)

pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
blue = (50, 150, 213)
green = (0, 255, 0)
gray = (100, 100, 100) # Wall color
bgcolor = (25, 25, 25)

# Screen settings
W, H = 800, 600
display = pygame.display.set_mode((W, H))
pygame.display.set_caption('Snake Game DB + Walls')

clock = pygame.time.Clock()
snake_block = 20 
base_snake_speed = 10    
speed_increase = 3     
foods_per_level = 3  
food_lifetime = 7000 

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def show_stats(score, level): 
    score_value = score_font.render("Score: " + str(score), True, yellow)
    display.blit(score_value, [10, 10])
    level_value = score_font.render("Level: " + str(level), True, yellow)
    display.blit(level_value, [10, 50])
    hint = font_style.render("P: Pause | X: Save & Exit", True, white)
    display.blit(hint, [W - 280, 10])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, blue, [x[0], x[1], snake_block, snake_block])

def draw_walls(walls):
    for w in walls:
        pygame.draw.rect(display, gray, [w[0], w[1], snake_block, snake_block])

def message(msg, color, y_displace=0):
    mesg = font_style.render(msg, True, color)
    text_rect = mesg.get_rect(center=(W / 2, H / 2 + y_displace))
    display.blit(mesg, text_rect)

# Walls
def get_walls(level):
    walls = []
    # Level 2 = wall in the middle
    if level >= 2:
        for x in range(200, 600, snake_block):
            walls.append([x, 300])
    
    # Level 3 =  vertical walls
    if level >= 3:
        for y in range(100, 500, snake_block):
            walls.append([160, y])
            walls.append([640, y])
            
    return walls

def generate_food(snake_list, walls):
    while True:
        foodx = round(random.randrange(0, W - snake_block) / snake_block) * snake_block
        foody = round(random.randrange(0, H - snake_block) / snake_block) * snake_block
        # Food must not be on snake or inside a wall
        if [foodx, foody] not in snake_list and [foodx, foody] not in walls:
            weight = 3 if random.randint(1, 5) == 1 else 1
            spawn_time = pygame.time.get_ticks() 
            return foodx, foody, weight, spawn_time

def gameLoop(username, start_lvl, start_score):
    game_over = False
    game_close = False

    x1 = W / 2
    y1 = H / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = start_score + 1
    level = start_lvl
    
    current_speed = base_snake_speed + ((level - 1) * speed_increase)
    food_eaten_this_level = 0
    
    # Generate walls for current level
    walls = get_walls(level)
    foodx, foody, food_weight, food_spawn_time = generate_food(snake_List, walls) 

    while not game_over:
        while game_close:
            display.fill(bgcolor)
            message("Game Over!", red, y_displace=-50)
            message("Q = Save & Quit / Close Window = Reset & Play Again", white, y_displace=50)
            show_stats(Length_of_snake - 1, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        save_game(username, level, Length_of_snake - 1)
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        save_game(username, 1, 0)
                        gameLoop(username, 1, 0)
                if event.type == pygame.QUIT:
                    save_game(username, level, Length_of_snake - 1)
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_game(username, level, Length_of_snake - 1)
                game_over = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block; y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block; y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block; x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block; x1_change = 0
                elif event.key == pygame.K_p:
                    save_game(username, level, Length_of_snake - 1)
                    paused = True
                    while paused:
                        display.fill(bgcolor)
                        message("PAUSED", yellow, -20)
                        message("Press P to Continue", white, 20)
                        pygame.display.update()
                        for e in pygame.event.get():
                            if e.type == pygame.KEYDOWN and e.key == pygame.K_p: paused = False
                            if e.type == pygame.QUIT: pygame.quit(); quit()

        if x1 >= W or x1 < 0 or y1 >= H or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        
        # Check Wall Collision
        if [x1, y1] in walls:
            game_close = True

        if pygame.time.get_ticks() - food_spawn_time > food_lifetime:
             foodx, foody, food_weight, food_spawn_time = generate_food(snake_List, walls)

        display.fill(bgcolor)
        
        # Draw Walls
        draw_walls(walls)
        
        # Draw Food
        color_food = green if food_weight == 3 else red
        pygame.draw.rect(display, color_food, [foodx, foody, snake_block, snake_block])
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        show_stats(Length_of_snake - 1, level)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            Length_of_snake += food_weight
            food_eaten_this_level += 1 
            foodx, foody, food_weight, food_spawn_time = generate_food(snake_List, walls)
            
            if food_eaten_this_level >= foods_per_level:
                level += 1
                current_speed += speed_increase
                food_eaten_this_level = 0
                # Generate new walls for next level
                walls = get_walls(level)

        clock.tick(current_speed)

    pygame.quit()
    quit()

if __name__ == "__main__":
    print("Snake")
    name = input("Username: ")
    if not name: name = "Player1"
    
    l, s = get_user_data(name)
    print(f"Loaded {name}: Level {l}, Score {s}")
    
    gameLoop(name, l, s)