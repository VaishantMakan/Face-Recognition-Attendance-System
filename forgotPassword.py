from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import smtplib
import numpy as np
import random
import datetime


class forgotPassword:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition Attendance System")

        # ======= Variables ============
        self.var_get_email = StringVar()  # memberType
        self.var_otp = StringVar()
        self.final_otp = ""
        self.var_password = StringVar()
        self.var_password_again = StringVar()
        self.var_after_5_min = ""
        self.var_memType = StringVar()

        # img1 = main background
        img1 = Image.open("Images/thapar1.jpeg")
        img1 = img1.resize((1550, 900), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1550, height=900)

        # img2 = thapar logo
        img2 = Image.open("Images/thaparLogo.png")
        img2 = img2.resize((432, 93), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        logo_img = Label(self.root, image=self.photoimg2)
        logo_img.place(x=20, y=20, width=432, height=93)

        # login frame
        login_frame = Frame(bg_img, bd=2, bg="white", highlightthickness=5)
        login_frame.place(x=510, y=220, width=500, height=440)

        login_frame.config(highlightbackground="black", highlightcolor="black")

        # account label
        account_label = Label(
            login_frame,
            text="Reset Password",
            font=("times new roman", 22),
            bg="white",
            fg="red",
        )
        account_label.grid(row=0, column=0, padx=0)

        # memberType label
        memType_label = Label(
            login_frame,
            text="Member Type",
            font=("times new roman", 17),
            bg="white",
        )
        memType_label.place(x=50, y=50, anchor=NW)

        # combo is used for dropdown like entering text
        memType_combo = ttk.Combobox(
            login_frame,
            textvariable=self.var_memType,
            font=("times new roman", 15),
            state="readonly",
            width=17,
        )
        memType_combo["values"] = (
            "Select Member Type",
            "Student",
            "Teacher",
            "Admin",
        )
        memType_combo.current(0)  # to give the bydeafault index

        memType_combo.place(x=275, y=50, anchor=NW)

        # Email
        email_label = Label(
            login_frame,
            text="Email (thapar.edu)",
            font=("times new roman", 17),
            bg="white",
        )
        email_label.place(x=50, y=100, anchor=NW)

        email_entry = ttk.Entry(
            login_frame,
            textvariable=self.var_get_email,
            width=22,
            font=("times new roman", 13),
        )
        email_entry.place(x=275, y=100, anchor=NW)

        # otp button
        otpSend_btn = Button(
            login_frame,
            command=self.get_otp,
            highlightthickness=1,
            width=17,
            height=2,
            text="Send OTP",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        otpSend_btn.place(x=50, y=145, anchor=NW)
        otpSend_btn.config(highlightbackground="grey", highlightcolor="grey")

        # otp label
        otp_label = Label(
            login_frame,
            text="OTP :",
            font=("times new roman", 17),
            bg="white",
        )
        otp_label.place(x=220, y=150, anchor=NW)

        otp_entry = ttk.Entry(
            login_frame,
            textvariable=self.var_otp,
            width=22,
            font=("times new roman", 13),
        )
        otp_entry.place(x=275, y=150, anchor=NW)

        # password
        password_label = Label(
            login_frame,
            text="New Password",
            font=("times new roman", 17),
            bg="white",
        )
        password_label.place(x=50, y=200, anchor=NW)

        password_entry = ttk.Entry(
            login_frame,
            textvariable=self.var_password,
            width=22,
            font=("times new roman", 13),
        )
        password_entry.place(x=275, y=200, anchor=NW)

        # password conditions
        passwordCondition1_label = Label(
            login_frame,
            text="• Should have at least one number",
            font=("times new roman", 13),
            bg="white",
        )
        passwordCondition1_label.place(x=60, y=230, anchor=NW)

        passwordCondition2_label = Label(
            login_frame,
            text="• Should have at least one uppercase \n and one lowercase character",
            font=("times new roman", 13),
            bg="white",
        )
        passwordCondition2_label.place(x=60, y=250, anchor=NW)

        passwordCondition3_label = Label(
            login_frame,
            text="• Should have at least one special symbol",
            font=("times new roman", 13),
            bg="white",
        )
        passwordCondition3_label.place(x=60, y=270, anchor=NW)

        passwordCondition4_label = Label(
            login_frame,
            text="• Should be between 6 to 20 characters long",
            font=("times new roman", 13),
            bg="white",
        )
        passwordCondition4_label.place(x=60, y=290, anchor=NW)

        # confirm Password
        confirmPassword_label = Label(
            login_frame,
            text="Confirm Password",
            font=("times new roman", 17),
            bg="white",
        )
        confirmPassword_label.place(x=50, y=330, anchor=NW)

        password_entry = ttk.Entry(
            login_frame,
            textvariable=self.var_password_again,
            width=22,
            font=("times new roman", 13),
        )
        password_entry.place(x=275, y=330, anchor=NW)

        # update button
        update_btn = Button(
            login_frame,
            command=self.update_otp,
            width=48,
            height=2,
            text="Update Password",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )

        update_btn.place(x=50, y=380, anchor=NW)

    # ---- functions -----#
    def get_otp(self):
        if self.var_get_email.get() == "" or self.var_memType.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)

        else:
            temp_email = self.var_get_email.get()
            table_name = self.var_memType.get()

            try:  # Now we will connect with SQL
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="ShadowWalker77",
                    database="face_recognition_db",
                    auth_plugin="mysql_native_password",
                )
                my_cursor = conn.cursor()  # To store the values given by the user
                temp_email1 = "'" + temp_email + "'"
                print(temp_email1)
                sql = "select email from {} where email={}".format(
                    str(table_name), str(temp_email1)
                )
                my_cursor.execute(sql)

                my_email = my_cursor.fetchall()

                conn.commit()
                # self.fetch_data()
                conn.close()  # Closing teh connection

            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

            if len(my_email) > 0:
                if str(my_email[0][0]) == str(temp_email):
                    # Give OTP
                    admin_email = "sphinxphoenix.adm@gmail.com"
                    admin_password = "Suv.square"

                    # Now wend the OTP

                    self.final_otp = np.random.randint(100000, 900000)
                    self.var_after_5_min = datetime.datetime.now() + datetime.timedelta(
                        minutes=5
                    )

                    try:
                        # creates SMTP session
                        s = smtplib.SMTP("smtp.gmail.com", 587)

                        # start TLS for security
                        s.starttls()

                        # Authentication
                        s.login(admin_email, admin_password)

                        # message to be sent
                        message = (
                            "Otp is "
                            + str(self.final_otp)
                            + ". OTP is valid for 5 minutes only."
                        )

                        # sending the mail
                        s.sendmail(admin_email, temp_email, message)

                        # terminating the session
                        s.quit()

                        messagebox.showinfo(
                            "Success",
                            "OTP has been sent to your registered email id",
                            parent=self.root,
                        )

                    except Exception as es:
                        messagebox.showerror(
                            "Error", f"Due to : {str(es)}", parent=self.root
                        )

                else:
                    messagebox.showerror(
                        "Error",
                        "Invalid Email (Enter the registered thapar mail",
                        parent=self.root,
                    )
            else:
                messagebox.showerror(
                    "Error",
                    "Invalid Email (Enter the registered thapar mail",
                    parent=self.root,
                )

    def update_otp(self):
        if (
            self.var_otp.get() == ""
            or self.var_password.get() == ""
            or self.var_password_again.get() == ""
            or self.var_get_email.get() == ""
            or self.var_memType.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)

        else:
            now_time = datetime.datetime.now()
            table_name = self.var_memType.get()

            if now_time < self.var_after_5_min:
                temp_otp = self.var_otp.get()
                temp_password = self.var_password.get()
                temp_password_again = self.var_password_again.get()
                temp_email = self.var_get_email.get()

                print(temp_otp)
                print(self.final_otp)

                if self.passwordConditions(str(temp_password)) == True:
                    if str(temp_password) == str(temp_password_again):

                        if str(temp_otp) == str(self.final_otp):
                            try:
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
                                password1 = "'" + temp_password + "'"
                                temp_email1 = "'" + temp_email + "'"

                                sql = "UPDATE {} SET password = {} WHERE email = {} ".format(
                                    str(table_name), str(password1), str(temp_email1)
                                )
                                my_cursor.execute(sql)

                                # password = my_cursor.fetchall()

                                conn.commit()
                                # self.fetch_data()
                                conn.close()  # Closing teh connection
                                # if(self.var_memType == "Teacher"):
                                messagebox.showinfo(
                                    "Success",
                                    "{} details have been added successfully".format(
                                        self.var_memType.get()
                                    ),
                                    parent=self.root,
                                )

                            except Exception as es:
                                messagebox.showerror(
                                    "Error", f"Due to : {str(es)}", parent=self.root
                                )

                        else:
                            messagebox.showerror(
                                "Error", "Invalid OTP", parent=self.root
                            )

                    else:
                        messagebox.showerror(
                            "Error", "Both passwords do not match", parent=self.root
                        )
                else:
                    messagebox.showerror(
                        "Error", "Password requirements not satisfied", parent=self.root
                    )
            else:
                messagebox.showerror(
                    "Error", "Login Session expired.", parent=self.root
                )

    def passwordConditions(self, passwd):
        SpecialSym = ["$", "@", "#", "%"]
        val = True

        if len(passwd) < 6:
            print("length should be at least 6")
            val = False

        if len(passwd) > 20:
            print("length should not be greater than 20")
            val = False

        if not any(char.isdigit() for char in passwd):
            print("Password should have at least one numeral")
            val = False

        if not any(char.isupper() for char in passwd):
            print("Password should have at least one uppercase letter")
            val = False

        if not any(char.islower() for char in passwd):
            print("Password should have at least one lowercase letter")
            val = False

        if not any(char in SpecialSym for char in passwd):
            print("Password should have at least one of the symbols $@#")
            val = False

        return val


if __name__ == "__main__":
    root = Tk()
    obj = forgotPassword(root)
    root.mainloop()
