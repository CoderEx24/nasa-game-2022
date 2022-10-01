import pygame
import sys
import math
from pyvidplayer import Video
from mars import mars_fun
from venus import venus_fun
from jupiter import jupiter_fun
from settings import *
from near_to_sun import *
from planet import Planet
import time
from text import Text
from button import Button
from dangers import Player


def solar_system_simulation():
    run = True
    pause = False
    show_distance = False
    neartosun = False
    clock = pygame.time.Clock()
    move_x = 0
    move_y = 0
    draw_line = True

    # Metric from: https://nssdc.gsfc.nasa.gov/planetary/factsheet/

    sun = Planet("sun", 0, 0, 30 * Planet.SCALE * 10 ** 9, COLOR_SUN, 1.98892 * 10 ** 30)
    sun.sun = True

    mercury = Planet("mercury", -0.387 * Planet.AU, 0, 5 * Planet.SCALE * 10 ** 9, COLOR_MERCURY, 3.30 * 10 ** 23)
    mercury.y_vel = 47.4 * 1000

    venus = Planet("venus", -0.723 * Planet.AU, 0, 9 * Planet.SCALE * 10 ** 9, COLOR_VENUS, 4.8685 * 10 ** 24)
    venus.y_vel = 35.02 * 1000

    earth = Planet("earth", -1 * Planet.AU, 0, 10 * Planet.SCALE * 10 ** 9, COLOR_EARTH, 5.9722 * 10 ** 24)
    earth.y_vel = 29.783 * 1000

    mars = Planet("mars", -1.524 * Planet.AU, 0, 5 * Planet.SCALE * 10 ** 9, COLOR_MARS, 6.39 * 10 ** 23)
    mars.y_vel = 24.077 * 1000

    jupiter = Planet("jupiter", -5.204 * Planet.AU, 0, 20 * Planet.SCALE * 10 ** 9, COLOR_JUPITER, 1.898 * 10 ** 27)
    jupiter.y_vel = 13.06 * 1000

    saturn = Planet("saturn", -9.573 * Planet.AU, 0, 18 * Planet.SCALE * 10 ** 9, COLOR_SATURN, 5.683 * 10 ** 26)
    saturn.y_vel = 9.68 * 1000

    uranus = Planet("uranus", -19.165 * Planet.AU, 0, 14 * Planet.SCALE * 10 ** 9, COLOR_URANUS, 8.681 * 10 ** 25)
    uranus.y_vel = 6.80 * 1000

    neptune = Planet("neptune", -30.178 * Planet.AU, 0, 12 * Planet.SCALE * 10 ** 9, COLOR_NEPTUNE, 1.024 * 10 ** 26)
    neptune.y_vel = 5.43 * 1000

    planets = [neptune, uranus, saturn, jupiter, mars, earth, venus, mercury, sun]

    text = Text(FONT_2)
    venus_button = Button("Venus", 120, 40, (45, 390), COLOR_VENUS, WHITE, COLOR_LIGHT_VENUS, COLOR_DARK_VENUS)
    mars_button = Button("Mars", 120, 40, (45, 490), RED, WHITE, COLOR_MARS)
    jupiter_button = Button("Jupiter", 120, 40, (45, 590), COLOR_DARK_JUPITER, WHITE, COLOR_JUPITER, COLOR_DARKER_JUPITER)
    space_counter = 0
    space_counter2 = 0

    while run:
        clock.tick(FPS)
        WINDOW.blit(BG, (0,0))

        # WINDOW.fill(COLOR_UNIVERSE)

        for planet in planets:
            if not pause:
                planet.update_position(planets)
                # planet.clicking()
            if show_distance:
                planet.draw(WINDOW, 1, move_x, move_y, draw_line)
            else:
                planet.draw(WINDOW, 0, move_x, move_y, draw_line)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and
                                             (event.key == pygame.K_x or event.key == pygame.K_ESCAPE)):
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                pause = not pause
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                show_distance = not show_distance
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                move_x, move_y = -sun.x * sun.SCALE, -sun.y * sun.SCALE
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                draw_line = not draw_line
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                Planet.SCALE *= 0.75
                for planet in planets:
                    planet.update_scale(0.75)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                Planet.SCALE *= 1.25
                for planet in planets:
                    planet.update_scale(1.25)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                space_counter += 2
                if space_counter % 3 == 0:
                    space_counter2 += 6

        keys = pygame.key.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        window_w, window_h = pygame.display.get_surface().get_size()
        distance = 10
        if keys[pygame.K_LEFT] or mouse_x == 0:
            move_x += distance
        if keys[pygame.K_RIGHT] or mouse_x == window_w - 1:
            move_x -= distance
        if keys[pygame.K_UP] or mouse_y == 0:
            move_y += distance
        if keys[pygame.K_DOWN] or mouse_y == window_h - 1:
            move_y -= distance

