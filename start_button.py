import pygame
import sys

class Button():
    def __init__(self):
        self.start_image = pygame.image.load('images/start_image.png')
        self.end_image = pygame.image.load('images/FinishLine.png')
        self.end_screen = pygame.image.load('images/GameOver.png')
        self.rect = self.start_image.get_rect()
        self.end_rect = self.end_image
        self.end_screen = self.end_screen
        self.screen = (0, 192)

    def draw_start_button(self, screen):
        screen.blit(self.start_image, self.screen)

    def draw_end_button(self, screen):
        screen.blit(self.end_image, (416, 576))

    def draw_end_screen(self, screen):
        screen.blit(self.end_screen, (0, 0))