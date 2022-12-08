import pygame
end_game = False

class Tank():
    def __init__(self):
        pygame.init()
        self.image = pygame.image.load('images/tank.png')
        self.rect = self.image.get_rect()

    def move(self, coordinate):
        self.rect.center = coordinate

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def check_collisions(self, walls):
        for wall in walls:
            collide = pygame.Rect.colliderect(self.rect, wall)
            if collide:
                #print('hi')
                return True
            #else:
                #return False

    # def checkCollisionsx(self, tiles):
    #     collisions = self.get_hits(tiles)
    #     for tile in collisions:

