from tkinter import *
import sqlite3
from tkinter import messagebox
import pygame

#Initialization
pygame.mixer.init()
pygame.init()

# Music
pygame.mixer.music.load('music/fun.mpeg')
pygame.mixer.music.play(100)
pygame.mixer.music.set_volume(.4)


# login page
def gotologin():
    conn = sqlite3.connect('quiz.db')
    create = conn.cursor()
    conn.commit()
    create.execute('SELECT * FROM userSignUp')
    z = create.fetchall()
    loginpage(z)


def logpg():
    sup.destroy()
    gotologin()


def loginpage(logdata):
    global login
    login = Tk()
    login.geometry("650x650+450+10")
    login.resizable(False, False)
    login.title("Guess It Out-teaching learning aid")
    login.configure(background="#ff99cc")
    login.iconbitmap(r'logo_.ico')
    login_canvas = Canvas(login, width=650, height=550, bg='#ff99cc', bd=0, highlightthickness=0)
    login_canvas.pack(expand=YES, fill=BOTH)

    # login image
    img = PhotoImage(file="login.png")
    lab_img = Label(login_canvas, image=img, bg='#ff99cc')
    lab_img.place(relx=0.3, rely=0.2)

    heading = Label(login_canvas, text="LOGIN", fg="black", bg="#ff99cc", font=("Comic Sans MS", 25, 'bold'))
    heading.place(relx=0.52, rely=0.28)

    # validation for login page
    user_name = StringVar()
    password = StringVar()
    f_name = StringVar()
    new_passw = StringVar()

    # username
    ulabel = Label(login_canvas, text="Username", fg='black', bg='#ff99cc', font=("Comic Sans MS", 12, 'bold'))
    ulabel.place(relx=0.16, rely=0.5)
    user = Entry(login_canvas, bg='#d3d3d3', fg='black', textvariable=user_name, width=30,
                 font=("Comic Sans MS", 12, 'bold'))
    user.place(relx=0.31, rely=0.5, height=30)

    # password
    plabel = Label(login_canvas, text="Password", fg='black', bg='#ff99cc', font=("Comic Sans MS", 12, 'bold'))
    plabel.place(relx=0.16, rely=0.6)
    pas = Entry(login_canvas, bg='#d3d3d3', fg='black', textvariable=password, width=30, show='*',
                font=("Comic Sans MS", 12, 'bold'))
    pas.place(relx=0.31, rely=0.6, height=30)

    # logic for validation check
    def check():

        check_counter = 0
        if user_name.get() == "" and pas.get() == "":
            messagebox.showinfo('Login Status', 'please fill credentials')

        else:
            if user_name.get() == "":
                messagebox.showerror('Login Status', "Username can't be empty")

            else:
                check_counter += 1

            if pas.get() == "":
                messagebox.showerror('Login Status', "Password can't be empty")

            else:
                check_counter += 1

            if check_counter == 2:
                for a, b, c in logdata:
                    if b == user.get() and c == pas.get():
                        messagebox.showinfo('Login Status', 'Logged in Successfully!')
                        oppt()
                        break
                else:
                    messagebox.showerror('Login Status', 'invalid username or password')
                    user.delete(0, END)
                    pas.delete(0, END)

    # forget password
    def forget_password():
        check_counter = 0
        if (f_name.get() == "") and (new_passw.get() == ""):
            messagebox.showerror('Error', "please fill the credentials", parent=top)
        else:
            if f_name.get() == "":
                messagebox.showerror('Error', "Full Name can't be empty", parent=top)
            else:
                check_counter += 1

            if new_passw.get() == "":
                messagebox.showerror('Error', "password can't be empty", parent=top)
            else:
                check_counter += 1

            if check_counter == 2:
                conn = sqlite3.connect('quiz.db')
                create = conn.cursor()
                # Find Existing username if any take proper action
                find_user = 'SELECT * FROM userSignUp WHERE USERNAME = ? and NAME = ?'
                create.execute(find_user, [(user.get()), (f_name.get())])
                row = create.fetchone()
                if row is None:
                    messagebox.showinfo('Error', 'Please enter correct name', parent=top)
                else:
                    find_user = 'UPDATE userSignUp set PASSWORD=? WHERE USERNAME = ?'
                    create.execute(find_user, [(new_passw.get()), (user.get())])
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Your password has been reset, Please login with new password",
                                        parent=top)
                    top.destroy()
                    login.destroy()
                    gotologin()
            # except EXCEPTION as es:
            #     messagebox.showerror("Error", es)

    def forget_password_window():
        if user_name.get() == "":
            messagebox.showinfo('Error', 'Please enter username to reset password')
        else:
            try:
                conn = sqlite3.connect('quiz.db')
                create = conn.cursor()
                # Find Existing username if any take proper action
                find_user = 'SELECT USERNAME FROM userSignUp WHERE USERNAME = ?'
                create.execute(find_user, [(user.get())])
                row = create.fetchone()
                if row is None:
                    messagebox.showinfo('Error', 'Please enter valid username to reset password')
                else:
                    conn.close()
                    global top
                    top = Toplevel(login)
                    top.geometry("350x350+450+10")
                    top.resizable(False, False)
                    top.configure(background="#ff99cc")
                    top.iconbitmap(r'logo_.ico')
                    top.focus_force()
                    top.grab_set()
                    top_canvas = Canvas(top, width=650, height=550, bg='#ff99cc', bd=0, highlightthickness=0)
                    top_canvas.pack(expand=YES, fill=BOTH)

                    head = Label(top_canvas, text="FORGET PASSWORD", fg="black", bg="#ff99cc",
                                 font=("Comic Sans MS", 15, 'bold'))
                    head.place(relx=0.2, rely=0.03)

                    flabel = Label(top_canvas, text="Name", fg='black', bg='#ff99cc',
                                   font=("Comic Sans MS", 11, 'bold'))
                    flabel.place(relx=0.03, rely=0.25)
                    fname = Entry(top_canvas, bg='#d3d3d3', fg='black', width=20, textvariable=f_name,
                                  font=("Comic Sans MS", 12, 'bold'))
                    fname.place(relx=0.36, rely=0.25, height=25)

                    new_password = Label(top_canvas, text="New Password", fg='black', bg='#ff99cc',
                                         font=("Comic Sans MS", 11, 'bold'))
                    new_password.place(relx=0.04, rely=0.45)
                    new_pass = Entry(top_canvas, bg='#d3d3d3', fg='black', width=20, textvariable=new_passw,
                                     font=("Comic Sans MS", 12, 'bold'))
                    new_pass.place(relx=0.36, rely=0.45, height=25)

                    btn_change_password = Button(top_canvas, text='Reset Password', command=forget_password,
                                                 borderwidth=2, fg="#000000", bg="#33ccff", cursor="hand2",
                                                 font=("Comic Sans MS", 14, 'bold'), activebackground="#33B5E5")
                    btn_change_password.place(relx=0.3, rely=0.65)

            except EXCEPTION as es:
                messagebox.showerror("Error", es)

    # LOGIN BUTTON
    log = Button(login_canvas, text='LOGIN', command=check, width=8, borderwidth=2, fg="#000000", bg="#33ccff",
                 font=("Comic Sans MS", 14, 'bold'), cursor="hand2", activebackground="#33B5E5")
    log.place(relx=0.42, rely=0.75)

    forg_btn = Button(login_canvas, text='forgot password?', font=("Comic Sans MS", 12, 'bold'),
                      command=forget_password_window, bg="#ff99cc", activebackground="#ff99cc", fg="blue", border=0)
    forg_btn.place(relx=0.4, rely=0.85)

    # back button for login page
    def logback():
        login.destroy()
        sign()

    img1 = PhotoImage(file="back.png")
    lab_img1 = Button(login_canvas, image=img1, bg="#ff99cc", border=0, justify='center', activebackground="#ff99cc",
                      command=lambda: logback())
    lab_img1.pack(anchor='nw', pady=10, padx=10)

    login.mainloop()


