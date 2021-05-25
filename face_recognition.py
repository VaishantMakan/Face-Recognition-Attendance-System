import numpy as np
import cv2
from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self, root, data):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition Attendance System")
        self.mydata = data
        title_lbl = Label(
            self.root,
            text="MARK ATTENDANCE",
            font=("times new roman", 35, "bold"),
            bg="black",
            fg="white",
        )
        title_lbl.place(x=0, y=0, width=1550, height=45)

        # left image
        img1 = Image.open("Images/face_recog2.jpg")
        img1 = img1.resize((675, 855), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=45, width=675, height=855)

        # right image
        img2 = Image.open("Images/face_recog.jpeg")
        img2 = img2.resize((875, 855), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=675, y=45, width=875, height=855)

        # button
        b1_1 = Button(
            bg_img,
            command=self.face_recog,
            text="Mark Attendance",
            cursor="hand2",
            font=("times new roman", 18, "bold"),
            bg="white",
            fg="black",
        )
        b1_1.place(x=365, y=765, width=150, height=40)

    # ====================create date=============================#

    def create_date(self, batch, d1):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="ShadowWalker77",
                database="face_recognition_db",
                auth_plugin="mysql_native_password",
            )

            string = "alter table {} add {} varchar(100) DEFAULT 'Absent' ".format(
                str(batch), str(d1)
            )
            print(string)
            my_cursor = conn.cursor()
            my_cursor.execute(string)

            conn.commit()
            conn.close()
        except mysql.connector.Error as e:
            print(e)

    # =====================mark attendance=======================#

    def mark__attendance(self, roll_num, batch, d1):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="ShadowWalker77",
                database="face_recognition_db",
                auth_plugin="mysql_native_password",
            )
            # query="UPDATE cn_2cs10 SET email = 'present' WHERE roll_no = %s "
            roll_num = "'" + str(roll_num) + "'"
            string = "UPDATE {} SET {} = {} WHERE enroll_no = {} ".format(
                str(batch), str(d1), str("'present'"), str(roll_num)
            )
            print(string)
            my_cursor = conn.cursor()
            my_cursor.execute(string)

            conn.commit()
            conn.close()
        except mysql.connector.Error as e:
            print(e)

    # ==================Face Recognition =========================#
    def face_recog(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("trainer/trainer.yml")
        cascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath)
        year = self.mydata[0]
        batch = self.mydata[2]
        course = self.mydata[3]
        table_name = year + "_" + batch + "_" + course
        print(table_name)
        now = datetime.now()
        d1 = now.strftime("_%d_%m_%Y_%H_%M")
        self.create_date(table_name, d1)

        font = cv2.FONT_HERSHEY_SIMPLEX

        # iniciate id counter
        id = 0

        # Initialize and start realtime video capture
        cam = cv2.VideoCapture(0)
        cam.set(3, 640)  # set video widht
        cam.set(4, 480)  # set video height

        # Define min window size to be recognized as a face
        minW = 0.1 * cam.get(3)
        minH = 0.1 * cam.get(4)

        while True:

            ret, img = cam.read()
            # img = cv2.flip(img, -1)  # Flip vertically

            if ret == False:
                continue

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(int(minW), int(minH)),
            )

            for (x, y, w, h) in faces:

                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

                id, confidence = recognizer.predict(gray[y : y + h, x : x + w])

                # Check if confidence is less them 100 ==> "0" is perfect match
                if confidence < 77:
                    confidence = "  {0}%".format(round(100 - confidence))
                    self.mark__attendance(id, table_name, d1)
                else:
                    id = "unknown"
                    confidence = "  {0}%".format(round(100 - confidence))

                cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)

                cv2.putText(
                    img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1
                )

            cv2.imshow("Marking Attendance", img)

            k = cv2.waitKey(100) & 0xFF  # Press 'ESC' for exiting video
            if k == 27:
                break

        # Do a bit of cleanup
        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
