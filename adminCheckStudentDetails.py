import numpy as np
import cv2

from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os


class adminCheckStudentDetails:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition Attendance System")

        # ======= Variables ============

        self.var_rollNum = StringVar()
        self.var_name = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_dep = (
            StringVar()
        )  # department --------------------- StringVar is used in tkinter and it is a class whose function is get()
        self.var_batch = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()

        self.var_fatherNum = StringVar()
        self.var_motherNum = StringVar()
        self.var_gender = StringVar()
        self.var_course1 = StringVar()
        self.var_course2 = StringVar()
        self.var_course3 = StringVar()
        self.var_course4 = StringVar()
        self.var_old_roll = ""
        self.var_password = ""
        self.var_stdIdforImage = ""
        self.var_radioButton1 = StringVar()
        self.var_defaultDob = StringVar()
        # img1 = main background
        img1 = Image.open("Images/bg_Student.jpeg")
        img1 = img1.resize((1550, 900), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1550, height=900)

        # title
        title_lbl = Label(
            bg_img,
            text="STUDENT MANAGEMENT SYSTEM",
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
            font=("times new roman", 12, "bold"),
        )
        Left_frame.place(x=10, y=10, width=700, height=777)

        class_Student_frame = LabelFrame(
            Left_frame,
            bd=3,
            bg="white",
            relief=SUNKEN,
            text="Class Student Information",
            font=("times new roman", 12, "bold"),
        )
        class_Student_frame.place(x=5, y=0, width=675, height=750)

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

        rollNum_entry = ttk.Entry(
            class_Student_frame,
            textvariable=self.var_rollNum,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        rollNum_entry.place(x=150, y=30, anchor=NW)

        # Name
        name_label = Label(
            class_Student_frame,
            text="Name",
            font=("times new roman", 17),
            bg="white",
        )
        name_label.place(x=10, y=90, anchor=NW)

        name_entry = ttk.Entry(
            class_Student_frame,
            textvariable=self.var_name,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        name_entry.place(x=150, y=90, anchor=NW)

        # Year label
        year_label = Label(
            class_Student_frame,
            text="Year",
            font=("times new roman", 17),
            bg="white",
        )
        year_label.place(x=10, y=150, anchor=NW)

        year_combo = ttk.Combobox(
            class_Student_frame,
            textvariable=self.var_year,
            font=("times new roman", 15, "bold"),
            state="readonly",
            width=17,
        )
        year_combo["values"] = ("Select Year", "I", "II", "III")
        year_combo.current(0)  # to give the bydeafault index
        year_combo.place(x=150, y=150, anchor=NW)

        # Semester label
        semester_label = Label(
            class_Student_frame,
            text="Semester",
            font=("times new roman", 17),
            bg="white",
        )
        semester_label.place(x=10, y=210, anchor=NW)

        semester_combo = ttk.Combobox(
            class_Student_frame,
            textvariable=self.var_semester,
            font=("times new roman", 15, "bold"),
            state="readonly",
            width=17,
        )
        semester_combo["values"] = (
            "Select Semester",
            "Semester-1",
            "Semester-2",
            "Semester-3",
        )
        semester_combo.current(0)  # to give the bydeafault index
        semester_combo.place(x=150, y=210, anchor=NW)

        # Department label
        dep_label = Label(
            class_Student_frame,
            text="Department",
            font=("times new roman", 17),
            bg="white",
        )
        dep_label.place(x=10, y=290, anchor=NW)

        dep_combo = ttk.Combobox(
            class_Student_frame,
            textvariable=self.var_dep,
            font=("times new roman", 15, "bold"),
            state="readonly",
            width=17,
        )
        dep_combo["values"] = ("Select Department", "CSE", "COE", "COBS", "IT")
        dep_combo.current(0)  # to give the bydeafault index
        dep_combo.place(x=150, y=290, anchor=NW)

        # Batch label
        batch_label = Label(
            class_Student_frame,
            text="Batch",
            font=("times new roman", 17),
            bg="white",
        )
        batch_label.place(x=10, y=360, anchor=NW)

        batch_combo = ttk.Combobox(
            class_Student_frame,
            textvariable=self.var_batch,
            font=("times new roman", 15),
            state="readonly",
            width=17,
        )
        batch_combo["values"] = ("", "2EE9", "2CS10", "2CS11", "2CS12")
        batch_combo.current(0)  # to give the bydeafault index

        batch_combo.place(x=150, y=360, anchor=NW)

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

        email_entry = ttk.Entry(
            class_Student_frame,
            textvariable=self.var_email,
            width=20,
            font=("times new roman", 13),
        )
        email_entry.place(x=150, y=440, anchor=NW)

        # Phone no.
        phone_label = Label(
            class_Student_frame,
            text="Phone No.",
            font=("times new roman", 17),
            bg="white",
        )
        phone_label.place(x=10, y=500, anchor=NW)

        phone_entry = ttk.Entry(
            class_Student_frame,
            textvariable=self.var_phone,
            width=20,
            font=("times new roman", 13),
        )
        phone_entry.place(x=150, y=500, anchor=NW)

        # ---------------------right-----------------------#

        # course_1 label
        course_1_label = Label(
            class_Student_frame,
            text="Course - 1",
            font=("times new roman", 17),
            bg="white",
        )
        course_1_label.place(x=400, y=30, anchor=NW)

        course_1_combo = ttk.Combobox(
            class_Student_frame,
            textvariable=self.var_course1,
            font=("times new roman", 15),
            state="readonly",
            width=14,
        )
        course_1_combo["values"] = (
            "Select Course",
            "UCS411_AI",
            "UCS414_CN",
            "UCS310_DBMS",
            "UMA035_OT",
            "UCS503_SE",
            "ECE202_Elec",
        )
        course_1_combo.current(0)  # to give the bydeafault index

        course_1_combo.place(x=530, y=30, anchor=NW)

        # course_2 label
        course_2_label = Label(
            class_Student_frame,
            text="Course - 2",
            font=("times new roman", 17),
            bg="white",
        )
        course_2_label.place(x=400, y=90, anchor=NW)

        course_2_combo = ttk.Combobox(
            class_Student_frame,
            textvariable=self.var_course2,
            font=("times new roman", 15),
            state="readonly",
            width=14,
        )
        course_2_combo["values"] = (
            "Select Course",
            "UCS411_AI",
            "UCS414_CN",
            "UCS310_DBMS",
            "UMA035_OT",
            "UCS503_SE",
            "ECE202_Elec",
        )
        course_2_combo.current(0)  # to give the bydeafault index

        course_2_combo.place(x=530, y=90, anchor=NW)

        # course_3 label
        course_3_label = Label(
            class_Student_frame,
            text="Course - 3",
            font=("times new roman", 17),
            bg="white",
        )
        course_3_label.place(x=400, y=150, anchor=NW)

        course_3_combo = ttk.Combobox(
            class_Student_frame,
            textvariable=self.var_course3,
            font=("times new roman", 15),
            state="readonly",
            width=14,
        )
        course_3_combo["values"] = (
            "Select Course",
            "UCS411_AI",
            "UCS414_CN",
            "UCS310_DBMS",
            "UMA035_OT",
            "UCS503_SE",
            "ECE202_Elec",
        )
        course_3_combo.current(0)  # to give the bydeafault index

        course_3_combo.place(x=530, y=150, anchor=NW)

        # course_4 label
        course_4_label = Label(
            class_Student_frame,
            text="Course - 4",
            font=("times new roman", 17),
            bg="white",
        )
        course_4_label.place(x=400, y=210, anchor=NW)

        course_4_combo = ttk.Combobox(
            class_Student_frame,
            textvariable=self.var_course4,
            font=("times new roman", 15),
            state="readonly",
            width=14,
        )
        course_4_combo["values"] = (
            "Select Course",
            "UCS411_AI",
            "UCS414_CN",
            "UCS310_DBMS",
            "UMA035_OT",
            "UCS503_SE",
            "ECE202_Elec",
        )
        course_4_combo.current(0)  # to give the bydeafault index

        course_4_combo.place(x=530, y=210, anchor=NW)

        # gender label
        gender_label = Label(
            class_Student_frame,
            text="Gender",
            font=("times new roman", 17),
            bg="white",
        )
        gender_label.place(x=400, y=290, anchor=NW)

        gender_combo = ttk.Combobox(
            class_Student_frame,
            textvariable=self.var_gender,
            font=("times new roman", 15),
            state="readonly",
            width=14,
        )
        gender_combo["values"] = ("", "Male", "Female", "Others", "Prefer not to say")
        gender_combo.current(0)  # to give the bydeafault index

        gender_combo.place(x=530, y=290, anchor=NW)

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

        dob_entry = ttk.Entry(
            class_Student_frame,
            textvariable=self.var_defaultDob,
            width=17,
            font=("times new roman", 13, "bold"),
        )
        dob_entry.place(x=530, y=370, anchor=NW)

        # fatherNum
        fatherNum_label = Label(
            class_Student_frame,
            text="Father's Ph.No.",
            font=("times new roman", 17),
            bg="white",
        )
        fatherNum_label.place(x=400, y=430, anchor=NW)

        fatherNum_entry = ttk.Entry(
            class_Student_frame,
            textvariable=self.var_fatherNum,
            width=17,
            font=("times new roman", 13),
        )
        fatherNum_entry.place(x=530, y=430, anchor=NW)

        # motherNum
        motherNum_label = Label(
            class_Student_frame,
            text="Mother's Ph.No.",
            font=("times new roman", 17),
            bg="white",
        )
        motherNum_label.place(x=400, y=500, anchor=NW)

        motherNum_entry = ttk.Entry(
            class_Student_frame,
            textvariable=self.var_motherNum,
            width=17,
            font=("times new roman", 13),
        )
        motherNum_entry.place(x=530, y=500, anchor=NW)

        #########################################################################

        # Button Frame
        btn_frame = Frame(class_Student_frame, bd=2, relief=RAISED, bg="black")
        btn_frame.place(x=0, y=640, width=675, height=40)

        # Save button in button frame
        save_btn = Button(
            btn_frame,
            command=self.search_data,
            width=23,
            height=2,
            text="Search",
            font=("times new roman", 13, "bold"),
            bg="white",
            fg="black",
        )
        save_btn.grid(row=0, column=0)

        # update button
        update_btn = Button(
            btn_frame,
            command=self.update_data,
            width=23,
            height=2,
            text="Update",
            font=("times new roman", 13, "bold"),
            bg="white",
            fg="black",
        )
        update_btn.grid(row=0, column=1)

        # delete button
        delete_btn = Button(
            btn_frame,
            command=self.delete_data,
            width=24,
            height=2,
            text="Delete",
            font=("times new roman", 13, "bold"),
            bg="white",
            fg="black",
        )
        delete_btn.grid(row=0, column=2)

        # reset button
        reset_btn = Button(
            btn_frame,
            command=self.reset_data,
            width=24,
            height=2,
            text="Reset",
            font=("times new roman", 13, "bold"),
            bg="white",
            fg="black",
        )
        reset_btn.grid(row=0, column=3)

        ###########################################################################################
        # Button Frame 2
        btn_frame1 = Frame(class_Student_frame, bd=2, relief=RAISED, bg="black")
        btn_frame1.place(x=0, y=675, width=675, height=40)

        upadte_photo_btn = Button(
            btn_frame1,
            command=self.update_dataset,
            width=100,
            height=2,
            text="Update Photo Sample",
            font=("times new roman", 13, "bold"),
            bg="white",
            fg="black",
        )
        upadte_photo_btn.grid(row=0, column=0)

        ##################################################

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
                "Enroll_no",
                "Name",
                "Year",
                "Sem",
                "Dep",
                "Batch",
                "Email",
                "Phone_no",
                "Father_no",
                "Mother_no",
                "Course1",
                "Course2",
                "Course3",
                "Course4",
                "Gender",
                "DOB",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)

        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)

        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Enroll_no", text="Enroll_no")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Sem", text="Sem")
        self.student_table.heading("Dep", text="Dep")
        self.student_table.heading("Batch", text="Batch")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone_no", text="Phone_no")
        self.student_table.heading("Father_no", text="Father_no")
        self.student_table.heading("Mother_no", text="Mother_no")
        self.student_table.heading("Course1", text="Course1")
        self.student_table.heading("Course2", text="Course2")
        self.student_table.heading("Course3", text="Course3")
        self.student_table.heading("Course4", text="Course4")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        # self.student_table.heading("Image", text="Image")
        self.student_table["show"] = "headings"

        self.student_table.column("Enroll_no", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Sem", width=100)
        self.student_table.column("Dep", width=100)
        self.student_table.column("Batch", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Phone_no", width=100)
        self.student_table.column("Father_no", width=100)

        self.student_table.column("Mother_no", width=100)
        self.student_table.column("Course1", width=200)
        self.student_table.column("Course2", width=200)
        self.student_table.column("Course3", width=200)
        self.student_table.column("Course4", width=200)
        self.student_table.column("Gender", width=200)
        self.student_table.column("DOB", width=200)
        # self.student_table.column("Image", width=200)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        # self.fetch_data()

    # ============================== Function Declaration ===================================#

    # =======================fetch data =================== #
    def fetch_data(self, table_name):
        year = self.var_year.get()
        batch = self.var_batch.get()
        table_name = year + "_" + batch

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ShadowWalker77",
            database="Face_Recognition_db",
            auth_plugin="mysql_native_password",
        )
        my_cursor = conn.cursor()

        my_cursor.execute("select * from {}".format(str(table_name)))
        data = my_cursor.fetchall()

        p = 0

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)

        else:
            self.student_table.delete(*self.student_table.get_children())

        conn.commit()
        conn.close()

    ######################################################################################

    def search_data(self):
        year = self.var_year.get()
        batch = self.var_batch.get()
        table_name = year + "_" + batch
        print(table_name)

        self.fetch_data(table_name)

    # ======================= get cursor =================#

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_rollNum.set(data[0]),
        self.var_name.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_dep.set(data[4]),
        self.var_batch.set(data[5]),
        self.var_email.set(data[6]),
        self.var_phone.set(data[7]),

        self.var_fatherNum.set(data[8]),
        self.var_motherNum.set(data[9]),
        self.var_course1.set(data[10]),
        self.var_course2.set(data[11]),
        self.var_course3.set(data[12]),
        self.var_course4.set(data[13]),
        self.var_gender.set(data[14]),
        self.var_defaultDob.set(data[15]),
        self.var_old_roll = data[0]
        print("Self.va", self.var_old_roll)
        try:  # Now we will connect with SQL
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="ShadowWalker77",
                database="face_recognition_db",
                auth_plugin="mysql_native_password",
            )

            my_cursor = conn.cursor()
            sql = "select password from student where enroll_No=%s"
            val = (self.var_old_roll,)
            my_cursor.execute(sql, val)
            password = my_cursor.fetchall()
            print("password", password)
            self.var_password = password[0][0]
            conn.commit()
            # self.fetch_data()
            conn.close()  # Closing teh connection
        except Exception as es:
            messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)
        # self.var_radioButton1.set(data[16]),

    # ======== delete function ======= #
    def delete_data(self):
        if self.var_rollNum.get() == "":
            messagebox.showerror(
                "Error", "Student ID must be required", parent=self.root
            )
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete Page",
                    "Do you want to delete this student ?",
                    parent=self.root,
                )
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="ShadowWalker77",
                        database="face_recognition_db",
                        auth_plugin="mysql_native_password",
                    )

                    my_cursor = conn.cursor()
                    roll2 = "'" + str(self.var_old_roll) + "'"
                    sql = "delete from student where enroll_No={}".format(str(roll2))
                    print(sql)
                    # print(self)
                    my_cursor.execute(sql)
                    my_cursor = conn.cursor()
                    temp_var = self.var_year.get() + "_" + self.var_batch.get()
                    sql = "delete from {} where enroll_No={}".format(
                        temp_var, str(roll2)
                    )
                    print(sql)
                    # val = (self.var_old_roll,)
                    my_cursor.execute(sql)
                    conn.commit()
                    self.fetch_data(temp_var)
                    conn.close()
                    temp_var1 = self.var_course1.get()
                    temp_var2 = self.var_course2.get()
                    temp_var3 = self.var_course3.get()
                    temp_var4 = self.var_course4.get()
                    li = [temp_var1, temp_var2, temp_var3, temp_var4]
                    print("li is ", li)

                    temp_year = self.var_year.get()
                    temp_batch = self.var_batch.get()

                    for i in li:

                        temp_var = temp_year + "_" + temp_batch + "_" + str(i)
                        # Now we will connect with SQL
                        conn = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="ShadowWalker77",
                            database="face_recognition_db",
                            auth_plugin="mysql_native_password",
                        )
                        sql = "delete from {} where enroll_No={}".format(
                            temp_var, str(roll2)
                        )
                        # val = (self.var_old_roll,)
                        my_cursor = (
                            conn.cursor()
                        )  # To store the values given by the use
                        my_cursor.execute(sql)

                        conn.commit()
                        # self.fetch_data()
                        conn.close()  # Closing teh connection
                        # messagebox.showinfo("Success","Student details have been added successfully", parent=self.root,) # To showthe sccess message on parent which is self.root
                else:
                    if not delete:
                        return
            except Exception as es:
                pass
                # messagebox.showerror("work done", parent=self.root)

    # ======== reset function ======== #
    def reset_data(self):

        self.var_rollNum.set("")
        self.var_name.set("")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_dep.set("Select Department")
        self.var_batch.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_defaultDob.set("")
        self.var_fatherNum.set("")
        self.var_motherNum.set("")
        self.var_gender.set("")
        self.var_course1.set("Select Course")
        self.var_course2.set("Select Course")
        self.var_course3.set("Select Course")
        self.var_course4.set("Select Course")

        self.var_radioButton1.get() == ""

    def update_data(
        self,
    ):  # Add this in 'save' button, so that this functinality will work for the 'save' button
        if (
            self.var_rollNum.get() == ""
            or self.var_name.get() == ""
            or self.var_year.get() == "Select Year"
            or self.var_semester.get() == "Select Semester"
            or self.var_dep.get() == "Select Department"
            or self.var_batch.get() == "Select Batch"
            or self.var_email.get() == ""
            or self.var_phone.get() == ""
            or self.var_fatherNum.get() == ""
            or self.var_motherNum.get() == ""
            # or self.var_password.get() == ""
            # or self.var_confirm_password.get() == ""
            or self.var_course1.get() == "Select Course"
            or self.var_course2.get() == "Select Course"
            or self.var_course3.get() == "Select Course"
            or self.var_course4.get() == "Select Course"
            or self.var_gender.get() == ""
            or self.var_defaultDob.get() == "Choose Date"
        ):
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root
            )  # Messagebox to show the error and parent=self.root to show the message in the same window is any of the fields would be missing

        else:  # Ab agar data aa jata hai to usse database mein save karna hai

            try:  # Now we will connect with SQL
                Update = messagebox.askyesno(
                    "Update",
                    "Do you want to update the student details",
                    parent=self.root,
                )
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="ShadowWalker77",
                        database="face_recognition_db",
                        auth_plugin="mysql_native_password",
                    )

                    my_cursor = conn.cursor()
                    roll1 = "'" + str(self.var_old_roll) + "'"
                    sql = "delete from student where enroll_No={}".format(str(roll1))
                    print(sql)
                    # print(self)
                    my_cursor.execute(sql)

                    my_cursor = conn.cursor()  # To store the values given by the user
                    my_cursor.execute(
                        "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.var_rollNum.get(),
                            self.var_name.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_dep.get(),
                            self.var_batch.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_fatherNum.get(),
                            self.var_motherNum.get(),
                            self.var_password,
                            self.var_course1.get(),
                            self.var_course2.get(),
                            self.var_course3.get(),
                            self.var_course4.get(),
                            self.var_gender.get(),
                            self.var_defaultDob.get(),
                        ),
                    )
                    conn.commit()
                    # self.fetch_data()
                    conn.close()  # Closing teh connection
                    messagebox.showinfo(
                        "Success",
                        "Student details have been added successfully",
                        parent=self.root,
                    )  # To showthe sccess message on parent which is self.root

                    ######################################################################
                    temp_var = self.var_year.get() + "_" + self.var_batch.get()
                    temp_dep = self.var_dep.get()
                    temp_roll = "'" + self.var_rollNum.get() + "'"
                    temp_name = "'" + self.var_name.get() + "'"
                    temp_year = "'" + self.var_year.get() + "'"
                    temp_sem = "'" + self.var_semester.get() + "'"
                    temp_dep1 = "'" + temp_dep + "'"
                    temp_batch = "'" + self.var_batch.get() + "'"
                    temp_email = "'" + self.var_email.get() + "'"
                    temp_phone = "'" + self.var_phone.get() + "'"
                    temp_fatherNum = "'" + self.var_fatherNum.get() + "'"
                    temp_motherNum = "'" + self.var_motherNum.get() + "'"
                    temp_course1 = "'" + self.var_course1.get() + "'"
                    temp_course2 = "'" + self.var_course2.get() + "'"
                    temp_course3 = "'" + self.var_course3.get() + "'"
                    temp_course4 = "'" + self.var_course4.get() + "'"
                    temp_gender = "'" + self.var_gender.get() + "'"
                    temp_dob = "'" + self.var_defaultDob.get() + "'"
                    print("dep is", self.var_dep.get())

                    try:  # Now we will connect with SQL
                        conn = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="ShadowWalker77",
                            database="face_recognition_db",
                            auth_plugin="mysql_native_password",
                        )

                        my_cursor = conn.cursor()
                        roll2 = "'" + str(self.var_old_roll) + "'"
                        sql = "delete from {} where enroll_No={}".format(
                            temp_var, roll2
                        )
                        print(sql)
                        # val = (self.var_old_roll,)
                        my_cursor.execute(sql)
                        my_cursor = (
                            conn.cursor()
                        )  # To store the values given by the user

                        sql = "insert into {} values({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(
                            str(temp_var),
                            temp_roll,
                            temp_name,
                            temp_year,
                            temp_sem,
                            temp_dep1,
                            temp_batch,
                            temp_email,
                            temp_phone,
                            temp_fatherNum,
                            temp_motherNum,
                            temp_course1,
                            temp_course2,
                            temp_course3,
                            temp_course4,
                            temp_gender,
                            temp_dob,
                        )
                        print(sql)
                        my_cursor.execute(sql)
                        conn.commit()
                        self.fetch_data(temp_var)
                        conn.close()  # Closing teh connection
                        messagebox.showinfo(
                            "Success",
                            "Student details have been added successfully",
                            parent=self.root,
                        )  # To showthe sccess message on parent which is self.root

                    except Exception as es:
                        messagebox.showerror(
                            "Error", f"Due to : {str(es)}", parent=self.root
                        )

                    ############################################################################
                    temp_var1 = self.var_course1.get()
                    temp_var2 = self.var_course2.get()
                    temp_var3 = self.var_course3.get()
                    temp_var4 = self.var_course4.get()
                    li = [temp_var1, temp_var2, temp_var3, temp_var4]
                    print("li is ", li)

                    temp_year = self.var_year.get()
                    temp_batch = self.var_batch.get()

                    for i in li:

                        temp_var = temp_year + "_" + temp_batch + "_" + str(i)
                        try:  # Now we will connect with SQL
                            conn = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                password="ShadowWalker77",
                                database="face_recognition_db",
                                auth_plugin="mysql_native_password",
                            )

                            my_cursor = (
                                conn.cursor()
                            )  # To store the values given by the user
                            my_cursor.execute(
                                "insert into {} values({})".format(
                                    temp_var, self.var_rollNum.get()
                                ),
                            )
                            conn.commit()
                            # self.fetch_data()
                            conn.close()  # Closing teh connection
                            # messagebox.showinfo("Success","Student details have been added successfully", parent=self.root,) # To showthe sccess message on parent which is self.root

                        except Exception as es:
                            pass
                            # messagebox.showerror("work done", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

    # ==== generate data set and take photo sample and also train the data set  ==== #
    def update_dataset(self):
        if (
            self.var_rollNum.get() == ""
            or self.var_name.get() == ""
            or self.var_year.get() == "Select Year"
            or self.var_semester.get() == "Select Semester"
            or self.var_dep.get() == "Select Department"
            or self.var_batch.get() == ""
            or self.var_email.get() == ""
            or self.var_phone.get() == ""
            # or self.var_dob.get() == ""
            or self.var_fatherNum.get() == ""
            or self.var_motherNum.get() == ""
            or self.var_gender.get() == ""
            or self.var_course1.get() == "Select Course"
            or self.var_course2.get() == "Select Course"
            or self.var_course3.get() == "Select Course"
            or self.var_course4.get() == "Select Course"
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            roll2 = self.var_rollNum.get()
            roll3 = roll2
            roll2 = "'" + roll2 + "'"
            try:
                Update = messagebox.askyesno(
                    "Update",
                    "Do you want to update the student details",
                    parent=self.root,
                )
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="ShadowWalker77",
                        database="Face_Recognition_db",
                        auth_plugin="mysql_native_password",
                    )
                    my_cursor = conn.cursor()
                    sql = "select enroll_no from student where enroll_no={}".format(
                        str(roll2)
                    )
                    my_cursor.execute(sql)
                    myroll = my_cursor.fetchall()

                conn.commit()
                # self.fetch_data()
                self.reset_data()
                conn.close()
                print(myroll[0][0])
                print(roll2)
                # == load predefined data on face frontals from opencv
                if str(myroll[0][0]) == str(roll3):
                    cam = cv2.VideoCapture(0)
                    cam.set(3, 640)  # set video width
                    cam.set(4, 480)  # set video height

                    face_detector = cv2.CascadeClassifier(
                        "haarcascade_frontalface_default.xml"
                    )

                    count = 0

                    while True:

                        ret, img = cam.read()
                        # img = cv2.flip(img, -1) # flip video image vertically
                        if ret == False:
                            continue

                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_detector.detectMultiScale(gray, 1.3, 5)

                        for (x, y, w, h) in faces:

                            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                            count += 1

                            # Save the captured image into the datasets folder
                            cv2.imwrite(
                                "dataset/" + str(roll3) + "." + str(count) + ".jpg",
                                gray[y : y + h, x : x + w],
                            )
                            cv2.putText(
                                img,
                                str(count),
                                (50, 50),
                                cv2.FONT_HERSHEY_COMPLEX,
                                2,
                                (0, 255, 0),
                                2,
                            )

                            cv2.imshow("image", img)

                        k = cv2.waitKey(100) & 0xFF  # Press 'ESC' for exiting video
                        if k == 27:  # escape key ASCII Value
                            break
                        elif count >= 100:  # Take 100 face sample and stop video
                            break

                    cam.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("success", "dataset updated", parent=self.root)
                else:
                    messagebox.showinfo(
                        "Error", "User is not registered", parent=self.root
                    )

            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = adminCheckStudentDetails(root)
    root.mainloop()
