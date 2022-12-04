import pygame

class Maze:
    def __init__(self):
        self.image = pygame.image.load('images/full_dirt.png')

    def draw_maze(self, surface):
            #N-A
            surface.blit(self.image, (0, 192))

            surface.blit(self.image, (64, 192))
            surface.blit(self.image, (64, 128))
            surface.blit(self.image, (64, 64))
            surface.blit(self.image, (64, 0))

            surface.blit(self.image, (128, 0))
            surface.blit(self.image, (192, 0))

            surface.blit(self.image, (192, 64))
            surface.blit(self.image, (192, 128))
            surface.blit(self.image, (192, 192))

            surface.blit(self.image, (256, 192))
            surface.blit(self.image, (320, 192))
            surface.blit(self.image, (448, 192))
            surface.blit(self.image, (512, 192))

            surface.blit(self.image, (320, 128))
            surface.blit(self.image, (320, 64))
            surface.blit(self.image, (320, 0))

            surface.blit(self.image, (384, 128))
            surface.blit(self.image, (384, 0))
            surface.blit(self.image, (448, 0))

            surface.blit(self.image, (448, 64))
            surface.blit(self.image, (448, 128))

            # Transition
            surface.blit(self.image, (576, 192))
            surface.blit(self.image, (576, 256))
            surface.blit(self.image, (576, 288))

            surface.blit(self.image, (512, 288))
            surface.blit(self.image, (448, 288))
            surface.blit(self.image, (384, 288))
            surface.blit(self.image, (320, 288))
            surface.blit(self.image, (256, 288))
            surface.blit(self.image, (192, 288))
            surface.blit(self.image, (128, 288))
            surface.blit(self.image, (64, 288))
            surface.blit(self.image, (0, 288))

            #V-Y
            surface.blit(self.image, (0, 320))
            surface.blit(self.image, (0, 384))
            surface.blit(self.image, (0, 448))
            surface.blit(self.image, (0, 512))
            surface.blit(self.image, (0, 576))

            surface.blit(self.image, (64, 576))
            surface.blit(self.image, (128, 576))
            surface.blit(self.image, (192, 576))

            surface.blit(self.image, (192, 512))
            surface.blit(self.image, (192, 448))
            surface.blit(self.image, (192, 384))

            surface.blit(self.image, (256, 448))
            surface.blit(self.image, (320, 448))
            surface.blit(self.image, (384, 448))
            surface.blit(self.image, (448, 448))
            surface.blit(self.image, (512, 448))

            surface.blit(self.image, (320, 384))

            surface.blit(self.image, (512, 384))

            # Uses 32 to split tile down letter Y
            surface.blit(self.image, (416, 512))
            surface.blit(self.image, (416, 576))

# class Wall(object):
#
#     wall_x = [0, 64, 64, 64, 64, 128, 192, 192, 192, 192, 256, 320, 448, 512, 320, 320, 320, 384, 384, 448, 448, 448, 576, 576, 576, 512, 448, 384, 320, 256, 192, 128, 64, 0, 0, 0, 0, 0, 0, 64, 128, 192, 192, 192, 192, 256, 320, 348, 448, 512, 320, 512, 416, 416]
#     wall_y = [192, 192, 128, 64, 0, 0, 0, 64, 128, 192, 192, 192, 192, 192, 128, 64, 0, 128, 0, 0, 64, 128, 192, 256, 288, 288, 288, 288, 288, 288, 288, 288, 288, 288, 320, 384, 448, 512, 576, 576, 576, 576, 512, 448, 384, 448, 448, 448, 448, 448, 384, 384, 512, 576]
#
#     def __init__(self, pos):
#         walls.append(self)
#         self.rect = pygame.Rect(pos[0], pos[1], 16, 16)




