import pygame
import sys
from tank import Tank
from dirt_maze import Maze
from start_button import Button

pygame.init()
pygame.display.set_caption("Tank Maze")

run_game = True
start_game = False

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
coordinate = (10, 192)

# Draw tank on screen
tank = Tank()

# Draw dirt on screen
dirt = Maze()

button = Button()

def draw_background():
    # drawing my ocean on the screen
    for x in range(rows):
        for y in range(cols):
            screen.blit(ice_image, (x * ice_rect.height, y * ice_rect.width))


clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 40, bold=True)

frame_count = 0
frame_rate = 60
start_time = 90

while run_game:
    draw_background()
    dirt.draw_maze(screen)
    button.draw_button(screen)

    coordinate_x = pygame.mouse.get_pos()[0]
    coordinate_y = pygame.mouse.get_pos()[1]

    recent_events = pygame.event.get()
    for event in recent_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if coordinate_x in range(11, 121) and coordinate_y in range(199, 242):
                print(coordinate_x, coordinate_y)
                start_game = True

    if start_game:
    # Tank Movement
        coordinate = pygame.mouse.get_pos()
        tank.move(coordinate)
        tank.draw(screen)

    # Time Factor
        total_seconds = frame_count // frame_rate
        # Divide by 60 to get total minutes
        minutes = total_seconds // 60
        # Use modulus (remainder) to get seconds
        seconds = total_seconds % 60
        # Use python string formatting to format in leading zeros
        output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
        # Blit to the screen
        text = font.render(output_string, True, (0, 0, 0))
        screen.blit(text, [230, 100])

        # --- Timer going down ---
        # --- Timer going up ---
        # Calculate total seconds
        total_seconds = start_time - (frame_count // frame_rate)
        if total_seconds < 0:
            total_seconds = 0
        frame_count += 1
        # Limit frames per second
        clock.tick(frame_rate)


    pygame.display.flip()



