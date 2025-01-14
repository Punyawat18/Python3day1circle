import pygame
import random

delay = int(input("Enter the delay: "))

screen_length = int(input("Enter the screen length in pixel: "))
screen_width = int(input("Enter the screen width in pixel: "))
screen = pygame.display.set_mode((screen_length, screen_width))

pygame.time.Clock().tick(10)

def move(circle):

    if circle.location[0] <= 0:
        circle.move_x = abs(circle.move_x)
    elif circle.location[0] >= screen_length:
        circle.move_x = -abs(circle.move_x)
    if circle.location[1] <= 0:
        circle.move_y = abs(circle.move_y)
    elif circle.location[1] >= screen_width:
        circle.move_y = -abs(circle.move_y)

    circle.location[0] += circle.move_x
    circle.location[1] += circle.move_y
    circle.delaycount += 1
    if circle.delaycount == circle.colordelay:
        circle.delaycount = 0
        circle.color[0] = random.randint(0, 255)
        circle.color[1] = random.randint(0, 255)
        circle.color[2] = random.randint(0, 255)

def draw(circle):
    pygame.draw.circle(screen, circle.color, circle.location, circle.radius)

class Circle:

    def __init__(self, radius, location, color, move_x=1, move_y=1, colordelay=0):
        self.radius = radius
        self.location = location
        self.color = color
        self.move_x = move_x
        self.move_y = move_y
        self.colordelay = colordelay
        self.delaycount = 0



allcircle = []
for i in range(int(input("Enter the number of circles: "))):
    allcircle.append(Circle(random.randint(1, 100),\
         [random.randint(1, screen_length), random.randint(1, screen_width)],\
             [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)],\
                 move_x=random.randint(1, 5), move_y=random.randint(1, 5),\
                    colordelay=random.randint(1, 100)))

while True:
    pygame.time.delay(delay)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    for circle in allcircle:
        draw(circle)
        move(circle)
    pygame.display.flip()
    screen.fill((0, 0, 0))
