import pygame, sys
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
#Player images
YELLOW_SPACE_SHIP = pygame.image.load("assets/Probe.png")
YELLOW_SPACE_SHIP = pygame.transform.scale(YELLOW_SPACE_SHIP,(256,256))
Explosion = pygame.image.load("assets/Explosion.png")
Explosion = pygame.transform.scale(Explosion,(256,256))
YELLOW_LASER = pygame.image.load("assets/pixel_laser_yellow.png")

#Player, Laser Values
player_vel = 0.5
laser_vel = 5

#Wires images
nioimg = pygame.image.load('assets/Notebook ,Niobium.png')
nioimgy = 100
nioimgx = -100
nioimg = pygame.transform.scale(nioimg,(756,500))
nio_img = pygame.image.load('assets/niobium1.png')
nio_img = pygame.transform.scale(nio_img,(500,300))

nio_img_pt = pygame.image.load('assets/nio_img_pt.png')
nio_img_pt = pygame.transform.scale(nio_img_pt,(100,100))


cuimg = pygame.image.load('assets/Notebook ,Copper.png')
cuimgy = 100
cuimgx = -100
cuimg = pygame.transform.scale(cuimg,(756,500))
cu_img = pygame.image.load('assets/copper_ ahmed.png')
cu_img = pygame.transform.scale(cu_img,(500,300))
cu_img_pt = pygame.image.load('assets/copper_pt.png')
cu_img_pt = pygame.transform.scale(cu_img_pt,(100,100))


#Shield Images
carbonimg = pygame.image.load('assets/Notebook ,Carbon.png')
carbonimgy = 100
carbonimgx = -100
carbonimg = pygame.transform.scale(carbonimg,(756,500))
carbon_img = pygame.image.load('assets/Solar-Probe-illustration_carbon2.png')
carbon_imgy = 80
carbon_imgx = 460
carbon_img = pygame.transform.scale(carbon_img,(800,500))

siliconimg = pygame.image.load('assets/Notebook ,Silicon.png')
siliconimgy = 100
siliconimgx = -100
siliconimg = pygame.transform.scale(siliconimg,(756,500))
silicon_img = pygame.image.load('assets/Solar-Probe-illustration_silicon2.png')
silicon_img = pygame.transform.scale(silicon_img,(800,500))
#Cup Images
ironimg = pygame.image.load('assets/Notebook ,iron.png')
ironimgy = 100
ironimgx = -100
ironimg = pygame.transform.scale(ironimg,(756,500))
iron_img = pygame.image.load('assets/iron.png')
iron_img = pygame.transform.scale(iron_img,(500,300))
iron_img_pt = pygame.image.load('assets/iron_pt.png')
iron_img_pt = pygame.transform.scale(iron_img_pt,(100,100))

tungimg = pygame.image.load('assets/Notebook ,Tungsten.png')
tungimgy = 100
tungimgx = -100
tungimg = pygame.transform.scale(tungimg,(756,500))
tung_img = pygame.image.load('assets/tungsten.png')
tung_img = pygame.transform.scale(tung_img,(500,300))
tung_img_pt = pygame.image.load('assets/tungsten_pt.png')
tung_img_pt = pygame.transform.scale(tung_img_pt,(100,100))

#Player
run = True

#BackGround
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Menu")
BG_1 = pygame.image.load("assets/bg.png")
BG_1 = pygame.transform.scale(BG_1,(WIDTH,HEIGHT))

#Materials Backgrounds
Materials_BG = pygame.image.load("assets/Main_BG.jpg")
Materials_BG = pygame.transform.scale(Materials_BG,(WIDTH,HEIGHT))
#text buttons
Text_box = pygame.image.load('assets/Text_box.png')
Text_box = pygame.transform.scale(Text_box,(500,220))
Text_box_1 = pygame.image.load('assets/Text_box_g3.png')
Text_box_1 = pygame.transform.scale(Text_box_1,(300,200))
#text box
astronaut = pygame.image.load('assets/astronaut.png')
astronaut = pygame.transform.scale(astronaut,(250,100))
Text_box_2 = pygame.image.load('assets/Quotes.jpeg')


#لPlay Backgrou
Play_BG = pygame.image.load("assets/abstract-blue-sky-background-with-tiny-clouds-free-photo.jpg")
Play_BG = pygame.transform.scale(Play_BG,(WIDTH,HEIGHT))

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)