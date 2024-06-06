import random

class BouncingObject:
    def __init__(self, shape, size, speed, config, display_width, display_height):
        self.shape = shape
        self.color = (255, 255, 255)
        self.size = size
        self.speed = list(speed)
        self.position = [random.randint(self.size, display_width - self.size), random.randint(self.size, display_height - self.size)]
        self.sides = 3 if self.shape == 'polygon' else None
        self.color_change = config.get("color_change", False)
        self.size_change = config.get("size_change", 0)
        self.sides_change = config.get("sides_change", 0)
        self.position_change = config.get("position_change", False)
        self.rect_x = config.get("rect_x", 100)
        self.rect_y = config.get("rect_y", 100)
        self.rect_width = config.get("rect_width", 440)
        self.rect_height = config.get("rect_height", 280)

    def move_object(self):
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]

    def bounce_object(self):
        if self.position[0] - self.size <= self.rect_x or self.position[0] + self.size >= self.rect_x + self.rect_width:
            self.speed[0] = -self.speed[0] * 1.01
            self.change_properties()
        if self.position[1] - self.size <= self.rect_y or self.position[1] + self.size >= self.rect_y + self.rect_height:
            self.speed[1] = -self.speed[1] * 1.01
            self.change_properties()

    def change_properties(self):
        if self.color_change:
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.size = max(10, self.size + self.size_change)
        if self.sides is not None:
            self.sides = min(12, self.sides + self.sides_change)
        if self.position_change:
            self.position = [random.randint(self.rect_x + self.size, self.rect_x + self.rect_width - self.size),
                             random.randint(self.rect_y + self.size, self.rect_y + self.rect_height - self.size)]

