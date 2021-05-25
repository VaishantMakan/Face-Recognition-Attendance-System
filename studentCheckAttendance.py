from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk
import numpy as np
import cv2
import mysql.connector
import os
import pandas as pd
from tkinter import messagebox
from tkinter import filedialog
import csv


class studentCheckAttendance:
    def __init__(self, root, data):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition Attendance System")

        # ======= Variables ============
        self.my_data = data
        self.new_data = []
        self.column_list = []
        self.dict = {}

        # ======= Variables ============
        self.var_rollNum = StringVar()
        self.var_name = StringVar()
        self.var_rollNumText = StringVar()
        self.var_nameText = StringVar()
        self.var_yearText = StringVar()
        self.var_semesterText = StringVar()
        self.var_depText = StringVar()
        self.var_batchText = StringVar()
        self.var_emailText = StringVar()
        self.var_phoneText = StringVar()
        self.var_course1Text = StringVar()
        self.var_course2Text = StringVar()
        self.var_course3Text = StringVar()
        self.var_course4Text = StringVar()
        self.var_dobText = StringVar()
        self.var_genderText = StringVar()
        self.var_fatherText = StringVar()
        self.var_motherText = StringVar()

        # Setting the variables
        self.var_rollNumText.set(self.my_data[0])
        self.var_nameText.set(self.my_data[1])
        self.var_yearText.set(self.my_data[2])
        self.var_semesterText.set(self.my_data[3])
        self.var_depText.set(self.my_data[4])
        self.var_batchText.set(self.my_data[5])
        self.var_emailText.set(self.my_data[6])
        self.var_phoneText.set(self.my_data[7])
        self.var_fatherText.set(self.my_data[8])
        self.var_motherText.set(self.my_data[9])
        self.var_course1Text.set(self.my_data[11])
        self.var_course2Text.set(self.my_data[12])
        self.var_course3Text.set(self.my_data[13])
        self.var_course4Text.set(self.my_data[14])
        self.var_genderText.set(self.my_data[15])
        self.var_dobText.set(self.my_data[16])

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
            text="CHECK YOUR ATTENDANCE",
            font=("times new roman", 25, "bold"),
            bg="black",
            fg="white",
        )
        title_lbl.place(x=510, y=160, width=500, height=40)

        # studentCheckAttendance frame
        attendance_frame = Frame(bg_img, bd=2, bg="white", highlightthickness=5)
        attendance_frame.place(x=510, y=220, width=500, height=275)

        attendance_frame.config(highlightbackground="black", highlightcolor="black")

        # Year label
        year_label = Label(
            attendance_frame,
            text="Year",
            font=("times new roman", 17),
            bg="white",
        )
        year_label.place(x=50, y=50, anchor=NW)

        # combo is used for dropdown like entering text
        year_combo = Label(
            attendance_frame,
            textvariable=self.var_yearText,
            font=("times new roman", 15),
            bg="white",
        )

        year_combo.place(x=275, y=50, anchor=NW)

        # Semester label
        semester_label = Label(
            attendance_frame,
            text="Semester",
            font=("times new roman", 17),
            bg="white",
        )
        semester_label.place(x=50, y=100, anchor=NW)

        # combo is used for dropdown like entering text
        semester_combo = Label(
            attendance_frame,
            textvariable=self.var_semesterText,
            font=("times new roman", 15),
            bg="white",
        )
        semester_combo.place(x=275, y=100, anchor=NW)

        # Batch label
        batch_label = Label(
            attendance_frame,
            text="Batch",
            font=("times new roman", 17),
            bg="white",
        )
        batch_label.place(x=50, y=150, anchor=NW)

        # combo is used for dropdown like entering text
        batch_combo = Label(
            attendance_frame,
            textvariable=self.var_batchText,
            font=("times new roman", 15),
            bg="white",
        )
        batch_combo.place(x=275, y=150, anchor=NW)

        # course label
        course_label = Label(
            attendance_frame,
            text="Course",
            font=("times new roman", 17),
            bg="white",
        )
        course_label.place(x=50, y=200, anchor=NW)

        # combo is used for dropdown like entering text
        course_combo = ttk.Combobox(
            attendance_frame,
            textvariable=self.var_course,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        course_combo["values"] = (
            "Select Course",
            self.my_data[11],
            self.my_data[12],
            self.my_data[13],
            self.my_data[14],
        )
        course_combo.current(0)  # to give the bydeafault index

        course_combo.place(x=275, y=200, anchor=NW)

        # ---- button ----#

        # studentCheckAttendance button
        studentCheckAttendance_btn = Button(
            bg_img,
            command=self.export_data,
            width=27,
            height=2,
            text="EXPORT ATTENDANCE",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )

        studentCheckAttendance_btn.place(x=650, y=520, anchor=NW)

    # ==============================functions======================================
    def export_data(self):
        if self.var_course == "":
            messagebox.showerror("Error", "Enter the course name", parent=self.root)

        else:
            roll = self.var_rollNumText
            roll = "'" + self.var_rollNumText.get() + "'"
            table_name = (
                self.var_yearText.get()
                + "_"
                + self.var_batchText.get()
                + "_"
                + self.var_course.get()
            )

            try:  # Now we will connect with SQL
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="ShadowWalker77",
                    database="face_recognition_db",
                    auth_plugin="mysql_native_password",
                )

                # ===================cursor 0============================= --- Getting the columns
                my_cursor = conn.cursor()
                sql = "select * from {} where Enroll_no={}".format(
                    str(table_name), str(roll)
                )
                df = pd.read_sql(sql, con=conn)
                df.to_csv("ai.csv")

                myData = df.values.tolist()

                try:
                    if len(myData) < 1:
                        messagebox.showerror(
                            "No Data", "No Data Found To Export", parent=self.root
                        )
                        return False

                    fln = filedialog.asksaveasfilename(
                        initialdir=os.getcwd(),
                        title="Open CSV",
                        filetypes=[("csv", ".CSV")],
                        parent=self.root,
                    )
                    df.to_csv(fln, index=False)
                    messagebox.showinfo(
                        "Data Exported",
                        "Your Data Exported to "
                        + os.path.basename(fln)
                        + " successfully",
                        parent=self.root,
                    )

                except Exception as es:
                    messagebox.showerror(
                        "Error", f"Due to : {str(es)}", parent=self.root
                    )

                conn.commit()
                # self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", "User not registered", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = studentCheckAttendance(root)
    root.mainloop()
