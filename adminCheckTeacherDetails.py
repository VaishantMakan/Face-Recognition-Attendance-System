import numpy as np
import cv2

from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os


class adminCheckTeacherDetails:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition Attendance System")

        self.var_id = StringVar()
        self.var_name = StringVar()

        self.var_email = StringVar()
        self.var_phone = StringVar()

        self.var_gender = StringVar()
        self.var_course1 = StringVar()
        self.var_course2 = StringVar()
        self.var_course3 = StringVar()

        self.var_old_roll = ""
        self.var_password = ""

        # img1 = main background
        img1 = Image.open("Images/bg_Student.jpeg")
        img1 = img1.resize((1550, 900), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1550, height=900)

        # title
        title_lbl = Label(
            bg_img,
            text="TEACHER MANAGEMENT SYSTEM",
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
            text="Teacher Details",
            font=("times new roman", 12, "bold"),
        )
        Left_frame.place(x=10, y=10, width=700, height=777)

        img_left = Image.open("Images/db2.png")
        img_left = img_left.resize((680, 257), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=3, y=0, width=680, height=257)

        ###########################################################################

        # Teacher information
        teacher_frame = LabelFrame(
            Left_frame,
            bd=3,
            bg="white",
            relief=SUNKEN,
            text="Teacher Details",
            font=("times new roman", 12, "bold"),
        )
        teacher_frame.place(x=5, y=270, width=680, height=480)

        # teacher ID
        teacherID_label = Label(
            teacher_frame,
            text="Teacher ID",
            font=("times new roman", 17),
            bg="white",
        )
        teacherID_label.place(x=10, y=30, anchor=NW)

        teacherID_entry = ttk.Entry(
            teacher_frame,
            textvariable=self.var_id,
            width=22,
            font=("times new roman", 13),
        )
        teacherID_entry.place(x=180, y=30, anchor=NW)

        # Name
        name_label = Label(
            teacher_frame,
            text="Name",
            font=("times new roman", 17),
            bg="white",
        )
        name_label.place(x=10, y=130, anchor=NW)

        name_entry = ttk.Entry(
            teacher_frame,
            textvariable=self.var_name,
            width=22,
            font=("times new roman", 13),
        )
        name_entry.place(x=180, y=130, anchor=NW)

        # Phone no.
        phone_label = Label(
            teacher_frame,
            text="Phone No.",
            font=("times new roman", 17),
            bg="white",
        )
        phone_label.place(x=10, y=230, anchor=NW)

        phone_entry = ttk.Entry(
            teacher_frame,
            textvariable=self.var_phone,
            width=22,
            font=("times new roman", 13),
        )
        phone_entry.place(x=180, y=230, anchor=NW)

        # Email
        email_label = Label(
            teacher_frame,
            text="Email (thapar.edu)",
            font=("times new roman", 17),
            bg="white",
        )
        email_label.place(x=10, y=350, anchor=NW)

        email_entry = ttk.Entry(
            teacher_frame,
            textvariable=self.var_email,
            width=22,
            font=("times new roman", 13),
        )
        email_entry.place(x=180, y=350, anchor=NW)

        # course_1 label
        course_1_label = Label(
            teacher_frame,
            text="Course - 1",
            font=("times new roman", 17),
            bg="white",
        )
        course_1_label.place(x=380, y=30, anchor=NW)

        # combo is used for dropdown like entering text
        course_1_combo = ttk.Combobox(
            teacher_frame,
            textvariable=self.var_course1,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        course_1_combo["values"] = (
            "",
            "UCS411_AI",
            "UCS414_CN",
            "UCS310_DBMS",
            "UMA035_OT",
            "UCS503_SE",
            "ECE202_Elec",
        )
        course_1_combo.current(0)  # to give the bydeafault index

        course_1_combo.place(x=480, y=30, anchor=NW)

        # course_2 label
        course_2_label = Label(
            teacher_frame,
            text="Course - 2",
            font=("times new roman", 17),
            bg="white",
        )
        course_2_label.place(x=380, y=130, anchor=NW)

        # combo is used for dropdown like entering text
        course_2_combo = ttk.Combobox(
            teacher_frame,
            textvariable=self.var_course2,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        course_2_combo["values"] = (
            "",
            "UCS411_AI",
            "UCS414_CN",
            "UCS310_DBMS",
            "UMA035_OT",
            "UCS503_SE",
            "ECE202_Elec",
        )
        course_2_combo.current(0)  # to give the bydeafault index

        course_2_combo.place(x=480, y=130, anchor=NW)

        # course_3 label
        course_3_label = Label(
            teacher_frame,
            text="Course - 3",
            font=("times new roman", 17),
            bg="white",
        )
        course_3_label.place(x=380, y=230, anchor=NW)

        # combo is used for dropdown like entering text
        course_3_combo = ttk.Combobox(
            teacher_frame,
            textvariable=self.var_course3,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        course_3_combo["values"] = (
            "",
            "UCS411_AI",
            "UCS414_CN",
            "UCS310_DBMS",
            "UMA035_OT",
            "UCS503_SE",
            "ECE202_Elec",
        )
        course_3_combo.current(0)  # to give the bydeafault index

        course_3_combo.place(x=480, y=230, anchor=NW)

        # gender label
        gender_label = Label(
            teacher_frame,
            text="Gender",
            font=("times new roman", 17),
            bg="white",
        )
        gender_label.place(x=380, y=350, anchor=NW)

        # combo is used for dropdown like entering text
        gender_combo = ttk.Combobox(
            teacher_frame,
            textvariable=self.var_gender,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        gender_combo["values"] = ("", "Male", "Female", "Others", "Prefer not to say")
        gender_combo.current(0)  # to give the bydeafault index

        gender_combo.place(x=480, y=350, anchor=NW)

        #########################################################################

        # Button Frame
        btn_frame = Frame(teacher_frame, bd=2, relief=RAISED, bg="black")
        btn_frame.place(x=0, y=420, width=675, height=40)

        # Save button in button frame
        save_btn = Button(
            btn_frame,
            # command=self.add_data,
            width=23,
            height=2,
            text="Save",
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

        # right label
        Right_frame = LabelFrame(
            main_frame,
            bd=5,
            bg="white",
            relief=RAISED,
            text="",
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
                "id",
                "Name",
                "Phone",
                "Email",
                "Gender",
                "Course1",
                "Course2",
                "Course3",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)

        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)

        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id", text="id")
        self.student_table.heading("Name", text="Name")

        self.student_table.heading("Phone", text="Phone")
        self.student_table.heading("Email", text="Email")

        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Course1", text="Course1")
        self.student_table.heading("Course2", text="Course2")
        self.student_table.heading("Course3", text="Course3")

        self.student_table["show"] = "headings"

        self.student_table.column("id", width=100)
        self.student_table.column("Name", width=100)

        self.student_table.column("Phone", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Gender", width=200)

        self.student_table.column("Course1", width=200)
        self.student_table.column("Course2", width=200)
        self.student_table.column("Course3", width=200)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ============================== Function Declaration ===================================#

    def add_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_course.get() == "Select Course"
            or self.var_year.get() == "Select Year"
            or self.var_semester.get() == "Select Semester"
            or self.var_rollNum.get() == ""
            or self.var_std_name.get() == ""
            or self.var_batch.get() == ""
            or self.var_batchNum.get() == ""
            or self.var_dob.get() == ""
            or self.var_email.get() == ""
            or self.var_phone.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="ShadowWalker77",
                    database="Face_Recognition_db",
                    auth_plugin="mysql_native_password",
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into student_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_rollNum.get(),
                        self.var_std_name.get(),
                        self.var_batch.get(),
                        self.var_batchNum.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_fatherNum.get(),
                        self.var_motherNum.get(),
                        self.var_radioButton1.get(),
                    ),
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success",
                    "Student details have been added successfully",
                    parent=self.root,
                )
            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

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
        my_cursor.execute("select * from teacher")
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
        self.var_id.set(data[0]),
        self.var_name.set(data[1]),

        self.var_phone.set(data[2]),
        self.var_email.set(data[3]),
        self.var_gender.set(data[4]),

        self.var_course1.set(data[5]),
        self.var_course2.set(data[6]),
        self.var_course3.set(data[7]),

        self.var_old_roll = data[0]
        try:  # Now we will connect with SQL
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="ShadowWalker77",
                database="face_recognition_db",
                auth_plugin="mysql_native_password",
            )

            my_cursor = conn.cursor()
            sql = "select password from teacher where id=%s"
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

    # ======= update function ======= #
    def update_data(self):
        if (
            self.var_id.get() == ""
            or self.var_name.get() == ""
            or self.var_email.get() == ""
            or self.var_phone.get() == ""
            or self.var_gender.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
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
                        database="face_recognition_db",
                        auth_plugin="mysql_native_password",
                    )

                    my_cursor = conn.cursor()
                    roll1 = "'" + str(self.var_old_roll) + "'"
                    sql = "delete from teacher where id={}".format(str(roll1))
                    print(sql)
                    my_cursor.execute(sql)

                    my_cursor = conn.cursor()  # To store the values given by the user
                    my_cursor.execute(
                        "insert into teacher values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.var_id.get(),
                            self.var_name.get(),
                            self.var_phone.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_course1.get(),
                            self.var_course2.get(),
                            self.var_course3.get(),
                            self.var_password,
                        ),
                    )
                    conn.commit()
                    self.fetch_data()
                    conn.close()  # Closing teh connection
                    messagebox.showinfo(
                        "Success",
                        "teacher details have been added successfully",
                        parent=self.root,
                    )  # To showthe sccess message on parent which is self.root

                else:
                    if not Update:
                        return
                messagebox.showinfo(
                    "Success", "Student details successfully updated", parent=self.root
                )
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # ======== delete function ======= #
    def delete_data(self):
        if self.var_id.get() == "":
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
                    roll1 = "'" + str(self.var_old_roll) + "'"
                    sql = "delete from teacher where id={}".format(str(roll1))
                    print(sql)
                    # print(self)
                    my_cursor.execute(sql)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo(
                        "Delete",
                        "Successfully deleted student details",
                        parent=self.root,
                    )
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # ======== reset function ======== #
    def reset_data(self):

        self.var_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_gender.set("")
        self.var_course1.set("Select Course")
        self.var_course2.set("Select Course")
        self.var_course3.set("Select Course")


if __name__ == "__main__":
    root = Tk()
    obj = adminCheckTeacherDetails(root)
    root.mainloop()
