import math
import pygame.draw
from settings import *


class Planet:
    AU = 149.6e6 * 1000  # Astronomical unit
    G = 6.67428e-11  # Gravitational constant
    TIMESTEP = 60 * 60 * 24    # Seconds in FPS days
    SCALE = 200 / AU  # 1AU = 200 pixels
    name_map = {
        "sun": sun,
        "earth": earth,
        "mars": mars,
        "venus": venus,
        "mercury": mercury,
        "jupiter": jupiter,
        "saturn": saturn,
        "uranus": uranus,
        "neptune": neptune}

    def __init__(self, name, x, y, radius, color, mass):
        self.name = name
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0
        self.x_vel = 0
        self.y_vel = 0
        self.image = 0
        #self.rect = self.image.get_rect()
        #self.mask = pygame.mask.from_surface(self.image)
        #self.xa = x * self.SCALE + WIDTH / 2 - self.image.get_width()/2
        #self.ya = y * self.SCALE + HEIGHT / 2 - self.image.get_height()/2
        #self.rect.x += self.rect.x * self.SCALE + WIDTH / 2 - self.image.get_width()/2
        #self.rect.y = self.rect.y * self.SCALE + HEIGHT / 2 - self.image.get_height()/2

    def draw(self, window, show, move_x, move_y, draw_line):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        if len(self.orbit) > abs(10**-31 * self.distance_to_sun**3):
            self.orbit = self.orbit[int(10**-31 * self.distance_to_sun**3) - 1000:]
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x + move_x, y + move_y))
            if draw_line:
                pygame.draw.lines(window, self.color, False, updated_points, 1)
        #pygame.draw.circle(window, self.color, (x + move_x, y + move_y), self.radius)
        self.image = pygame.transform.scale(self.name_map[self.name], (self.radius * 3.5, self.radius * 3.5))
        x_m = x - self.image.get_width()/2
        y_m = y - self.image.get_height()/2

        window.blit(self.image, (x_m + move_x, y_m + move_y))
        if not self.sun:
            distance_text = FONT_3.render(f"{round(self.distance_to_sun * 1.057 * 10 ** -16, 8)} light years",
                                          True, COLOR_WHITE)
            if show:
                window.blit(distance_text, (x - distance_text.get_width() / 2 + move_x,
                                            y - distance_text.get_height() / 2 - 20 + move_y))

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        if other.sun:
            self.distance_to_sun = distance
        force = self.G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy
        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))

    def update_scale(self, scal):
        self.radius *= scal

    def clicking(self, move_x, move_y):
        self.rect.x += move_x
        self.rect.y += move_y
        pos = pygame.mouse.get_pos()
        pos_in_mask = pos[0] - self.rect.x, pos[1] - self.rect.y
        touching = self.rect.collidepoint(pos) and self.mask.get_at(pos_in_mask)

        if self.rect.collidepoint(pos):
            print(self.name)
