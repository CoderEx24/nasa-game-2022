import pygame,sys
from Button import Button
from Constant import *
from PlayerLaser import Ship,Laser,Player
from Cup_Material import *
from run1 import *

def material_Plastic():

    global player

    while True:

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("yellow")

        PLAY_BACK = Button(image=None, pos=(640, 660),
                           text_input="Plastic", font=get_font(40), base_color="White", hovering_color="Green")
        iron()
        cup()
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    player.shield = 'Plastic'
                    print(player.cupp)
                    print(player.shield)
                    play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    material_Carbon()
                if event.key == pygame.K_LEFT:
                    material_Carbon()
        pygame.display.update()

def material_Carbon():

    global player

    while True:

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("orange")

        PLAY_BACK = Button(image=None, pos=(640, 660),
                           text_input="Carbon", font=get_font(40), base_color="White", hovering_color="Green")
        iron()
        cup()
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    player.shield = 'Carbon'
                    print(player.cupp)
                    print(player.shield)
                    play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    material_Plastic()
                if event.key == pygame.K_LEFT:
                    material_Plastic()
        pygame.display.update()
