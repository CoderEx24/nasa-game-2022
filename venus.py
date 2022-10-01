import pygame
import os
import time
import cv2
import random
from hand_tracking import HandTracking
from settings import *
from dangers import Laser, Ship, Player, Enemy, collide
from text import Text

pygame.font.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter Tutorial")

# Background
#BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))


def venus_fun():
    run = True
    level = 0
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    enemies = []
    wave_length = 100
    enemy_vel = 13
    player_vel = 15
    player = Player(WIDTH / 2 - 100, 630)
    clock = pygame.time.Clock()
    lost = False
    win = False
    win_count = 0
    lost_count = 0
    space_count4 = 0
    space_count3 = 0
    continue_count = 0
    stat_show = False
    text = Text(FONT_1)
    i = 0
    k = 0
    hand = HandTracking()
    cap = cv2.VideoCapture(0)
    cap.set(3, 200)

    while run:
        success, image = cap.read()
        hand.display_hand(hand.scan_hands(image))
        clock.tick(FPS)

        # WINDOW.blit(BG, (0, - (2 * HEIGHT - i)))
        WINDOW.blit(BG, (0, i))
        WINDOW.blit(BG, (0, - (HEIGHT - i)))
        i += 5
        if i >= HEIGHT:
            WINDOW.blit(BG, (0, - (HEIGHT - i)))
            i = 0

        # draw text
        # level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        # WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, HEIGHT - level_label.get_height() - 10))
        if not stat_show:
            WINDOW.blit(astronaut, (k, HEIGHT / 6 + 60))
        k += 3

        if k > (WIDTH / 2 - 450):
            stat_show = True

        if space_count4 < 16 and stat_show:
            if k > (WIDTH / 2 - 250):
                text_surface = FONT_1.render("Press SPACE to continue reading ", True, COLOR_WHITE)
                WINDOW.blit(text_surface, (WIDTH - 350, 30))
            if k > (WIDTH / 2 - 350):
                text_surface = FONT_0.render("Cosmic dust", True, COLOR_WHITE)
                WINDOW.blit(text_surface, (WIDTH / 2 - text_surface.get_width() / 2 - 10, HEIGHT / 6))
            WINDOW.blit(astronaut, (WIDTH / 2 - 450, HEIGHT / 6 + 60))

            if space_count3 > 4:
                space_count3 = 0
            if space_count3 >= 0:
                if STORY_LIST4[1 + space_count4] == 1 and k > (WIDTH / 2 - 150):
                    text.write(STORY_LIST4[0 + space_count4], WIDTH/2 - 300, HEIGHT/6 + 80)
            if space_count3 >= 2:
                if STORY_LIST4[3 + space_count4] == 1:
                    text.write(STORY_LIST4[2 + space_count4], WIDTH/2 - 300, HEIGHT/6 + 120)
            if space_count3 == 4:
                if STORY_LIST3[3 + space_count4] == 1:
                    text.write(STORY_LIST4[4 + space_count4], WIDTH/2 - 300, HEIGHT/6 + 160)
        elif stat_show and space_count4 > 11:
            continue_count += 1
            for enemy in enemies:
                enemy.draw(WIN)

            if len(enemies) == 0:
                level += 1
                wave_length += 30
                for j in range(wave_length):
                    enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-2500, -100))
                    enemies.append(enemy)

        player.draw(WIN)

        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
            WIN.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))

        if win:
            win_label = lost_font.render("Congratulations!!", 1, (255, 255, 255))
            WIN.blit(win_label, (WIDTH / 2 - win_label.get_width() / 2, 200))
            win_label = lost_font.render("You have passed all the dust!!", 1, (255, 255, 255))
            WIN.blit(win_label, (WIDTH / 2 - win_label.get_width() / 2, 350))

        pygame.display.update()

        if player.health <= 0:
            lost = True
            lost_count += 1

        if level > 5:
            win = True
            win_count += 1

        if win:
            if win_count > FPS * 4:
                run = False
            else:
                continue

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and k > (WIDTH / 2 - 120):
                space_count3 += 2
                if space_count3 % 3 == 0:
                    space_count4 += 6

        keys = pygame.key.get_pressed()
        player.x, player.y = hand.get_hand_center()
        player.x -= 60
        player.y -= 60
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player.x - player_vel > 0:  # left
            player.x -= player_vel
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player.x + player_vel + player.get_width() < WIDTH:  # right
            player.x += player_vel
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and player.y - player_vel > 0: # up
            player.y -= player_vel
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player.y + player_vel + player.get_height() + 15 < HEIGHT:  # down
            player.y += player_vel

        for enemy in enemies[:]:
            enemy.move(enemy_vel)

            if collide(enemy, player):
                player.health -= 0.8
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                enemies.remove(enemy)

    return win

