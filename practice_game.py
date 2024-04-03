import pygame
import os


WIDTH , HEIGHT = 1000,600
WIN = pygame.display.set_mode((WIDTH , HEIGHT))
white = (255,255,255)
black = (0,0,0)

YELLOW_HIT == pygame.USEREVENT + 1
RED_HIT == pygame.userevent + 2

SPACESHIP_WIDTH , SPACESHIP_HEIGHT = 55 , 45

BORDER = pygame.Rect(WIDTH/2 - 5,0,10,HEIGHT)

pygame.display.set_caption("First Game")

FPS = 60
VEL = 5
BULLET_VEL = 8
MAX_BULLETS = 5

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
BULLET_IMAGE = pygame.image.load(os.path.join('Assets','bullet.png'))
SCALED_BULLET = pygame.transform.scale(BULLET_IMAGE,(15,40))
RED_BULLET = pygame.transform.rotate(SCALED_BULLET, 90)
YELLOW_BULLET = pygame.transform.rotate(SCALED_BULLET, 270)
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

def draw_window(yellow, red, yellow_bullet, red_bullet):
    WIN.fill(white)
    pygame.draw.rect(WIN,black, BORDER)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    WIN.blit(RED_BULLET, (red_bullet.x,red_bullet.y))
    WIN.blit(YELLOW_BULLET, (yellow_bullet.x,yellow_bullet.y))
    pygame.display.update()

def handle_yellow_movement(keys_pressed,yellow):
    if keys_pressed [pygame.K_a] and yellow.x - VEL > 0: # LEFT
        yellow.x -= VEL
    if keys_pressed [pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: # RIGHT
        yellow.x += VEL
    if keys_pressed [pygame.K_w] and yellow.y - VEL > 0: # UP
        yellow.y -= VEL
    if keys_pressed [pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15: # DOWN
        yellow.y += VEL

def handle_red_movement(keys_pressed,red):
    if keys_pressed [pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width // 2: # LEFT
        red.x -= VEL
    if keys_pressed [pygame.K_RIGHT] and red.x + VEL < WIDTH - SPACESHIP_WIDTH - VEL: # RIGHT
        red.x += VEL
    if keys_pressed [pygame.K_UP] and red.y - VEL > 0 : # UP
        red.y -= VEL
    if keys_pressed [pygame.K_DOWN] and red.y + VEL + red.height +15 < HEIGHT  : # DOWN
        red.y += VEL

def handle_bullet_movements(yellow_bullets, red_bullets, yellow, red):
    for yellow_bullet in yellow_bullets:
        yellow_bullet.x += BULLET_VEL
        if red.colliderect(yellow_bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.pop(yellow_bullet)
        
        for red_bullet in red_bullets:
            red_bullet.x -= BULLET_VEL
            if yellow.colliderect(red_bullet):
                pygame.event.post(pygame.event.Event(YELLOW_HIT))
                red_bullets.pop(red_bullet)

def main():
    yellow = pygame.Rect(100,300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pygame.Rect(700,300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    red_bullets = []
    yellow_bullets = []
    
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                yellow_bullet = pygame.Rect(yellow.x + yellow.width - 5, yellow.y + yellow.height // 2 - 20, 40, 15)
                yellow_bullets.append(yellow_bullet)

            if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                red_bullet = pygame.Rect(red.x, red.y +yellow.height // 2 -20, 40, 15)
                red_bullets.append(red_bullet)


        
        keys_pressed = pygame.key.get_pressed()
        handle_yellow_movement(keys_pressed,yellow)
        handle_red_movement(keys_pressed,red)
        handle_bullet_movements(yellow_bullets, red_bullets, yellow, red)
        draw_window(yellow, red, red_bullet, yellow_bullet)

    pygame.quit()


if __name__ == '__main__':
    main()