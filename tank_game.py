import pygame
import sys
from tank import Tank
from dirt_maze import Maze
from start_button import Button

pygame.init()
pygame.display.set_caption("Tank Maze")

ice_image = pygame.image.load('images/ice_image.png')
ice_rect = ice_image.get_rect()
tile_size = ice_rect.width
screen = pygame.display.set_mode((10*tile_size, 10*tile_size))
screen_rect = screen.get_rect()
rows = screen_rect.height // tile_size  # rounds the result to the nearest whole number
cols = screen_rect.width // tile_size

width = screen.get_width()
height = screen.get_height()

# Gets mouse position
coordinate = (0, 192)

# Draw tank on screen
tank = Tank()

# Draw dirt on screen
dirt = Maze()
# dirt.move((320, 32))

button = Button()

def draw_background():
    # drawing my ocean on the screen
    for x in range(rows):
        for y in range(cols):
            screen.blit(ice_image, (x * ice_rect.height, y * ice_rect.width))

while True:
    recent_events = pygame.event.get()
    for event in recent_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            coordinate = pygame.mouse.get_pos()
            print(coordinate)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if coordinate == (0, 192):
                sys.exit()


    draw_background()
    dirt.draw_maze(screen)
    button.draw_button(screen)

    tank.move(coordinate)
    tank.draw(screen)


    pygame.display.flip()
