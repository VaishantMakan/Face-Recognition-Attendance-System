from tkinter import *
from tkinter import ttk
import tkinter  # ttk is used for styling
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox

import numpy as np
import cv2
import mysql.connector
import os


class studentRegister:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition Attendance System")

        # ======= Variables ============
        self.defaultDob = StringVar()
        self.defaultDob.set("Choose Date")

        self.dobDate = StringVar()
        self.dobDate.set("")

        ################################################################
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
        self.var_password = StringVar()
        self.var_confirm_password = StringVar()
        # self.var_dob = StringVar()
        self.var_fatherNum = StringVar()
        self.var_motherNum = StringVar()
        self.var_gender = StringVar()
        self.var_course1 = StringVar()
        self.var_course2 = StringVar()
        self.var_course3 = StringVar()
        self.var_course4 = StringVar()

        ###############################################################

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

        # title
        title_lbl = Label(
            bg_img,
            text="STUDENT REGISTRATION",
            font=("times new roman", 25, "bold"),
            justify=CENTER,
            anchor=S,
            bg="black",
            fg="white",
        )
        title_lbl.place(x=350, y=105, width=900, height=30)

        # Enrollment no.
        rollNum_label = Label(
            register_frame,
            text="Enrollment Number",
            font=("times new roman", 17),
            bg="white",
        )
        rollNum_label.place(x=10, y=30, anchor=NW)

        rollNum_entry = ttk.Entry(
            register_frame,
            textvariable=self.var_rollNum,
            width=22,
            font=("times new roman", 13),
        )
        rollNum_entry.place(x=245, y=30, anchor=NW)

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
            textvariable=self.var_name,
            width=22,
            font=("times new roman", 13),
        )
        name_entry.place(x=245, y=90, anchor=NW)

        # Year label
        year_label = Label(
            register_frame,
            text="Year",
            font=("times new roman", 17),
            bg="white",
        )
        year_label.place(x=10, y=150, anchor=NW)

        # combo is used for dropdown like entering text
        year_combo = ttk.Combobox(
            register_frame,
            textvariable=self.var_year,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        year_combo["values"] = ("Select Year", "I", "II", "III", "IV")
        year_combo.current(0)  # to give the bydeafault index

        year_combo.place(x=245, y=150, anchor=NW)

        # Semester label
        semester_label = Label(
            register_frame,
            text="Semester",
            font=("times new roman", 17),
            bg="white",
        )
        semester_label.place(x=10, y=210, anchor=NW)

        # combo is used for dropdown like entering text
        semester_combo = ttk.Combobox(
            register_frame,
            textvariable=self.var_semester,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        semester_combo["values"] = (
            "Select Semester",
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

        semester_combo.place(x=245, y=210, anchor=NW)

        # Department label
        dep_label = Label(
            register_frame,
            text="Department",
            font=("times new roman", 17),
            bg="white",
        )
        dep_label.place(x=10, y=270, anchor=NW)

        # combo is used for dropdown like entering text
        dep_combo = ttk.Combobox(
            register_frame,
            textvariable=self.var_dep,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        dep_combo["values"] = ("Select Department", "COE", "CSE", "COBS", "EE")
        dep_combo.current(0)  # to give the bydeafault index

        dep_combo.place(x=245, y=270, anchor=NW)

        # Batch label
        batch_label = Label(
            register_frame,
            text="Batch",
            font=("times new roman", 17),
            bg="white",
        )
        batch_label.place(x=10, y=330, anchor=NW)

        # combo is used for dropdown like entering text
        batch_combo = ttk.Combobox(
            register_frame,
            textvariable=self.var_batch,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        batch_combo["values"] = ("Select Batch", "2EE9", "2CS10", "2CS11", "2CS12")
        batch_combo.current(0)  # to give the bydeafault index

        batch_combo.place(x=245, y=330, anchor=NW)

        # Email
        email_label = Label(
            register_frame,
            text="Email (thapar.edu)",
            font=("times new roman", 17),
            bg="white",
        )
        email_label.place(x=10, y=390, anchor=NW)

        email_entry = ttk.Entry(
            register_frame,
            textvariable=self.var_email,
            width=22,
            font=("times new roman", 13),
        )
        email_entry.place(x=245, y=390, anchor=NW)

        # Phone no.
        phone_label = Label(
            register_frame,
            text="Phone No.",
            font=("times new roman", 17),
            bg="white",
        )
        phone_label.place(x=10, y=450, anchor=NW)

        phone_entry = ttk.Entry(
            register_frame,
            textvariable=self.var_phone,
            width=22,
            font=("times new roman", 13),
        )
        phone_entry.place(x=245, y=450, anchor=NW)

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
            textvariable=self.var_password,
            width=22,
            font=("times new roman", 13),
        )
        pass_entry.place(x=245, y=510, anchor=NW)

        # ---------------------right-----------------------#

        # course_1 label
        course_1_label = Label(
            register_frame,
            text="Course - 1",
            font=("times new roman", 17),
            bg="white",
        )
        course_1_label.place(x=525, y=30, anchor=NW)

        # combo is used for dropdown like entering text
        course_1_combo = ttk.Combobox(
            register_frame,
            textvariable=self.var_course1,
            font=("times new roman", 15),
            state="readonly",
            width=18,
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

        course_1_combo.place(x=700, y=30, anchor=NW)

        # course_2 label
        course_2_label = Label(
            register_frame,
            text="Course - 2",
            font=("times new roman", 17),
            bg="white",
        )
        course_2_label.place(x=525, y=90, anchor=NW)

        # combo is used for dropdown like entering text
        course_2_combo = ttk.Combobox(
            register_frame,
            textvariable=self.var_course2,
            font=("times new roman", 15),
            state="readonly",
            width=18,
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

        course_2_combo.place(x=700, y=90, anchor=NW)

        # course_3 label
        course_3_label = Label(
            register_frame,
            text="Course - 3",
            font=("times new roman", 17),
            bg="white",
        )
        course_3_label.place(x=525, y=150, anchor=NW)

        # combo is used for dropdown like entering text
        course_3_combo = ttk.Combobox(
            register_frame,
            textvariable=self.var_course3,
            font=("times new roman", 15),
            state="readonly",
            width=18,
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

        course_3_combo.place(x=700, y=150, anchor=NW)

        # course_4 label
        course_4_label = Label(
            register_frame,
            text="Course - 4",
            font=("times new roman", 17),
            bg="white",
        )
        course_4_label.place(x=525, y=210, anchor=NW)

        # combo is used for dropdown like entering text
        course_4_combo = ttk.Combobox(
            register_frame,
            textvariable=self.var_course4,
            font=("times new roman", 15),
            state="readonly",
            width=18,
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

        course_4_combo.place(x=700, y=210, anchor=NW)

        # gender label
        gender_label = Label(
            register_frame,
            text="Gender",
            font=("times new roman", 17),
            bg="white",
        )
        gender_label.place(x=525, y=270, anchor=NW)

        # combo is used for dropdown like entering text
        gender_combo = ttk.Combobox(
            register_frame,
            textvariable=self.var_gender,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        gender_combo["values"] = ("", "Male", "Female", "Others", "Prefer not to say")
        gender_combo.current(0)  # to give the bydeafault index

        gender_combo.place(x=700, y=270, anchor=NW)

        # DOB
        dob_label = Label(
            register_frame,
            text="DOB (DD-MM-YYYY)",
            font=("times new roman", 15),
            bg="white",
        )
        dob_label.place(x=525, y=332, anchor=NW)

        # dob button
        dob_btn = Button(
            register_frame,
            command=self.dateFunction,
            width=20,
            height=2,
            textvariable=self.defaultDob,
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )

        dob_btn.place(x=700, y=325, anchor=NW)

        # fatherNum
        fatherNum_label = Label(
            register_frame,
            text="Father's Ph.No.",
            font=("times new roman", 17),
            bg="white",
        )
        fatherNum_label.place(x=525, y=390, anchor=NW)

        fatherNum_entry = ttk.Entry(
            register_frame,
            textvariable=self.var_fatherNum,
            width=22,
            font=("times new roman", 13),
        )
        fatherNum_entry.place(x=700, y=390, anchor=NW)

        # motherNum
        motherNum_label = Label(
            register_frame,
            text="Mother's Ph.No.",
            font=("times new roman", 17),
            bg="white",
        )
        motherNum_label.place(x=525, y=450, anchor=NW)

        motherNum_entry = ttk.Entry(
            register_frame,
            textvariable=self.var_motherNum,
            width=22,
            font=("times new roman", 13),
        )
        motherNum_entry.place(x=700, y=450, anchor=NW)

        # confirmPass
        confirmPass_label = Label(
            register_frame,
            text="Confirm Password",
            font=("times new roman", 17),
            bg="white",
        )
        confirmPass_label.place(x=525, y=510, anchor=NW)

        confirmPass_entry = ttk.Entry(
            register_frame,
            textvariable=self.var_confirm_password,
            width=22,
            font=("times new roman", 13),
        )
        confirmPass_entry.place(x=700, y=510, anchor=NW)

        # -------Buttons------- #

        # uploadPhoto button
        uploadPhoto_btn = Button(
            register_frame,
            command=self.take_photo,
            width=50,
            height=2,
            text="Upload Photo Sample",
            font=("times new roman", 17, "bold"),
            bg="white",
            fg="black",
        )

        uploadPhoto_btn.place(x=245, y=570, anchor=NW)

        # save button
        save_btn = Button(
            register_frame,
            command=self.add_data,
            width=25,
            height=2,
            text="Save Details",
            font=("times new roman", 17, "bold"),
            bg="white",
            fg="black",
        )

        save_btn.place(x=350, y=630, anchor=NW)

    # ------- Functions --------------------------------------#

    def dateFunction(self):
        # Create Object
        rootNew = Tk()

        # Set geometry
        rootNew.geometry("300x300")

        rootNew.title("Calendar")

        # Add Calender
        cal = Calendar(
            rootNew,
            foreground="black",
            selectforeground="red",
            selectmode="day",
            year=2021,
            month=5,
            day=13,
        )

        cal.pack(pady=20)

        def grad_date():
            self.defaultDob.set(str(cal.get_date()))
            rootNew.destroy()

        # Add Button and Label
        Button(rootNew, text="Get Date", command=grad_date).pack(pady=20)

        date = Label(rootNew, text="")
        date.pack(pady=20)

    def add_data(
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
            or self.var_password.get() == ""
            or self.var_confirm_password.get() == ""
            or self.var_course1.get() == "Select Course"
            or self.var_course2.get() == "Select Course"
            or self.var_course3.get() == "Select Course"
            or self.var_course4.get() == "Select Course"
            or self.var_gender.get() == ""
            or self.defaultDob.get() == "Choose Date"
        ):
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root
            )  # Messagebox to show the error and parent=self.root to show the message in the same window is any of the fields would be missing

        else:  # Ab agar data aa jata hai to usse database mein save karna hai
            temp_pass = self.var_password.get()
            temp_confirm_pass = self.var_confirm_password.get()

            if str(temp_pass) == str(temp_confirm_pass):
                try:  # Now we will connect with SQL
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="ShadowWalker77",
                        database="face_recognition_db",
                        auth_plugin="mysql_native_password",
                    )
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
                            self.var_password.get(),
                            self.var_course1.get(),
                            self.var_course2.get(),
                            self.var_course3.get(),
                            self.var_course4.get(),
                            self.var_gender.get(),
                            self.defaultDob.get(),
                        ),
                    )
                    conn.commit()
                    # self.fetch_data()
                    conn.close()  # Closing teh connection
                # messagebox.showinfo("Success","Student details have been added successfully", parent=self.root,) # To showthe sccess message on parent which is self.root

                except Exception as es:
                    messagebox.showerror(
                        "Error", f"Due to : {str(es)}", parent=self.root
                    )

                #########################################################
                temp_var = self.var_year.get() + "_" + self.var_batch.get()

                temp_roll = "'" + self.var_rollNum.get() + "'"
                temp_name = "'" + self.var_name.get() + "'"
                temp_year = "'" + self.var_year.get() + "'"
                temp_sem = "'" + self.var_semester.get() + "'"
                temp_dep = "'" + self.var_dep.get() + "'"
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
                temp_dob = "'" + self.defaultDob.get() + "'"

                try:  # Now we will connect with SQL
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="ShadowWalker77",
                        database="face_recognition_db",
                        auth_plugin="mysql_native_password",
                    )
                    my_cursor = conn.cursor()  # To store the values given by the user
                    sql = "insert into {} values({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(
                        str(temp_var),
                        temp_roll,
                        temp_name,
                        temp_year,
                        temp_sem,
                        temp_dep,
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
                    # self.fetch_data()
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

                ###########################3333333333333333333333333333333333333333333333333333333
                temp_var1 = self.var_course1.get()
                temp_var2 = self.var_course2.get()
                temp_var3 = self.var_course3.get()
                temp_var4 = self.var_course4.get()
                li = [temp_var1, temp_var2, temp_var3, temp_var4]

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
                        messagebox.showerror(
                            "Error", f"Due to : {str(es)}", parent=self.root
                        )

            else:
                messagebox.showerror(
                    "Error", "Both passwords does not match", parent=self.root
                )

    # =========================take photo sample==========================================#
    def take_photo(self):
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
            or self.var_password.get() == ""
            or self.var_confirm_password.get() == ""
            or self.var_course1.get() == "Select Course"
            or self.var_course2.get() == "Select Course"
            or self.var_course3.get() == "Select Course"
            or self.var_course4.get() == "Select Course"
            or self.var_gender.get() == ""
            or self.defaultDob.get() == "Choose Date"
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            cam = cv2.VideoCapture(0)
            cam.set(3, 640)  # set video width
            cam.set(4, 480)  # set video height
            temp1 = self.var_rollNum.get()

            face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            count = 0

            while True:

                ret, img = cam.read()
                # img = cv2.flip(img, -1) # flip video image vertically
                if ret == False:
                    continue

                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_detector.detectMultiScale(gray, 1.3, 5)
                # 1.3 - Scaling Factors
                # 5 - Minimum neighbours

                for (x, y, w, h) in faces:

                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    count += 1

                    # Save the captured image into the datasets folder
                    cv2.imwrite(
                        "dataset/" + str(temp1) + "." + str(count) + ".jpg",
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


if __name__ == "__main__":
    root = Tk()
    obj = studentRegister(root)
    root.mainloop()
