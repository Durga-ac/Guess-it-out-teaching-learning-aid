from tkinter import *
from tkinter import messagebox

from main import eng, option


def elvl():
    global lvl
    lvl = Tk()
    lvl.geometry("650x650+450+10")
    lvl.resizable(False, False)
    lvl.title("Guess It Out-teaching learning aid")
    lvl.configure(background="#ff99cc")
    lvl.iconbitmap(r'logo_.ico')
    elvl_canvas = Canvas(lvl, width=650, height=550, bg='#ff99cc', bd=0, highlightthickness=0)
    elvl_canvas.pack(expand=YES, fill=BOTH)
    img = PhotoImage(file="back.png")
    lab_img = Button(elvl_canvas, image=img, bg="#ff99cc", border=0, justify='center', activebackground="#ff99cc",
                     command=lambda: lback())
    lab_img.place(relx=0.03, rely=0.03)

    img1 = PhotoImage(file="home.png")
    lab_img1 = Button(elvl_canvas, image=img1, bg="#ff99cc", border=0, justify='center', activebackground="#ff99cc",
                      command=lambda: llback())
    lab_img1.place(relx=0.87, rely=0.05)

    sel_btn1 = Button(elvl_canvas, text="level1", width=14, borderwidth=8, font=("Comic Sans MS", 18), fg="#000000",
                      bg="#94C11F", cursor="hand2", command=lambda: start_game(1))
    sel_btn1.pack(pady=(200, 0))

    sel_btn2 = Button(elvl_canvas, text="level2", width=14, borderwidth=8, font=("Comic Sans MS", 18), fg="#000000",
                      bg="#94C11F", cursor="hand2", command=lambda: start_game(2))
    sel_btn2.pack(pady=(100, 5))

    def start_game(args):
        if args == 1:
            lvl.destroy()
            from Options import level_1
            level_1.main()
        elif args == 2:
            from Options.level_1 import points
            if points < 10:
                messagebox.showerror("Error", 'Score at least 10 to Unlock level 2')
            else:
                messagebox.showinfo('Success', 'Level Unlocked')
                lvl.destroy()
                from Options import level_2
                level_2.main()

    def lback():
        lvl.destroy()
        eng()

    def llback():
        lvl.destroy()
        option()

    lvl.mainloop()


def hlvl():
    global lvll
    lvll = Tk()
    lvll.geometry("650x650+450+10")
    lvll.resizable(False, False)
    lvll.title("Guess It Out-teaching learning aid")
    lvll.configure(background="#ff99cc")
    lvll.iconbitmap(r'logo_.ico')
    hlvl_canvas = Canvas(lvll, width=650, height=550, bg='#ff99cc', bd=0, highlightthickness=0)
    hlvl_canvas.pack(expand=YES, fill=BOTH)
    img = PhotoImage(file="back.png")
    lab_img = Button(hlvl_canvas, image=img, bg="#ff99cc", border=0, justify='center', activebackground="#ff99cc",
                     command=lambda: lback())
    lab_img.place(relx=0.03, rely=0.03)

    img1 = PhotoImage(file="home.png")
    lab_img1 = Button(hlvl_canvas, image=img1, bg="#ff99cc", border=0, justify='center', activebackground="#ff99cc",
                      command=lambda: llback())
    lab_img1.place(relx=0.87, rely=0.05)

    sel_btn1 = Button(hlvl_canvas, text="level1", width=14, borderwidth=8, font=("Comic Sans MS", 18), fg="#000000",
                      bg="#94C11F", cursor="hand2", command=lambda: start_game(3))
    sel_btn1.pack(pady=(200, 0))

    sel_btn2 = Button(hlvl_canvas, text="level2", width=14, borderwidth=8, font=("Comic Sans MS", 18), fg="#000000",
                      bg="#94C11F", cursor="hand2", command=lambda: start_game(4))
    sel_btn2.pack(pady=(100, 5))

    def start_game(args):
        if args == 3:
            lvll.destroy()
            from Options import level_3
            level_3.main()
        elif args == 4:
            from Options.level_3 import points
            if points < 10:
                messagebox.showerror("Error", 'Score at least 10 to Unlock level 2')
            else:
                messagebox.showinfo('Success', 'Level Unlocked')
                lvll.destroy()
                from Options import level_4
                level_4.main()

    def lback():
        lvll.destroy()
        eng()

    def llback():
        lvll.destroy()
        option()

    lvll.mainloop()
