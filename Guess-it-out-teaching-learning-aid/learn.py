from tkinter import *
from tkinter import messagebox




def board():
    root = Tk()
    root.title("Guess It Out-teaching learning aid")
    root.geometry('840x700+300+20')
    root.resizable(False, False)
    root.configure(background="#ff99cc")
    root.iconbitmap(r'logo_.ico')
    # ==========================variable======================
    var = StringVar()

    # =============================function===============
    def mul():
        txtResult.delete(1.0, END)
        m = var.get()
        if m.isdigit():
            m = int(m)
            for i in range(1, 11):
                txtResult.insert(END, '\n\t')
                txtResult.insert(END, m, '\t', 'X', '\t', i, '\t', '=', '\t', (m * i))
                txtResult.insert(END, '\n')
            return True
        else:
            messagebox.showwarning('Error', 'Invalid Data ,Please Enter Number')
            var.set('')
            return False

    def Reset():
        if messagebox.askyesno('Multiplication Table', 'Confirm if you want to Reset'):
            txtResult.delete(1.0, END)
            var.set('')

    def Exit():
        if messagebox.askyesno('Multiplication Table', 'Confirm if you want to Quit'):
            root.destroy()
            from main import option
            option()
        else:
            txtResult.delete(1.0, END)
            var.set('')

    # ================================Frame============================
    f = Frame(root, bg='#ff99cc', relief=RIDGE, padx=20, pady=30)
    f.grid()
    lf = Frame(f, bd=7, width=500, height=600, bg='#ff99cc')
    lf.grid(row=0, column=0, padx=30)

    Rf = Frame(f, bd=7, width=500, height=600, relief=RIDGE, bg="#33ccff")
    Rf.grid(row=0, column=1, padx=30)

    # =========================Entry and Label========================
    titleLabel = Label(Rf, text='WHITE BOARD', font=("Comic Sans MS", 25, 'bold'), bg="#33ccff", fg='crimson')
    titleLabel.grid(row=0, column=0, padx=30, pady=20)

    txtResult = Text(Rf, font=('Comic Sans MS', 13), bd=10, width=25, height=20)
    txtResult.grid(row=1, column=0, pady=10)

    title = Label(lf, text='Enter A Number', font=("Comic Sans MS", 25, 'bold'), bg='#ff99cc', fg='crimson')
    title.grid(row=0, column=0, padx=30, pady=20)

    e = Entry(lf, font=("Comic Sans MS", 15), textvariable=var, bd=10, justify='center')
    e.grid(row=1, column=0, pady=20)

    # =================================Button==========================
    bt1 = Button(lf, text='Multiplication Table', font=("Comic Sans MS", 16), bg='lime', bd=10, width=16, command=mul)
    bt1.grid(row=2, column=0, pady=20)
    bt2 = Button(lf, text='Reset', font=("Comic Sans MS", 16), bg='lime', bd=10, width=16, command=Reset)
    bt2.grid(row=3, column=0, pady=20)
    bt3 = Button(lf, text='Exit', font=("Comic Sans MS", 16), bg='lime', bd=10, width=16, command=Exit)
    bt3.grid(row=4, column=0, pady=20)

    root.mainloop()


