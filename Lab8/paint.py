import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    color = (0, 0, 255)
    background = pygame.Surface((640, 480))
    background.fill((0, 0, 0))
    drawing = False
    start_pos = None
    tool = 'draw'
    font = pygame.font.Font(pygame.font.get_default_font(), 20)

def get_rect(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    left = min(x1, x2)
    top = min(y1, y2)
    width = abs(x1 - x2)
    height = abs(y1 - y2)
    return pygame.Rect(left, top, width, height)

    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                    color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    mode = 'green'
                    color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    mode = 'blue'
                    color = (0, 0, 255)
                
                elif event.key == pygame.K_1:
                    tool = 'draw'
                elif event.key == pygame.K_2:
                    tool = 'rect'
                elif event.key == pygame.K_3:
                    tool = 'circle'
                elif event.key == pygame.K_4 or event.key == pygame.K_e:
                    tool = 'erase'
                
                elif event.key == pygame.K_c:
                    background.fill((0, 0, 0))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # left click grows radius
                    radius = min(100, radius + 1)
                elif event.button == 5:  # right click shrinks radius
                    radius = max(1, radius - 1)
                
                if event.button == 1:
                    drawing = True
                    start_pos = event.pos
                    if tool == 'draw':
                        pygame.draw.circle(background, color, event.pos, radius // 2)
                    elif tool == 'erase':
                        pygame.draw.circle(background, (0, 0, 0), event.pos, radius // 2)
                        
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    end_pos = event.pos
                    
                    if tool == 'rect' and start_pos:
                        rect = get_rect(start_pos, end_pos)
                        pygame.draw.rect(background, color, rect, 2)
                    
                    elif tool == 'circle' and start_pos:
                        rect = get_rect(start_pos, end_pos)
                        if rect.width > 0 and rect.height > 0:
                            pygame.draw.ellipse(background, color, rect, 2)
                    
                    start_pos = None

            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                if drawing:
                    current_pos = event.pos
                    if tool == 'draw':
                        pygame.draw.line(background, color, start_pos, current_pos, radius)
                        start_pos = current_pos
                    
                    elif tool == 'erase':
                        pygame.draw.line(background, (0, 0, 0), start_pos, current_pos, radius)
                        start_pos = current_pos
        
        screen.blit(background, (0, 0))
        
        ui_str = f"Tool: {tool} [1-4] | Color: {mode} [R,G,B] | Size: {radius} [Scroll]"
        ui_text = font.render(ui_str, True, (255, 255, 255))
        screen.blit(ui_text, (5, 5))
        
        pygame.display.flip()
        clock.tick(60)

main()
