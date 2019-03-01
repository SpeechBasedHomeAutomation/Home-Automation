from tkinter import *
from tkinter import messagebox

z = ("Times", 20, "italic")

top = Tk()
top.geometry("1500x1000")
# top.configure(background="AntiqueWhite1")
C = Canvas(top, bg="blue", height=250, width=300)
filename = PhotoImage(file="C:\\Users\\patha\\Desktop\\FY project\\011.gif")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
top.mainloop


def login_1():
    top = Tk()
    top.geometry("1500x1000")
    top.configure(background="#aedb9f")

    def add_user():
        pass

    def remove_user():
        pass

    def command():
        pass

    L2 = Label(top, text="Add User", fg="#5c6268", bg="#aedb9f", font=z)
    L2.pack(side=LEFT)
    L2.place(x=550, y=50)

    L2 = Label(top, text="Remove user", fg="#5c6268", bg="#aedb9f", font=z)
    L2.pack(side=LEFT)
    L2.place(x=550, y=250)

    B_9 = Button(top, text="Add", command=add_user, bg="white", fg="#5c6268", activebackground="green")
    B_9.place(x=650, y=200)

    B_9 = Button(top, text="Remove", command=remove_user, bg="white", fg="#5c6268", activebackground="green")
    B_9.place(x=650, y=350)

    L2 = Label(top, text="Username", fg="#5c6268", bg="#aedb9f", font=z)
    L2.pack(side=LEFT)
    L2.place(x=450, y=100)

    L2 = Label(top, text="Password", fg="#5c6268", bg="#aedb9f", font=z)
    L2.pack(side=LEFT)
    L2.place(x=450, y=150)

    L2 = Label(top, text="Username", fg="#5c6268", bg="#aedb9f", font=z)
    L2.pack(side=LEFT)
    L2.place(x=450, y=300)

    L2 = Label(top, text="Fan", fg="#5c6268", bg="#aedb9f", font=z)
    L2.pack(side=LEFT)
    L2.place(x=450, y=450)

    L2 = Label(top, text="Light", fg="#5c6268", bg="#aedb9f", font=z)
    L2.pack(side=LEFT)
    L2.place(x=630, y=450)

    L2 = Label(top, text="AC", fg="#5c6268", bg="#aedb9f", font=z)
    L2.pack(side=LEFT)
    L2.place(x=850, y=450)

    B_9 = Button(top, text="ON", command=remove_user, bg="white", fg="#5c6268", activebackground="green")
    B_9.place(x=400, y=550)

    B_9 = Button(top, text="OFF", command=remove_user, bg="white", fg="#5c6268", activebackground="green")
    B_9.place(x=480, y=550)

    B_9 = Button(top, text="ON", command=remove_user, bg="white", fg="#5c6268", activebackground="green")
    B_9.place(x=600, y=550)

    B_9 = Button(top, text="OFF", command=remove_user, bg="white", fg="#5c6268", activebackground="green")
    B_9.place(x=680, y=550)

    B_9 = Button(top, text="ON", command=remove_user, bg="white", fg="#5c6268", activebackground="green")
    B_9.place(x=800, y=550)

    B_9 = Button(top, text="OFF", command=remove_user, bg="white", fg="#5c6268", activebackground="green")
    B_9.place(x=880, y=550)

    E2 = Entry(top, bd=2)
    E2.pack(side=RIGHT)
    E2.place(x=650, y=110)

    E2 = Entry(top, bd=2)
    E2.pack(side=RIGHT)
    E2.place(x=650, y=160)

    E2 = Entry(top, bd=2)
    E2.pack(side=RIGHT)
    E2.place(x=650, y=310)


def login_2():
    top = Tk()
    top.geometry("1500x1000")
    top.configure(background="#aedb9f")

    def remove_user():
        pass

    L2 = Label(top, text="Fan", fg="#5c6268", bg="#aedb9f", font=z)
    L2.pack(side=LEFT)
    L2.place(x=450, y=150)

    L2 = Label(top, text="Light", fg="#5c6268", bg="#aedb9f", font=z)
    L2.pack(side=LEFT)
    L2.place(x=630, y=150)

    L2 = Label(top, text="AC", fg="#5c6268", bg="#aedb9f", font=z)
    L2.pack(side=LEFT)
    L2.place(x=850, y=150)

    B_9 = Button(top, text="ON", command=remove_user, bg="white", fg="#5c6268", activebackground="green")
    B_9.place(x=400, y=250)

    B_9 = Button(top, text="OFF", command=remove_user, bg="white", fg="#5c6268", activebackground="green")
    B_9.place(x=480, y=250)

    B_9 = Button(top, text="ON", command=remove_user, bg="white", fg="#5c6268", activebackground="green")
    B_9.place(x=600, y=250)

    B_9 = Button(top, text="OFF", command=remove_user, bg="white", fg="#5c6268", activebackground="green")
    B_9.place(x=680, y=250)

    B_9 = Button(top, text="ON", command=remove_user, bg="white", fg="#5c6268", activebackground="green")
    B_9.place(x=800, y=250)

    B_9 = Button(top, text="OFF", command=remove_user, bg="white", fg="#5c6268", activebackground="green")
    B_9.place(x=880, y=250)


L2 = Label(top, text="Username", fg="#5c6268", bg="#d7ccc8", font=z)
L2.pack(side=LEFT)
L2.place(x=450, y=150)

L2 = Label(top, text="Password", fg="#5c6268", bg="#d7ccc8", font=z)
L2.pack(side=LEFT)
L2.place(x=450, y=250)

L2 = Label(top, text="Username", fg="#5c6268", bg="#d7ccc8", font=z)
L2.pack(side=LEFT)
L2.place(x=450, y=450)

L2 = Label(top, text="Password", fg="#5c6268", bg="#d7ccc8", font=z)
L2.pack(side=LEFT)
L2.place(x=450, y=550)

L2 = Label(top, text="Admin Login", fg="#5c6268", bg="AntiqueWhite1", font=z)
L2.pack(side=LEFT)
L2.place(x=550, y=100)

L2 = Label(top, text="User Login", fg="#5c6268", bg="AntiqueWhite1", font=z)
L2.pack(side=LEFT)
L2.place(x=550, y=400)

E2 = Entry(top, bd=2)
E2.pack(side=RIGHT)
E2.place(x=650, y=160)

E2 = Entry(top, bd=2)
E2.pack(side=RIGHT)
E2.place(x=650, y=260)

E2 = Entry(top, bd=2)
E2.pack(side=RIGHT)
E2.place(x=650, y=460)

E2 = Entry(top, bd=2)
E2.pack(side=RIGHT)
E2.place(x=650, y=560)

##E3 = Entry(top, bd =2)
##E3.pack(side = RIGHT)
##E3.place(x=140,y=150,width=1030,height=80)

B_9 = Button(top, text="LOGIN", command=login_1, bg="white", fg="#5c6268", activebackground="green")
B_9.place(x=600, y=300)

B_9 = Button(top, text="LOGIN", command=login_2, bg="white", fg="#5c6268", activebackground="green")
B_9.place(x=600, y=600)

top.mainloop()

##"#5c6268"

