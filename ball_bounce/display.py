import pygame

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

    def update_display(self, shape, color, position, size, sides=None):
        self.window.fill(self.background_color)
        if shape == 'circle':
            pygame.draw.circle(self.window, color, position, size)
        elif shape == 'rectangle':
            pygame.draw.rect(self.window, color, (position[0] - size, position[1] - size, size * 2, size * 2))
        elif shape == 'polygon' and sides:
            points = self.calculate_polygon_points(position, size, sides)
            pygame.draw.polygon(self.window, color, points)
        pygame.display.flip()

    def calculate_polygon_points(self, position, size, sides):
        points = []
        angle = 360 / sides
        for i in range(sides):
            x = position[0] + size * pygame.math.cos(pygame.math.radians(angle * i))
            y = position[1] + size * pygame.math.sin(pygame.math.radians(angle * i))
            points.append((x, y))
        return points

    def tick(self, fps):
        self.clock.tick(fps)

    def stop(self):
        pygame.quit()
