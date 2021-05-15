import numpy as np
import cv2

from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition Attendance System")

        # ======= Variables ============
        self.var_rollNum = StringVar()
        self.var_name = StringVar()
        var_rollNumText = StringVar()
        var_nameText = StringVar()
        var_yearText = StringVar()
        var_semesterText = StringVar()
        var_depText = StringVar()
        var_batchText = StringVar()
        var_emailText = StringVar()
        var_phoneText = StringVar()
        var_course1Text = StringVar()
        var_course2Text = StringVar()
        var_course3Text = StringVar()
        var_course4Text = StringVar()
        var_dobText = StringVar()
        var_genderText = StringVar()
        var_fatherText = StringVar()
        var_motherText = StringVar()

        # self.var_rollNum.set("101916054")
        # self.var_name.set("Hello")
        # var_rollNumText.set("Hello")
        # var_nameText.set("Hello")
        # var_yearText.set("Hello")
        # var_semesterText.set("Hello")
        # var_depText.set("Hello")
        # var_batchText.set("Hello")
        # var_emailText.set("vmakan_be19@thapar.edu")
        # var_phoneText.set("Hello")
        # var_course1Text.set("Hello")
        # var_course2Text.set("Hello")
        # var_course3Text.set("Hello")
        # var_course4Text.set("Hello")
        # var_dobText.set("11-12-2000")
        # var_genderText.set("Hello")
        # var_fatherText.set("Hello")
        # var_motherText.set("Hello")

        # img1 = main background
        img1 = Image.open("Images/wall.jpeg")
        img1 = img1.resize((1550, 900), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1550, height=900)

        # title
        title_lbl = Label(
            bg_img,
            text="ATTENDANCE DETAILS",
            font=("times new roman", 35, "bold"),
            bg="black",
            fg="white",
        )
        title_lbl.place(x=0, y=0, width=1550, height=45)

        ##########################################################

        # main frame
        main_frame = Frame(bg_img, bd=2, bg="black")
        main_frame.place(x=34, y=70, width=1480, height=800)
        # divide into label frame in main frame .... # label frame m ham title daal skte hai

        #########################################################

        # upper label frame
        upper_frame = LabelFrame(
            main_frame,
            bd=5,
            bg="white",
            relief=RAISED,
            text="Student Details",
            font=("times new roman", 12, "bold"),
        )
        upper_frame.place(x=10, y=10, width=1460, height=250)

        # img2 = thapar logo
        img2 = Image.open("Images/db2.png")
        img2 = img2.resize((700, 230), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        logo_img = Label(upper_frame, image=self.photoimg2)
        logo_img.place(x=745, y=-3, width=700, height=230)

        # Enrollment no.
        rollNum_label = Label(
            upper_frame,
            text="Enrollment Number",
            font=("times new roman", 17),
            bg="white",
        )
        rollNum_label.place(x=10, y=10, anchor=NW)

        rollNum_entry = ttk.Entry(
            upper_frame,
            # textvariable=self.var_rollNum,
            width=22,
            font=("times new roman", 13),
        )
        rollNum_entry.place(x=245, y=10, anchor=NW)

        # date
        date_label = Label(
            upper_frame,
            text="Date  (dd/mm/yyyy)",
            font=("times new roman", 17),
            bg="white",
        )
        date_label.place(x=10, y=70, anchor=NW)

        date_entry = ttk.Entry(
            upper_frame,
            # textvariable=self.var_rollNum,
            width=22,
            font=("times new roman", 13),
        )
        date_entry.place(x=245, y=70, anchor=NW)

        # status label
        status_label = Label(
            upper_frame,
            text="Status",
            font=("times new roman", 17),
            bg="white",
        )
        status_label.place(x=10, y=130, anchor=NW)

        # combo is used for dropdown like entering text
        status_combo = ttk.Combobox(
            upper_frame,
            # textvariable=self.var_memType,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        status_combo["values"] = ("", "Present", "Absent")
        status_combo.current(0)  # to give the bydeafault index

        status_combo.place(x=245, y=130, anchor=NW)

        # time
        time_label = Label(
            upper_frame,
            text="Time (hh:mm) ",
            font=("times new roman", 17),
            bg="white",
        )
        time_label.place(x=10, y=190, anchor=NW)

        time_entry = ttk.Entry(
            upper_frame,
            # textvariable=self.var_rollNum,
            width=22,
            font=("times new roman", 13),
        )
        time_entry.place(x=245, y=190, anchor=NW)

        # --- buttons --- #

        updateAttendance_btn = Button(
            upper_frame,
            width=20,
            height=3,
            text="Update Student\n  Attendance",
            font=("time new roman", 15, "bold"),
            bg="grey",
            fg="black",
        )
        updateAttendance_btn.place(x=475, y=80)

        ###########################################################################################

        # lower label
        lower_frame = LabelFrame(
            main_frame,
            bd=5,
            bg="white",
            relief=RAISED,
            text="Attendance Details",
            font=("times new roman", 12, "bold"),
        )
        lower_frame.place(x=10, y=267, width=1460, height=520)

        # ========Search System=============
        Search_frame = LabelFrame(
            lower_frame,
            bd=3,
            bg="white",
            relief=SUNKEN,
            text="Search System",
            font=("times new roman", 12, "bold"),
        )
        Search_frame.place(x=5, y=10, width=1450, height=115)

        # Label
        search_label = Label(
            Search_frame,
            text="Search By : ",
            font=("times new roman", 20, "bold"),
            height=1,
            width=15,
            relief=SUNKEN,
            bg="red",
            fg="white",
        )
        # search_label.grid(row=0, column=0, padx=10, pady=20, sticky=W)
        search_label.place(x=10, y=17)

        search_combo = ttk.Combobox(
            Search_frame,
            font=("times new roman", 13, "bold"),
            state="readonly",
            width=15,
        )
        search_combo["values"] = ("Select", "Roll No", "Phone No")
        search_combo.current(0)  # to give the bydeafault index
        search_combo.place(x=230, y=20)

        search_entry = ttk.Entry(
            Search_frame, width=25, font=("times new roman", 13, "bold")
        )
        search_entry.place(x=450, y=20)

        # Buttons
        search_btn = Button(
            Search_frame,
            width=20,
            text="Search",
            font=("time new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        search_btn.place(x=700, y=20)

        showAll_btn = Button(
            Search_frame,
            width=20,
            text="Show All",
            font=("time new roman", 15, "bold"),
            bg="grey",
            fg="black",
        )
        showAll_btn.place(x=950, y=20)

        exportAll_btn = Button(
            Search_frame,
            width=20,
            text="Export All Attendance",
            font=("time new roman", 15, "bold"),
            bg="grey",
            fg="black",
        )
        exportAll_btn.place(x=1200, y=20)

        # =========Table frame=================
        table_frame = Frame(lower_frame, bd=3, bg="white", relief=SUNKEN)
        table_frame.place(x=5, y=100, width=1450, height=395)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            column=(
                "dep",
                "course",
                "year",
                "sem",
                "roll_no",
                "name",
                "batch",
                "batch_no",
                "gender",
                "DOB",
                "email",
                "phone_no",
                "Father_contact",
                "Mother_contact",
                "photo",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)

        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)

        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("roll_no", text="Roll No")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("batch", text="Batch")
        self.student_table.heading("batch_no", text="Batch No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("DOB", text="DOB(DD-MM-YYYY")
        self.student_table.heading("email", text="Email (thapar.edu)")
        self.student_table.heading("phone_no", text="Phone Number")
        self.student_table.heading("Father_contact", text="Father's Ph.No")
        self.student_table.heading("Mother_contact", text="Mother's Ph.No")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=120)
        self.student_table.column("course", width=120)
        self.student_table.column("year", width=120)
        self.student_table.column("sem", width=120)
        self.student_table.column("roll_no", width=120)
        self.student_table.column("name", width=120)
        self.student_table.column("batch", width=120)
        self.student_table.column("batch_no", width=120)
        self.student_table.column("gender", width=120)
        self.student_table.column("DOB", width=150)
        self.student_table.column("email", width=220)
        self.student_table.column("phone_no", width=120)
        self.student_table.column("Father_contact", width=120)
        self.student_table.column("Mother_contact", width=120)
        self.student_table.column("photo", width=200)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ============================== Function Declaration ===================================#

    # =======================fetch data =================== #
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ShadowWalker77",
            database="Face_Recognition_db",
            auth_plugin="mysql_native_password",
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student_table")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)

        else:
            self.student_table.delete(*self.student_table.get_children())

        conn.commit()
        conn.close()

    # ======================= get cursor =================#

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_rollNum.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_batch.set(data[6]),
        self.var_batchNum.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_fatherNum.set(data[12]),
        self.var_motherNum.set(data[13]),
        self.var_radioButton1.set(data[14]),

        self.var_stdIdforImage = str(data[4])


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
