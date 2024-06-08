import cv2
import numpy as np
import pygame
from moviepy.editor import VideoFileClip, AudioFileClip
import os

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

    def combine_video_audio(self, audio_file, final_output_file):
        video_clip = VideoFileClip(self.output_file)
        audio_clip = AudioFileClip(audio_file)
        final_clip = video_clip.set_audio(audio_clip)
        final_clip.write_videofile(final_output_file, codec='libx264', audio_codec='aac')
        
        # Delete the original video file after combining
        os.remove(self.output_file)
