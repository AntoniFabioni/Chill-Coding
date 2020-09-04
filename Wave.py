'''
This program displays an animation of a travelling wave.
'''

import pygame
import os
import math

os.environ["SDL_VIDEO_CENTERED"]='1'
black, white  = (20, 20, 20), (230, 230, 230)
width, height = 1920, 1080

pygame.init()
pygame.display.set_caption("Wave")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 1.5 * 60

run = True
while run:
    clock.tick(fps)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                run = False

pygame.quit()