import pygame
import os

WINDOW_CAPTION = "Gravity assist"
pygame.init()
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
WINDOW = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
COLOR_WHITE = (255, 255, 255)
COLOR_UNIVERSE = (36, 36, 36)
COLOR_SUN = (252, 150, 1)
COLOR_MERCURY = (173, 168, 165)
COLOR_LIGHT_VENUS = (255, 198, 68)
COLOR_VENUS = (227, 158, 28)
COLOR_DARK_VENUS = (187, 118, 0)
COLOR_EARTH = (107, 147, 214)
COLOR_MARS = (193, 68, 14)
COLOR_LIGHT_JUPITER = (216, 202, 157)
COLOR_JUPITER = (216, 202, 157)
COLOR_DARKER_JUPITER = (126, 112, 67)
COLOR_DARK_JUPITER = (166, 152, 107)
COLOR_SATURN = (191, 189, 175)
COLOR_URANUS = (209, 231, 231)
COLOR_NEPTUNE = (63, 84, 186)
FONT_0 = pygame.font.SysFont("Trebuchet MS", 26)
FONT_1 = pygame.font.SysFont("Trebuchet MS", 21)
FONT_2 = pygame.font.SysFont("Trebuchet MS", 19)
FONT_3 = pygame.font.SysFont("Trebuchet MS", 16)

pygame.display.set_caption("Solar System Simulation")

FPS = 60
YELLOW = 255, 255, 0
BLUE = 100, 149, 237
RED = 188, 39, 50
DARK_RED = 148, 0, 10
DARK_GREY = 80, 78, 81
WHITE = 255, 255, 255
BG_COLOR = 0, 0, 0
# WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.font.init()
FONT = pygame.font.SysFont("comicsans", 16)
BG = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'bg.png')), (WIDTH, HEIGHT))
sun = pygame.image.load(os.path.join('assets', 'sun.png'))
earth = pygame.image.load(os.path.join('assets', 'earth.png'))
mars = pygame.image.load(os.path.join('assets', 'mars.png'))
venus = pygame.image.load(os.path.join('assets', 'venus.png'))
mercury = pygame.image.load(os.path.join('assets', 'mercury.png'))
jupiter = pygame.image.load(os.path.join('assets', 'jupiter.png'))
saturn = pygame.image.load(os.path.join('assets', 'saturn.png'))
uranus = pygame.image.load(os.path.join('assets', 'uranus.png'))
neptune = pygame.image.load(os.path.join('assets', 'neptune.png'))

STORY_LIST = ["Hi Captain,  welcome in Gravity assist stage", 1,
              "Here you have all the solar system under your control",1,
              "Our mission here is to define the Parker’s Solar Probe orbit ",1,
              "The truth is, no rocket could supply the amount of power required, SAD :(",1,
              "But we can borrow a force from another planet, right?",1,
              "WHAT??  WHAT IS THAT??",1,
              "It sounds like science fiction",1,
              "but in reality, spacecraft can use the gravity of other planets to speed up",1,
              "like a slingshot, or to slow down, like tapping the brakes.",1,
              "And that what we call ",1,
              "GRAVITY ASSIST \(•_•)/ ", 0,
              "Our solar probe will need gravity assist form another planet to reach to the sun",1,
              "And our mission is to find the best plant for this assist",1,
              "Here Captain, we offer to you a real simulation for our solar system",1,
              "Build on Newtonian mechanics laws of motion",1,
              "You can Zoom, Move, and observe the planets motion ",1,
              "And based on your observation, we believe you will find the best choice",1,
              "Also our Nasa scientists will help you in this", 1,
              "IMPORTANT NEWS",2,
              "According to our Nasa scientists studies, We believe that…  ",1,
              "The best planet for the mission is one of those three (Jupiter, Mars, Venus)",1,
              "From the buttons on the left",1,
              "Choose the planet that you think will offer the best gravity assist", 1,
              "REMEMBER: The right planet is one of (Jupiter, Mars, Venus)", 1
              ]

STORY_LIST2 = ["Hey Captain!", 1,
               "It’s me again, sorry for interruption ", 1,
               "You have chosen your planet and its gravity to assist us to reach to the sun  ", 1,
               "But the problems didn’t end yet ", 1,
               "You will face all sorts of dangers in your journey to reach to the sun", 1,
               "At the end, you will know is that was the best choice for the gravity assist maneuver", 1,
               "And if not, you will understand why", 1]

STORY_LIST3 = ["The sun is surrounded by a thin disk of dust spread throughout the inner solar system", 1,
               "some dust are the remains of collisions that formed the planets,asteroids,", 1,
               "and comets billions of years ago", 1,

               "While some of it comes from comets ", 1,
               "when a comet gets close to the Sun, it starts heating up ", 1,
               "and begins to turn to gas, bringing dust with it ", 1,

               "Because you are moving by mars", 1,
               "You are a part of inner solar system and will face this dust", 1,
               "And your mission is to avoid this dust as much as possible", 1]

STORY_LIST4 = ["The sun is surrounded by a thin disk of dust spread throughout the inner solar system", 1,
               "some dust are the remains of collisions that formed the planets,asteroids,", 1,
               "and comets billions of years ago", 1,

               "While some of it comes from comets ", 1,
               "when a comet gets close to the Sun, it starts heating up ", 1,
               "and begins to turn to gas, bringing dust with it ", 1,

               "Because you are moving by venus", 1,
               "You are a part of inner solar system and will face this dust", 1,
               "And your mission is to avoid this dust as much as possible", 1]

STORY_LIST5 = ["The asteroidal dust are located around the asteroid belt", 1,
               "roughly between the orbits of the planets Jupiter and Mars.", 1,
               "It contains a great many solid, irregularly shaped bodies, of many sizes", 1,

               "Because you are moving by Jupiter", 1,
               "You have to pass these asteroids and asteroidal dust zone", 1,
               "And your mission is to avoid these asteroids as much as possible", 1]


# Load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

# Player player
probe = pygame.image.load(os.path.join("assets", "probe.png"))
probe = pygame.transform.scale(probe, (200, 200))

# Lasers
FLARE = pygame.transform.rotate(pygame.image.load(os.path.join("assets", "flare.png")), 180)

astronaut = pygame.image.load(os.path.join("assets", "astronaut.png"))
astronaut = pygame.transform.scale(astronaut, (150, 100))
rock = pygame.transform.rotate(pygame.image.load(os.path.join("assets", "rock1.png")), 90)

