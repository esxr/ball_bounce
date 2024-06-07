import random
import math

class Shape:
    def __init__(self, config):
        self.shape = config["shape"]
        self.size = float(config.get("initial_size", 20))
        self.speed = [float(config.get("initial_speed_x", 5)), float(config.get("initial_speed_y", 5))]
        self.position = [random.randint(int(self.size), 640 - int(self.size)), random.randint(int(self.size), 480 - int(self.size))]
        self.color = (255, 255, 255)
        self.sides = 3 if self.shape == 'polygon' else None
        self.color_change = config.get("color_change", False)
        self.size_change = config.get("size_change", 0)
        self.sides_change = config.get("sides_change", 0)
        self.speed_increase_factor = float(config.get("speed_increase_factor", 1.01))
        self.growth_rate = float(config.get("growth_rate", 0.1))
        self.carrying_capacity = float(config.get("carrying_capacity", 300))

    def move(self):
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]

    def bounce(self, boundary):
        collision = False
        max_size = min(boundary.width, boundary.height) / 2 - 5

        if self.position[0] - self.size <= boundary.x:
            self.speed[0] = abs(self.speed[0]) * self.speed_increase_factor
            self.position[0] = boundary.x + self.size
            self.change_properties(max_size)
            collision = True
        elif self.position[0] + self.size >= boundary.x + boundary.width:
            self.speed[0] = -abs(self.speed[0]) * self.speed_increase_factor
            self.position[0] = boundary.x + boundary.width - self.size
            self.change_properties(max_size)
            collision = True
        
        if self.position[1] - self.size <= boundary.y:
            self.speed[1] = abs(self.speed[1]) * self.speed_increase_factor
            self.position[1] = boundary.y + self.size
            self.change_properties(max_size)
            collision = True
        elif self.position[1] + self.size >= boundary.y + boundary.height:
            self.speed[1] = -abs(self.speed[1]) * self.speed_increase_factor
            self.position[1] = boundary.y + boundary.height - self.size
            self.change_properties(max_size)
            collision = True

        return collision

    def change_properties(self, max_size):
        if self.color_change:
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if self.size_change != 0:
            self.size += self.growth_rate * self.size * (1 - self.size / self.carrying_capacity)
        self.size = min(max(10, self.size), max_size)
        if self.sides is not None:
            self.sides = min(12, self.sides + self.sides_change)
