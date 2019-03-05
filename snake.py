import pygame


yellowTile = pygame.image.load("yellow_tile.png")
orangeTile = pygame.image.load("orange_tile.png")


class snake:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.trail = []

    def moveSnake(self, direction):
        if direction != 0:
            self.trail.append(trail(self.x, self.y))
            if direction == 1:
                self.y -= 1
            elif direction == 2:
                self.x += 1
            elif direction == 3:
                self.y += 1
            elif direction == 4:
                self.x -= 1

    def updateSnake(self, key, screen):
        direction = findDirection(key)
        self.moveSnake(direction)
        for item in self.trail:
            item.draw(screen)
        screen.blit(orangeTile, (self.x, self.y))


class trail:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(yellowTile, (self.x, self.y))


def findDirection(key):
    direction = 0
    if key[pygame.K_UP]:
        direction = 1
    if key[pygame.K_RIGHT]:
        direction = 2
    if key[pygame.K_DOWN]:
        direction = 3
    if key[pygame.K_LEFT]:
        direction = 4
    return direction
