from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk

from student import Student
import os

from face_recognition import Face_Recognition
from attendance import Attendance


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

        # buttons

        # img2 .. student details
        img2 = Image.open("Images/student.png")
        img2 = img2.resize((220, 220), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1 = Button(
            bg_img,
            command=self.student_details,
            image=self.photoimg2,
            cursor="hand2",
            borderwidth=3,
        )
        b1.place(x=200, y=100, width=230, height=230)

        b1_1 = Button(
            bg_img,
            command=self.student_details,
            text="Student Details",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        b1_1.place(x=200, y=300, width=230, height=40)

        # img3 .. face detector
        img3 = Image.open("Images/face_detector1.jpeg")
        img3 = img3.resize((220, 220), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b1 = Button(
            bg_img,
            command=self.face_data,
            image=self.photoimg3,
            cursor="hand2",
            borderwidth=3,
        )
        b1.place(x=650, y=100, width=230, height=230)

        b1_1 = Button(
            bg_img,
            command=self.face_data,
            text="Face Detector",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        b1_1.place(x=650, y=300, width=230, height=40)

        # img4 .. Attendance
        img4 = Image.open("Images/attendance.jpeg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(
            bg_img, command=self.attendance_data, image=self.photoimg4, cursor="hand2"
        )
        b1.place(x=1100, y=100, width=230, height=230)

        b1_1 = Button(
            bg_img,
            command=self.attendance_data,
            text="Attendance",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        b1_1.place(x=1100, y=300, width=230, height=40)

        # img5 .. Train Data
        img5 = Image.open("Images/trainData2.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b1.place(x=200, y=400, width=230, height=230)

        b1_1 = Button(
            bg_img,
            text="Train Data",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        b1_1.place(x=200, y=600, width=230, height=40)

        # img6 .. Photos
        img6 = Image.open("Images/photos.png")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(bg_img, command=self.open_img, image=self.photoimg6, cursor="hand2")
        b1.place(x=650, y=400, width=230, height=230)

        b1_1 = Button(
            bg_img,
            command=self.open_img,
            text="Photos",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        b1_1.place(x=650, y=600, width=230, height=40)

        # img7 .. Exit
        img7 = Image.open("Images/exit2.jpeg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b1.place(x=1100, y=400, width=230, height=230)

        b1_1 = Button(
            bg_img,
            text="Exit",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        b1_1.place(x=1100, y=600, width=230, height=40)

    ######################functions buttons###########################

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def open_img(self):
        os.system("open dataset")

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = face_recognition_system(root)
    root.mainloop()
