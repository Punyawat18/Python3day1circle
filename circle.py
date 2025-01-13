import pygame
import random

screen = pygame.display.set_mode((500, 500))
pygame.time.Clock().tick(10)

def move(circle):

    if circle.location[0] == 0:
        circle.status0 = "up"
    elif circle.location[0] == 500:
        circle.status0 = "down"
    if circle.location[1] == 0:
        circle.status1 = "up"
    elif circle.location[1] == 500:
        circle.status1 = "down"
    if circle.status0 == "up":
        circle.location[0] += 1
    else:
        circle.location[0] -= 1
    if circle.status1 == "up":
        circle.location[1] += 1
    else:
        circle.location[1] -= 1

    circle.color[0] = random.randint(0, 255)
    circle.color[1] = random.randint(0, 255)
    circle.color[2] = random.randint(0, 255)


class Circle:
    def __init__(self, radius, location=[500,500], color=[255, 255, 255], status0="up", status1="up"):
        self.radius = radius
        self.location = location
        self.color = color
        self.status0 = status0
        self.status1 = status1

    def draw(self):
        pygame.draw.circle(screen, self.color, self.location, self.radius)


mycircle1 = Circle(50, [0, 500])
mycircle2 = Circle(50, [500, 0])
mycircle3 = Circle(50, [500, 500])
mycircle4 = Circle(50, [0, 0])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    mycircle1.draw()
    mycircle2.draw()
    mycircle3.draw()
    mycircle4.draw()
    move(mycircle1)
    move(mycircle2)
    move(mycircle3)
    move(mycircle4)
    pygame.display.flip()
    screen.fill((0, 0, 0))