# signup page
def signuppage():
    root.destroy()
    sign()


def sign():
    global sup
    sup = Tk()
    sup.geometry("650x650+450+10")
    sup.resizable(False, False)
    sup.title("Guess It Out-teaching learning aid")
    sup.configure(background="#ff99cc")
    sup.iconbitmap(r'logo_.ico')
    sup_canvas = Canvas(sup, width=650, height=550, bg='#ff99cc', bd=0, highlightthickness=0)
    sup_canvas.pack(expand=YES, fill=BOTH)
    img = PhotoImage(file="signup.png")

    lab_img = Label(sup_canvas, image=img, bg='#ff99cc')
    lab_img.place(relx=0.4, rely=0.15)

    # validation for signup page
    fname = StringVar()
    uname = StringVar()
    passW = StringVar()

    # full name
    flabel = Label(sup_canvas, text="Name", fg='black', bg='#ff99cc', font=("Comic Sans MS", 12, 'bold'))
    flabel.place(relx=0.16, rely=0.4)
    fname = Entry(sup_canvas, bg='#d3d3d3', fg='black', textvariable=fname, width=30,
                  font=("Comic Sans MS", 12, 'bold'))
    fname.place(relx=0.31, rely=0.4, height=30)

    # username
    ulabel = Label(sup_canvas, text="Username", fg='black', bg='#ff99cc', font=("Comic Sans MS", 12, 'bold'))
    ulabel.place(relx=0.16, rely=0.5)
    user = Entry(sup_canvas, bg='#d3d3d3', fg='black', textvariable=uname, width=30, font=("Comic Sans MS", 12, 'bold'))
    user.place(relx=0.31, rely=0.5, height=30)

    # password
    plabel = Label(sup_canvas, text="Password", fg='black', bg='#ff99cc', font=("Comic Sans MS", 12, 'bold'))
    plabel.place(relx=0.16, rely=0.6)
    pas = Entry(sup_canvas, bg='#d3d3d3', fg='black', textvariable=passW, width=30, show='*',
                font=("Comic Sans MS", 12, 'bold'))
    pas.place(relx=0.31, rely=0.6, height=30)

    def addUserToDataBase():

        name = fname.get()
        username = user.get()
        password = pas.get()

        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        create.execute('CREATE TABLE IF NOT EXISTS userSignUp(NAME text, USERNAME text NOT NULL PRIMARY KEY,'
                       'PASSWORD text)')
        create.execute("INSERT INTO userSignUp VALUES (?,?,?)", (name, username, password))
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z = create.fetchall()
        print(z)
        # L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
        conn.close()
        logpg()
        # loginpage(z)

    # def gotologin():
    #     conn = sqlite3.connect('quiz.db')
    #     create = conn.cursor()
    #     conn.commit()
    #     create.execute('SELECT * FROM userSignUp')
    #     z = create.fetchall()
    #     loginpage(z)

    # validation check for signup
    def insert_record():
        check_counter = 0
        if (fname.get() == "") and (user.get() == "") and (pas.get() == ""):
            messagebox.showerror('Error', "please fill the credentials")

        else:
            if (fname.get()).isalpha():
                check_counter += 1

            else:
                messagebox.showerror('Error', "Name field can't be empty and it should not contain numbers, symbol, "
                                              "spaces,")

            if user.get() == "":
                messagebox.showerror('Error', "username can't be empty")

            else:
                check_counter += 1

            if pas.get() == "":
                messagebox.showerror('Error', "password can't be empty")
            else:
                check_counter += 1

            if check_counter == 3:
                conn = sqlite3.connect('quiz.db')
                create = conn.cursor()
                create.execute('CREATE TABLE IF NOT EXISTS userSignUp(NAME text,'
                               ' USERNAME text NOT NULL PRIMARY KEY, PASSWORD text)')

                conn.commit()
                # Find Existing username if any take proper action
                find_user = 'SELECT USERNAME FROM userSignUp WHERE USERNAME = ?'
                create.execute(find_user, [(user.get())])
                if create.fetchall():
                    messagebox.showerror('Error!', 'This Username already exist, Create another one.')
                else:
                    # Create New Account
                    messagebox.showinfo('Success!', 'Account Created!')
                    addUserToDataBase()


    # signup BUTTON
    sp = Button(sup_canvas, text='SignUp', command=insert_record, width=8, borderwidth=2, fg="#000000",
                bg="#33ccff", font=("Comic Sans MS", 14, 'bold'), cursor="hand2", activebackground="#33B5E5")
    sp.place(relx=0.42, rely=0.8)

    log = Button(sup_canvas, text='Already have a Account?', font=("Comic Sans MS", 12, 'bold'),
                 command=logpg, bg="#ff99cc", activebackground="#ff99cc", fg="blue", border=0)
    log.place(relx=0.34, rely=0.9)

    # back button for singup page
    def back():
        sup.destroy()
        start()

    img1 = PhotoImage(file="back.png")
    lab_img1 = Button(sup_canvas, image=img1, bg="#ff99cc", border=0, justify='center', activebackground="#ff99cc",
                      command=lambda: back())
    lab_img1.pack(anchor='nw', pady=10, padx=10)

    sup.mainloop()