#  Story text part
        if space_counter2 < 43:
            if space_counter > 4:
                space_counter = 0
            if space_counter >= 0:
                if STORY_LIST[1 + space_counter2] == 1:
                    text.write(STORY_LIST[0 + space_counter2], WIDTH - 700, 30)
                elif STORY_LIST[1 + space_counter2] == 2:
                    text_surface = FONT_0.render(STORY_LIST[0 + space_counter2], True, RED)
                    WINDOW.blit(text_surface, (WIDTH - 500, 26))
            if space_counter >= 2:
                if STORY_LIST[3 + space_counter2] == 1:
                    text.write(STORY_LIST[2 + space_counter2], WIDTH - 700, 60)
                elif STORY_LIST[3 + space_counter2] == 0:
                    text.write(STORY_LIST[2 + space_counter2], WIDTH - 503, 30)
            if space_counter == 4:
                if STORY_LIST[3 + space_counter2] == 1:
                    text.write(STORY_LIST[4 + space_counter2], WIDTH - 700, 90)
                elif STORY_LIST[3 + space_counter2] == 0:
                    text.write(STORY_LIST[4 + space_counter2], WIDTH - 700, 60)

# features on the left of the screen

        fps_text = FONT_1.render("FPS: " + str(int(clock.get_fps())), True, COLOR_WHITE)
        WINDOW.blit(fps_text, (15, 15))
        text_surface = FONT_1.render("Press X or ESC to exit", True, COLOR_WHITE)
        WINDOW.blit(text_surface, (15, 45))
        text_surface = FONT_1.render("Press D to turn on/off distance", True, COLOR_WHITE)
        WINDOW.blit(text_surface, (15, 75))
        text_surface = FONT_1.render("Press S to turn on/off drawing orbit lines", True, COLOR_WHITE)
        WINDOW.blit(text_surface, (15, 105))
        text_surface = FONT_1.render("Use mouse or arrow keys to move around", True, COLOR_WHITE)
        WINDOW.blit(text_surface, (15, 135))
        text_surface = FONT_1.render("Press C to center", True, COLOR_WHITE)
        WINDOW.blit(text_surface, (15, 165))
        text_surface = FONT_1.render("Press F to pause/unpause", True, COLOR_WHITE)
        WINDOW.blit(text_surface, (15, 195))
        text_surface = FONT_1.render("Press SPACE to continue reading ", True, COLOR_WHITE)
        WINDOW.blit(text_surface, (15, 225))
        text_surface = FONT_1.render("Use scroll-wheel to zoom", True, COLOR_WHITE)
        WINDOW.blit(text_surface, (15, 255))

