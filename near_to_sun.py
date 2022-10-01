import pygame
import cv2
import os
import time
import random
from hand_tracking import HandTracking

pygame.font.init()
pygame.init()
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("One Sun, Five Invaders")

#مركبة اللاعب
Probe_SHIP = pygame.image.load("assets/Probe_SHIP.png")
Probe_SHIP = pygame.transform.scale(Probe_SHIP, (150, 150))
#الليزر
Flare = pygame.image.load(os.path.join("assets", "Flare.png"))
Flare = pygame.transform.scale(Flare, (90, 90))
#الخلفية
BG_2= pygame.transform.scale(pygame.image.load(os.path.join("assets", "backgr.jpg")), (WIDTH, HEIGHT))
#الشمس
sun = pygame.transform.rotate(pygame.image.load(os.path.join("assets", "SUN.png")), 270)
sun = pygame.transform.scale(sun, (1400, 400))
#الاحتياجات
wind = pygame.image.load(os.path.join("assets", "wind.png"))
switch = pygame.image.load(os.path.join("assets", "switch.png"))
magnet = pygame.image.load(os.path.join("assets", "magnet.png"))
wind = pygame.transform.scale(wind, (100, 120))
switch = pygame.transform.scale(switch, (80, 200))
magnet = pygame.transform.scale(magnet, (120, 120))


class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x - 30, self.y - 70))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not (self.y <= height and self.y >= 0)

    def collision(self,obj):
        return collide(self, obj)

class Ship:
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw (self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x + 25.5, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 20

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


class Player(Ship):
    def __init__(self, x, y, health=100):
     super().__init__(x, y, health)
     self.ship_img = Probe_SHIP
     self.laser_img = Flare
     self.mask = pygame.mask.from_surface(self.ship_img)
     self.max_health = health

     def move_lasers(self, vel, objs):
         self.cooldown()
         for laser in self.lasers:
             laser.move(vel)
             if laser.off_screen(HEIGHT):
                 self.lasers.remove(laser)
             else:
                 for obj in objs:
                     if laser.collision(obj):
                         objs.remove(obj)
                         if laser in self.lasers:
                             self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x+50, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 20
    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health / self.max_health), 10))



class Enemy(Ship):
    COLOR_MAP = {
                 "red":  wind,
                 "green":  magnet,
                 "blue": switch
                }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


