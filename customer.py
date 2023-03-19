import random
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

from PIL import Image, ImageTk
import self as self
from django.db.models.sql import where


class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1045x550+230+220")

        # ============variables=============

        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_idtype = StringVar()
        self.var_idno = StringVar()

        # =============TITLE===============

        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 30, "bold")
                          , bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1350, height=50)

        # ============LOGO=============

        image2 = Image.open("img_6.png")
        image2 = image2.resize((100, 40), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(image2)

        lblimage = Label(self.root, image=self.photoimage2, bd=2, relief=RIDGE)
        lblimage.place(x=5, y=2, width=100, height=45)

        # ==============CUSTOMER_DETAIL_FRAME===============

        labelframeleft = LabelFrame(self.root, text="Customer Details", font=("times new roman", 18, "bold"), bd=2,
                                    relief=RIDGE,
                                    padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=370)

        # ====================Entry's===========

        # customer reference
        cust_ref = Label(labelframeleft, text="Customer Ref no. :", font=("times new roman", 12, "bold", "italic"),
                         pady=6,
                         padx=2)
        cust_ref.grid(row=0, column=0, sticky=W)

        enty_ref = ttk.Entry(labelframeleft, state="readonly", width=30, textvariable=self.var_ref,
                             font=("times new roman", 13, "bold"))
        enty_ref.grid(row=0, column=1)

        # customer name
        cust_nm = Label(labelframeleft, text="Customer Name:", font=("times new roman", 12, "bold", "italic"), pady=6,
                        padx=2)
        cust_nm.grid(row=1, column=0, sticky=W)
        enty_nm = ttk.Entry(labelframeleft, width=30, textvariable=self.var_cust_name,
                            font=("times new roman", 13, "bold"))
        enty_nm.grid(row=1, column=1)

        # contact number
        contact_no = Label(labelframeleft, text="Contact Number:", font=("times new roman", 12, "bold", "italic"),
                           pady=6,
                           padx=2)
        contact_no.grid(row=2, column=0, sticky=W)

        enty_no = ttk.Entry(labelframeleft, width=30, textvariable=self.var_contact,
                            font=("times new roman", 13, "bold"))
        enty_no.grid(row=2, column=1)

        # Email
        email = Label(labelframeleft, text="Email:", font=("times new roman", 12, "bold", "italic"),
                      pady=6,
                      padx=2)
        email.grid(row=3, column=0, sticky=W)
        email = ttk.Entry(labelframeleft, textvariable=self.var_email, width=30, font=("times new roman", 13, "bold"))
        email.grid(row=3, column=1)

        # Gender Type
        gender = Label(labelframeleft, text="Gender:", font=("times new roman", 12, "bold", "italic"),
                       pady=6,
                       padx=2)
        gender.grid(row=4, column=0, sticky=W)
        combo_gender = ttk.Combobox(labelframeleft, textvariable=self.var_gender, font=("times new roman", 12, "bold",),
                                    width=27, state="readonly")
        combo_gender["value"] = ("Male", "Female", "Others")
        combo_gender.current(0)
        combo_gender.grid(row=4, column=1)

        # ID Proof Type
        ID = Label(labelframeleft, text="ID Proof Type:", font=("times new roman", 12, "bold", "italic"),
                   pady=6,
                   padx=2)
        ID.grid(row=5, column=0, sticky=W)
        ID = ttk.Combobox(labelframeleft, textvariable=self.var_idtype, font=("times new roman", 12, "bold",), width=27,
                          state="readonly")
        ID["value"] = ("Aadhaar Card", "Driving Licence", "PAN Card", "Voter ID", "Passport")
        ID.current(0)
        ID.grid(row=5, column=1)

        # ID number
        id_no = Label(labelframeleft, text="ID Number:", font=("times new roman", 12, "bold", "italic"),
                      pady=6,
                      padx=2)
        id_no.grid(row=6, column=0, sticky=W)
        id_no = ttk.Entry(labelframeleft, width=30, textvariable=self.var_idno, font=("times new roman", 13, "bold"))
        id_no.grid(row=6, column=1)

        # ============BUTTONS============
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=270, width=412, height=40)

        btnADD = Button(btn_frame, text="SAVE", command=self.add_data, font=("times new roman", 12, "bold",),
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

        # ========View & Search_frame===========

        view_search_frame = LabelFrame(self.root, text="View Details And Search System",
                                       font=("times new roman", 18, "bold"),
                                       bd=2,
                                       relief=RIDGE,
                                       padx=2)
        view_search_frame.place(x=435, y=50, width=830, height=370)

        search_lbl = Label(view_search_frame, text="Search by:", fg="gold", bg="black",
                           font=("times new roman", 17, "bold",), pady=6, padx=2)
        search_lbl.grid(row=0, column=0, sticky=W, padx=2)

        self.ser_var = StringVar()

        combo_search = ttk.Combobox(view_search_frame, textvariable=self.ser_var, font=("times new roman", 12, "bold",),
                                    width=24,
                                    state="readonly")
        combo_search["value"] = ("Contact no.", "Ref no.")
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

        self.cust_details_tbl = ttk.Treeview(details_tbl,
                                             columns=("ref", "name", "con_no.", "email", "gender", "id_type", "id_no.")
                                             , xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.cust_details_tbl.xview)
        scroll_y.config(command=self.cust_details_tbl.yview)

        self.cust_details_tbl.heading("ref", text="Refer no.")
        self.cust_details_tbl.heading("name", text="Name")
        self.cust_details_tbl.heading("con_no.", text="Contact no.")
        self.cust_details_tbl.heading("email", text="Email")
        self.cust_details_tbl.heading("gender", text="Gender")
        self.cust_details_tbl.heading("id_type", text="ID proof type")
        self.cust_details_tbl.heading("id_no.", text="ID no.")

        self.cust_details_tbl["show"] = "headings"
        self.cust_details_tbl.pack(fill=BOTH, expand=1)
        self.cust_details_tbl.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_contact.get() == "" or self.var_idno.get() == "" or self.var_cust_name.get() == "" or self.var_email.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="220901", database="hotel")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into Custo values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_idtype.get(),
                    self.var_idno.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "customer has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="220901", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from Custo")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.cust_details_tbl.delete(*self.cust_details_tbl.get_children())
            for i in rows:
                self.cust_details_tbl.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.cust_details_tbl.focus()
        content = self.cust_details_tbl.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_contact.set(row[2]),
        self.var_email.set(row[3]),
        self.var_gender.set(row[4]),
        self.var_idtype.set(row[5]),
        self.var_idno.set(row[6]),

    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter mobile no.", parent=self.root)
        conn = mysql.connector.connect(host="localhost", username="root", password="220901", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("update Custo set cusname=%s,contact=%s,email=%s,gender=%s,idtype=%s ,idno=%s where ref=%s", (

            self.var_cust_name.get(),
            self.var_contact.get(),
            self.var_email.get(),
            self.var_gender.get(),
            self.var_idtype.get(),
            self.var_idno.get(),
            self.var_ref.get()
        ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update", "Customer details has been updated successful", parent=self.root)

    def delete(self):
        global conn
        delete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer", parent=self.root)
        if delete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="220901", database="hotel")
            my_cursor = conn.cursor()
            query = "delete from custo where ref=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query, value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        # self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_contact.set(""),
        self.var_email.set(""),
        # self.var_gender.set(""),
        # self.var_idtype.set(""),
        self.var_idno.set("")

        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="220901", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from Custo where"+str(self.ser_var.get())+"LIKE'%"+str(self.txt_ser.get())+"%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.cust_details_tbl.delete(*self.cust_details_tbl.get_children())
            for i in rows:
                self.cust_details_tbl.insert("", END, values=i)
            conn.commit()
        conn.close()


if __name__ == " __main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
