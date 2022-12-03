import pygame

class Tank():
    def __init__(self):
        pygame.init()
        self.image = pygame.image.load('images/tank.png')
        self.rect = self.image.get_rect()

    def move(self, coordinate):
        self.rect.center = coordinate

    def draw(self, screen):
        screen.blit(self.image, self.rect)