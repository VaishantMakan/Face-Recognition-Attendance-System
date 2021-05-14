from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk


class register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition Attendance System")

        # img1 = main background
        img1 = Image.open("Images/gradientBg1.jpg")
        img1 = img1.resize((1550, 900), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1550, height=900)

        # title
        title_lbl = Label(
            bg_img,
            text="REGISTRATION PORTAL",
            font=("times new roman", 30, "bold"),
            bg="black",
            fg="white",
        )
        title_lbl.place(x=350, y=100, width=850, height=40)

        # student frame
        student_frame = Frame(bg_img, bd=2, bg="white", highlightthickness=5)
        student_frame.place(x=350, y=160, width=350, height=600)

        student_frame.config(highlightbackground="black", highlightcolor="black")

        # teacher frame
        teacher_frame = Frame(bg_img, bd=2, bg="white", highlightthickness=5)
        teacher_frame.place(x=850, y=160, width=350, height=600)

        teacher_frame.config(highlightbackground="black", highlightcolor="black")

        # img2 = student image
        img2 = Image.open("Images/student2.jpeg")
        img2 = img2.resize((300, 300), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=373, y=173, width=300, height=300)

        # img3 = teacher image
        img3 = Image.open("Images/teacher2.jpeg")
        img3 = img3.resize((300, 300), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=865, y=167, width=320, height=300)

        # student button
        student_btn = Button(
            student_frame,
            # command=self.add_data,
            width=25,
            height=6,
            text="Register As Student",
            font=("times new roman", 23, "bold"),
            bg="white",
            fg="black",
        )
        student_btn.grid(row=0, column=0)

        student_btn.place(x=15, y=400, anchor=NW)

        # teacher button
        teacher_btn = Button(
            teacher_frame,
            # command=self.add_data,
            width=25,
            height=6,
            text="Register As Teacher",
            font=("times new roman", 23, "bold"),
            bg="white",
            fg="black",
        )
        teacher_btn.grid(row=0, column=0)

        teacher_btn.place(x=15, y=400, anchor=NW)


if __name__ == "__main__":
    root = Tk()
    obj = register(root)
    root.mainloop()
