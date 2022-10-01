import math
import pygame
from settings import *


class Text:
    def __init__(self, font):
        self.font = font
    def write(self, string, x, y):
        text_surface = self.font.render(string, True, COLOR_WHITE)
        WINDOW.blit(text_surface, (x, y))




