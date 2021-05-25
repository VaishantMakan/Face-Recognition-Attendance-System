from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from studentCheckDetails import studentCheckDetails
from studentCheckAttendance import studentCheckAttendance


class studentMainPage:
    def __init__(self, root, data):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition Attendance System")

        # ---- Variables --- #
        self.my_data = data

        # img1 = main background
        img1 = Image.open("Images/CoolBlues.jpeg")
        img1 = img1.resize((1550, 900), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1550, height=900)

        # title
        title_lbl = Label(
            bg_img,
            text="STUDENT PORTAL",
            font=("times new roman", 30, "bold"),
            bg="black",
            fg="white",
        )
        title_lbl.place(x=350, y=100, width=850, height=40)

        # attendance frame
        attendance_frame = Frame(bg_img, bd=2, bg="white", highlightthickness=5)
        attendance_frame.place(x=350, y=160, width=350, height=600)

        attendance_frame.config(highlightbackground="black", highlightcolor="black")

        # details frame
        details_frame = Frame(bg_img, bd=2, bg="white", highlightthickness=5)
        details_frame.place(x=850, y=160, width=350, height=600)

        details_frame.config(highlightbackground="black", highlightcolor="black")

        # img2 = Attendance image
        img2 = Image.open("Images/attendanceImage.jpeg")
        img2 = img2.resize((300, 300), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=373, y=183, width=300, height=300)

        # img3 = Details image
        img3 = Image.open("Images/studentDetails.jpeg")
        img3 = img3.resize((300, 300), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=865, y=183, width=320, height=300)

        # student button
        attendance_btn = Button(
            attendance_frame,
            command=self.attendance_is,
            width=25,
            height=6,
            text="Check My Attendance",
            font=("times new roman", 23, "bold"),
            bg="white",
            fg="black",
        )
        attendance_btn.grid(row=0, column=0)

        attendance_btn.place(x=15, y=400, anchor=NW)

        # details button
        details_btn = Button(
            details_frame,
            command=self.details,
            width=25,
            height=6,
            text="Check My Details",
            font=("times new roman", 23, "bold"),
            bg="white",
            fg="black",
        )
        details_btn.grid(row=0, column=0)

        details_btn.place(x=15, y=400, anchor=NW)

        # ============================Functions ===================================

    def attendance_is(self):
        self.new_window = Toplevel(
            self.root
        )  # This asks where we want to open our window
        self.app = studentCheckAttendance(self.new_window, self.my_data)

    def details(self):
        self.new_window = Toplevel(
            self.root
        )  # This asks where we want to open our window
        self.app = studentCheckDetails(self.new_window, self.my_data)


if __name__ == "__main__":
    root = Tk()
    obj = studentMainPage(root)
    root.mainloop()