# option page
def oppt():
    login.destroy()
    option()


def option():
    global opt
    opt = Tk()
    opt.geometry("650x650+450+10")
    opt.resizable(False, False)
    opt.title("Guess It Out-teaching learning aid")
    opt.configure(background="#ff99cc")
    opt.iconbitmap(r'logo_.ico')
    opt_canvas = Canvas(opt, width=650, height=550, bg='#ff99cc', bd=0, highlightthickness=0)
    opt_canvas.pack(expand=YES, fill=BOTH)
    img1 = PhotoImage(file="logout.png")
    lab_img1 = Button(opt_canvas, image=img1, bg="#ff99cc", border=0, justify='center', activebackground="#ff99cc",
                      command=lambda: logout())
    lab_img1.pack(anchor='nw', pady=15, padx=15)

    sel_btn1 = Button(opt_canvas, text="MATH", width=14, borderwidth=8, font=("Comic Sans MS", 18), fg="#000000",
                      bg="#94C11F", cursor="hand2", command=mathstart)
    sel_btn1.pack(pady=(110, 0))

    img = PhotoImage(file="student.png")
    lab_img = Label(opt_canvas, image=img, bg='#ff99cc')
    lab_img.pack(pady=(30, 0))

    img2 = PhotoImage(file="math.png")
    lab_img = Label(opt_canvas, image=img2, bg='#ff99cc')
    lab_img.place(relx=0.63, rely=0.08)

    img3 = PhotoImage(file="girl.png")
    lab_img = Label(opt_canvas, image=img3, bg='#ff99cc')
    lab_img.place(relx=0.75, rely=0.2)

    img4 = PhotoImage(file="eng.png")
    lab_img = Label(opt_canvas, image=img4, bg='#ff99cc')
    lab_img.place(relx=0.14, rely=0.533)

    img5 = PhotoImage(file="boy.png")
    lab_img = Label(opt_canvas, image=img5, bg='#ff99cc')
    lab_img.place(relx=0.03, rely=0.69)

    sel_btn2 = Button(opt_canvas, text="ENGLISH", width=14, borderwidth=8, font=("Comic Sans MS", 18), fg="#000000",
                      bg="#94C11F", cursor="hand2", command=engstart)
    sel_btn2.pack(pady=(30, 5))

    sel_btn3 = Button(opt_canvas, text="Let's Learn!!", bg="#ff99cc", border=0, activebackground="#ff99cc",
                      command=lambda: whiteboard(), cursor="hand2", font=("Comic Sans MS", 18))
    sel_btn3.place(relx=0.75, rely=0.9)

    def whiteboard():
        opt.destroy()
        from learn import board
        board()

    def logout():
        messagebox.showinfo('Success', 'Logged Out Successfully')
        opt.destroy()
        gotologin()

    opt.mainloop()


