from tkinter import *

from tkinter import ttk  # ttk is used for styling

from PIL import Image, ImageTk

import os


class face_recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition Attendance System")

        # img1 = main background
        img1 = Image.open("Images/db2.png")
        img1 = img1.resize((1550, 900), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1550, height=900)

        # title
        title_lbl = Label(
            bg_img,
            text="FACE RECOGNITION ATTENDANCE SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="black",
            fg="white",
        )
        title_lbl.place(x=0, y=0, width=1550, height=45)


if __name__ == "__main__":
    root = Tk()
    obj = face_recognition_system(root)
    root.mainloop()
