import pygame
import numpy as np
import math
import colorsys

pygame.init()
W, H = 1000, 700
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("RYO | Anime Dimension Warp")

clock = pygame.time.Clock()

# 3D spiral points
points = []
for i in range(800):
    a = i * 0.12
    r = 0.02 * i
    x = r * math.cos(a)
    y = r * math.sin(a)
    z = i * 0.015
    points.append([x, y, z])

angle = 0
zoom = 1

def project(x, y, z):
    z += 5
    f = 350 / z
    return int(x * f + W//2), int(y * f + H//2)

running = True
while running:
    screen.fill((10, 10, 25))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    for i, p in enumerate(points):
        # Rotate
        rx = p[0] * math.cos(angle) - p[2] * math.sin(angle)
        rz = p[0] * math.sin(angle) + p[2] * math.cos(angle)
        ry = p[1] * math.cos(angle*0.7) - rz * math.sin(angle*0.7)
        rz2 = p[1] * math.sin(angle*0.7) + rz * math.cos(angle*0.7)

        x, y = project(rx*zoom, ry*zoom, rz2)

        hue = (i / len(points) + angle * 0.1) % 1
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
        color = (int(r*255), int(g*255), int(b*255))

        size = max(1, int(6 - rz2))
        pygame.draw.circle(screen, color, (x, y), size)

    angle += 0.015
    zoom = 1 + math.sin(angle) * 0.2

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