def engstart():
    opt.destroy()
    eng()


def eng():
    global eg
    eg = Tk()
    eg.geometry("650x650+450+10")
    eg.resizable(False, False)
    eg.title("Guess It Out-teaching learning aid")
    eg.configure(background="#ff99cc")
    eg.iconbitmap(r'logo_.ico')
    eg_canvas = Canvas(eg, width=650, height=550, bg="#ff99cc", bd=0, highlightthickness=0)
    eg_canvas.pack(expand=YES, fill=BOTH)
    img = PhotoImage(file="back.png")
    lab_img1 = Button(eg_canvas, image=img, bg="#ff99cc", border=0, justify='center', activebackground="#ff99cc",
                      command=lambda: engback())
    lab_img1.pack(anchor='nw', pady=15, padx=15)

    level = Label(eg_canvas, text='Select your Difficulty Level !!', bg="#ff99cc", font=("Comic Sans MS", 27, 'bold'))
    level.place(relx=0.09, rely=0.2)

    var = IntVar()
    easyR = Radiobutton(eg_canvas, text='Easy', bg="#ff99cc", font=("Comic Sans MS", 20), value=1, variable=var,
                        activebackground='#ff99cc')
    easyR.place(relx=0.25, rely=0.4)

    hardR = Radiobutton(eg_canvas, text='Hard', bg="#ff99cc", font=("Comic Sans MS", 20), value=2, variable=var,
                        activebackground='#ff99cc')
    hardR.place(relx=0.25, rely=0.56)

    def navigate():

        x = var.get()
        if x == 1:
            eg.destroy()
            import english
            english.elvl()
        elif x == 2:
            eg.destroy()
            import english
            english.hlvl()
        else:
            pass

    def engback():
        eg.destroy()
        option()

    nxt = Button(eg_canvas, text='NEXT', command=navigate, width=8, borderwidth=2, fg="#000000", bg="#33ccff",
                 font=("Comic Sans MS", 14, 'bold'), cursor="hand2", activebackground="#33B5E5")
    nxt.place(relx=0.25, rely=0.76)

    eg.mainloop()


