from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import filedialog
import pandas as pd
import os


class adminCheckAttendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition Attendance System")

        # ======= Variables ============
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_batch = StringVar()
        self.var_course = StringVar()

        # img1 = main background
        img1 = Image.open("Images/Harvey.jpeg")
        img1 = img1.resize((1550, 900), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1550, height=900)

        # title
        title_lbl = Label(
            bg_img,
            text="CHECK ATTENDANCE",
            font=("times new roman", 25, "bold"),
            bg="black",
            fg="white",
        )
        title_lbl.place(x=510, y=160, width=500, height=40)

        # adminCheckAttendance frame
        attendance_frame = Frame(bg_img, bd=2, bg="white", highlightthickness=5)
        attendance_frame.place(x=510, y=220, width=500, height=275)

        attendance_frame.config(highlightbackground="black", highlightcolor="black")

        # Year label
        year_label = Label(
            attendance_frame,
            text="Year",
            font=("times new roman", 17),
            bg="white",
        )
        year_label.place(x=50, y=50, anchor=NW)

        # combo is used for dropdown like entering text
        year_combo = ttk.Combobox(
            attendance_frame,
            textvariable=self.var_year,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        year_combo["values"] = ("", "I", "II", "III", "IV")
        year_combo.current(0)  # to give the bydeafault index

        year_combo.place(x=275, y=50, anchor=NW)

        # Semester label
        semester_label = Label(
            attendance_frame,
            text="Semester",
            font=("times new roman", 17),
            bg="white",
        )
        semester_label.place(x=50, y=100, anchor=NW)

        # combo is used for dropdown like entering text
        semester_combo = ttk.Combobox(
            attendance_frame,
            textvariable=self.var_sem,
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

        semester_combo.place(x=275, y=100, anchor=NW)

        # Batch label
        batch_label = Label(
            attendance_frame,
            text="Batch",
            font=("times new roman", 17),
            bg="white",
        )
        batch_label.place(x=50, y=150, anchor=NW)

        # combo is used for dropdown like entering text
        batch_combo = ttk.Combobox(
            attendance_frame,
            textvariable=self.var_batch,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        batch_combo["values"] = ("", "2EE9", "2CS10", "2CS11", "2CS12")
        batch_combo.current(0)  # to give the bydeafault index

        batch_combo.place(x=275, y=150, anchor=NW)

        # course label
        course_label = Label(
            attendance_frame,
            text="Course",
            font=("times new roman", 17),
            bg="white",
        )
        course_label.place(x=50, y=200, anchor=NW)

        # combo is used for dropdown like entering text
        course_combo = ttk.Combobox(
            attendance_frame,
            textvariable=self.var_course,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        course_combo["values"] = (
            "",
            "UCS411_AI",
            "UCS414_CN",
            "UCS310_DBMS",
            "UMA035_OT",
            "UCS503_SE",
            "ECE202_Elec",
        )
        course_combo.current(0)  # to give the bydeafault index

        course_combo.place(x=275, y=200, anchor=NW)

        # ---- button ----#

        # adminCheckAttendance button
        adminCheckAttendance_btn = Button(
            bg_img,
            command=self.export_data,
            width=27,
            height=2,
            text="EXPORT ATTENDANCE",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )

        adminCheckAttendance_btn.place(x=650, y=520, anchor=NW)

    # Functions
    def export_data(self):
        if (
            self.var_course.get() == ""
            or self.var_year.get() == ""
            or self.var_batch.get() == ""
            or self.var_sem.get() == ""
        ):
            messagebox.showerror("Error", "Enter all the fields", parent=self.root)

        else:
            year = self.var_year.get()
            batch = self.var_batch.get()
            course = self.var_course.get()

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
                sql = "select * from {}".format(str(table_name))
                df = pd.read_sql(sql, con=conn)

                conn.commit()
                conn.close()

                try:

                    fln = filedialog.asksaveasfilename(
                        initialdir=os.getcwd(),
                        title="Open CSV",
                        filetypes=[("csv", ".CSV")],
                        # filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
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
                    messagebox.showerror(
                        "Error", f"Due to : {str(es)}", parent=self.root
                    )
                # df.to_csv('Cou.csv', index = False)

            except Exception as es:
                messagebox.showerror("Error", "User not registered", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = adminCheckAttendance(root)
    root.mainloop()
