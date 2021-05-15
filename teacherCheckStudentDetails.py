import numpy as np
import cv2

from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os


class teacherCheckStudentDetails:
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
        img1 = Image.open("Images/bg_Student.jpeg")
        img1 = img1.resize((1550, 900), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1550, height=900)

        # title
        title_lbl = Label(
            bg_img,
            text="STUDENT DETAILS",
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

        # left label frame
        Left_frame = LabelFrame(
            main_frame,
            bd=5,
            bg="white",
            relief=RAISED,
            text="Student Details",
            font=("times new roman", 12, "bold"),
        )
        Left_frame.place(x=10, y=10, width=700, height=777)

        img_left = Image.open("Images/db2.png")
        img_left = img_left.resize((700, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=680, height=130)

        class_Student_frame = LabelFrame(
            Left_frame,
            bd=3,
            bg="white",
            relief=SUNKEN,
            text="Class Student Information",
            font=("times new roman", 12, "bold"),
        )
        class_Student_frame.place(x=5, y=155, width=680, height=595)

        # Enrollment no.
        rollNum_label = Label(
            class_Student_frame,
            text="Enrollment",
            font=("times new roman", 17),
            bg="white",
        )
        rollNum_label.place(x=10, y=30, anchor=NW)

        rollNum2_label = Label(
            class_Student_frame,
            text="Number",
            font=("times new roman", 17),
            bg="white",
        )
        rollNum2_label.place(x=10, y=50, anchor=NW)

        rollNum_text_label = Label(
            class_Student_frame,
            textvariable=var_rollNumText,
            font=("times new roman", 17),
            bg="white",
        )
        rollNum_text_label.place(x=150, y=30, anchor=NW)

        # Name
        name_label = Label(
            class_Student_frame,
            text="Name",
            font=("times new roman", 17),
            bg="white",
        )
        name_label.place(x=10, y=90, anchor=NW)

        name_text_label = Label(
            class_Student_frame,
            textvariable=var_nameText,
            font=("times new roman", 17),
            bg="white",
        )
        name_text_label.place(x=150, y=90, anchor=NW)

        # Year label
        year_label = Label(
            class_Student_frame,
            text="Year",
            font=("times new roman", 17),
            bg="white",
        )
        year_label.place(x=10, y=150, anchor=NW)

        year_text_label = Label(
            class_Student_frame,
            textvariable=var_yearText,
            font=("times new roman", 17),
            bg="white",
        )
        year_text_label.place(x=150, y=150, anchor=NW)

        # Semester label
        semester_label = Label(
            class_Student_frame,
            text="Semester",
            font=("times new roman", 17),
            bg="white",
        )
        semester_label.place(x=10, y=210, anchor=NW)

        semester_text_label = Label(
            class_Student_frame,
            textvariable=var_semesterText,
            font=("times new roman", 17),
            bg="white",
        )
        semester_text_label.place(x=150, y=210, anchor=NW)

        # Department label
        dep_label = Label(
            class_Student_frame,
            text="Department",
            font=("times new roman", 17),
            bg="white",
        )
        dep_label.place(x=10, y=290, anchor=NW)

        dep_text_label = Label(
            class_Student_frame,
            textvariable=var_depText,
            font=("times new roman", 17),
            bg="white",
        )
        dep_text_label.place(x=150, y=290, anchor=NW)

        # Batch label
        batch_label = Label(
            class_Student_frame,
            text="Batch",
            font=("times new roman", 17),
            bg="white",
        )
        batch_label.place(x=10, y=360, anchor=NW)

        batch_text_label = Label(
            class_Student_frame,
            textvariable=var_batchText,
            font=("times new roman", 17),
            bg="white",
        )
        batch_text_label.place(x=150, y=360, anchor=NW)

        # Email
        email_label = Label(
            class_Student_frame,
            text="Email ",
            font=("times new roman", 17),
            bg="white",
        )
        email_label.place(x=10, y=430, anchor=NW)

        # Email thapar.edu
        emailThapar_label = Label(
            class_Student_frame,
            text="(thapar.edu)",
            font=("times new roman", 17),
            bg="white",
        )
        emailThapar_label.place(x=8, y=450, anchor=NW)

        email_text_label = Label(
            class_Student_frame,
            textvariable=var_emailText,
            font=("times new roman", 17),
            bg="white",
        )
        email_text_label.place(x=150, y=440, anchor=NW)

        # Phone no.
        phone_label = Label(
            class_Student_frame,
            text="Phone No.",
            font=("times new roman", 17),
            bg="white",
        )
        phone_label.place(x=10, y=500, anchor=NW)

        phone_text_label = Label(
            class_Student_frame,
            textvariable=var_phoneText,
            font=("times new roman", 17),
            bg="white",
        )
        phone_text_label.place(x=150, y=500, anchor=NW)

        # ---------------------right-----------------------#

        # course_1 label
        course_1_label = Label(
            class_Student_frame,
            text="Course - 1",
            font=("times new roman", 17),
            bg="white",
        )
        course_1_label.place(x=400, y=30, anchor=NW)

        course_1_text_label = Label(
            class_Student_frame,
            textvariable=var_course1Text,
            font=("times new roman", 17),
            bg="white",
        )
        course_1_text_label.place(x=550, y=30, anchor=NW)

        # course_2 label
        course_2_label = Label(
            class_Student_frame,
            text="Course - 2",
            font=("times new roman", 17),
            bg="white",
        )
        course_2_label.place(x=400, y=90, anchor=NW)

        course_2_text_label = Label(
            class_Student_frame,
            textvariable=var_course2Text,
            font=("times new roman", 17),
            bg="white",
        )
        course_2_text_label.place(x=560, y=90, anchor=NW)

        # course_3 label
        course_3_label = Label(
            class_Student_frame,
            text="Course - 3",
            font=("times new roman", 17),
            bg="white",
        )
        course_3_label.place(x=400, y=150, anchor=NW)

        course_3_text_label = Label(
            class_Student_frame,
            textvariable=var_course3Text,
            font=("times new roman", 17),
            bg="white",
        )
        course_3_text_label.place(x=560, y=150, anchor=NW)

        # course_4 label
        course_4_label = Label(
            class_Student_frame,
            text="Course - 4",
            font=("times new roman", 17),
            bg="white",
        )
        course_4_label.place(x=400, y=210, anchor=NW)

        course_4_text_label = Label(
            class_Student_frame,
            textvariable=var_course4Text,
            font=("times new roman", 17),
            bg="white",
        )
        course_4_text_label.place(x=560, y=210, anchor=NW)

        # gender label
        gender_label = Label(
            class_Student_frame,
            text="Gender",
            font=("times new roman", 17),
            bg="white",
        )
        gender_label.place(x=400, y=290, anchor=NW)

        gender_text_label = Label(
            class_Student_frame,
            textvariable=var_genderText,
            font=("times new roman", 17),
            bg="white",
        )
        gender_text_label.place(x=560, y=290, anchor=NW)

        # DOB
        dob_label = Label(
            class_Student_frame,
            text="DOB",
            font=("times new roman", 15),
            bg="white",
        )
        dob_label.place(x=400, y=360, anchor=NW)

        dob_label = Label(
            class_Student_frame,
            text="(DD-MM-YYYY)",
            font=("times new roman", 15),
            bg="white",
        )
        dob_label.place(x=398, y=380, anchor=NW)

        dob_text_label = Label(
            class_Student_frame,
            textvariable=var_dobText,
            font=("times new roman", 17),
            bg="white",
        )
        dob_text_label.place(x=560, y=370, anchor=NW)

        # fatherNum
        fatherNum_label = Label(
            class_Student_frame,
            text="Father's Ph.No.",
            font=("times new roman", 17),
            bg="white",
        )
        fatherNum_label.place(x=400, y=430, anchor=NW)

        father_text_label = Label(
            class_Student_frame,
            textvariable=var_fatherText,
            font=("times new roman", 17),
            bg="white",
        )
        father_text_label.place(x=560, y=430, anchor=NW)

        # motherNum
        motherNum_label = Label(
            class_Student_frame,
            text="Mother's Ph.No.",
            font=("times new roman", 17),
            bg="white",
        )
        motherNum_label.place(x=400, y=500, anchor=NW)

        mother_text_label = Label(
            class_Student_frame,
            textvariable=var_motherText,
            font=("times new roman", 17),
            bg="white",
        )
        mother_text_label.place(x=560, y=500, anchor=NW)

        ###########################################################################################

        # right label
        Right_frame = LabelFrame(
            main_frame,
            bd=5,
            bg="white",
            relief=RAISED,
            text="Student Details",
            font=("times new roman", 12, "bold"),
        )
        Right_frame.place(x=720, y=10, width=745, height=777)

        img_right = Image.open("Images/thapar2.jpeg")
        img_right = img_right.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=720, height=130)

        # ========Search System=============
        Search_frame = LabelFrame(
            Right_frame,
            bd=3,
            bg="white",
            relief=SUNKEN,
            text="Search System",
            font=("times new roman", 12, "bold"),
        )
        Search_frame.place(x=5, y=155, width=710, height=115)

        # Label
        search_label = Label(
            Search_frame,
            text="Search By : ",
            font=("times new roman", 20, "bold"),
            height=1,
            width=12,
            relief=SUNKEN,
            bg="red",
            fg="white",
        )
        search_label.grid(row=0, column=0, padx=10, pady=20, sticky=W)

        search_combo = ttk.Combobox(
            Search_frame,
            font=("times new roman", 13, "bold"),
            state="readonly",
            width=12,
        )
        search_combo["values"] = ("Select", "Roll No", "Phone No")
        search_combo.current(0)  # to give the bydeafault index
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(
            Search_frame, width=15, font=("times new roman", 13, "bold")
        )
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        # Buttons
        search_btn = Button(
            Search_frame,
            width=14,
            text="Search",
            font=("time new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        search_btn.grid(
            row=0,
            column=3,
            padx=4,
        )

        showAll_btn = Button(
            Search_frame,
            width=14,
            text="Show All",
            font=("time new roman", 15, "bold"),
            bg="grey",
            fg="black",
        )
        showAll_btn.grid(row=0, column=4, padx=4)

        # =========Table frame=================
        table_frame = Frame(Right_frame, bd=3, bg="white", relief=SUNKEN)
        table_frame.place(x=5, y=250, width=710, height=480)

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

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("roll_no", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("batch", width=100)
        self.student_table.column("batch_no", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("email", width=200)
        self.student_table.column("phone_no", width=100)
        self.student_table.column("Father_contact", width=100)
        self.student_table.column("Mother_contact", width=100)
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
    obj = teacherCheckStudentDetails(root)
    root.mainloop()
