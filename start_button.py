import pygame
import sys

class Button():
    def __init__(self):
        self.image = pygame.image.load('images/start_image.png')
        self.rect = self.image.get_rect()
        self.screen = (0, 192)

    def draw_button(self, screen):
        screen.blit(self.image, self.screen)
