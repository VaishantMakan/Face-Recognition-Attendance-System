import numpy as np
import cv2

from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import csv
from tkinter import filedialog

# global variable
myData = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Attendance")

        # ======= Variables ============
        self.var_rollNum = StringVar()  # department
        self.var_name = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendanceStatus = StringVar()

        # img1 = main background
        img1 = Image.open("Images/bg2.jpeg")
        img1 = img1.resize((1550, 900), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1550, height=900)

        # title
        title_lbl = Label(
            bg_img,
            text="Attendance",
            font=("times new roman", 35, "bold"),
            bg="black",
            fg="white",
        )
        title_lbl.place(x=0, y=0, width=1550, height=45)

        ##########################################################

        # main frame
        main_frame = Frame(bg_img, bd=2, bg="black")
        main_frame.place(x=34, y=70, width=1480, height=800)

        # divide into label frame in main frame .... # label frame m ham title daal skte hai

        # left label frame
        Left_frame = LabelFrame(
            main_frame,
            bd=5,
            bg="white",
            relief=RAISED,
            text="Student Details",
            font=("times new roman", 12, "bold"),
        )
        Left_frame.place(x=10, y=10, width=700, height=777)

        img_left = Image.open("Images/db2.png")
        img_left = img_left.resize((700, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=680, height=130)

        left_inside_frame = Frame(Left_frame, bd=2, relief=SUNKEN, bg="white")
        left_inside_frame.place(x=5, y=155, width=680, height=600)

        # ===== Labels ========#
        # AttendanceID
        attendanceID_lable = Label(
            left_inside_frame,
            text="Roll Num: ",
            font=("times new roman", 17, "bold"),
            bg="white",
        )
        attendanceID_lable.grid(row=0, column=0, padx=2, sticky=W)

        attendanceID_entry = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_rollNum,
            width=15,
            font=("times new roman", 13, "bold"),
        )
        attendanceID_entry.grid(row=0, column=1, padx=30, pady=5, sticky=W)

        # # Name
        # name_lable = Label(
        #     left_inside_frame,
        #     text="Name: ",
        #     font=("times new roman", 17, "bold"),
        #     bg="white",
        # )
        # name_lable.grid(row=0, column=2, padx=2, sticky=W)

        # name_entry = ttk.Entry(
        #     left_inside_frame,
        #     textvariable=self.var_name,
        #     width=15,
        #     font=("times new roman", 13, "bold"),
        # )
        # name_entry.grid(row=0, column=3, padx=30, pady=5, sticky=W)

        # Time
        time_lable = Label(
            left_inside_frame,
            text="Time:",
            font=("times new roman", 17, "bold"),
            bg="white",
        )
        time_lable.grid(row=1, column=0, padx=2, sticky=W)

        time_entry = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_time,
            width=15,
            font=("times new roman", 13, "bold"),
        )
        time_entry.grid(row=1, column=1, padx=30, pady=5, sticky=W)

        # date
        date_lable = Label(
            left_inside_frame,
            text="Date:",
            font=("times new roman", 17, "bold"),
            bg="white",
        )
        date_lable.grid(row=1, column=2, padx=2, sticky=W)

        date_entry = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_date,
            width=15,
            font=("times new roman", 13, "bold"),
        )
        date_entry.grid(row=1, column=3, padx=30, pady=5, sticky=W)

        # attendance
        attendance_label = Label(
            left_inside_frame,
            text="Attendance Status",
            font=("times new roman", 17, "bold"),
            bg="white",
        )
        attendance_label.grid(row=2, column=0, padx=2, sticky=W)

        attendance_combo = ttk.Combobox(
            left_inside_frame,
            textvariable=self.var_attendanceStatus,
            font=("times new roman", 15, "bold"),
            state="readonly",
            width=17,
        )
        attendance_combo["values"] = ("Status", "Present", "Absent")
        attendance_combo.current(0)  # to give the bydeafault index
        attendance_combo.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # Button Frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RAISED, bg="black")
        btn_frame.place(x=0, y=385, width=675, height=40)

        # importCSV button in button frame
        importCSV_btn = Button(
            btn_frame,
            command=self.importCsv,
            width=23,
            height=2,
            text="Import csv",
            font=("times new roman", 13, "bold"),
            bg="white",
            fg="black",
        )
        importCSV_btn.grid(row=0, column=0)

        # exportCSV button
        exportCSV_btn = Button(
            btn_frame,
            command=self.exportCsv,
            width=23,
            height=2,
            text="Export csv",
            font=("times new roman", 13, "bold"),
            bg="white",
            fg="black",
        )
        exportCSV_btn.grid(row=0, column=1)

        # update button
        update_btn = Button(
            btn_frame,
            # command=self.exportCsv,
            width=24,
            height=2,
            text="Update",
            font=("times new roman", 13, "bold"),
            bg="white",
            fg="black",
        )
        update_btn.grid(row=0, column=2)

        # reset button
        reset_btn = Button(
            btn_frame,
            command=self.reset_data,
            width=24,
            height=2,
            text="Reset",
            font=("times new roman", 13, "bold"),
            bg="white",
            fg="black",
        )
        reset_btn.grid(row=0, column=3)

        ##################################################

        # right label
        Right_frame = LabelFrame(
            main_frame,
            bd=5,
            bg="white",
            relief=RAISED,
            text="Student Details",
            font=("times new roman", 12, "bold"),
        )
        Right_frame.place(x=720, y=10, width=745, height=777)

        table_frame = Frame(Right_frame, bd=3, bg="white", relief=SUNKEN)
        table_frame.place(x=5, y=155, width=720, height=600)

        img_right = Image.open("Images/thapar2.jpeg")
        img_right = img_right.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=720, height=130)

        # ======== scroll bar table ========= #
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendanceReportTable = ttk.Treeview(
            table_frame,
            column=("RollNum", "Time", "Date", "Attendance"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)

        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.attendanceReportTable.xview)

        scroll_y.config(command=self.attendanceReportTable.yview)

        self.attendanceReportTable.heading("RollNum", text="RollNum")
        # self.attendanceReportTable.heading("Name", text="Name")
        self.attendanceReportTable.heading("Time", text="Time")
        self.attendanceReportTable.heading("Date", text="Date")
        self.attendanceReportTable.heading("Attendance", text="Attendance")

        self.attendanceReportTable["show"] = "headings"
        self.attendanceReportTable.column("RollNum", width=100)
        # self.attendanceReportTable.column("Name", width=100)
        self.attendanceReportTable.column("Time", width=100)
        self.attendanceReportTable.column("Date", width=100)
        self.attendanceReportTable.column("Attendance", width=100)

        self.attendanceReportTable.pack(fill=BOTH, expand=1)
        self.attendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # ====== fetch data ======= #
    def fetchData(self, rows):
        self.attendanceReportTable.delete(*self.attendanceReportTable.get_children())
        for i in rows:
            self.attendanceReportTable.insert("", END, values=i)

    # import csv
    def importCsv(self):
        global myData
        myData.clear()
        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
            parent=self.root,
        )
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetchData(myData)

    # export csv
    def exportCsv(self):
        try:
            if len(myData) < 1:
                messagebox.showerror(
                    "No Data", "No Data Found To Export", parent=self.root
                )
                return False

            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Open CSV",
                filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
                parent=self.root,
            )
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in myData:
                    exp_write.writerow(i)
                messagebox.showinfo(
                    "Data Exported",
                    "Your Data Exported to " + os.path.basename(fln) + " successfully",
                )

        except Exception as es:
            messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.attendanceReportTable.focus()
        content = self.attendanceReportTable.item(cursor_row)
        rows = content["values"]

        self.var_rollNum.set(rows[0])
        self.var_time.set(rows[1])
        self.var_date.set(rows[2])
        self.var_attendanceStatus.set(rows[3])

    def reset_data(self):
        self.var_rollNum.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendanceStatus.set("Status")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
