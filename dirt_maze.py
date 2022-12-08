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
            surface.blit(self.image, (576, 320))

            surface.blit(self.image, (512, 320))
            surface.blit(self.image, (448, 320))
            surface.blit(self.image, (384, 320))
            surface.blit(self.image, (320, 320))
            surface.blit(self.image, (256, 320))
            surface.blit(self.image, (192, 320))
            surface.blit(self.image, (128, 320))
            surface.blit(self.image, (64, 320))
            surface.blit(self.image, (0, 320))

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

            surface.blit(self.image, (0, 256))
            surface.blit(self.image, (256, 576))

            surface.blit(self.image, (320, 576))
            surface.blit(self.image, (384, 576))

            surface.blit(self.image, (64, 448))
            surface.blit(self.image, (128, 448))
            surface.blit(self.image, (256, 256))

class Wall(object):
    def __init__(self, pos, walls):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 2, 2)