# planets buttons

        if space_counter2 < 40:
            mercury_surface = FONT_1.render("- Mercury", True, COLOR_MERCURY)
            WINDOW.blit(mercury_surface, (15, 315))
            venus_surface = FONT_1.render("- Venus", True, COLOR_VENUS)
            WINDOW.blit(venus_surface, (15, 345))
            earth_surface = FONT_1.render("- Earth", True, COLOR_EARTH)
            WINDOW.blit(earth_surface, (15, 375))
            mars_surface = FONT_1.render("- Mars", True, COLOR_MARS)
            WINDOW.blit(mars_surface, (15, 405))
            jupiter_surface = FONT_1.render("- Jupiter", True, COLOR_JUPITER)
            WINDOW.blit(jupiter_surface, (15, 435))
            saturn_surface = FONT_1.render("- Saturn", True, COLOR_SATURN)
            WINDOW.blit(saturn_surface, (15, 465))
            uranus_surface = FONT_1.render("- Uranus", True, COLOR_URANUS)
            WINDOW.blit(uranus_surface, (15, 495))
            neptune_surface = FONT_1.render("- Neptune", True, COLOR_NEPTUNE)
            WINDOW.blit(neptune_surface, (15, 525))

        else:
            mars_button.draw(WINDOW)
            mars_button.check_click()
            jupiter_button.draw(WINDOW)
            jupiter_button.check_click()
            venus_button.draw(WINDOW)
            venus_button.check_click()

        if mars_button.is_btn_clicked() or jupiter_button.is_btn_clicked() or venus_button.is_btn_clicked():
            execute_plant_journey()
        if mars_button.is_btn_clicked():
            mars_button.mode = mars_fun()
            mars_button.clicked = False

        if venus_button.is_btn_clicked():
            venus_button.mode = venus_fun()
            venus_button.clicked = False

        if jupiter_button.is_btn_clicked():
            jupiter_button.mode = jupiter_fun()
            jupiter_button.clicked = False

        if venus_button.mode or jupiter_button.mode:
            vidvid()
            venus_button.mode = False
            jupiter_button.mode = False
            neartosun = True
        if neartosun == True :
            main()

        pygame.display.update()

    pygame.quit()


def execute_plant_journey():
    run = True
    space_counter3 = 0
    space_counter4 = 0
    player = Player(WIDTH/2 - 60, 630)
    i = 0
    continue_counter = 0
    text = Text(FONT_0)
    while run:
        WINDOW.blit(BG, (0, i))
        WINDOW.blit(BG, (0, - (HEIGHT - i)))
        i += 0.5
        if i == HEIGHT:
            WINDOW.blit(BG, (0, - (HEIGHT - i)))
            i = 0

        if space_counter4 < 11:
            text_surface = FONT_1.render("Press SPACE to continue reading ", True, COLOR_WHITE)
            WINDOW.blit(text_surface, (WIDTH - 350, 30))
            if space_counter3 > 4:
                space_counter3 = 0
            if space_counter3 >= 0:
                if STORY_LIST2[1 + space_counter4] == 1:
                    text.write(STORY_LIST2[0 + space_counter4], 120, 30)
            if space_counter3 >= 2:
                if STORY_LIST2[3 + space_counter4] == 1:
                    text.write(STORY_LIST2[2 + space_counter4], 120, 60)
            if space_counter3 == 4:
                if STORY_LIST2[3 + space_counter4] == 1:
                    text.write(STORY_LIST2[4 + space_counter4], 120, 90)
        else:
            player.y -= 1
            continue_counter += 1
        if continue_counter > FPS * 16:
            run = False

        player.draw(WINDOW, False)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                space_counter3 += 2
                if space_counter3 % 3 == 0:
                    space_counter4 += 6

        pygame.display.update()


def vidvid():
    vid = Video("assets/GA.mp4")
    vid.set_size((WIDTH, HEIGHT))
    run_vid = True
    while run_vid:
        vid.draw(WINDOW, (0, 0))
        text_surface = FONT_1.render("Press SPACE to pause the video", True, COLOR_WHITE)
        WINDOW.blit(text_surface, (WIDTH - 350, 30))
        text_surface = FONT_1.render("Press ESCAPE to SKIP ", True, COLOR_WHITE)
        WINDOW.blit(text_surface, (WIDTH - 350, 60))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                vid.close()
                run_vid = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                vid.toggle_pause()




