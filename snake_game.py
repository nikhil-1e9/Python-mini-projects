print("Let's play the snake game!")

import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
disp_width = 800
disp_height = 500
 
disp = pygame.display.set_mode((disp_width, disp_height))
pygame.display.set_caption('The Snake game')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("georgia", 25)
score_font = pygame.font.SysFont("calibri", 20)
 

def Score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    disp.blit(value, [0, 0])
  
def Snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(disp, black, [x[0], x[1], snake_block, snake_block])
  
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    disp.blit(mesg, [disp_width / 6, disp_height / 3])
 
def gameLoop():
    game_over = False
    game_close = False
 
    x = disp_width / 2
    y = disp_height / 2
 
    dx = 0
    dy = 0
 
    snake_List = []
    snake_len = 1
 
    foodx = round(random.randrange(0, disp_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, disp_height - snake_block) / 10.0) * 10.0
 
    
    while not game_over:
 
        while game_close == True:
            disp.fill(blue)
            message("Game Over! Press Enter to Play Again or Q to Quit", green)
            Score(snake_len - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_RETURN:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -snake_block
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = snake_block
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -snake_block
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = snake_block
                    dx = 0
 
        if x >= disp_width or x < 0 or y >= disp_height or y < 0:
            game_close = True
        x += dx
        y += dy
        disp.fill(blue)
        pygame.draw.rect(disp, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake_List.append(snake_Head)
        if len(snake_List) > snake_len:
            del snake_List[0]
 
        for i in snake_List[:-1]:
            if i == snake_Head:
                game_close = True
 
        Snake(snake_block, snake_List)
        Score(snake_len - 1)
 
        pygame.display.update()
 
        if x == foodx and y == foody:
            foodx = round(random.randrange(0, disp_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, disp_height - snake_block) / 10.0) * 10.0
            snake_len += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    # quit()
 
 
gameLoop()
