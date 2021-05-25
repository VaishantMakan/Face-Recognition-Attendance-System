import numpy as np
import cv2
from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk
from tkinter import messagebox
import pandas as pd
import mysql.connector
import os
from tkinter import filedialog


class Student_attendance:
    def __init__(self, root, data):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition Attendance System")

        # ======= Variables ============
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
        self.mydata = data

        # img1 = main background
        img1 = Image.open("Images/wall.jpeg")
        img1 = img1.resize((1550, 900), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1550, height=900)

        self.var_roll = StringVar()
        self.var_status = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()

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
            textvariable=self.var_roll,
            width=22,
            font=("times new roman", 13),
        )
        rollNum_entry.place(x=245, y=10, anchor=NW)

        # date
        date_label = Label(
            upper_frame,
            text="Date  (_dd_mm_yyyy)",
            font=("times new roman", 17),
            bg="white",
        )
        date_label.place(x=10, y=70, anchor=NW)

        date_entry = ttk.Entry(
            upper_frame,
            textvariable=self.var_date,
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
            textvariable=self.var_status,
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
            text="Time (hh_mm)",
            font=("times new roman", 17),
            bg="white",
        )
        time_label.place(x=9, y=170, anchor=NW)

        timeFormat_label = Label(
            upper_frame,
            text="(24 hour format) ",
            font=("times new roman", 16),
            bg="white",
        )
        timeFormat_label.place(x=11, y=190, anchor=NW)

        time_entry = ttk.Entry(
            upper_frame,
            textvariable=self.var_time,
            width=22,
            font=("times new roman", 13),
        )
        time_entry.place(x=245, y=190, anchor=NW)

        # --- buttons --- #

        updateAttendance_btn = Button(
            upper_frame,
            command=self.update_attendance,
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

        year_combo = ttk.Combobox(
            Search_frame,
            font=("times new roman", 13, "bold"),
            state="readonly",
            width=17,
        )
        year_combo["values"] = ("Select Year", "I", "II", "III", "IV")
        year_combo.current(0)  # to give the bydeafault index
        year_combo.place(x=230, y=20)

        batch_combo = ttk.Combobox(
            Search_frame,
            font=("times new roman", 13, "bold"),
            state="readonly",
            width=17,
        )
        batch_combo["values"] = ("Select Batch", "2CS9", "2CS10", "2CS11", "2CS12")
        batch_combo.current(0)  # to give the bydeafault index
        batch_combo.place(x=450, y=20)

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
            command=self.export_data,
            width=20,
            text="Export All Attendance",
            font=("time new roman", 15, "bold"),
            bg="grey",
            fg="black",
        )
        exportAll_btn.place(x=1200, y=20)

        # =========Table frame=================

        table_frame = Frame(lower_frame, bd=3, bg="white", relief=SUNKEN)
        table_frame.place(x=5, y=100, width=1450, height=300)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        tup = self.get_columns()
        self.student_table = ttk.Treeview(
            table_frame,
            column=tup,
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)

        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)

        scroll_y.config(command=self.student_table.yview)

        for i in range(len(tup)):
            self.student_table.heading(tup[i], text=tup[i])

        self.student_table["show"] = "headings"

        self.student_table.pack(fill=BOTH, expand=1)

        self.fetch_data()

    # ============================== Function Declaration ===================================#

    # =======================fetch data =================== #

    def get_columns(self):
        year = self.mydata[0]
        batch = self.mydata[2]
        course = self.mydata[3]
        table_name = year + "_" + batch + "_" + course
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ShadowWalker77",
            database="Face_Recognition_db",
            auth_plugin="mysql_native_password",
        )
        my_cursor = conn.cursor()
        sql1 = "select * from {}".format(str(table_name))
        # my_cursor.execute(sql1)
        df = pd.read_sql(sql1, con=conn)
        # data = my_cursor.fetchall()
        conn.commit()
        conn.close()
        column = df.columns
        tup = tuple(column)
        # print(tup)
        return tup

    def fetch_data(self):
        year = self.mydata[0]
        batch = self.mydata[2]
        course = self.mydata[3]
        table_name = year + "_" + batch + "_" + course
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ShadowWalker77",
            database="Face_Recognition_db",
            auth_plugin="mysql_native_password",
        )
        my_cursor = conn.cursor()
        sql1 = "select * from {}".format(str(table_name))
        my_cursor.execute(sql1)
        # df=pd.read_sql(sql1,con=conn)
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)

        else:
            self.student_table.delete(*self.student_table.get_children())

        conn.commit()
        conn.close()

    def update_attendance(self):
        rol = self.var_roll.get()
        rol = "'" + rol + "'"
        year = self.mydata[0]
        batch = self.mydata[2]
        course = self.mydata[3]
        table_name = year + "_" + batch + "_" + course
        d1 = self.var_date.get() + "_" + self.var_time.get()
        status = self.var_status.get()
        status = "'" + status + "'"

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="ShadowWalker77",
                database="face_recognition_db",
                auth_plugin="mysql_native_password",
            )

            string = "UPDATE {} SET {} = {} WHERE enroll_no = {} ".format(
                str(table_name), str(d1), str(status), str(rol)
            )
            print(string)
            my_cursor = conn.cursor()
            my_cursor.execute(string)

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo(
                "Success", "Student attendance successfully updated", parent=self.root
            )

        except mysql.connector.Error as e:
            messagebox.showinfo("Error", "Invalid Credentials", parent=self.root)

    #################################################################################################################################

    def export_data(self):

        year = self.mydata[0]
        batch = self.mydata[2]
        course = self.mydata[3]
        table_name = year + "_" + batch + "_" + course

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

            sql = "select * from {}".format(str(table_name))
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
                fln = fln + ".csv"
                df.to_csv(fln, index=False)

                if fln != ".csv":
                    messagebox.showinfo(
                        "Data Exported",
                        "Your Data Exported to "
                        + os.path.basename(fln)
                        + " successfully",
                        parent=self.root,
                    )

            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

            conn.commit()
            conn.close()

        except Exception as es:
            messagebox.showerror("Error", "User not registered", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student_attendance(root)
    root.mainloop()
