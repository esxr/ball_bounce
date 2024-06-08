import random
import math
import logging
import asyncio
from datetime import datetime

from pydub.generators import Sine

# Set up the logger
logger = logging.getLogger('shape_collision_logger')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('shape_collisions.log')
fh.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

# Define some random notes (frequencies in Hz)
NOTES = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]  # C4, D4, E4, F4, G4, A4, B4

class Shape:
    shape_counter = 0

    def __init__(self, config):
        Shape.shape_counter += 1
        self.identifier = Shape.shape_counter
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
        self.collisions = []
        self.note = random.choice(NOTES)

    def move(self):
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]

    async def log_collision(self):
        log_message = f"Shape ID: {self.identifier} hit the boundary with note {self.note}"
        logger.info(log_message)
        self.collisions.append((datetime.now(), self.identifier, self.note))

    async def bounce(self, boundary):
        collision = False
        max_size = min(boundary.width, boundary.height) / 2

        if self.position[0] - self.size <= boundary.x:
            self.speed[0] = abs(self.speed[0]) * self.speed_increase_factor
            self.position[0] = boundary.x + self.size
            self.change_properties(max_size)
            await self.log_collision()
            collision = True
        elif self.position[0] + self.size >= boundary.x + boundary.width:
            self.speed[0] = -abs(self.speed[0]) * self.speed_increase_factor
            self.position[0] = boundary.x + boundary.width - self.size
            self.change_properties(max_size)
            await self.log_collision()
            collision = True
        
        if self.position[1] - self.size <= boundary.y:
            self.speed[1] = abs(self.speed[1]) * self.speed_increase_factor
            self.position[1] = boundary.y + self.size
            self.change_properties(max_size)
            await self.log_collision()
            collision = True
        elif self.position[1] + self.size >= boundary.y + boundary.height:
            self.speed[1] = -abs(self.speed[1]) * self.speed_increase_factor
            self.position[1] = boundary.y + boundary.height - self.size
            self.change_properties(max_size)
            await self.log_collision()
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

    def get_collisions(self):
        return self.collisions
