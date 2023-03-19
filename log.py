from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter import messagebox
from home import wwindow
from getpass import getpass

window = Tk()
window.title("login_page")
window.geometry("1550x800+0+0")

bg = PhotoImage(file="Hotel-PNG-Background-Image.png")

my_label = Label(window, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = Frame(window, bg="beige")
frame.place(x=500, y=100, width=340, height=450)

img1 = Image.open("imgn_1.png")
img1 = img1.resize((100, 100), Image.LANCZOS)
window.photoimage1 = ImageTk.PhotoImage(img1)
my_labelimage = Label(image=window.photoimage1, bg="beige", borderwidth=0)
my_labelimage.place(x=620, y=100, width=100, height=100)

get_str = Label(frame, text="Staff Login", font=("times new roman", 20, "bold"), fg="black", bg="beige")
get_str.place(x=95, y=100)

username = my_label = Label(frame, text="Username:-", font=("times new roman", 15, "bold")
                            , fg="black", bg="beige")
username.place(x=70, y=155)

window.txtuser = ttk.Entry(frame, font=("times new roman", 15,))
window.txtuser.place(x=40, y=180, width=270)

password = my_label = Label(frame, text="Password:-", font=("times new roman", 15, "bold")
                            , fg="black", bg="beige")
password.place(x=70, y=220)

window.txtpass = ttk.Entry(frame, show='*', font=("times new roman", 15,))
window.txtpass.place(x=40, y=250, width=270)


def show_password():
    if window.txtpass.cget('show') == '*':
        window.txtpass.config(show='')
    else:
        window.txtpass.config(show='*')


check_btn = Checkbutton(frame, text="show password", command=show_password)
check_btn.place(x=40, y=290)

img2 = Image.open("imgn_2.png")
img2 = img2.resize((25, 25), Image.LANCZOS)
window.photoimage2 = ImageTk.PhotoImage(img2)
my_labelimage = Label(image=window.photoimage2, bg="beige", borderwidth=0)
my_labelimage.place(x=540, y=255, width=25, height=25)

img3 = Image.open("imgn_4.png")
img3 = img3.resize((25, 25), Image.LANCZOS)
window.photoimage3 = ImageTk.PhotoImage(img3)
my_labelimage = Label(image=window.photoimage3, bg="beige", borderwidth=0)
my_labelimage.place(x=540, y=327, width=25, height=25)


def login_function():
    if window.txtuser.get() == "" or window.txtpass.get() == "":
        messagebox.showerror("Error", "All field required")
    elif window.txtuser.get() == "pythonproject" and window.txtpass.get() == "rgit123":
        messagebox.showinfo("Success", "Welcome to our project")
        window.new_window = Toplevel(window.new_window)
        window.app = window

    else:
        messagebox.showerror("Invalid", "Invalid username or password")


login_button = Button(frame, cursor="hand2", text="Login", font=("times new roman", 15, "bold"),
                      bd=3, relief=RIDGE, fg="black", bg="orange", activebackground="orange", activeforeground="black",
                      command=login_function)
login_button.place(x=110, y=330, width=120, height=35, )

window.mainloop()
