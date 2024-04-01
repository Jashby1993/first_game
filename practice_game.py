import pygame
import os


WIDTH , HEIGHT = 1000,600
WIN = pygame.display.set_mode((WIDTH , HEIGHT))
white = (255,255,255)
black = (0,0,0)

SPACESHIP_WIDTH , SPACESHIP_HEIGHT = 55 , 45

BORDER = pygame.Rect(WIDTH/2 - 5,0,10,HEIGHT)

pygame.display.set_caption("First Game")

FPS = 60
VEL = 4

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

def draw_window(yellow, red):
    WIN.fill(white)
    pygame.draw.rect(WIN,black, BORDER)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    pygame.display.update()

def handle_yellow_movement(keys_pressed,yellow):
    if keys_pressed [pygame.K_a] and yellow.x - VEL > 0: # LEFT
        yellow.x -= VEL
    if keys_pressed [pygame.K_d]: # RIGHT
        yellow.x += VEL
    if keys_pressed [pygame.K_w] and yellow.y - VEL > 0: # UP
        yellow.y -= VEL
    if keys_pressed [pygame.K_s] and yellow.y + VEL < HEIGHT - SPACESHIP_HEIGHT: # DOWN
        yellow.y += VEL

def handle_red_movement(keys_pressed,red):
    if keys_pressed [pygame.K_LEFT]: # LEFT
        red.x -= VEL
    if keys_pressed [pygame.K_RIGHT]: # RIGHT
        red.x += VEL
    if keys_pressed [pygame.K_UP]: # UP
        red.y -= VEL
    if keys_pressed [pygame.K_DOWN]: # DOWN
        red.y += VEL


def main():
    yellow = pygame.Rect(100,300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pygame.Rect(700,300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window(yellow, red)
        keys_pressed = pygame.key.get_pressed()
        handle_yellow_movement(keys_pressed,yellow)
        handle_red_movement(keys_pressed,red)


    pygame.quit()


if __name__ == '__main__':
    main()