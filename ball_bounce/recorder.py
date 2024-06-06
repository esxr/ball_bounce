import pygame
import cv2
import numpy as np

class Recorder:
    def __init__(self, width, height, filename):
        self.width = width
        self.height = height
        self.filename = filename
        self.video_writer = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

    def record_frame(self, window):
        frame = np.frombuffer(pygame.image.tostring(window, 'RGB'), dtype=np.uint8)
        frame = frame.reshape((self.height, self.width, 3))
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        self.video_writer.write(frame)

    def release(self):
        self.video_writer.release()
