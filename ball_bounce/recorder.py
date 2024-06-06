import cv2
import numpy as np
import pygame

class Recorder:
    def __init__(self, width, height, output_file):
        self.width = width
        self.height = height
        self.output_file = output_file
        self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.video_writer = cv2.VideoWriter(output_file, self.fourcc, 30.0, (width, height))

    def record_frame(self, surface):
        frame = pygame.surfarray.array3d(surface)
        frame = np.rot90(frame, 3)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        self.video_writer.write(frame)

    def release(self):
        self.video_writer.release()
