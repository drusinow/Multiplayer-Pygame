import pygame
import random
import thorpy as tp
import PongGui
import function
import GameObjects

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
WIDTH, HEIGHT = 1280, 720

# Game loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    
    function.StarterGui()

    pygame.draw.circle(screen, "red", GameObjects.ball_pos, 40)
    pygame.draw.rect(screen, "black", (GameObjects.player_one_pos_x, GameObjects.player_one_pos_y, 10, 125))
    pygame.draw.rect(screen, "black", (GameObjects.player_two_pos_x, GameObjects.player_two_pos_y, 10, 125))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and GameObjects.player_one_pos_y > -1:
        GameObjects.player_one_pos_y -= 300 * dt
    if keys[pygame.K_s] and GameObjects.player_one_pos_y < 600:
        GameObjects.player_one_pos_y += 300 * dt
    if keys[pygame.K_UP] and GameObjects.player_two_pos_y > -1:
        GameObjects.player_two_pos_y -= 300 * dt
    if keys[pygame.K_DOWN] and GameObjects.player_two_pos_y < 600:
        GameObjects.player_two_pos_y += 300 * dt

    #Ball login in loop
    GameObjects.ball_pos.x += GameObjects.ball_pos_vx * dt
    GameObjects.ball_pos.y += GameObjects.ball_pos_vy * dt

    if GameObjects.ball_pos.x - 40 <= 0 or GameObjects.ball_pos.x + 40 >= WIDTH:
        GameObjects.ball_pos_vx = -GameObjects.ball_pos_vx
    if GameObjects.ball_pos.y - 40 <= 0 or GameObjects.ball_pos.y + 40 >= HEIGHT:
        GameObjects.ball_pos_vy = -GameObjects.ball_pos_vy

    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()