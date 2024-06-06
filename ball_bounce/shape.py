import random
import math

class Shape:
    def __init__(self, shape, size, speed, color_change=False, size_change=0, sides_change=0, position_change=False):
        self.shape = shape
        self.size = size
        self.speed = list(speed)
        self.position = [random.randint(self.size, 640 - self.size), random.randint(self.size, 480 - self.size)]
        self.color = (255, 255, 255)
        self.sides = 3 if self.shape == 'polygon' else None
        self.color_change = color_change
        self.size_change = size_change
        self.sides_change = sides_change
        self.position_change = position_change

    def move(self):
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]

    def bounce(self, boundary):
        if self.position[0] - self.size <= boundary.x:
            self.speed[0] = abs(self.speed[0]) * 1.01
            self.position[0] = boundary.x + self.size
            self.change_properties()
        elif self.position[0] + self.size >= boundary.x + boundary.width:
            self.speed[0] = -abs(self.speed[0]) * 1.01
            self.position[0] = boundary.x + boundary.width - self.size
            self.change_properties()
        
        if self.position[1] - self.size <= boundary.y:
            self.speed[1] = abs(self.speed[1]) * 1.01
            self.position[1] = boundary.y + self.size
            self.change_properties()
        elif self.position[1] + self.size >= boundary.y + boundary.height:
            self.speed[1] = -abs(self.speed[1]) * 1.01
            self.position[1] = boundary.y + boundary.height - self.size
            self.change_properties()

    def change_properties(self):
        if self.color_change:
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.size = max(10, self.size + self.size_change)
        if self.sides is not None:
            self.sides = min(12, self.sides + self.sides_change)
        if self.position_change:
            self.position = [random.randint(self.size, 640 - self.size), random.randint(self.size, 480 - self.size)]
