print("Let's play the snake game!")

# importing the necessary libraries
import pygame
import time
import random
 
# giving the snake its speed
snake_speed = 15

# defing the width and height of the window 
width = 800
height = 500
 
# defining the colors for the text shown on the board
white = pygame.Color(175, 220, 195)
yellow = pygame.Color(255, 255, 102)
black = pygame.Color(0, 0, 0)
red = pygame.Color(213, 50, 80)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(40, 60, 120)
 
# Initialize the pygame
pygame.init()

# Initialise the window and title of the game 
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('The Snake game')
 
# Control the frames per second 
fps = pygame.time.Clock()
 
# Defining the snake position at default
snake_body = 10
 
# Defining the preferred font for displaying the score
font_style = pygame.font.SysFont("georgia", 25)
score_font = pygame.font.SysFont("calibri", 20)
 
# Function to calculate the score of the player
def Score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    window.blit(value, [0, 0])
  
# Function to create the snake
def Snake(snake_body, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, black, [x[0], x[1], snake_body, snake_body])
  
# Display a message when the game is over
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [width / 6, height / 3])

# Main function to run the entire game
def gameLoop():
    game_over = False
    game_close = False
    
    # Initialize the starting position of the snake
    x = width / 2
    y = height / 2
    
    # Variables to accomodate the movement of the snake
    dx = 0
    dy = 0
 
    snake_List = []
    # Initialize the snake length to 1
    snake_len = 1
 
    # Spawn the food at random locations on the screen 
    foodx = round(random.randrange(0, width - snake_body) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_body) / 10.0) * 10.0
 
    
    while not game_over:
 
        while game_close == True:
            # Wait time after the game is over
            time.sleep(1)
            window.fill(blue)
            message("Game Over! Press Enter to Play Again or Q to Quit", red)
            Score(snake_len - 1)
            pygame.display.update()
            
            # Assigning the functionalities to the given keys
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_RETURN:
                        gameLoop()
        
        # Quit the game after game is over
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            # Making the snake move
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -snake_body
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = snake_body
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -snake_body
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = snake_body
                    dx = 0
        
        # If snake hits the boundary then game gets over
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        
        # Move the snake and capture the new coordinates
        x += dx
        y += dy
        
        window.fill(blue)
        # Displaying the food
        pygame.draw.rect(window, white, [foodx, foody, snake_body, snake_body])
        
        # If snake collides with itself the game gets over
        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake_List.append(snake_Head)
        if len(snake_List) > snake_len:
            del snake_List[0]
 
        for i in snake_List[:-1]:
            if i == snake_Head:
                game_close = True
 
        Snake(snake_body, snake_List)
        Score(snake_len - 1)
 
        pygame.display.update()
        
        # Creating the food for the snake 
        # Everytime the snake eat the food its size increases
        if x == foodx and y == foody:
            foodx = round(random.randrange(0, width - snake_body) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_body) / 10.0) * 10.0
            snake_len += 1
        
        # Refresh Rate
        fps.tick(snake_speed)

    # Quit the game 
    pygame.quit()
 
gameLoop()
