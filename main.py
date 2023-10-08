import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
from moviepy.editor import VideoFileClip

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player")

        # Create a frame for the video display
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        # Create a label for displaying video frames
        self.video_label = ttk.Label(self.frame)
        self.video_label.pack()

        self.video_clip = VideoFileClip('video.mp4'
        self.audio_clip = self.video_clip.audio

        self.update()

    def update(self):
        ret, frame = self.video_clip.read_frame()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            self.display_frame(frame)
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
