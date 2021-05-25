from tkinter import *
from tkinter import ttk
import tkinter  # ttk is used for styling
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox


class studentCheckDetails:
    def __init__(self, root, data):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition Attendance System")
        self.my_data = data

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
            textvariable=self.var_rollNumText,
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
            textvariable=self.var_nameText,
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
            textvariable=self.var_yearText,
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
            textvariable=self.var_semesterText,
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
            textvariable=self.var_depText,
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
            textvariable=self.var_batchText,
            font=("times new roman", 17),
            bg="white",
        )
        batch_text_label.place(x=245, y=330, anchor=NW)

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
            textvariable=self.var_emailText,
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
            textvariable=self.var_phoneText,
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
            textvariable=self.var_course1Text,
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
            textvariable=self.var_course2Text,
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
            textvariable=self.var_course3Text,
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
            textvariable=self.var_course4Text,
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
            textvariable=self.var_genderText,
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
            textvariable=self.var_dobText,
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
            textvariable=self.var_fatherText,
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
            textvariable=self.var_motherText,
            font=("times new roman", 17),
            bg="white",
        )
        mother_text_label.place(x=700, y=450, anchor=NW)


if __name__ == "__main__":
    root = Tk()
    obj = studentCheckDetails(root)
    root.mainloop()
