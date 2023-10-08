import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player")

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.video_label = ttk.Label(self.frame)
        self.video_label.pack()

        self.video_capture = cv2.VideoCapture('video.mp4') 

        self.update()

    def update(self):
        ret, frame = self.video_capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.display_frame(frame)
        else:
            # If the video ends, you can add logic to handle this event
            self.video_capture.release()

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