import pygame
import random
import thorpy as tp
import PongGui
import function
import GameLoop


# Ball logic
ball_pos = pygame.Vector2(GameLoop.screen.get_width() / 2, GameLoop.screen.get_height() / 2)

ball_speed = 200
ball_pos_vy = random.choice([-1,1]) * ball_speed
ball_pos_vx = random.choice([-1,1]) * ball_speed

#player 1 
player_one_pos_x = 0
player_one_pos_y = 300

#player 2
player_two_pos_x = 1270
player_two_pos_y = 300
