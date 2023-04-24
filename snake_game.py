import pygame
 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 155)
 
dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('The Snake')
 
game_over = False
 
x = 300
y = 300
 
dx = 0       
dy = 0
 
clock = pygame.time.Clock()
 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -10
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = 10
                dy = 0
            elif event.key == pygame.K_UP:
                dy = -10
                dx = 0
            elif event.key == pygame.K_DOWN:
                dy = 10
                dx = 0
 
    x += dx
    y += dy
    dis.fill(blue)
    pygame.draw.rect(dis, red, [x, y, 10, 10])
 
    pygame.display.update()
 
    clock.tick(30)
 
pygame.quit()