def mathstart():
    opt.destroy()
    maths()


def maths():
    global mat
    mat = Tk()
    mat.geometry("650x650+450+10")
    mat.resizable(False, False)
    mat.title("Guess It Out-teaching learning aid")
    mat.configure(background="#ff99cc")
    mat.iconbitmap(r'logo_.ico')
    mat_canvas = Canvas(mat, width=650, height=550, bg="#ff99cc", bd=0, highlightthickness=0)
    mat_canvas.pack(expand=YES, fill=BOTH)
    img = PhotoImage(file="back.png")
    lab_img1 = Button(mat_canvas, image=img, bg="#ff99cc", border=0, justify='center', activebackground="#ff99cc",
                      command=lambda: mathback())
    lab_img1.pack(anchor='nw', pady=15, padx=15)

    level = Label(mat_canvas, text='Select your Difficulty Level !!', bg="#ff99cc", font=("Comic Sans MS", 27, 'bold'))
    level.place(relx=0.09, rely=0.2)

    var = IntVar()
    easyR = Radiobutton(mat_canvas, text='Easy', bg="#ff99cc", font=("Comic Sans MS", 20), value=1, variable=var,
                        activebackground='#ff99cc')
    easyR.place(relx=0.25, rely=0.4)

    hardR = Radiobutton(mat_canvas, text='Hard', bg="#ff99cc", font=("Comic Sans MS", 20), value=2, variable=var,
                        activebackground='#ff99cc')
    hardR.place(relx=0.25, rely=0.56)

    def navigate():

        x = var.get()
        if x == 1:
            mat.destroy()
            import matth
            matth.elvl()
        elif x == 2:
            mat.destroy()
            import matth
            matth.hlvl()
        else:
            pass

    def mathback():
        mat.destroy()
        option()

    nxt = Button(mat_canvas, text='NEXT', command=navigate, width=8, borderwidth=2, fg="#000000", bg="#33ccff",
                 font=("Comic Sans MS", 14, 'bold'), cursor="hand2", activebackground="#33B5E5")
    nxt.place(relx=0.25, rely=0.76)

    mat.mainloop()


def start():
    global root
    root = Tk()
    root.geometry("650x650+450+10")
    root.resizable(False, False)
    root.title("Guess It Out-teaching learning aid")
    root.configure(background="#ff99cc")
    root.iconbitmap(r'logo_.ico')
    canvas = Canvas(root, width=650, height=550, bg='#ff99cc', bd=0, highlightthickness=0)
    canvas.pack(expand=YES, fill=BOTH)
    img = PhotoImage(file="logo.png")

    lab_img = Label(canvas, image=img, bg='#e6fff5')
    lab_img.pack(pady=(50, 0))

    button = Button(canvas, text='Start', command=signuppage, width=18, borderwidth=8, fg="#000000", bg="#33ccff",
                    font=("Comic Sans MS", 18, 'bold'), cursor="hand2", activebackground="#33B5E5")
    button.pack(pady=(50, 20))


    root.mainloop()


if __name__ == '__main__':
    start()
