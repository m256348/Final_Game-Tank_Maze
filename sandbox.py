import pygame
import sys
from tank import Tank
from dirt_maze import Maze
from start_button import Button
from dirt_maze import Wall

pygame.init()
pygame.display.set_caption("Tank Maze")

run_game = True
start_game = False
end_game = False
end_screen = False
fail_screen = False

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
clock = pygame.time.Clock()
frame_count = 0

# Create Wall
wall_x = [0, 64, 64, 64, 64, 128, 192, 192, 192, 192, 256, 320, 448, 512, 320, 320, 320, 384, 384, 448, 448, 448, 576, 576, 576, 512, 448, 384, 320, 256, 192, 128, 64, 0, 0, 0, 0, 0, 0, 64, 128, 192, 192, 192, 192, 256, 320, 348, 448, 512, 320, 512, 416, 416]
wall_y = [192, 192, 128, 64, 0, 0, 0, 64, 128, 192, 192, 192, 192, 192, 128, 64, 0, 128, 0, 0, 64, 128, 192, 256, 320, 320, 320, 320, 320, 320, 320, 320, 320, 320, 320, 384, 448, 512, 576, 576, 576, 576, 512, 448, 384, 448, 448, 448, 448, 448, 384, 384, 512, 576]
walls = []
# 320, 192

for row in range(len(wall_x)):
    for col in range(len(wall_y)):
        Wall((wall_x[row], wall_y[col]), walls)

def draw_background():
    # drawing my ocean on the screen
    for x in range(rows):
        for y in range(cols):
            screen.blit(ice_image, (x * ice_rect.height, y * ice_rect.width))

def time_update(frame_count):
    font = pygame.font.SysFont(None, 40, bold=True)
    frame_rate = 60
    start_time = 0
    total_seconds = start_time + (frame_count // frame_rate)
    # Divide by 60 to get total minutes
    minutes = total_seconds // 60
    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60
    # Use python string formatting to format in leading zeros
    output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
    # Blit to the screen
    text = font.render(output_string, True, (0, 0, 0))
    screen.blit(text, [230, 100])
    frame_count += 1
    # Limit frames per second
    clock.tick(frame_rate)

while run_game:
    draw_background()
    dirt.draw_maze(screen)
    button.draw_start_button(screen)

    coordinate_x = pygame.mouse.get_pos()[0]
    coordinate_y = pygame.mouse.get_pos()[1]

    recent_events = pygame.event.get()
    for event in recent_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if coordinate_x in range(11, 121) and coordinate_y in range(199, 242):
                start_game = True

    if start_game:
    # Tank Movement
        coordinate = pygame.mouse.get_pos()
        print(coordinate)
        coordinate_x = pygame.mouse.get_pos()[0]
        coordinate_y = pygame.mouse.get_pos()[1]
        tank.move(coordinate)
        tank.draw(screen)
        if coordinate_x in range(100, 150) and coordinate_y in range(590, 625):
            start_game = False
            end_game = False
            fail_screen = True
        if coordinate_x in range(100, 150) and coordinate_y in range(335, 360):
            start_game = False
            end_game = False
            fail_screen = True
        if coordinate_x in range(100, 150) and coordinate_y in range(460, 490):
            start_game = False
            end_game = False
            fail_screen = True
        if tank.check_collisions(walls):
            start_game = False
            end_game = False
            fail_screen = True

        button.draw_end_button(screen)
        end_game = True

    if end_game:
        coordinate_x = pygame.mouse.get_pos()[0]
        coordinate_y = pygame.mouse.get_pos()[1]

        # Time Factor
        frame_count += 1
        time_update(frame_count)


        if coordinate_x in range(440, 456) and coordinate_y in range(573, 639):
            end_game = False
            end_screen = True


    if end_screen:
        start_game = False
        end_time = frame_count//60
        screen.fill((0, 0, 0))
        button.draw_end_screen(screen)
        minutes = end_time//60
        seconds = end_time % 60
        output_string = "{0:02}:{1:02}".format(minutes, seconds)
        # Blit to the screen
        font = pygame.font.SysFont(None, 40, bold=True)
        text = font.render(output_string, True, (255, 255, 255))
        screen.blit(text, [330, 150])

    if fail_screen:
        button.draw_fail_screen(screen)



    pygame.display.flip()




