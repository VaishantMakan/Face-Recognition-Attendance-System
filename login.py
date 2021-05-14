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
        login_frame.place(x=510, y=220, width=500, height=320)

        login_frame.config(highlightbackground="black", highlightcolor="black")

        # account label
        account_label = Label(
            login_frame,
            text="Already have an account ?",
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
            "",
            "Student",
            "Teacher",
            "Admin",
        )
        memType_combo.current(0)  # to give the bydeafault index
        memType_combo.grid(row=1, column=1)

        memType_combo.place(x=275, y=50, anchor=NW)

        # Email
        email_label = Label(
            login_frame,
            text="Email (thapar.edu)",
            font=("times new roman", 17),
            bg="white",
        )
        email_label.grid(row=2, column=0, padx=50, pady=10, sticky=W)

        email_label.place(x=50, y=100, anchor=NW)

        email_entry = ttk.Entry(
            login_frame,
            textvariable=self.var_rollNum,
            width=22,
            font=("times new roman", 13),
        )
        email_entry.grid(row=2, column=1, padx=0, pady=10, sticky=W)

        email_entry.place(x=275, y=100, anchor=NW)

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
            width=22,
            font=("times new roman", 13),
        )
        password_entry.grid(row=3, column=1, padx=0, pady=10, sticky=W)

        password_entry.place(x=275, y=150, anchor=NW)

        # Forgot Password button
        forgotPass_btn = Button(
            login_frame,
            # command=self.add_data,
            width=23,
            height=2,
            text="Forgot Password",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        forgotPass_btn.place(x=50, y=200, anchor=NW)

        # Reset button
        reset_btn = Button(
            login_frame,
            # command=self.add_data,
            width=20,
            height=2,
            text="Reset",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        reset_btn.grid(row=4, column=1)

        reset_btn.place(x=275, y=200, anchor=NW)

        # Login button
        login_btn = Button(
            login_frame,
            # command=self.add_data,
            width=48,
            height=2,
            text="Login",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )

        login_btn.place(x=50, y=250, anchor=NW)


if __name__ == "__main__":
    root = Tk()
    obj = login(root)
    root.mainloop()
