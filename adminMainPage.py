from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk


class adminMainPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition Attendance System")

        # ---- Variables --- #

        # img1 = main background
        img1 = Image.open("Images/50 Shades of Grey.jpeg")
        img1 = img1.resize((1550, 900), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1550, height=900)

        # title
        title_lbl = Label(
            bg_img,
            text="ADMIN PORTAL",
            font=("times new roman", 35, "bold"),
            bg="black",
            fg="white",
        )
        title_lbl.place(x=0, y=0, width=1550, height=45)

        # card 1
        # registerStudent frame
        registerStudent_frame = Frame(bg_img, bd=2, bg="white", highlightthickness=5)
        registerStudent_frame.place(x=20, y=70, width=290, height=385)

        registerStudent_frame.config(
            highlightbackground="black", highlightcolor="black"
        )

        # img2 = registerStudent image
        img2 = Image.open("Images/student2.jpeg")
        img2 = img2.resize((225, 190), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        student_img = Label(registerStudent_frame, image=self.photoimg2)
        student_img.place(x=23, y=15, width=225, height=190)

        # registerStudent button
        registerStudent_btn = Button(
            registerStudent_frame,
            # command=self.add_data,
            width=21,
            height=3,
            text="Register Student",
            font=("times new roman", 23, "bold"),
            bg="white",
            fg="black",
        )
        registerStudent_btn.place(x=8, y=250, anchor=NW)

        # card 2
        # Register teacher frame
        registerTeacher_frame = Frame(bg_img, bd=2, bg="white", highlightthickness=5)
        registerTeacher_frame.place(x=440, y=70, width=290, height=385)

        registerTeacher_frame.config(
            highlightbackground="black", highlightcolor="black"
        )

        # img3 = registerTeacher image
        img3 = Image.open("Images/teacher2.jpeg")
        img3 = img3.resize((225, 190), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        teacher_img = Label(registerTeacher_frame, image=self.photoimg3)
        teacher_img.place(x=23, y=15, width=225, height=190)

        # registerTeacher button
        registerTeacher_btn = Button(
            registerTeacher_frame,
            # command=self.add_data,
            width=21,
            height=3,
            text="Register Teacher",
            font=("times new roman", 23, "bold"),
            bg="white",
            fg="black",
        )
        registerTeacher_btn.place(x=8, y=250, anchor=NW)

        # card 3
        # checkStudentDetails frame
        checkStudentDetails_frame = Frame(
            bg_img, bd=2, bg="white", highlightthickness=5
        )
        checkStudentDetails_frame.place(x=850, y=70, width=290, height=385)

        checkStudentDetails_frame.config(
            highlightbackground="black", highlightcolor="black"
        )

        # img4 = registerTeacher image
        img4 = Image.open("Images/id.jpeg")
        img4 = img4.resize((255, 200), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        checkStudentDetails_img = Label(checkStudentDetails_frame, image=self.photoimg4)
        checkStudentDetails_img.place(x=10, y=10, width=255, height=200)

        # registerTeacher button
        checkStudentDetails_btn = Button(
            checkStudentDetails_frame,
            # command=self.add_data,
            width=21,
            height=3,
            text="Check / Edit\n Student Details",
            font=("times new roman", 23, "bold"),
            bg="white",
            fg="black",
        )
        checkStudentDetails_btn.place(x=8, y=250, anchor=NW)

        # card 4
        # checkTeacherDetails frame
        checkTeacherDetails_frame = Frame(
            bg_img, bd=2, bg="white", highlightthickness=5
        )
        checkTeacherDetails_frame.place(x=1245, y=70, width=290, height=385)

        checkTeacherDetails_frame.config(
            highlightbackground="black", highlightcolor="black"
        )

        # img5 = registerTeacher image
        img5 = Image.open("Images/teacherID.jpeg")
        img5 = img5.resize((255, 200), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        checkTeacherDetails_img = Label(checkTeacherDetails_frame, image=self.photoimg5)
        checkTeacherDetails_img.place(x=10, y=10, width=255, height=200)

        # registerTeacher button
        checkTeacherDetails_btn = Button(
            checkTeacherDetails_frame,
            # command=self.add_data,
            width=21,
            height=3,
            text="Check / Edit\n Teacher Details",
            font=("times new roman", 23, "bold"),
            bg="white",
            fg="black",
        )
        checkTeacherDetails_btn.place(x=8, y=250, anchor=NW)

        # card 5
        # trainData frame
        trainData_frame = Frame(bg_img, bd=2, bg="white", highlightthickness=5)
        trainData_frame.place(x=220, y=485, width=290, height=385)

        trainData_frame.config(highlightbackground="black", highlightcolor="black")

        # img6 = registerTeacher image
        img6 = Image.open("Images/trainData2.jpg")
        img6 = img6.resize((255, 200), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        trainData_img = Label(trainData_frame, image=self.photoimg6)
        trainData_img.place(x=10, y=10, width=255, height=200)

        # registerTeacher button
        trainData_btn = Button(
            trainData_frame,
            # command=self.add_data,
            width=21,
            height=3,
            text="Train Data",
            font=("times new roman", 23, "bold"),
            bg="white",
            fg="black",
        )
        trainData_btn.place(x=8, y=250, anchor=NW)

        # card 6
        # photos frame
        photos_frame = Frame(bg_img, bd=2, bg="white", highlightthickness=5)
        photos_frame.place(x=665, y=485, width=290, height=385)

        photos_frame.config(highlightbackground="black", highlightcolor="black")

        # img7 = registerTeacher image
        img7 = Image.open("Images/photos.jpeg")
        img7 = img7.resize((255, 200), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        photos_img = Label(photos_frame, image=self.photoimg7)
        photos_img.place(x=10, y=10, width=255, height=200)

        # registerTeacher button
        photos_btn = Button(
            photos_frame,
            # command=self.add_data,
            width=21,
            height=3,
            text="Photos",
            font=("times new roman", 23, "bold"),
            bg="white",
            fg="black",
        )
        photos_btn.place(x=8, y=250, anchor=NW)

        # card 7
        # checkAttendance frame
        checkAttendance_frame = Frame(bg_img, bd=2, bg="white", highlightthickness=5)
        checkAttendance_frame.place(x=1065, y=485, width=290, height=385)

        checkAttendance_frame.config(
            highlightbackground="black", highlightcolor="black"
        )

        # img7 = checkAttendance image
        img8 = Image.open("Images/attendance2.jpeg")
        img8 = img8.resize((255, 200), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        checkAttendance_img = Label(checkAttendance_frame, image=self.photoimg8)
        checkAttendance_img.place(x=10, y=10, width=255, height=200)

        # checkAttendance button
        checkAttendance_btn = Button(
            checkAttendance_frame,
            # command=self.add_data,
            width=21,
            height=3,
            text="Check Attendance",
            font=("times new roman", 23, "bold"),
            bg="white",
            fg="black",
        )
        checkAttendance_btn.place(x=8, y=250, anchor=NW)


if __name__ == "__main__":
    root = Tk()
    obj = adminMainPage(root)
    root.mainloop()
