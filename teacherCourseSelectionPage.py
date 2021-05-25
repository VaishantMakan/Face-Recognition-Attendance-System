from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from teacherMainPage import teacherMainPage


class teacherCourseSelection:
    def __init__(self, root, data):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition Attendance System")
        self.mydata = data
        # ======= Variables ============
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_batch = StringVar()
        self.var_course = StringVar()

        # img1 = main background
        img1 = Image.open("Images/Harvey.jpeg")
        img1 = img1.resize((1550, 900), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1550, height=900)

        # title
        title_lbl = Label(
            bg_img,
            text="TEACHER COURSE SELECTION",
            font=("times new roman", 25, "bold"),
            bg="black",
            fg="white",
        )
        title_lbl.place(x=510, y=160, width=500, height=40)

        # teacherCourseSelection frame
        teacherCourseSelection_frame = Frame(
            bg_img, bd=2, bg="white", highlightthickness=5
        )
        teacherCourseSelection_frame.place(x=510, y=220, width=500, height=275)

        teacherCourseSelection_frame.config(
            highlightbackground="black", highlightcolor="black"
        )

        # Year label
        year_label = Label(
            teacherCourseSelection_frame,
            text="Year",
            font=("times new roman", 17),
            bg="white",
        )
        year_label.place(x=50, y=50, anchor=NW)

        # combo is used for dropdown like entering text
        year_combo = ttk.Combobox(
            teacherCourseSelection_frame,
            textvariable=self.var_year,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        year_combo["values"] = ("", "I", "II", "III", "IV")
        year_combo.current(0)  # to give the bydeafault index

        year_combo.place(x=275, y=50, anchor=NW)

        # Semester label
        semester_label = Label(
            teacherCourseSelection_frame,
            text="Semester",
            font=("times new roman", 17),
            bg="white",
        )
        semester_label.place(x=50, y=100, anchor=NW)

        # combo is used for dropdown like entering text
        semester_combo = ttk.Combobox(
            teacherCourseSelection_frame,
            textvariable=self.var_sem,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        semester_combo["values"] = (
            "",
            "I",
            "II",
            "III",
            "IV",
            "V",
            "VI",
            "VII",
            "VIII",
        )
        semester_combo.current(0)  # to give the bydeafault index

        semester_combo.place(x=275, y=100, anchor=NW)

        # Batch label
        batch_label = Label(
            teacherCourseSelection_frame,
            text="Batch",
            font=("times new roman", 17),
            bg="white",
        )
        batch_label.place(x=50, y=150, anchor=NW)

        # combo is used for dropdown like entering text
        batch_combo = ttk.Combobox(
            teacherCourseSelection_frame,
            textvariable=self.var_batch,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        batch_combo["values"] = ("", "2EE9", "2CS10", "2CS11", "2CS12")
        batch_combo.current(0)  # to give the bydeafault index

        batch_combo.place(x=275, y=150, anchor=NW)

        # course label
        course_label = Label(
            teacherCourseSelection_frame,
            text="Course",
            font=("times new roman", 17),
            bg="white",
        )
        course_label.place(x=50, y=200, anchor=NW)

        # combo is used for dropdown like entering text
        course_combo = ttk.Combobox(
            teacherCourseSelection_frame,
            textvariable=self.var_course,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )

        li = []
        course_combo["values"] = (
            "",
            data[5],
            data[6],
            data[7],
        )
        course_combo.current(0)  # to give the bydeafault index

        course_combo.place(x=275, y=200, anchor=NW)

        # ---- button ----#

        # teacherCourseSelection button
        teacherCourseSelection_btn = Button(
            bg_img,
            command=self.course_selection,
            width=27,
            height=2,
            text="PROCEED",
            font=("times new roman", 18, "bold"),
            bg="white",
            fg="black",
        )

        teacherCourseSelection_btn.place(x=650, y=520, anchor=NW)

    ################################3function =========================
    def course_selection(self):
        if (
            self.var_course.get() == ""
            or self.var_batch.get() == ""
            or self.var_sem.get() == ""
            or self.var_year.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)

        else:
            data = [
                self.var_year.get(),
                self.var_sem.get(),
                self.var_batch.get(),
                self.var_course.get(),
            ]
            self.new_window = Toplevel(
                self.root
            )  # This asks where we want to open our window
            self.app = teacherMainPage(self.new_window, data)


if __name__ == "__main__":
    root = Tk()
    obj = teacherCourseSelection(root)
    root.mainloop()
