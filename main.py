import pygame,sys
from Buttoon import Button1
import cv2
from Constant import *
from hand_tracking import HandTracking
from PlayerLaser import Ship, Laser, Player1
from solar_system_simulation import *

pygame.init()

player = Player1(None, None, None, 660, 400)


def material_niobium():

    global player

    while True:
        SCREEN.blit(Materials_BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BACK = Button1(image=None, pos=(800, 760),
                           text_input="Niobium", font=get_font(40), base_color="White", hovering_color="Green")

        SCREEN.blit(nioimg,(nioimgx,nioimgy))
        SCREEN.blit(nio_img, (600, 200))
        SCREEN.blit(nio_img_pt, (800, 100))
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    player.wire = 'Niobium'
                    Materials()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    material_Copper()
                if event.key == pygame.K_LEFT:
                    material_Copper()
        pygame.display.update()


def material_Copper():
    global player

    while True:
        SCREEN.blit(Materials_BG, (0, 0))
        SCREEN.blit(cu_img,(600,200))
        SCREEN.blit(cu_img_pt,(800,100))

        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK = Button1(image=None, pos=(800, 760),
                           text_input="Copper", font=get_font(40), base_color="White", hovering_color="Green")
        SCREEN.blit(cuimg,(cuimgx,cuimgy))

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    player.wire = 'Copper'
                    Materials()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    material_niobium()
                if event.key == pygame.K_LEFT:
                    material_niobium()
        pygame.display.update()


def material_Iron():

    global player

    while True:

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(Materials_BG, (0, 0))
        SCREEN.blit(ironimg,(ironimgx,ironimgy))
        SCREEN.blit(iron_img, (600, 200))
        SCREEN.blit(iron_img_pt, (800, 100))

        PLAY_BACK = Button1(image=None, pos=(800, 760),
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

        SCREEN.blit(Materials_BG, (0, 0))
        SCREEN.blit(tungimg,(tungimgx,tungimgy))
        SCREEN.blit(tung_img, (600, 200))
        SCREEN.blit(tung_img_pt, (800, 100))
        PLAY_BACK = Button1(image=None, pos=(800, 760),
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
        SCREEN.blit(Materials_BG, (0, 0))
        SCREEN.blit(silicon_img,(carbon_imgx,carbon_imgy))
        SCREEN.blit(siliconimg, (siliconimgx, siliconimgy))
        PLAY_BACK = Button1(image=None, pos=(800, 760),
                           text_input="Silicon", font=get_font(40), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    player.shield = 'Silicon'
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

        SCREEN.blit(Materials_BG, (0, 0))
        SCREEN.blit(carbonimg,(carbonimgx,carbonimgy))
        SCREEN.blit(carbon_img,(carbon_imgx,carbon_imgy))

        PLAY_BACK = Button1(image=None, pos=(800, 760),
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
                    material_Silicon()
                if event.key == pygame.K_LEFT:
                    material_Silicon()
        pygame.display.update()

#Materials - Choose
def Materials():
    global player
    space_counter = 0
    cont = True
    cont_1 = True
    cont_2 = True
    space_counter2 = 0
    while True:
        SCREEN.blit(Materials_BG, (0, 0))
        SCREEN.blit(Text_box,(500,180))
        SCREEN.blit(Text_box,(500,280))
        SCREEN.blit(Text_box,(500,380))
        SCREEN.blit(Text_box_1, (600, 600))

        list= ["press space to continue",
               "Hello captain ^_^",
               "Welcome to NASA.",
               "We've heard great things about you",
               ",and you seem to have the full support of the director.",
               "Your task for the day is to determine ",
               "the materials to construst Parker Solar Probe.",
               "Take your time getting acquainted ",
               "with list of materials some of them might be new.",
               "This is a monumental project in the field of space exploration.",
               "Choose wisely in order to guarantee the success of the mission."]

        if cont :
            Lost_TEXT = get_font(18).render(list[0], True, "White")
            Lost_RECT = Lost_TEXT.get_rect(center=(760, 90))
            SCREEN.blit(Lost_TEXT, Lost_RECT)
        if cont_1 == True:
            if space_counter >= 1:
                Lost_TEXT = get_font(18).render(list[1], True, "White")
                Lost_RECT = Lost_TEXT.get_rect(center=(760, 90))
                SCREEN.blit(Lost_TEXT, Lost_RECT)

            if space_counter >= 2:
                Lost_TEXT = get_font(18).render(list[2], True, "White")
                Lost_RECT = Lost_TEXT.get_rect(center=(760, 120))
                SCREEN.blit(Lost_TEXT, Lost_RECT)
            if space_counter >= 3:
                Lost_TEXT = get_font(18).render(list[3], True, "White")
                Lost_RECT = Lost_TEXT.get_rect(center=(760, 150))
                SCREEN.blit(Lost_TEXT, Lost_RECT)
            if space_counter >= 4:
                Lost_TEXT = get_font(18).render(list[4], True, "White")
                Lost_RECT = Lost_TEXT.get_rect(center=(760, 180))
                SCREEN.blit(Lost_TEXT, Lost_RECT)
        if cont_2 == True:
            if space_counter >= 5:
                Lost_TEXT = get_font(18).render(list[5], True, "White")
                Lost_RECT = Lost_TEXT.get_rect(center=(760, 90))
                SCREEN.blit(Lost_TEXT, Lost_RECT)
            if space_counter >= 6:
                Lost_TEXT = get_font(18).render(list[6], True, "White")
                Lost_RECT = Lost_TEXT.get_rect(center=(760, 120))
                SCREEN.blit(Lost_TEXT, Lost_RECT)
            if space_counter >= 7:
                Lost_TEXT = get_font(18).render(list[7], True, "White")
                Lost_RECT = Lost_TEXT.get_rect(center=(760, 150))
                SCREEN.blit(Lost_TEXT, Lost_RECT)
            if space_counter >= 8:
                Lost_TEXT = get_font(18).render(list[8], True, "White")
                Lost_RECT = Lost_TEXT.get_rect(center=(760, 180))
                SCREEN.blit(Lost_TEXT, Lost_RECT)

        if space_counter >= 9:
            cont_2 = False
            Lost_TEXT = get_font(18).render(list[9], True, "White")
            Lost_RECT = Lost_TEXT.get_rect(center=(760, 90))
            SCREEN.blit(Lost_TEXT, Lost_RECT)
        if space_counter >= 10:
            Lost_TEXT = get_font(18).render(list[10], True, "White")
            Lost_RECT = Lost_TEXT.get_rect(center=(760, 120))
            SCREEN.blit(Lost_TEXT, Lost_RECT)


        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        Wire_Material = Button1(image=None, pos=(750, 300),
                           text_input=f"Wires : {player.wire}", font=get_font(20), base_color="White", hovering_color="Green")
        Wire_Material.changeColor(PLAY_MOUSE_POS)
        Wire_Material.update(SCREEN)
        Cup_Material = Button1(image=None, pos=(750, 400),
                              text_input=f"Cup : {player.cupp}", font=get_font(20), base_color="White",
                              hovering_color="Green")
        Cup_Material.changeColor(PLAY_MOUSE_POS)
        Cup_Material.update(SCREEN)
        Shield_Material = Button1(image=None, pos=(750, 500),
                           text_input=f"Shield : {player.shield}", font=get_font(20), base_color="White", hovering_color="Green")
        Shield_Material.changeColor(PLAY_MOUSE_POS)
        Shield_Material.update(SCREEN)
        Play = Button1(image=None, pos=(750, 710),
                           text_input="Play", font=get_font(30), base_color="White", hovering_color="Green")
        Play.changeColor(PLAY_MOUSE_POS)
        Play.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Cup_Material.checkForInput(PLAY_MOUSE_POS):
                    material_Iron()
                if Wire_Material.checkForInput(PLAY_MOUSE_POS):
                    material_niobium()
                if Play.checkForInput(PLAY_MOUSE_POS):
                    if player.cupp != None and player.wire and player.shield != None  :
                        play()
                if Shield_Material.checkForInput(PLAY_MOUSE_POS):
                    material_Silicon()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                space_counter += 1
                cont = False
                if space_counter == 5:
                    cont_1 = False


        pygame.display.update()
#Lost:
def Lost_IPC():

    while True:
        SCREEN.fill("black")
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        Play_Again = Button1(image=None, pos=(750, 600),
                              text_input="Play Again", font=get_font(40), base_color="White",
                              hovering_color="Green")
        Play_Again.changeColor(PLAY_MOUSE_POS)
        Lost_TEXT = get_font(15).render(
            "You are FIRED!!! becuase you wasted billons of dollars in a rocket that doesn't work.", True, "White")
        Lost_RECT = Lost_TEXT.get_rect(center=(700, 260))
        SCREEN.blit(Lost_TEXT, Lost_RECT)
        Lost_TEXT_1 = get_font(15).render(
            "You should know that Copper,Silicon and Iron will melt when our ship is close to the sun!!!", True, "White")
        Lost_RECT_1 = Lost_TEXT.get_rect(center=(700, 300))
        SCREEN.blit(Lost_TEXT_1, Lost_RECT_1)
        Lost_TEXT_2 = get_font(15).render(
            "   - If we are in space, our ship won't be protected because the shield would melt!!", True,
            "White")
        Lost_RECT_2 = Lost_TEXT.get_rect(center=(700, 340))
        SCREEN.blit(Lost_TEXT_2, Lost_RECT_2)
        Lost_TEXT_3 = get_font(15).render(
            "   - Also, our ship won't send information about winds because the cup would melt!!", True,
            "White")
        Lost_RECT_3 = Lost_TEXT.get_rect(center=(700, 380))
        SCREEN.blit(Lost_TEXT_3, Lost_RECT_3)
        Lost_TEXT_4 = get_font(15).render(
            "   - Also, our ship won't work because the wires would melt!!", True,
            "White")
        Lost_RECT_4 = Lost_TEXT.get_rect(center=(700, 420))
        SCREEN.blit(Lost_TEXT_4, Lost_RECT_4)
        Play_Again.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Play_Again.checkForInput(PLAY_MOUSE_POS):
                    Materials()
        pygame.display.update()

def Lost_IP():

    while True:
        SCREEN.fill("black")
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        Play_Again = Button1(image=None, pos=(640, 600),
                              text_input="Play Again", font=get_font(40), base_color="White",
                              hovering_color="Green")
        Play_Again.changeColor(PLAY_MOUSE_POS)
        Lost_TEXT = get_font(12).render(
            "You are FIRED!!! becuase you wasted billons of dollars in a rocket that doesn't work.", True, "White")
        Lost_RECT = Lost_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(Lost_TEXT, Lost_RECT)
        Lost_TEXT_1 = get_font(12).render(
            "You should know that Silicon and Iron will melt when our ship is close to the sun!!!", True, "White")
        Lost_RECT_1 = Lost_TEXT.get_rect(center=(640, 290))
        SCREEN.blit(Lost_TEXT_1, Lost_RECT_1)
        Lost_TEXT_2 = get_font(12).render(
            "   - If we are in space, our ship won't be protected because the shield would melt!!", True,
            "White")
        Lost_RECT_2 = Lost_TEXT.get_rect(center=(640, 320))
        SCREEN.blit(Lost_TEXT_2, Lost_RECT_2)
        Lost_TEXT_3 = get_font(12).render(
            "   - Also, our ship won't send information about winds because the cup would melt!!", True,
            "White")
        Lost_RECT_3 = Lost_TEXT.get_rect(center=(640, 350))
        SCREEN.blit(Lost_TEXT_3, Lost_RECT_3)
        Play_Again.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Play_Again.checkForInput(PLAY_MOUSE_POS):
                    Materials()
        pygame.display.update()

def Lost_CP():

    while True:
        SCREEN.fill("black")
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        Play_Again = Button1(image=None, pos=(640, 600),
                              text_input="Play Again", font=get_font(40), base_color="White",
                              hovering_color="Green")
        Play_Again.changeColor(PLAY_MOUSE_POS)
        Lost_TEXT = get_font(12).render(
            "You are FIRED!!! becuase you wasted billons of dollars in a rocket that doesn't work.", True, "White")
        Lost_RECT = Lost_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(Lost_TEXT, Lost_RECT)
        Lost_TEXT_1 = get_font(12).render(
            "You should know that Silicon and copper will melt when our ship is close to the sun!!!", True, "White")
        Lost_RECT_1 = Lost_TEXT.get_rect(center=(640, 290))
        SCREEN.blit(Lost_TEXT_1, Lost_RECT_1)
        Lost_TEXT_2 = get_font(12).render(
            "   - If we are in space, our ship won't be protected because the shield would melt!!", True,
            "White")
        Lost_RECT_2 = Lost_TEXT.get_rect(center=(640, 320))
        SCREEN.blit(Lost_TEXT_2, Lost_RECT_2)
        Lost_TEXT_3 = get_font(12).render(
            "   - Also, our ship won't work because the wires would melt!!", True,
            "White")
        Lost_RECT_3 = Lost_TEXT.get_rect(center=(640, 350))
        SCREEN.blit(Lost_TEXT_3, Lost_RECT_3)
        Play_Again.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Play_Again.checkForInput(PLAY_MOUSE_POS):
                    Materials()
        pygame.display.update()

def Lost_CI():

    while True:
        SCREEN.fill("black")
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        Play_Again = Button1(image=None, pos=(640, 600),
                              text_input="Play Again", font=get_font(40), base_color="White",
                              hovering_color="Green")
        Play_Again.changeColor(PLAY_MOUSE_POS)
        Lost_TEXT = get_font(12).render(
            "You are Fired!!! becuase you wasted billons of dollars in rocket that doesn't work", True, "White")
        Lost_RECT = Lost_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(Lost_TEXT, Lost_RECT)
        Lost_TEXT_1 = get_font(12).render(
            "you should know that iron and copper will melt when our ship is close to the sun!!!", True, "White")
        Lost_RECT_1 = Lost_TEXT.get_rect(center=(640, 290))
        SCREEN.blit(Lost_TEXT_1, Lost_RECT_1)
        Lost_TEXT_2 = get_font(12).render(
            "If we are in space, our ship won't send information about winds because the cup would melt!!", True,
            "White")
        Lost_RECT_2 = Lost_TEXT.get_rect(center=(640, 320))
        SCREEN.blit(Lost_TEXT_2, Lost_RECT_2)
        Lost_TEXT_3 = get_font(12).render(
            "also our ship won't work because the wires would melt!!", True,
            "White")
        Lost_RECT_3 = Lost_TEXT.get_rect(center=(640, 350))
        SCREEN.blit(Lost_TEXT_3, Lost_RECT_3)
        Play_Again.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Play_Again.checkForInput(PLAY_MOUSE_POS):
                    Materials()
        pygame.display.update()

def Lost_C():

    while True:
        SCREEN.blit(Materials_BG,(0,0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        Play_Again = Button1(image=None, pos=(640, 600),
                              text_input="Play Again", font=get_font(40), base_color="White",
                              hovering_color="Green")
        Play_Again.changeColor(PLAY_MOUSE_POS)
        Lost_TEXT = get_font(12).render("You are Fired!!! becuase you wasted billons of dollars in rocket that doesn't work", True, "White")
        Lost_RECT = Lost_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(Lost_TEXT, Lost_RECT)
        Lost_TEXT_1 = get_font(12).render(
            "you should know that copper will melt when our ship is close to the sun!!!", True, "White")
        Lost_RECT_1 = Lost_TEXT.get_rect(center=(640, 290))
        SCREEN.blit(Lost_TEXT_1, Lost_RECT_1)
        Lost_TEXT_2 = get_font(12).render(
            "If we are in space, our ship won't work because the wires would melt!!", True, "White")
        Lost_RECT_2 = Lost_TEXT.get_rect(center=(640, 320))
        SCREEN.blit(Lost_TEXT_2, Lost_RECT_2)
        Play_Again.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Play_Again.checkForInput(PLAY_MOUSE_POS):
                    Materials()
        pygame.display.update()

def Lost_P():

    while True:
        SCREEN.blit(Materials_BG,(0,0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        Play_Again = Button1(image=None, pos=(640, 600),
                              text_input="Play Again", font=get_font(40), base_color="White",
                              hovering_color="Green")
        Play_Again.changeColor(PLAY_MOUSE_POS)
        Lost_TEXT = get_font(12).render(
            "You are Fired!!! becuase you wasted billons of dollars in rocket that doesn't work", True, "White")
        Lost_RECT = Lost_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(Lost_TEXT, Lost_RECT)
        Lost_TEXT_1 = get_font(12).render(
            "you should know that Silicon will melt when our ship is close to the sun!!!", True, "White")
        Lost_RECT_1 = Lost_TEXT.get_rect(center=(640, 290))
        SCREEN.blit(Lost_TEXT_1, Lost_RECT_1)
        Lost_TEXT_2 = get_font(12).render(
            "If we are in space, our ship won't be protected because the shield would melt!!", True, "White")
        Lost_RECT_2 = Lost_TEXT.get_rect(center=(640, 320))
        SCREEN.blit(Lost_TEXT_2, Lost_RECT_2)
        Play_Again.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Play_Again.checkForInput(PLAY_MOUSE_POS):
                    Materials()
        pygame.display.update()

def Lost_I():

    while True:
        SCREEN.blit(Materials_BG,(0,0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        Play_Again = Button1(image=None, pos=(640, 600),
                              text_input="Play Again", font=get_font(40), base_color="White",
                              hovering_color="Green")
        Play_Again.changeColor(PLAY_MOUSE_POS)
        Lost_TEXT = get_font(12).render(
            "You are Fired!!! becuase you wasted billons of dollars in rocket that doesn't work", True, "White")
        Lost_RECT = Lost_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(Lost_TEXT, Lost_RECT)
        Lost_TEXT_1 = get_font(12).render(
            "you should know that iron will melt when our ship is close to the sun!!!", True, "White")
        Lost_RECT_1 = Lost_TEXT.get_rect(center=(640, 290))
        SCREEN.blit(Lost_TEXT_1, Lost_RECT_1)
        Lost_TEXT_2 = get_font(12).render(
            "If we are in space, our ship won't send information about winds because the cup would melt!!", True, "White")
        Lost_RECT_2 = Lost_TEXT.get_rect(center=(640, 320))
        SCREEN.blit(Lost_TEXT_2, Lost_RECT_2)
        Play_Again.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Play_Again.checkForInput(PLAY_MOUSE_POS):
                    Materials()
        pygame.display.update()


#Play
def play():
    global player
    FPS = 60
    clock = pygame.time.Clock()
    i = 1
    s = 1
    key = True
    began = False
    cont = True
    finish = False
    global run
    hand = HandTracking()
    cap = cv2.VideoCapture(0)
    cap.set(3, 200)
    while True:
        if cont == True:
            success, image = cap.read()
            hand.display_hand(hand.scan_hands(image))
        SCREEN.blit(Play_BG,(0,0))
        player.draw(SCREEN)
        if finish == True :
            if player.y <= -100:
                Lost_TEXT = get_font(20).render(
                    "Congrats, You Passed the Testing Phase", True, "White")
                Lost_RECT = Lost_TEXT.get_rect(center=(700, 400))
                SCREEN.blit(Lost_TEXT, Lost_RECT)
                if player.y <= -500:
                    finish = False
        if began:
            Lost_TEXT = get_font(20).render(
                    "Testing Phase", True, "White")
            Lost_RECT = Lost_TEXT.get_rect(center=(640, 260))
            SCREEN.blit(Lost_TEXT, Lost_RECT)

            Lost_TEXT_1 = get_font(10).render(
                "Press w to move up", True, "White")
            Lost_RECT_1 = Lost_TEXT.get_rect(center=(1200, 10))
            SCREEN.blit(Lost_TEXT_1, Lost_RECT_1)


            Lost_TEXT_2 = get_font(10).render(
                "Press s to move down", True, "White")
            Lost_RECT_2 = Lost_TEXT.get_rect(center=(1200, 30))
            SCREEN.blit(Lost_TEXT_2, Lost_RECT_2)

            Lost_TEXT_3 = get_font(10).render(
                "Press a to move left", True, "White")
            Lost_RECT_3 = Lost_TEXT.get_rect(center=(1200, 50))
            SCREEN.blit(Lost_TEXT_3, Lost_RECT_3)
            Lost_TEXT_4 = get_font(10).render(
                "Press d to move right", True, "White")
            Lost_RECT_4 = Lost_TEXT.get_rect(center=(1200, 70))
            SCREEN.blit(Lost_TEXT_4, Lost_RECT_4)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()

        if key:
            keys = pygame.key.get_pressed()
            player.x, player.y = hand.get_hand_center()
            player.x -= 60
            player.y -= 60

            if keys[pygame.K_a] and player.x - player_vel > 0: # left
                player.x -= player_vel
                began = False
            if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: # right
                player.x += player_vel
                began = False
            if keys[pygame.K_w] and player.y - player_vel > 0: # up
                player.y -= player_vel
                began = False
            if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT: # down
                player.y += player_vel
                began = False

        if player.cupp == 'iron' or player.shield == 'Silicon' or player.wire == 'Copper':
            cont = True
            player.ship_img = YELLOW_SPACE_SHIP
            player.health = 100
            i += 1
            print(i)
            if i >= 150:
                key = False
                player.ship_img = Explosion
                player.health = 0
                cont = False
            if i >= 320:
                if player.cupp == 'iron' and player.shield == 'Silicon' and player.wire == 'Copper':
                    Lost_IPC()

                if player.cupp == 'iron' and player.shield == 'Silicon':
                    Lost_IP()

                if player.wire == 'Copper' and player.shield == 'Silicon':
                    Lost_CP()

                if player.wire == 'Copper' and player.cupp == 'iron':
                    Lost_CI()

                if player.wire == 'Copper':
                    Lost_C()

                if player.shield == 'Silicon':
                    Lost_P()

                if player.cupp == 'iron':
                    Lost_I()

        if player.cupp == 'Tungsten' and player.shield == 'Carbon' and player.wire == 'Niobium':
            cont = True
            player.ship_img = YELLOW_SPACE_SHIP
            player.health = 100
            s += 1
            print(s)
            if s >= 150:
                key = False
                player.y -= 2
                finish = True
                cont = False
                if s >= 700:
                    solar_system_simulation()

        pygame.display.update()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button1(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG_1, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(750, 200))

        PLAY_BUTTON = Button1(image=pygame.image.load("assets/Play Rect.png"), pos=(750, 350),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button1(image=pygame.image.load("assets/Options Rect.png"), pos=(750, 500),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button1(image=pygame.image.load("assets/Quit Rect.png"), pos=(750, 650),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Materials()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()