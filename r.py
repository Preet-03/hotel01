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


class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1045x550+230+220")

        # ===========Variables==========
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noOfdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

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

        labelframeleft = LabelFrame(self.root, text="Room Booking Details", font=("times new roman", 18, "bold"), bd=2,
                                    relief=RIDGE,
                                    padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=650)

        # ===========Fetch bttn===========
        btnfetch = Button(labelframeleft, command=self.Fetch_contact, text="Fetch Data",
                          font=("times new roman", 11, "bold",),
                          cursor="hand2", bg="black",
                          fg="gold", width=7)
        btnfetch.place(x=330, y=4)

        # ===============ENTRY'S==================

        # Customer contact

        cust_con = Label(labelframeleft, text="Customer contact:", font=("times new roman", 12, "bold", "italic"),
                         pady=6,
                         padx=2)
        cust_con.grid(row=0, column=0, sticky=W)

        enty_con = ttk.Entry(labelframeleft, textvariable=self.var_contact, width=20,
                             font=("times new roman", 13, "bold"))
        enty_con.grid(row=0, column=1, sticky=W)

        # check in date

        check_in_date = Label(labelframeleft, text="Check in date:", font=("times new roman", 12, "bold", "italic"),
                              pady=6,
                              padx=2)
        check_in_date.grid(row=1, column=0, sticky=W)

        enty_check_in = ttk.Entry(labelframeleft, textvariable=self.var_checkin, width=30,
                                  font=("times new roman", 13, "bold"))
        enty_check_in.grid(row=1, column=1)

        # Check out date

        check_out_date = Label(labelframeleft, text="Check out date:",
                               font=("times new roman", 12, "bold", "italic"),
                               pady=6,
                               padx=2)
        check_out_date.grid(row=2, column=0, sticky=W)

        enty_out_date = ttk.Entry(labelframeleft, textvariable=self.var_checkout, width=30,
                                  font=("times new roman", 13, "bold"))
        enty_out_date.grid(row=2, column=1)

        # Room type

        R_type = Label(labelframeleft, text="Room Type:", font=("times new roman", 12, "bold", "italic"),
                       pady=6,
                       padx=2)
        R_type.grid(row=3, column=0, sticky=W)

        combo_R_type = ttk.Combobox(labelframeleft, textvariable=self.var_roomtype,
                                    font=("times new roman", 12, "bold",),
                                    width=30,
                                    state="readonly")
        combo_R_type["value"] =("Single","Double","Luxury","Duplex")
        combo_R_type.current(0)
        combo_R_type.grid(row=3, column=1, )

        # Availabel Room

        AVL_R = Label(labelframeleft, text="Available Room:", font=("times new roman", 12, "bold", "italic"),
                      pady=6,
                      padx=2)
        AVL_R.grid(row=4, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="220901",
                                       database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows = my_cursor.fetchall()

        combo_R_A = ttk.Combobox(labelframeleft, textvariable=self.var_roomavailable,
                                    font=("times new roman", 12, "bold",),
                                    width=30,
                                    state="readonly")
        combo_R_A["value"] =rows
        combo_R_A.current(0)
        combo_R_A.grid(row=4, column=1, )

        #enty_AVL = ttk.Entry(labelframeleft, textvariable=self.var_roomavailable, width=30,font=("times new roman", 13, "bold"))
        #enty_AVL.grid(row=4, column=1)

        # Meal

        cust_meal = Label(labelframeleft, text="Meal:", font=("times new roman", 12, "bold", "italic"),
                          pady=6,
                          padx=2)
        cust_meal.grid(row=5, column=0, sticky=W)

        combo_M_type = ttk.Combobox(labelframeleft, textvariable=self.var_meal,
                                    font=("times new roman", 12, "bold",),
                                    width=30,
                                    state="readonly")
        combo_M_type["value"] = ("Lunch", "Dinner", "All")
        combo_M_type.current(0)
        combo_M_type.grid(row=5, column=1, )

        # No. of Days

        No_days = Label(labelframeleft, text="No. of Days:", font=("times new roman", 12, "bold", "italic"),
                        pady=6,
                        padx=2)
        No_days.grid(row=6, column=0, sticky=W)

        enty_days = ttk.Entry(labelframeleft, textvariable=self.var_noOfdays, width=30,
                              font=("times new roman", 13, "bold"))
        enty_days.grid(row=6, column=1)

        # Paid TAx

        cust_tax = Label(labelframeleft, text="Paid Tax:", font=("times new roman", 12, "bold", "italic"),
                         pady=6,
                         padx=2)
        cust_tax.grid(row=7, column=0, sticky=W)

        enty_tax = ttk.Entry(labelframeleft, textvariable=self.var_paidtax, width=30,
                             font=("times new roman", 13, "bold"))
        enty_tax.grid(row=7, column=1)

        # Sub Total

        sub_ttl = Label(labelframeleft, text="Sub Total:", font=("times new roman", 12, "bold", "italic"),
                        pady=6,
                        padx=2)
        sub_ttl.grid(row=8, column=0, sticky=W)

        enty_sub = ttk.Entry(labelframeleft, textvariable=self.var_actualtotal, width=30,
                             font=("times new roman", 13, "bold"))
        enty_sub.grid(row=8, column=1)

        # Total cost

        Total = Label(labelframeleft, text="Total Cost:", font=("times new roman", 12, "bold", "italic"),
                      pady=6,
                      padx=2)
        Total.grid(row=9, column=0, sticky=W)

        enty_cost = ttk.Entry(labelframeleft, textvariable=self.var_total, width=30,
                              font=("times new roman", 13, "bold"))
        enty_cost.grid(row=9, column=1)

        # ==========bill btn=========
        btnbill = Button(labelframeleft, command=self.total, text="BIll", font=("times new roman", 12, "bold",),
                         cursor="hand2", bg="black",
                         fg="gold", width=10)
        btnbill.grid(row=10, column=0, padx=1, sticky=W)

        # =========Image============

        # ============BUTTONS============
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=37)

        btnADD = Button(btn_frame, command=self.add_data, text="ADD", font=("times new roman", 12, "bold",),
                        cursor="hand2", bg="black",
                        fg="gold", width=10)
        btnADD.grid(row=0, column=0, padx=1)

        btnreset = Button(btn_frame, command=self.reset, text="RESET", font=("times new roman", 12, "bold",),
                          cursor="hand2", bg="black",
                          fg="gold", width=10)
        btnreset.grid(row=0, column=1, padx=1)

        btndel = Button(btn_frame, command=self.delete, text="DELETE", font=("times new roman", 12, "bold",),
                        cursor="hand2", bg="black",
                        fg="gold", width=10)
        btndel.grid(row=0, column=2, padx=1)

        btnupdate = Button(btn_frame, command=self.update, text="UPDATE", font=("times new roman", 12, "bold",),
                           cursor="hand2", bg="black",
                           fg="gold", width=10)
        btnupdate.grid(row=0, column=3, padx=1)

        # ========View & Search_frame===========

        view_search_frame = LabelFrame(self.root, text="View Details And Search System",
                                       font=("times new roman", 18, "bold"),
                                       bd=2,
                                       relief=RIDGE,
                                       padx=2)
        view_search_frame.place(x=435, y=280, width=830, height=400)

        search_lbl = Label(view_search_frame, text="Search by:", fg="gold", bg="black",
                           font=("times new roman", 17, "bold",), pady=6, padx=2)
        search_lbl.grid(row=0, column=0, sticky=W, padx=2)

        self.ser_var = StringVar()

        combo_search = ttk.Combobox(view_search_frame, textvariable=self.ser_var, font=("times new roman", 12, "bold",),
                                    width=24,
                                    state="readonly")
        combo_search["value"] = ("Contact no.", "Room")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_ser = StringVar()
        textsearch = ttk.Entry(view_search_frame, textvariable=self.txt_ser, font=("times new roman", 13, "bold"),
                               width=24)
        textsearch.grid(row=0, column=2, padx=2)

        btnsearch = Button(view_search_frame, command=self.search, text="Search", font=("times new roman", 12, "bold",),
                           cursor="hand2",
                           bg="black",
                           fg="gold", width=10, bd=2)
        btnsearch.grid(row=0, column=3, padx=1)

        btnshowall = Button(view_search_frame, command=self.fetch_data, text="Show all",
                            font=("times new roman", 12, "bold",), cursor="hand2",
                            bg="black",
                            fg="gold", width=10, bd=2)
        btnshowall.grid(row=0, column=4, padx=1)

        # =============show data tabel============

        details_tbl = Frame(view_search_frame, bd=2, relief=RIDGE)
        details_tbl.place(x=0, y=50, width=820, height=250)

        scroll_x = ttk.Scrollbar(details_tbl, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_tbl, orient=VERTICAL)

        self.room_tbl = ttk.Treeview(details_tbl,
                                     columns=(
                                         "contact", "checkin", "checkout", "roomtype", "roomavailable", "meal",
                                         "noOfdays",)
                                     , xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_tbl.xview)
        scroll_y.config(command=self.room_tbl.yview)

        self.room_tbl.heading("contact", text="Contact")
        self.room_tbl.heading("checkin", text="Check-in")
        self.room_tbl.heading("checkout", text="Check-out.")
        self.room_tbl.heading("roomtype", text="Room Type")
        self.room_tbl.heading("roomavailable", text="Room No")
        self.room_tbl.heading("meal", text="Meal")
        self.room_tbl.heading("noOfdays", text="No. of Days")

        self.room_tbl["show"] = "headings"
        self.room_tbl.pack(fill=BOTH, expand=1)

        self.room_tbl.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "" or self.var_checkout.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="220901",
                                               database="hotel")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room2 values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_contact.get(),
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noOfdays.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room has been Booked", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="220901",
                                       database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room2")
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

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noOfdays.set(row[6])

    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter mobile no.", parent=self.root)
        conn = mysql.connector.connect(host="localhost", username="root", password="220901", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute(
            "update room2 set check_in=%s,check_out=%s,roomtype=%s,roomavaliable=%s ,meal=%s,noOfdays=%s where Contact=%s",
            (

                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_noOfdays.get(),
                self.var_contact.get()
            ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update", "Room details has been updated successful", parent=self.root)

    def delete(self):
        global conn
        delete = messagebox.askyesno("Hotel Management System", "Do you want to delete this Room", parent=self.root)
        if delete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="220901", database="hotel")
            my_cursor = conn.cursor()
            query = "delete from room2 where Contact=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_checkin.set("")
        self.var_checkout.set("")
        # self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noOfdays.set("")
        self.var_contact.set("")
        self.var_total.set("")
        self.var_actualtotal.set("")
        self.var_paidtax.set("")

    # ============All Data Fetch==============

    def Fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter contact no.", parent=self.root)
        else:
            # ===========Name Fetch==========
            conn = mysql.connector.connect(host="localhost", username="root", password="220901", database="hotel")
            my_cursor = conn.cursor()
            query = ("select cusname from custo where contact=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "This number is Not Found ", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataframe.place(x=455, y=55, width=820, height=220)

                lblname = Label(showDataframe, text="Name", font=("ariel", 12, "bold"))
                lblname.place(x=0, y=0)

                lbl = Label(showDataframe, text=row, font=("ariel", 12, "bold"))
                lbl.place(x=90, y=0)

                # ============Email Fetch============

                conn = mysql.connector.connect(host="localhost", username="root", password="220901", database="hotel")
                my_cursor = conn.cursor()
                query = ("select email from custo where contact=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblemail = Label(showDataframe, text="Email", font=("ariel", 12, "bold"))
                lblemail.place(x=0, y=30)

                lbl2 = Label(showDataframe, text=row, font=("ariel", 12, "bold"))
                lbl2.place(x=90, y=30)

                # ==========Gender Fetch=========

                conn = mysql.connector.connect(host="localhost", username="root", password="220901", database="hotel")
                my_cursor = conn.cursor()
                query = ("select gender from custo where contact=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblgender = Label(showDataframe, text="Gender", font=("ariel", 12, "bold"))
                lblgender.place(x=0, y=60)

                lbl1 = Label(showDataframe, text=row, font=("ariel", 12, "bold"))
                lbl1.place(x=90, y=60)

                # ==============ID Type Fetch=================

                conn = mysql.connector.connect(host="localhost", username="root", password="220901", database="hotel")
                my_cursor = conn.cursor()
                query = ("select idtype from custo where contact=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblidt = Label(showDataframe, text="ID Type", font=("ariel", 12, "bold"))
                lblidt.place(x=0, y=90)

                lbl3 = Label(showDataframe, text=row, font=("ariel", 12, "bold"))
                lbl3.place(x=90, y=90)

                # ================ID No==================

                conn = mysql.connector.connect(host="localhost", username="root", password="220901", database="hotel")
                my_cursor = conn.cursor()
                query = ("select idno from custo where contact=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblidn = Label(showDataframe, text="ID NO.", font=("ariel", 12, "bold"))
                lblidn.place(x=0, y=120)

                lbl4 = Label(showDataframe, text=row, font=("ariel", 12, "bold"))
                lbl4.place(x=90, y=120)

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="220901", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room2 where" + str(self.ser_var.get()) + " LIKE '%" + str(self.txt_ser.get()) +
                          "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_tbl.delete(*self.root_tbl.get_children())
            for i in rows:
                self.room_tbl.insert("", END, values=i)
            conn.commit()
        conn.close()

    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")
        self.var_noOfdays.set(abs(outDate - inDate).days)

        if (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Single"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.2))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.2)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        if (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Single"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.2))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.2)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        if (self.var_meal.get() == "All" and self.var_roomtype.get() == "Single"):
            q1 = float(1000)
            q2 = float(1000)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.2))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.2)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "All" and self.var_roomtype.get() == "Luxury"):
            q1 = float(2300)
            q2 = float(1700)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.2))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.2)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "All" and self.var_roomtype.get() == "Duplex"):
            q1 = float(3000)
            q2 = float(2000)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.2))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.2)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Double"):
            q1 = float(1300)
            q2 = float(900)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.2))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.2)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Double"):
            q1 = float(1300)
            q2 = float(900)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.2))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.2)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        else:
            (self.var_meal.get() == "ALL" and self.var_roomtype.get() == "Double")
            q1 = float(1300)
            q2 = float(1700)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.2))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.2)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


if __name__ == " __main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
