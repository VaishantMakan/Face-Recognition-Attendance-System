from tkinter import *

from tkinter import ttk

from PIL import Image, ImageTk


class face_recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")


if __name__ == "__main__":
    root = Tk()
    obj = face_recognition_system(root)
    root.mainloop()
