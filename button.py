import math
import pygame.draw
from settings import *


class Button:
    def __init__(self, text, width, height, pos, rec_color, text_color, click_rec_color=RED, bottom_color=DARK_RED, elevation= 6):
        # top rec
        self.top_rec = pygame.Rect(pos, (width, height))
        self.rec_color = rec_color
        self.top_color = rec_color
        self.click_rec_color = click_rec_color
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]
        self.clicked = False
        #bottom rec
        self.bottom_rec = pygame.Rect(pos, (width, elevation))
        self.bottom_color = bottom_color

        #text
        self.text = FONT_0.render(text, True, text_color)
        self.text_rect = self.text.get_rect(center=self.top_rec.center)
        self.mode = False

    def draw(self, window):
        # elevation logic
        self.top_rec.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rec.center
        self.bottom_rec.midtop = self.top_rec.midtop
        self.bottom_rec.height = self.top_rec.height + self.dynamic_elevation

        pygame.draw.rect(window, self.bottom_color, self.bottom_rec, border_radius= 18)
        pygame.draw.rect(window, self.top_color, self.top_rec, border_radius= 18)
        window.blit(self.text, self.text_rect)

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rec.collidepoint(mouse_pos):
            self.top_color = self.click_rec_color
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                if self.pressed:
                    self.dynamic_elevation = self.elevation
                    self.clicked = True
                    self.pressed = False
        else:
            self.top_color = self.rec_color
            self.dynamic_elevation = self.elevation

    def is_btn_clicked(self):
        return self.clicked

    def win(self):
        return self.mode







