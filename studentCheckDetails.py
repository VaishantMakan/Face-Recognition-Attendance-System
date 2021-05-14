from tkinter import *
from tkinter import ttk
import tkinter  # ttk is used for styling
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry


class studentCheckDetails:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition Attendance System")

        # ======= Variables ============
        self.var_rollNum = StringVar()
        self.var_name = StringVar()
        var_rollNumText = StringVar()
        var_nameText = StringVar()
        var_yearText = StringVar()
        var_semesterText = StringVar()
        var_depText = StringVar()
        var_batchText = StringVar()
        var_emailText = StringVar()
        var_phoneText = StringVar()
        var_course1Text = StringVar()
        var_course2Text = StringVar()
        var_course3Text = StringVar()
        var_course4Text = StringVar()
        var_dobText = StringVar()
        var_genderText = StringVar()
        var_fatherText = StringVar()
        var_motherText = StringVar()

        # img1 = main background
        img1 = Image.open("Images/bg2.jpeg")
        img1 = img1.resize((1550, 900), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1550, height=900)

        # details frame
        details_frame = Frame(bg_img, bd=2, bg="white", highlightthickness=5)
        details_frame.place(x=350, y=130, width=900, height=500)

        details_frame.config(highlightbackground="black", highlightcolor="black")

        # title
        title_lbl = Label(
            bg_img,
            text="CHECK YOUR DETAILS",
            font=("times new roman", 25, "bold"),
            justify=CENTER,
            anchor=S,
            bg="black",
            fg="white",
        )
        title_lbl.place(x=350, y=105, width=900, height=30)

        # Enrollment no.
        rollNum_label = Label(
            details_frame,
            text="Enrollment Number",
            font=("times new roman", 17),
            bg="white",
        )
        rollNum_label.place(x=10, y=30, anchor=NW)

        rollNum_text_label = Label(
            details_frame,
            textvariable=var_rollNumText,
            font=("times new roman", 17),
            bg="white",
        )
        rollNum_text_label.place(x=245, y=30, anchor=NW)

        # Name
        name_label = Label(
            details_frame,
            text="Name",
            font=("times new roman", 17),
            bg="white",
        )
        name_label.place(x=10, y=90, anchor=NW)

        name_text_label = Label(
            details_frame,
            textvariable=var_nameText,
            font=("times new roman", 17),
            bg="white",
        )
        name_text_label.place(x=245, y=90, anchor=NW)

        # Year label
        year_label = Label(
            details_frame,
            text="Year",
            font=("times new roman", 17),
            bg="white",
        )
        year_label.place(x=10, y=150, anchor=NW)

        year_text_label = Label(
            details_frame,
            textvariable=var_yearText,
            font=("times new roman", 17),
            bg="white",
        )
        year_text_label.place(x=245, y=150, anchor=NW)

        # Semester label
        semester_label = Label(
            details_frame,
            text="Semester",
            font=("times new roman", 17),
            bg="white",
        )
        semester_label.place(x=10, y=210, anchor=NW)

        semester_text_label = Label(
            details_frame,
            textvariable=var_semesterText,
            font=("times new roman", 17),
            bg="white",
        )
        semester_text_label.place(x=245, y=210, anchor=NW)

        # Department label
        dep_label = Label(
            details_frame,
            text="Department",
            font=("times new roman", 17),
            bg="white",
        )
        dep_label.place(x=10, y=270, anchor=NW)

        dep_text_label = Label(
            details_frame,
            textvariable=var_depText,
            font=("times new roman", 17),
            bg="white",
        )
        dep_text_label.place(x=245, y=270, anchor=NW)

        # Batch label
        batch_label = Label(
            details_frame,
            text="Batch",
            font=("times new roman", 17),
            bg="white",
        )
        batch_label.place(x=10, y=330, anchor=NW)

        batch_text_label = Label(
            details_frame,
            textvariable=var_batchText,
            font=("times new roman", 17),
            bg="white",
        )
        batch_text_label.place(x=245, y=300, anchor=NW)

        # Email
        email_label = Label(
            details_frame,
            text="Email (thapar.edu)",
            font=("times new roman", 17),
            bg="white",
        )
        email_label.place(x=10, y=390, anchor=NW)

        email_text_label = Label(
            details_frame,
            textvariable=var_emailText,
            font=("times new roman", 17),
            bg="white",
        )
        email_text_label.place(x=245, y=390, anchor=NW)

        # Phone no.
        phone_label = Label(
            details_frame,
            text="Phone No.",
            font=("times new roman", 17),
            bg="white",
        )
        phone_label.place(x=10, y=450, anchor=NW)

        phone_text_label = Label(
            details_frame,
            textvariable=var_phoneText,
            font=("times new roman", 17),
            bg="white",
        )
        phone_text_label.place(x=245, y=450, anchor=NW)

        # ---------------------right-----------------------#

        # course_1 label
        course_1_label = Label(
            details_frame,
            text="Course - 1",
            font=("times new roman", 17),
            bg="white",
        )
        course_1_label.place(x=525, y=30, anchor=NW)

        course_1_text_label = Label(
            details_frame,
            textvariable=var_course1Text,
            font=("times new roman", 17),
            bg="white",
        )
        course_1_text_label.place(x=700, y=30, anchor=NW)

        # course_2 label
        course_2_label = Label(
            details_frame,
            text="Course - 2",
            font=("times new roman", 17),
            bg="white",
        )
        course_2_label.place(x=525, y=90, anchor=NW)

        course_2_text_label = Label(
            details_frame,
            textvariable=var_course2Text,
            font=("times new roman", 17),
            bg="white",
        )
        course_2_text_label.place(x=700, y=90, anchor=NW)

        # course_3 label
        course_3_label = Label(
            details_frame,
            text="Course - 3",
            font=("times new roman", 17),
            bg="white",
        )
        course_3_label.place(x=525, y=150, anchor=NW)

        course_3_text_label = Label(
            details_frame,
            textvariable=var_course3Text,
            font=("times new roman", 17),
            bg="white",
        )
        course_3_text_label.place(x=700, y=150, anchor=NW)

        # course_4 label
        course_4_label = Label(
            details_frame,
            text="Course - 4",
            font=("times new roman", 17),
            bg="white",
        )
        course_4_label.place(x=525, y=210, anchor=NW)

        course_4_text_label = Label(
            details_frame,
            textvariable=var_course4Text,
            font=("times new roman", 17),
            bg="white",
        )
        course_4_text_label.place(x=700, y=210, anchor=NW)

        # gender label
        gender_label = Label(
            details_frame,
            text="Gender",
            font=("times new roman", 17),
            bg="white",
        )
        gender_label.place(x=525, y=270, anchor=NW)

        gender_text_label = Label(
            details_frame,
            textvariable=var_genderText,
            font=("times new roman", 17),
            bg="white",
        )
        gender_text_label.place(x=700, y=270, anchor=NW)

        # DOB
        dob_label = Label(
            details_frame,
            text="DOB (DD-MM-YYYY)",
            font=("times new roman", 15),
            bg="white",
        )
        dob_label.place(x=525, y=332, anchor=NW)

        dob_text_label = Label(
            details_frame,
            textvariable=var_dobText,
            font=("times new roman", 17),
            bg="white",
        )
        dob_text_label.place(x=700, y=325, anchor=NW)

        # fatherNum
        fatherNum_label = Label(
            details_frame,
            text="Father's Ph.No.",
            font=("times new roman", 17),
            bg="white",
        )
        fatherNum_label.place(x=525, y=390, anchor=NW)

        father_text_label = Label(
            details_frame,
            textvariable=var_fatherText,
            font=("times new roman", 17),
            bg="white",
        )
        father_text_label.place(x=700, y=390, anchor=NW)

        # motherNum
        motherNum_label = Label(
            details_frame,
            text="Mother's Ph.No.",
            font=("times new roman", 17),
            bg="white",
        )
        motherNum_label.place(x=525, y=450, anchor=NW)

        mother_text_label = Label(
            details_frame,
            textvariable=var_motherText,
            font=("times new roman", 17),
            bg="white",
        )
        mother_text_label.place(x=700, y=450, anchor=NW)

        # -------Buttons------- #

    # ------- Functions --------------------------------------#


if __name__ == "__main__":
    root = Tk()
    obj = studentCheckDetails(root)
    root.mainloop()
