import random
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime

from PIL import Image, ImageTk
import self as self
from django.db.models.sql import where


class Details:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1045x550+230+220")

        # =============TITLE===============

        lbl_title = Label(self.root, text="Room Booking Details", font=("times new roman", 30, "bold")
                          , bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1350, height=50)

        # ============LOGO=============

        image2 = Image.open("img_6.png")
        image2 = image2.resize((100, 40), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(image2)

        lblimage = Label(self.root, image=self.photoimage2, bd=2, relief=RIDGE)
        lblimage.place(x=5, y=2, width=100, height=45)

        labelframeleft = LabelFrame(self.root, text=" New Room Add", font=("times new roman", 18, "bold"), bd=2,
                                    relief=RIDGE,
                                    padx=2)
        labelframeleft.place(x=5, y=50, width=540, height=350)

        # Floor

        Floor = Label(labelframeleft, text="Floor", font=("times new roman", 12, "bold", "italic"),
                      pady=6,
                      padx=2)
        Floor.grid(row=0, column=0, sticky=W)

        self.var_floor = StringVar()

        enty_floor = ttk.Entry(labelframeleft, textvariable=self.var_floor, width=20,
                               font=("times new roman", 13, "bold"))
        enty_floor.grid(row=0, column=1, sticky=W)

        # Room No.

        Room_no = Label(labelframeleft, text="Room no.", font=("times new roman", 12, "bold", "italic"),
                        pady=6,
                        padx=2)
        Room_no.grid(row=1, column=0, sticky=W)
        self.var_room_no = StringVar()

        enty_Rn = ttk.Entry(labelframeleft, textvariable=self.var_room_no, width=20,
                            font=("times new roman", 13, "bold"))
        enty_Rn.grid(row=1, column=1, sticky=W)

        # Room Type

        R_type = Label(labelframeleft, text="Room Type", font=("times new roman", 12, "bold", "italic"),
                       pady=6,
                       padx=2)
        R_type.grid(row=2, column=0, sticky=W)

        self.var_room_type = StringVar()

        combo_R_type = ttk.Combobox(labelframeleft, textvariable=self.var_room_type,
                                    font=("times new roman", 12, "bold",),
                                    width=20,
                                    state="readonly")
        combo_R_type["value"] = ("Single", "Double", "Luxary","Duplex")
        combo_R_type.current(0)
        combo_R_type.grid(row=2, column=1, )

        # ============BUTTONS============
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=250, width=412, height=37)

        btnADD = Button(btn_frame, command=self.add_data, text="ADD", font=("times new roman", 12, "bold",),
                        cursor="hand2", bg="black",
                        fg="gold", width=10)
        btnADD.grid(row=0, column=0, padx=1)

        btnreset = Button(btn_frame, text="RESET", command=self.reset, font=("times new roman", 12, "bold",),
                          cursor="hand2", bg="black",
                          fg="gold", width=10)
        btnreset.grid(row=0, column=1, padx=1)

        btndel = Button(btn_frame, text="DELETE", command=self.delete, font=("times new roman", 12, "bold",),
                        cursor="hand2", bg="black",
                        fg="gold", width=10)
        btndel.grid(row=0, column=2, padx=1)

        btnupdate = Button(btn_frame, text="UPDATE", command=self.update, font=("times new roman", 12, "bold",),
                           cursor="hand2", bg="black",
                           fg="gold", width=10)
        btnupdate.grid(row=0, column=3, padx=1)

        Tableframe = LabelFrame(self.root, text="Show Room Details", font=("times new roman", 18, "bold"), bd=2,
                                relief=RIDGE,
                                padx=2)
        Tableframe.place(x=600, y=55, width=650, height=350)

        scroll_x = ttk.Scrollbar(Tableframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Tableframe, orient=VERTICAL)

        self.room_tbl = ttk.Treeview(Tableframe,
                                     columns=("floor", "roomno", "roomtype",), xscrollcommand=scroll_x.set,
                                     yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_tbl.xview)
        scroll_y.config(command=self.room_tbl.yview)

        self.room_tbl.heading("floor", text="Floor")
        self.room_tbl.heading("roomno", text="Room No")
        self.room_tbl.heading("roomtype", text="Room Type")

        self.room_tbl["show"] = "headings"
        self.room_tbl.pack(fill=BOTH, expand=1)
        self.room_tbl.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_floor.get() == "" or self.var_room_no.get() == "" or self.var_room_type.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="preet0305",
                                               database="hotel")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)", (
                    self.var_floor.get(),
                    self.var_room_no.get(),
                    self.var_room_type.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="preet0305",
                                       database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_tbl.delete(*self.room_tbl.get_children())
            for i in rows:
                self.room_tbl.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.room_tbl.focus()
        content = self.room_tbl.item(cursor_row)
        row = content["values"]

        self.var_floor.set(row[0]),
        self.var_room_no.set(row[1]),
        self.var_room_type.set(row[2]),

    def update(self):
        if self.var_floor.get() == "" or self.var_room_no.get() =="":
            messagebox.showerror("Error", "all fields are required", parent=self.root)
        conn = mysql.connector.connect(host="localhost", username="root", password="preet0305", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute(
            "update details set Floor=%s,RoomType=%s where RoomNo=%s",
            (

                self.var_floor.get(),
                self.var_room_type.get(),
                self.var_room_no.get(),

            ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update", "New Room Details has been updated successful", parent=self.root)

    def delete(self):
        global conn
        delete = messagebox.askyesno("Hotel Management System", "Do you want to delete this Room details",
                                     parent=self.root)
        if delete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="preet0305", database="hotel")
            my_cursor = conn.cursor()
            query = "delete from details where RoomNo=%s"
            value = (self.var_room_no.get(),)
            my_cursor.execute(query, value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):

        self.var_floor.set("")
        self.var_room_no.set("")
        # self.var_room_type.set("")


if __name__ == " __main__":
    root = Tk()
    obj = Details(root)
    root.mainloop()
