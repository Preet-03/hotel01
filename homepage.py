from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_Win
from r import Roombooking
from d import Details


window = Tk()
window.title("Hotel Management System")
window.geometry("1550x800+0+0")

# ===========1st image===========

image1 = Image.open("img_8.png")
image1 = image1.resize((1550, 140), Image.LANCZOS)
window.photoimage1 = ImageTk.PhotoImage(image1)

lblimage = Label(window, image=window.photoimage1, bd=4, relief=RIDGE)
lblimage.place(x=0, y=0, width=1550, height=140)

# ================logo================

image2 = Image.open("img_6.png")
image2 = image2.resize((230, 140), Image.LANCZOS)
window.photoimage2 = ImageTk.PhotoImage(image2)

lblimage = Label(window, image=window.photoimage2, bd=4, relief=RIDGE)
lblimage.place(x=0, y=0, width=230, height=140)

# ================Title============
lbl_title = Label(window, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold")
                  , bg="black", fg="gold", bd=4, relief=RIDGE)
lbl_title.place(x=0, y=140, width=1550, height=50)

# ==============main_Frame=============
main_frame = Frame(window, bd=4, relief=RIDGE)
main_frame.place(x=0, y=190, width=1550, height=620)

# ===============Menue============
lbl_menue = Label(main_frame, text="MENUE", font=("times new roman", 20, "bold")
                  , bg="black", fg="gold", bd=4, relief=RIDGE)
lbl_menue.place(x=0, y=0, width=230)


def cust_d():
    window.new_window = Toplevel(window)
    window.app = Cust_Win(window.new_window)


def roombooking():
    window.new_window = Toplevel(window)
    window.app = Roombooking(window.new_window)

def details():
    window.new_window = Toplevel(window)
    window.app = Details(window.new_window)

def logout():
    window.destroy()


# ============frame&Buttons================
btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
btn_frame.place(x=0, y=35, width=228, height=185)

cust_btn = Button(btn_frame, text="CUSTOMER", command=cust_d, width=22, font=("times new roman", 14)
                  , bg="black", fg="gold", bd=0, cursor="hand2", activeforeground="gold", activebackground="black")
cust_btn.grid(row=0, column=0, pady=1)

room_btn = Button(btn_frame, text="ROOM",command=roombooking, width=22, font=("times new roman", 14)
                  , bg="black", fg="gold", bd=0, cursor="hand2", activeforeground="gold", activebackground="black")
room_btn.grid(row=1, column=0, pady=1)

details_btn = Button(btn_frame, text="DETAILS",command=details, width=22, font=("times new roman", 14)
                     , bg="black", fg="gold", bd=0, cursor="hand2", activeforeground="gold", activebackground="black")
details_btn.grid(row=2, column=0, pady=1)


logout_btn = Button(btn_frame, text="LOGOUT",command=logout, width=22, font=("times new roman", 14)
                    , bg="black", fg="gold", bd=0, cursor="hand2", activeforeground="gold", activebackground="black")
logout_btn.grid(row=4, column=0, pady=1)

# =====================right_image===============

image3 = Image.open("img_12.png")
image3 = image3.resize((1310, 590), Image.LANCZOS)
window.photoimage3 = ImageTk.PhotoImage(image3)

lblimage1 = Label(main_frame, image=window.photoimage3, bd=4, relief=RIDGE)
lblimage1.place(x=225, y=0, width=1310, height=590)

window.mainloop()
