import os
from tkinter import *
from random import *
from tkinter import messagebox
import time
from main import option
from matth import elvl

level_6_WORD = ['7+4+3', '69+4+11', '10+36+41', '111+12+11', '44-20-12', '76-52-8', '99-21-34', '80-60-20', '20-13-4',
                '34+24+15', '77-34-40', '24+32+61', ]

level_6_ANSWER = ['14', '84', '87', '134', '12', '16', '44', '0', '3',
                  '73', '3', '117', ]

ran_num = randrange(0, (len(level_6_WORD)))
jumbled_rand_word = level_6_WORD[ran_num]

points = 0


def main():
    def back():
        my_window.destroy()
        elvl()

    def home():
        my_window.destroy()
        option()

    def change():
        global ran_num
        ran_num = randrange(0, (len(level_6_WORD)))
        word.configure(text=level_6_WORD[ran_num])
        get_input.delete(0, END)
        ans.configure(text="Answer")

    def cheak():
        global points, ran_num
        user_word = get_input.get().upper()
        if user_word == level_6_ANSWER[ran_num]:
            points += 5
            score.configure(text="Score:- " + str(points))
            messagebox.showinfo('correct', "Correct Answer.. Keep it Up!")
            ran_num = randrange(0, (len(level_6_WORD)))
            word.configure(text=level_6_WORD[ran_num])
            get_input.delete(0, END)
            ans.configure(text="Answer")
        else:
            messagebox.showerror("Error", "Inorrect Answer..Try your best!")
            get_input.delete(0, END)

    def show_answer():
        global points
        if points > 4:
            points -= 5
            score.configure(text="Score:- " + str(points))
            time.sleep(0.5)
            ans.configure(text="Answer= " + level_6_ANSWER[ran_num])
        else:
            messagebox.showerror("Error", 'Not enough points')

    my_window = Tk()
    my_window.geometry("620x650+500+30")
    my_window.resizable(False, False)
    my_window.title("Guess It Out-teaching learning aid")
    my_window.configure(background="#ff99cc")
    my_window.iconbitmap(r'logo_.ico')
    img = PhotoImage(file="back.png")
    img1 = PhotoImage(file="home.png")
    lab_img = Button(my_window, image=img, bg="#ff99cc", border=0, justify='center', activebackground="#ff99cc",
                     command=back)
    lab_img.place(relx=0.03, rely=0.03)

    lab_img1 = Button(my_window, image=img1, bg="#ff99cc", border=0, justify='center', activebackground="#ff99cc",
                      command=home)
    lab_img1.place(relx=0.87, rely=0.04)

    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")
    with open("highscore.txt", "r") as f:
        highscore = f.read()

    if points > int(highscore):
        highscore = points
        with open("highscore.txt", "w") as f:
            f.write(str(highscore))

    score = Label(
        text="Score:-"+str(points),
        bg="#ff99cc",
        fg="#000000",
        font=("Comic Sans MS", 20, 'bold'),
    )
    score.pack(anchor="n", pady=10)
    score.place(relx=0.4, rely=0.12)

    hscore = Label(
        text="Highscore:-" + str(highscore),
        bg="#ff99cc",
        fg="#000000",
        font=("Comic Sans MS", 20, 'bold'),
    )
    hscore.place(relx=0.35, rely=0.04)

    word = Label(
        text=level_6_WORD[ran_num],
        bg="#ff99cc",
        fg="#000000",
        font=("Comic Sans MS", 20, 'bold'),
    )
    word.pack(pady=(140, 15))

    get_input = Entry(
        font=("Comic Sans MS", 25, 'bold'),
        borderwidth=10,
        justify='center',
    )
    get_input.pack(pady=(10, 35))

    submit = Button(
        text="Submit",
        width=18,
        borderwidth=8,
        font=("Comic Sans MS", 14, 'bold'),
        fg="#000000",
        bg="#99ffd6",
        command=cheak,
    )
    submit.pack(pady=(10, 35))

    change = Button(
        text="Change Word",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("Comic Sans MS", 14, 'bold'),
        command=change,
    )
    change.pack(pady=(10, 35))

    ans = Button(
        text="Answer",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("Comic Sans MS", 14, 'bold'),
        command=show_answer,
    )
    ans.pack(pady=(10, 35))

    my_window.mainloop()



