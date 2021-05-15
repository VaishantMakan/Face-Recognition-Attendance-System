from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk


class login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition Attendance System")

        # ======= Variables ============
        self.var_memType = StringVar()  # memberType
        self.var_rollNum = StringVar()
        self.var_password = StringVar()

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
        login_frame.place(x=510, y=220, width=500, height=360)

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
        memType_label.place(x=50, y=250, anchor=NW)

        # combo is used for dropdown like entering text
        memType_combo = ttk.Combobox(
            login_frame,
            # textvariable=self.var_memType,
            font=("times new roman", 15),
            state="readonly",
            width=17,
        )
        memType_combo["values"] = (
            "",
            "Student",
            "Teacher",
            "Admin",
        )
        memType_combo.current(0)  # to give the bydeafault index

        memType_combo.place(x=275, y=250, anchor=NW)

        # Email
        email_label = Label(
            login_frame,
            text="Email (thapar.edu)",
            font=("times new roman", 17),
            bg="white",
        )
        email_label.place(x=50, y=50, anchor=NW)

        email_entry = ttk.Entry(
            login_frame,
            # textvariable=self.var_rollNum,
            width=22,
            font=("times new roman", 13),
        )
        email_entry.place(x=275, y=50, anchor=NW)

        # otp button
        otpSend_btn = Button(
            login_frame,
            # command=self.add_data,
            highlightthickness=1,
            width=17,
            height=2,
            text="Send OTP",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        otpSend_btn.place(x=50, y=95, anchor=NW)
        otpSend_btn.config(highlightbackground="grey", highlightcolor="grey")

        # otp label
        otp_label = Label(
            login_frame,
            text="OTP :",
            font=("times new roman", 17),
            bg="white",
        )
        otp_label.place(x=220, y=100, anchor=NW)

        otp_entry = ttk.Entry(
            login_frame,
            # textvariable=self.var_rollNum,
            width=22,
            font=("times new roman", 13),
        )
        otp_entry.place(x=275, y=100, anchor=NW)

        # password
        password_label = Label(
            login_frame,
            text="New Password",
            font=("times new roman", 17),
            bg="white",
        )
        password_label.place(x=50, y=150, anchor=NW)

        password_entry = ttk.Entry(
            login_frame,
            textvariable=self.var_password,
            width=22,
            font=("times new roman", 13),
        )
        password_entry.place(x=275, y=150, anchor=NW)

        # confirm Password
        confirmPassword_label = Label(
            login_frame,
            text="Confirm Password",
            font=("times new roman", 17),
            bg="white",
        )
        confirmPassword_label.place(x=50, y=200, anchor=NW)

        password_entry = ttk.Entry(
            login_frame,
            textvariable=self.var_password,
            width=22,
            font=("times new roman", 13),
        )
        password_entry.place(x=275, y=200, anchor=NW)

        # update button
        update_btn = Button(
            login_frame,
            # command=self.add_data,
            width=48,
            height=2,
            text="Update Password",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )

        update_btn.place(x=50, y=300, anchor=NW)

    # ---- functions -----#


if __name__ == "__main__":
    root = Tk()
    obj = login(root)
    root.mainloop()
