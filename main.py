import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import pygame
from pygame.locals import *
from moviepy.editor import VideoFileClip

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player")

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.video_label = ttk.Label(self.frame)
        self.video_label.pack()

        self.video_clip = VideoFileClip('your_video.mp4') 
        self.audio_clip = self.video_clip.audio
        self.audio_initialized = False

        self.update()

    def update(self):
        frame = self.video_clip.get_frame(self.video_clip.get_time())
        if frame is not None:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            self.display_frame(frame)

            if not self.audio_initialized:
                pygame.mixer.init()
                pygame.mixer.music.load(self.audio_clip.fps, self.audio_clip.reader.nchannels)
                pygame.mixer.music.set_volume(1.0)
                pygame.mixer.music.play()
                self.audio_initialized = True
        else:
            self.video_clip.close()

        self.root.after(10, self.update)

    def display_frame(self, frame):
        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image=image)
        self.video_label.config(image=photo)
        self.video_label.image = photo

if __name__ == "__main__":
    root = tk.Tk()
    player = VideoPlayer(root)
    root.mainloop()
