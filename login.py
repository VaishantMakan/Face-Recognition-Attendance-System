from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from forgotPassword import forgotPassword
from adminRegisterStudent import studentRegister
from adminRegisterTeacher import teacherRegister
from studentMainPage import studentMainPage
from teacherCourseSelectionPage import teacherCourseSelection
from adminMainPage import adminMainPage


class login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition Attendance System")

        # ======= Variables ============
        self.var_memType = StringVar()  # memberType
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.roll_num = ""
        self.my_data = []

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
        login_frame.place(x=510, y=220, width=500, height=400)

        login_frame.config(highlightbackground="black", highlightcolor="black")

        # account label
        account_label = Label(
            login_frame,
            text="Already have an account?",
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
        memType_label.grid(row=1, column=0, padx=0, pady=15)

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
        memType_combo.grid(row=1, column=1)

        memType_combo.place(x=275, y=50, anchor=NW)

        # Enrollment no.
        rollNum_label = Label(
            login_frame,
            text="Email Id",
            font=("times new roman", 17),
            bg="white",
        )
        rollNum_label.grid(row=2, column=0, padx=50, pady=10, sticky=W)

        rollNum_label.place(x=50, y=100, anchor=NW)

        rollNum_entry = ttk.Entry(
            login_frame,
            textvariable=self.var_email,
            width=22,
            font=("times new roman", 13),
        )
        rollNum_entry.grid(row=2, column=1, padx=0, pady=10, sticky=W)

        rollNum_entry.place(x=275, y=100, anchor=NW)

        # password
        password_label = Label(
            login_frame,
            text="Password",
            font=("times new roman", 17),
            bg="white",
        )
        password_label.grid(row=3, column=0, padx=50, pady=10, sticky=W)

        password_label.place(x=50, y=150, anchor=NW)

        password_entry = ttk.Entry(
            login_frame,
            textvariable=self.var_password,
            show="*",
            width=22,
            font=("times new roman", 13),
        )
        password_entry.grid(row=3, column=1, padx=0, pady=10, sticky=W)

        password_entry.place(x=275, y=150, anchor=NW)

        # Login button
        login_btn = Button(
            login_frame,
            command=self.login_details,
            width=23,
            height=2,
            text="Login",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        login_btn.grid(row=4, column=0)

        login_btn.place(x=50, y=200, anchor=NW)

        # Reset button
        reset_btn = Button(
            login_frame,
            command=self.reset_data,
            width=20,
            height=2,
            text="Reset",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        reset_btn.grid(row=4, column=1)

        reset_btn.place(x=275, y=200, anchor=NW)

        # line seperator
        lineSeperator_frame = Frame(
            login_frame, bd=0, relief=GROOVE, bg="white", highlightthickness=5
        )
        lineSeperator_frame.place(x=-7, y=250, width=500, height=143)

        lineSeperator_frame.config(highlightbackground="black", highlightcolor="black")

        # New label
        new_label = Label(
            lineSeperator_frame,
            text="Reset Password ?",
            font=("times new roman", 22),
            bg="white",
            fg="red",
        )
        new_label.grid(row=0, column=0, padx=0)

        new_label.place(x=2, y=5, anchor=NW)

        # Register button
        register_btn = Button(
            lineSeperator_frame,
            command=self.forgot_details,
            width=49,
            height=2,
            text="Forgot password",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        register_btn.grid(row=1, column=0)

        register_btn.place(x=50, y=50, anchor=NW)

        # ================Function========================

    def login_details(self):
        if (
            self.var_memType.get() == "Select Member Type"
            or self.var_email.get() == ""
            or self.var_password.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)

        else:
            temp_email = self.var_email.get().strip()
            temp_password = self.var_password.get().strip()
            temp_table_name = self.var_memType.get()
            temp_mem = self.var_memType.get()
            password = ""

            try:  # Now we will connect with SQL
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="ShadowWalker77",
                    database="face_recognition_db",
                    auth_plugin="mysql_native_password",
                )

                # ===================cursor 0=============================
                # to check the credentials
                my_cursor = conn.cursor()  # To store the values given by the user
                temp_email = "'" + temp_email + "'"
                sql = "select password from {} where email={}".format(
                    str(temp_table_name), str(temp_email)
                )
                print(sql)
                my_cursor.execute(sql)

                password = my_cursor.fetchall()
                print(password[0][0])
                print(type(password[0]))
                print(temp_password)

                # =================cursor 1==============================
                if temp_mem == "Student":
                    my_cursor2 = conn.cursor()
                    sql = "select * from student where email ={}".format(
                        str(temp_email)
                    )
                    print(sql)
                    my_cursor2.execute(
                        sql
                    )  # To execute this query and store in mycursor
                    data = my_cursor2.fetchall()  # To fetch all the data
                    self.my_data = list(data[0])
                    print(self.my_data)

                ############################################ for teachers cursor 2#########################################3
                if temp_mem == "Teacher":
                    my_cursor2 = conn.cursor()
                    sql = "select * from teacher where email ={}".format(
                        str(temp_email)
                    )
                    print(sql)
                    my_cursor2.execute(
                        sql
                    )  # To execute this query and store in mycursor
                    data = my_cursor2.fetchall()  # To fetch all the data
                    self.my_data = list(data[0])
                    print(self.my_data)

                conn.commit()
                # self.fetch_data()
                conn.close()  # Closing teh connection

            except Exception as es:
                messagebox.showerror("Error", "User not registered", parent=self.root)

            if str(password[0][0]) == str(temp_password):
                if temp_table_name == "Admin":
                    self.new_window = Toplevel(
                        self.root
                    )  # This asks where we want to open our window
                    self.app = adminMainPage(self.new_window)
                elif temp_table_name == "Student":
                    # a = self.roll_num
                    # print(a)
                    self.new_window = Toplevel(
                        self.root
                    )  # This asks where we want to open our window
                    self.app = studentMainPage(self.new_window, self.my_data)
                elif temp_table_name == "Teacher":
                    # a = self.roll_num
                    # print(a)
                    self.new_window = Toplevel(
                        self.root
                    )  # This asks where we want to open our window
                    self.app = teacherCourseSelection(self.new_window, self.my_data)

            else:
                messagebox.showerror("Error", "Invalid credentials", parent=self.root)

    def forgot_details(self):
        self.new_window = Toplevel(
            self.root
        )  # This asks where we want to open our window
        self.app = forgotPassword(self.new_window)

    def reset_data(self):
        self.var_memType.set("Select Member Type")  # memberType
        self.var_email.set("")
        self.var_password.set("")


if __name__ == "__main__":
    root = Tk()
    obj = login(root)
    root.mainloop()
