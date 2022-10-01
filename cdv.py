import pygame,sys
from Button import Button
from Cup_Material import *
from Shield_Material import *
from Constant import *
from PlayerLaser import Ship,Laser,Player


pygame.init()


player = Player(None, None,None,660,400)

#Material_Cup
def material_Iron():

    global player

    while True:

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_BACK = Button(image=None, pos=(640, 660),
                           text_input="Iron", font=get_font(40), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    player.cupp = 'iron'
                    print(player.cupp)
                    print(player.shield)
                    Materials()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    material_Tungsten()
                if event.key == pygame.K_LEFT:
                    material_Tungsten()
        pygame.display.update()

def material_Tungsten():
    global player
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Blue")

        PLAY_BACK = Button(image=None, pos=(640, 660),
                           text_input="Tungsten", font=get_font(40), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    player.cupp = 'Tungsten'
                    print(player.cupp)
                    print(player.shield)
                    Materials()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    material_Iron()
                if event.key == pygame.K_LEFT:
                    material_Iron()

        pygame.display.update()

#Material _ Shield
def material_Silicon():

    global player

    while True:

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("yellow")

        PLAY_BACK = Button(image=None, pos=(640, 660),
                           text_input="Silicon", font=get_font(40), base_color="White", hovering_color="Green")

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
                    Materials()
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
                    Materials()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    material_Plastic()
                if event.key == pygame.K_LEFT:
                    material_Plastic()
        pygame.display.update()

#Materials - Choose
def Materials():
    global player
    while True:
        SCREEN.blit(Materials_BG, (0, 0))
        Lost_TEXT = get_font(45).render("You lost bla bla bla.", True, "White")
        Lost_RECT = Lost_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(Lost_TEXT, Lost_RECT)
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(Text_box,(390,290))
        SCREEN.blit(Text_box,(390,190))
        SCREEN.blit(Text_box_1, (485, 490))
        Cup_Material = Button(image=None, pos=(640, 300),
                           text_input=f"Cup : {player.cupp}", font=get_font(20), base_color="White", hovering_color="Green")
        Cup_Material.changeColor(PLAY_MOUSE_POS)
        Cup_Material.update(SCREEN)

        Shield_Material = Button(image=None, pos=(640, 400),
                           text_input=f"Shield : {player.shield}", font=get_font(20), base_color="White", hovering_color="Green")
        Shield_Material.changeColor(PLAY_MOUSE_POS)
        Shield_Material.update(SCREEN)
        Play = Button(image=None, pos=(640, 600),
                           text_input="Play", font=get_font(30), base_color="White", hovering_color="Green")
        Play.changeColor(PLAY_MOUSE_POS)
        Play.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Cup_Material.checkForInput(PLAY_MOUSE_POS):
                    print(player.cupp)
                    print(player.shield)
                    material_Iron()
                if Play.checkForInput(PLAY_MOUSE_POS):
                    print(player.cupp)
                    print(player.shield)
                    if player.cupp != None and player.shield != None :
                        play()
                    #elif player.cupp == None and player.shield == None:
                        #Text : Appear to choose
                if Shield_Material.checkForInput(PLAY_MOUSE_POS):
                    print(player.cupp)
                    print(player.shield)
                    material_Plastic()
        pygame.display.update()
#Lost
def Lost():

    while True:
        SCREEN.fill("black")
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        Play_Again = Button(image=None, pos=(640, 600),
                              text_input="Play Again", font=get_font(40), base_color="White",
                              hovering_color="Green")
        Play_Again.changeColor(PLAY_MOUSE_POS)
        Lost_TEXT = get_font(45).render("You lost bla bla bla.", True, "White")
        Lost_RECT = Lost_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(Lost_TEXT, Lost_RECT)
        Play_Again.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Play_Again.checkForInput(PLAY_MOUSE_POS):
                    Materials()
        pygame.display.update()

def play():
    global player
    FPS = 60
    clock = pygame.time.Clock()
    i = 1

    global run
    while True:
        SCREEN.fill('blue')
        player.draw(SCREEN)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and player.x - player_vel > 0: # left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: # right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0: # up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT: # down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()
        if player.cupp == 'iron' or player.shield == 'Plastic':
            player.ship_img = YELLOW_SPACE_SHIP
            player.health = 100
            i += 1
            print(i)
            if 1000 > i >= 500:
                player.ship_img = Explosion
                player.health = 0
            if i >= 1000:
                Lost()


        pygame.display.update()
#Play
Materials()