def main():
    run= True
    Finish = False
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsansms", 50)
    lost_font = pygame.font.SysFont("comicsansms", 50)
    enemies = []
    wave_length = 170
    enemy_vel = 10
    player_vel = 15
    player = Player(700,500)
    clock = pygame.time.Clock()
    space_counter = 0
    lost = False
    #PLAY
    play = False
    level_1 =  True
    level_2 = True
    level_3 = True
    #before text images
    before = True
    img1 = pygame.image.load("Quotes/1 Welcoming and before the solar wind/1.jpeg")
    img1 = pygame.transform.scale(img1,(WIDTH,HEIGHT))
    img2 = pygame.image.load("Quotes/1 Welcoming and before the solar wind/2.jpeg")
    img2 = pygame.transform.scale(img2, (WIDTH, HEIGHT))
    img3 = pygame.image.load("Quotes/1 Welcoming and before the solar wind/3.jpeg")
    img3 = pygame.transform.scale(img3, (WIDTH, HEIGHT))
    img4 = pygame.image.load("Quotes/1 Welcoming and before the solar wind/4.jpeg")
    img4 = pygame.transform.scale(img4, (WIDTH, HEIGHT))
    img5 = pygame.image.load("Quotes/1 Welcoming and before the solar wind/5.jpeg")
    img5 = pygame.transform.scale(img5, (WIDTH, HEIGHT))
    img6 = pygame.image.load("Quotes/1 Welcoming and before the solar wind/6.jpeg")
    img6 = pygame.transform.scale(img6, (WIDTH, HEIGHT))
    img7 = pygame.image.load("Quotes/1 Welcoming and before the solar wind/7.jpeg")
    img7 = pygame.transform.scale(img7, (WIDTH, HEIGHT))
    #After level 1
    After_1 = False
    img11 = pygame.image.load("Quotes/2 After the Solar Wind and Before The Magnet/11.jpeg")
    img11 = pygame.transform.scale(img11,(WIDTH,HEIGHT))
    img22 = pygame.image.load("Quotes/2 After the Solar Wind and Before The Magnet/22.jpeg")
    img22 = pygame.transform.scale(img22, (WIDTH, HEIGHT))
    img33 = pygame.image.load("Quotes/2 After the Solar Wind and Before The Magnet/33.jpeg")
    img33 = pygame.transform.scale(img33, (WIDTH, HEIGHT))
    img44 = pygame.image.load("Quotes/2 After the Solar Wind and Before The Magnet/44.jpeg")
    img44 = pygame.transform.scale(img44, (WIDTH, HEIGHT))
    img55 = pygame.image.load("Quotes/2 After the Solar Wind and Before The Magnet/45.jpeg")
    img55 = pygame.transform.scale(img55, (WIDTH, HEIGHT))
    #After Level 2
    After_2 = False
    img111 = pygame.image.load("Quotes/3 After the Magnet and before the Switchbacks/111.jpeg")
    img111 = pygame.transform.scale(img111, (WIDTH, HEIGHT))
    img222 = pygame.image.load("Quotes/3 After the Magnet and before the Switchbacks/222.jpeg")
    img222 = pygame.transform.scale(img222, (WIDTH, HEIGHT))
    img333 = pygame.image.load("Quotes/3 After the Magnet and before the Switchbacks/333.jpeg")
    img333 = pygame.transform.scale(img333, (WIDTH, HEIGHT))
    img444 = pygame.image.load("Quotes/3 After the Magnet and before the Switchbacks/444.jpeg")
    img444 = pygame.transform.scale(img444, (WIDTH, HEIGHT))
    img555 = pygame.image.load("Quotes/3 After the Magnet and before the Switchbacks/555.jpeg")
    img555 = pygame.transform.scale(img555, (WIDTH, HEIGHT))
    img666 = pygame.image.load("Quotes/3 After the Magnet and before the Switchbacks/666.jpeg")
    img666 = pygame.transform.scale(img666, (WIDTH, HEIGHT))
    #After level 3 and finish
    After_3 = False
    img1111 = pygame.image.load("Quotes/Final Reward/1111.jpeg")
    img1111 = pygame.transform.scale(img1111, (WIDTH, HEIGHT))


    bar = 1
    lost_count = 0
    laser_vel = 6
    hand = HandTracking()
    cap = cv2.VideoCapture(0)
    cap.set(3, 200)

    while run:
        success, image = cap.read()
        hand.display_hand(hand.scan_hands(image))
        clock.tick(FPS)

        WIN.blit(BG_2, (0, 0))
        # هنكتب الليفل و اللايف
        level_label = main_font.render(f"Level: {level}", 1, (0, 255, 255))

        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, HEIGHT - level_label.get_height() - 10))
        WIN.blit(sun, (WIDTH / 2 - sun.get_width() / 2, - (HEIGHT / 2 - sun.get_height() / 2)))
        for enemy in enemies:
            enemy.draw(WIN)
        player.draw(WIN)
        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (0, 255, 0))
            WIN.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))
            main()

        if before:
            list = [img1,img2,img3,img4,img5,img6,img7]
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # شمال
                    space_counter+=1
            if space_counter == 1:
                WIN.blit(list[0], (0, 0))
                pygame.display.update()
            if space_counter == 2:
                WIN.blit(list[1], (0, 0))
                pygame.display.update()
            if space_counter == 3:
                WIN.blit(list[2], (0, 0))
                pygame.display.update()
            if space_counter == 4:
                WIN.blit(list[3], (0, 0))
                pygame.display.update()
            if space_counter == 5:
                WIN.blit(list[4], (0, 0))
                pygame.display.update()
            if space_counter == 6:
                WIN.blit(list[5], (0, 0))
                pygame.display.update()
            if space_counter == 7:
                WIN.blit(list[6], (0, 0))
                pygame.display.update()
            if space_counter == 8:
                space_counter = 0
                before = False
                play = True
                pygame.display.update()

        if After_1:
            list = [img11,img22,img33,img44,img55]
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # شمال
                    space_counter+=1
            if space_counter == 1:
                WIN.blit(list[0], (0, 0))
                pygame.display.update()
            if space_counter == 2:
                WIN.blit(list[1], (0, 0))
                pygame.display.update()
            if space_counter == 3:
                WIN.blit(list[2], (0, 0))
                pygame.display.update()
            if space_counter == 4:
                WIN.blit(list[3], (0, 0))
                pygame.display.update()
            if space_counter == 5:
                WIN.blit(list[4], (0, 0))
                pygame.display.update()
            if space_counter == 6:
                space_counter = 0
                After_1 = False
                play = True
                pygame.display.update()
        if After_2:
            list = [img111,img222,img333,img444,img555,img666]
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # شمال
                    space_counter+=1
                    print(space_counter)
            if space_counter == 1:
                WIN.blit(list[0], (0, 0))
                pygame.display.update()
            if space_counter == 2:
                WIN.blit(list[1], (0, 0))
                pygame.display.update()
            if space_counter == 3:
                WIN.blit(list[2], (0, 0))
                pygame.display.update()
            if space_counter == 4:
                WIN.blit(list[3], (0, 0))
                pygame.display.update()
            if space_counter == 5:
                WIN.blit(list[4], (0, 0))
                pygame.display.update()
            if space_counter == 6:
                WIN.blit(list[5], (0, 0))
                pygame.display.update()
            if space_counter == 7:
                space_counter = 0
                After_2 = False
                play = True
                pygame.display.update()
        if After_3:
            list = [img1111]
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # شمال
                    space_counter+=1
                    print(space_counter)
            if space_counter == 1:
                WIN.blit(list[0], (0, 0))
                pygame.display.update()
            if space_counter == 2:
                space_counter = 0
                After_3 = False
                play = True
                quit()

        if level == 1:
            pygame.draw.rect(WIN, (105, 225, 193), (WIDTH - 1520, 120, 30, 700), 1)
            pygame.display.flip()
        if level == 2:
            pygame.draw.rect(WIN, (105, 225, 193), (WIDTH - 1520, 120, 30, 700), 1)
            pygame.draw.rect(WIN, (105, 225, 193), (WIDTH - 1515, 585, 20, (687.25) / 3))
            pygame.display.flip()

        if level == 3:
            pygame.draw.rect(WIN, (105, 225, 193), (WIDTH - 1520, 120, 30, 700), 1)
            pygame.draw.rect(WIN, (105, 225, 193), (WIDTH - 1515, 585, 20, (687.25) / 3))
            pygame.draw.rect(WIN, (105, 225, 193), (WIDTH - 1515, 355, 20, (687.25 * 2) / 3))
            pygame.display.flip()

        if level == 4:
            pygame.draw.rect(WIN, (105, 225, 193), (WIDTH - 1520, 120, 30, 700), 1)
            pygame.draw.rect(WIN, (105, 225, 193), (WIDTH - 1515, 585, 20, (687.25) / 3))
            pygame.draw.rect(WIN, (105, 225, 193), (WIDTH - 1515, 355, 20, (687.25 * 2) / 3))
            pygame.draw.rect(WIN, (105, 225, 193), (WIDTH - 1515, 127, 20, 687.25))
            pygame.display.flip()
            finish = True


        pygame.display.update()
        if player.health <= 0:
            lost = True
            lost_count += 1
        if lost:
            if lost_count > FPS*5:
                run = False
            else:
                continue
        if play:
            if len(enemies) == 0:
                level += 1
                bar += 0.5
                wave_length += 5

                if level_1 == True:
                    if level == 1:
                        for i in range(wave_length):
                            enemy = Enemy(random.randrange(100, WIDTH - 250), random.randrange(-4000, -100), 'red')
                            enemies.append(enemy)
                    if level == 2:
                        play = False
                        level_1 = False
                        After_1 = True
                if level_2 == True:
                    if level == 2:
                        for i in range(wave_length):
                            enemy = Enemy(random.randrange(100, WIDTH - 150), random.randrange(-4000, -100), 'green')
                            enemies.append(enemy)
                    if level == 3:
                        play = False
                        level_2 = False
                        After_2 = True
                if level_3 == True:
                    if level == 3:
                        for i in range(wave_length):
                            enemy = Enemy(random.randrange(100, WIDTH - 150), random.randrange(-4000, -100), 'blue')
                            enemies.append(enemy)
                    if level == 4:
                        play = False
                        level_3 = False
                        After_3 = True

            player.x, player.y = hand.get_hand_center()
            player.x -= 60
            player.y -= 60
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    run = False
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player.x - player_vel > 0: #شمال
                player.x -= player_vel
            if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player.x + player_vel +player.get_width() < WIDTH:  # يمين
                player.x += player_vel
            if (keys[pygame.K_w] or keys[pygame.K_UP]) and player.y - player_vel > 0:  # فوق
                player.y -= player_vel
            if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player.y + player_vel + player.get_height()+ 20 < HEIGHT :  # تحت
                player.y += player_vel
            if keys[pygame.K_SPACE] or hand.hand_closed:
                player.shoot()

            for enemy in enemies[:]:
                enemy.move(enemy_vel)

                if collide(enemy, player):
                    player.health -= 5
                    enemies.remove(enemy)

                elif enemy.y + enemy.get_height() > HEIGHT:
                    enemies.remove(enemy)

            player.move_lasers(-laser_vel, enemies)



