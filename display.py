import pygame
import math

class Display:
    def __init__(self, width, height):
        pygame.init()
        self.width, self.height = width, height
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Bouncing Object ASMR")
        self.background_color = (0, 0, 0)
        self.clock = pygame.time.Clock()
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update_display(self, shapes, boundary):
        self.window.fill(self.background_color)
        # Draw the boundary
        pygame.draw.rect(self.window, (255, 255, 255), (boundary.x, boundary.y, boundary.width, boundary.height), 2)
        # Draw each shape within the boundary
        for shape in shapes:
            if shape.shape == 'circle':
                pygame.draw.circle(self.window, shape.color, [int(coord) for coord in shape.position], int(shape.size))
            elif shape.shape == 'rectangle':
                pygame.draw.rect(self.window, shape.color, (shape.position[0] - shape.size, shape.position[1] - shape.size, shape.size * 2, shape.size * 2))
            elif shape.shape == 'polygon' and shape.sides:
                points = self.calculate_polygon_points(shape.position, shape.size, shape.sides)
                pygame.draw.polygon(self.window, shape.color, points)
        pygame.display.flip()
        return self.window.copy()

    def calculate_polygon_points(self, position, size, sides):
        points = []
        angle = 360 / sides
        for i in range(sides):
            x = position[0] + size * math.cos(math.radians(angle * i))
            y = position[1] + size * math.sin(math.radians(angle * i))
            points.append((x, y))
        return points

    def tick(self, fps):
        self.clock.tick(fps)

    def stop(self):
        pygame.quit()
