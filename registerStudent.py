from tkinter import *
from tkinter import ttk
import tkinter  # ttk is used for styling
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry


class studentRegister:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition Attendance System")

        # ======= Variables ============
        self.var_rollNum = StringVar()
        self.var_name = StringVar()

        self.defaultDob = StringVar()
        self.defaultDob.set("Choose Date")

        self.dobDate = StringVar()
        self.dobDate.set("")

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
            # textvariable=self.var_memType,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        year_combo["values"] = ("", "I", "II", "III", "IV")
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
            # textvariable=self.var_memType,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        semester_combo["values"] = (
            "",
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
            # textvariable=self.var_memType,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        dep_combo["values"] = ("", "COE", "CSE", "COBS", "EE")
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
            # textvariable=self.var_memType,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        batch_combo["values"] = ("", "2CS9", "2CS10", "2CS11", "2CS12")
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
            # textvariable=self.var_rollNum,
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
            # textvariable=self.var_rollNum,
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
            # textvariable=self.var_rollNum,
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
            # textvariable=self.var_memType,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        course_1_combo["values"] = (
            "",
            "UCS411 - AI",
            "UCS414 - CN",
            "UCS310 - DBMS",
            "UMA035 - OT",
            "UCS503 - SE",
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
            # textvariable=self.var_memType,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        course_2_combo["values"] = (
            "",
            "UCS411 - AI",
            "UCS414 - CN",
            "UCS310 - DBMS",
            "UMA035 - OT",
            "UCS503 - SE",
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
            # textvariable=self.var_memType,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        course_3_combo["values"] = (
            "",
            "UCS411 - AI",
            "UCS414 - CN",
            "UCS310 - DBMS",
            "UMA035 - OT",
            "UCS503 - SE",
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
            # textvariable=self.var_memType,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        course_4_combo["values"] = (
            "",
            "UCS411 - AI",
            "UCS414 - CN",
            "UCS310 - DBMS",
            "UMA035 - OT",
            "UCS503 - SE",
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
            # textvariable=self.var_memType,
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
            # textvariable=self.var_rollNum,
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
            # textvariable=self.var_rollNum,
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
            # textvariable=self.var_rollNum,
            width=22,
            font=("times new roman", 13),
        )
        confirmPass_entry.place(x=700, y=510, anchor=NW)

        # -------Buttons------- #

        # uploadPhoto button
        uploadPhoto_btn = Button(
            register_frame,
            # command=self.add_data,
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
            # command=self.add_data,
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


if __name__ == "__main__":
    root = Tk()
    obj = studentRegister(root)
    root.mainloop()
