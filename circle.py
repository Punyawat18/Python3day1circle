import pygame
import random

screen = pygame.display.set_mode((500, 500))
pygame.time.Clock().tick(10)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    class Circle:
        def __init__(self, radius):
            self.radius = radius

        def draw(self, color, location):
            pygame.draw.circle(screen, color, location, self.radius)
            pygame.display.flip()

        def bounce(self):
            location = [500, 500]
            color = [255, 255, 255]
            status0 = "up"
            status1 = "up"
            while True:
                self.draw(color, location)
                screen.fill((0, 0, 0))
                if location[0] == 500:
                    status0 = "down"
                if location[1] == 500:
                    status1 = "down"
                if location[0] == 0:    
                    status0 = "up"
                if location[1] == 0:
                    status1 = "up"
                if status0 == "up":
                    location[0] += 1
                else:
                    location[0] -= 1
                if status1 == "up":
                    location[1] += 1
                else:
                    location[1] -= 1
                color[0] = random.randint(0, 255)
                color[1] = random.randint(0, 255)
                color[2] = random.randint(0, 255)

    mycircle = Circle(50)
    mycircle.bounce()


