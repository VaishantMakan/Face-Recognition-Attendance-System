from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk


class teacherCourseSelection:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition Attendance System")

        # ======= Variables ============

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
            # textvariable=self.var_memType,
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
            # textvariable=self.var_memType,
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
            # textvariable=self.var_memType,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        batch_combo["values"] = ("", "2CS9", "2CS10", "2CS11", "2CS12")
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
            # textvariable=self.var_memType,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        course_combo["values"] = (
            "",
            "UCS411 - AI",
            "UCS414 - CN",
            "UCS310 - DBMS",
            "UMA035 - OT",
            "UCS503 - SE",
        )
        course_combo.current(0)  # to give the bydeafault index

        course_combo.place(x=275, y=200, anchor=NW)

        # ---- button ----#

        # teacherCourseSelection button
        teacherCourseSelection_btn = Button(
            bg_img,
            # command=self.add_data,
            width=27,
            height=2,
            text="PROCEED",
            font=("times new roman", 18, "bold"),
            bg="white",
            fg="black",
        )

        teacherCourseSelection_btn.place(x=650, y=520, anchor=NW)


if __name__ == "__main__":
    root = Tk()
    obj = teacherCourseSelection(root)
    root.mainloop()
