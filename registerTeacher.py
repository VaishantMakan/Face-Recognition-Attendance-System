from tkinter import *
from tkinter import ttk
import tkinter  # ttk is used for styling
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry


class teacherRegister:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition Attendance System")

        # ======= Variables ============

        # img1 = main background
        img1 = Image.open("Images/bg2.jpeg")
        img1 = img1.resize((1550, 900), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1550, height=900)

        # register frame
        register_frame = Frame(bg_img, bd=2, bg="white", highlightthickness=5)
        register_frame.place(x=350, y=130, width=900, height=700)

        register_frame.config(highlightbackground="black", highlightcolor="black")

        # img2 = right background
        img2 = Image.open("Images/registerTeacher.png")
        img2 = img2.resize((425, 675), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        right_img = Label(register_frame, image=self.photoimg2)
        right_img.place(x=455, y=5, width=425, height=675)

        # title
        title_lbl = Label(
            bg_img,
            text="TEACHER REGISTRATION",
            font=("times new roman", 25, "bold"),
            justify=CENTER,
            anchor=S,
            bg="black",
            fg="white",
        )
        title_lbl.place(x=350, y=105, width=900, height=30)

        # teacher ID
        teacherID_label = Label(
            register_frame,
            text="Teacher ID",
            font=("times new roman", 17),
            bg="white",
        )
        teacherID_label.place(x=10, y=30, anchor=NW)

        teacherID_entry = ttk.Entry(
            register_frame,
            # textvariable=self.var_rollNum,
            width=22,
            font=("times new roman", 13),
        )
        teacherID_entry.place(x=245, y=30, anchor=NW)

        # Name
        name_label = Label(
            register_frame,
            text="Name",
            font=("times new roman", 17),
            bg="white",
        )
        name_label.place(x=10, y=90, anchor=NW)

        name_entry = ttk.Entry(
            register_frame,
            # textvariable=self.var_name,
            width=22,
            font=("times new roman", 13),
        )
        name_entry.place(x=245, y=90, anchor=NW)

        # Phone no.
        phone_label = Label(
            register_frame,
            text="Phone No.",
            font=("times new roman", 17),
            bg="white",
        )
        phone_label.place(x=10, y=150, anchor=NW)

        phone_entry = ttk.Entry(
            register_frame,
            # textvariable=self.var_rollNum,
            width=22,
            font=("times new roman", 13),
        )
        phone_entry.place(x=245, y=150, anchor=NW)

        # Email
        email_label = Label(
            register_frame,
            text="Email (thapar.edu)",
            font=("times new roman", 17),
            bg="white",
        )
        email_label.place(x=10, y=210, anchor=NW)

        email_entry = ttk.Entry(
            register_frame,
            # textvariable=self.var_rollNum,
            width=22,
            font=("times new roman", 13),
        )
        email_entry.place(x=245, y=210, anchor=NW)

        # gender label
        gender_label = Label(
            register_frame,
            text="Gender",
            font=("times new roman", 17),
            bg="white",
        )
        gender_label.place(x=10, y=270, anchor=NW)

        # combo is used for dropdown like entering text
        gender_combo = ttk.Combobox(
            register_frame,
            # textvariable=self.var_memType,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        gender_combo["values"] = ("", "Male", "Female", "Others", "Prefer not to say")
        gender_combo.current(0)  # to give the bydeafault index

        gender_combo.place(x=245, y=270, anchor=NW)

        # course_1 label
        course_1_label = Label(
            register_frame,
            text="Course - 1",
            font=("times new roman", 17),
            bg="white",
        )
        course_1_label.place(x=10, y=330, anchor=NW)

        # combo is used for dropdown like entering text
        course_1_combo = ttk.Combobox(
            register_frame,
            # textvariable=self.var_memType,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        course_1_combo["values"] = (
            "",
            "UCS411 - AI",
            "UCS414 - CN",
            "UCS310 - DBMS",
            "UMA035 - OT",
            "UCS503 - SE",
        )
        course_1_combo.current(0)  # to give the bydeafault index

        course_1_combo.place(x=245, y=330, anchor=NW)

        # course_2 label
        course_2_label = Label(
            register_frame,
            text="Course - 2",
            font=("times new roman", 17),
            bg="white",
        )
        course_2_label.place(x=10, y=390, anchor=NW)

        # combo is used for dropdown like entering text
        course_2_combo = ttk.Combobox(
            register_frame,
            # textvariable=self.var_memType,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        course_2_combo["values"] = (
            "",
            "UCS411 - AI",
            "UCS414 - CN",
            "UCS310 - DBMS",
            "UMA035 - OT",
            "UCS503 - SE",
        )
        course_2_combo.current(0)  # to give the bydeafault index

        course_2_combo.place(x=245, y=390, anchor=NW)

        # course_3 label
        course_3_label = Label(
            register_frame,
            text="Course - 3",
            font=("times new roman", 17),
            bg="white",
        )
        course_3_label.place(x=10, y=450, anchor=NW)

        # combo is used for dropdown like entering text
        course_3_combo = ttk.Combobox(
            register_frame,
            # textvariable=self.var_memType,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        course_3_combo["values"] = (
            "",
            "UCS411 - AI",
            "UCS414 - CN",
            "UCS310 - DBMS",
            "UMA035 - OT",
            "UCS503 - SE",
        )
        course_3_combo.current(0)  # to give the bydeafault index

        course_3_combo.place(x=245, y=450, anchor=NW)

        # Password
        pass_label = Label(
            register_frame,
            text="Password",
            font=("times new roman", 17),
            bg="white",
        )
        pass_label.place(x=10, y=510, anchor=NW)

        pass_entry = ttk.Entry(
            register_frame,
            # textvariable=self.var_rollNum,
            width=22,
            font=("times new roman", 13),
        )
        pass_entry.place(x=245, y=510, anchor=NW)

        # confirmPass
        confirmPass_label = Label(
            register_frame,
            text="Confirm Password",
            font=("times new roman", 17),
            bg="white",
        )
        confirmPass_label.place(x=10, y=570, anchor=NW)

        confirmPass_entry = ttk.Entry(
            register_frame,
            # textvariable=self.var_rollNum,
            width=22,
            font=("times new roman", 13),
        )
        confirmPass_entry.place(x=245, y=570, anchor=NW)

        # -------Buttons------- #

        # save button
        save_btn = Button(
            register_frame,
            # command=self.add_data,
            width=44,
            height=2,
            text="Save Details",
            font=("times new roman", 17, "bold"),
            bg="white",
            fg="black",
        )

        save_btn.place(x=10, y=630, anchor=NW)

    # ------- Functions --------------------------------------#


if __name__ == "__main__":
    root = Tk()
    obj = teacherRegister(root)
    root.mainloop()
