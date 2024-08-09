import os
from tkinter import *
from random import *
from tkinter import messagebox
import time
from main import option
from english import elvl

level_1_WORD = ['CADI', 'EANC', 'PAEX', 'QUAA', 'EARA', 'AIRD', 'RLIA', 'YRAM', 'RSAT', 'LYRA', 'AYSH', 'ATMO', 'OAPT',
                'AUTN', 'RUAA', 'TAOU', 'YWAA', 'AXEL', 'IASX', 'LXEA', 'AONX', 'YBAB', 'KACB', 'EDBA', 'HBAT', 'LBAI',
                'IABT', 'BEAK', 'DLBA', 'LBAE', 'KBLA', 'ABLL', 'BMAL', 'NBAD', 'BEAN', 'GANB', 'ANBK', 'ABRE', 'ARBF',
                'RBKA', 'NBAK', 'BAER', 'LWOB', 'ELBU', 'ULBR', 'OBRA', 'TOBA', 'OBYD', 'GYOB', 'BILO', 'ODLB', 'LLBO',
                'BOLT', 'OMBB', 'DNBO', 'OBNE', 'NOGB', 'NOBK', 'BYON', 'OKOB', 'BOMO', 'AEGC', 'KECA', 'CLAF', 'CLLA',
                'MALC', 'MCEA', 'PACM', 'ACST', 'CVEA', 'ECLL', 'NETC', 'CPAH', 'CARH', 'HTAC', 'CFEH', 'EHWC', 'HCIN',
                'CHPI', 'IHTC', 'CHPO', 'HOCW', 'UHCB', 'TICY', 'CADL', 'LMAC', 'LCNA', 'KDRA', 'RAND', 'ADTR', 'HSAD',
                'ADTA', 'TADE', 'WNAD', 'ZDEA', 'DDAE', 'FDAE', 'LADE', 'ADNE', 'RAED', 'EBDT', 'CEDK', 'ODEV', 'DWNO',
                'ZDOE', 'RAGD', 'WARD', 'WDRE', 'IDPR', 'PDOR', 'GURD', 'RDMU', 'LDAU', 'UCKD', 'TCUD', 'UELD', 'EUFD',
                'LEFI', 'FLIL', 'LIMF', 'NFDI', 'EINF', 'KINF', 'FERI', 'RIMF', 'HSIF', 'TSIF', 'EIVF', 'ZFIZ', 'AFGL',
                'LKFA', 'FLPA', 'TFAL', 'FWLA', 'AFEL', 'FDEL', 'LEFE', 'WEFL', 'FLXE', 'LFPI', 'TFLI', 'OFLP', 'LFOW',
                'AING', 'AEGM', 'GGAN', 'GAOL', 'APSG', 'ATEG', 'AVEG', 'AGZE', 'EGRA', 'GKEE', 'GESE', 'SEGM', 'ENEG',
                'RMGE', 'GIDR', 'TSGI', 'ALGD', 'LGAM', 'OGLM', 'WOLG', 'ULGE', 'TAGO', 'SEOG', 'OLDG', 'OGLF', 'GNOE',
                'GNGO', 'GDOO', 'NGWO', 'AEHD', 'LAHE', 'EHAP', 'HRAE', 'LHED', 'LHLE', 'ELPH', 'BREH', 'HEID', 'HIGH',
                'HKEI', 'LLIH', 'HNDI', 'OHPE', 'HNRO', 'THSO', 'HRUO', 'HEVO', 'OWHL', 'EIDC', 'CINO', 'IEAD', 'DLEI',
                'DLOI', 'NICH', 'NOFI', 'TNOI', 'SIRI', 'RONI', 'IHCT', 'EITM', 'LJIA', 'ZZAJ', 'EAJN', 'EJPE', 'REJK',
                'NXIJ', 'JOBS', 'KOJC', 'NIOJ', 'KEOJ', 'TLJO', 'DUJO', 'JUPM', 'UJKN', 'UJRY', 'SUJT', 'EKEN', 'PEEK',
                'EKPT', 'OEKT', 'IKCK', 'NDKI', 'NKIG', 'ISKS', 'TKIE', 'IWIK', 'KENE', 'EKWN', 'NKTI', 'NOKT', 'WOKN',
                'CAEL', 'LAKC', 'DALY', 'DLAI', 'LKEA', 'AHKL', 'LBAM', 'MAEL', 'LPAM', 'NALD', 'LEFA', 'ELKA', 'ANLE',
                'AELP', 'FETL', 'LIKC', 'EDLI', 'LEIS', 'FIEL', 'LTFI', 'LKIE', 'ADEM', 'DMAI', 'LIMA', 'AMIN', 'AEKM',
                'ELMA', 'ALML', 'MLEA', 'NMAE', 'TAME', 'EICM', 'LIDM', 'EILM', 'IMKL', 'MLIL', 'MNOO', 'OMEP', 'OMRE',
                'MTSO', 'NILA', 'MNAE', 'AYNV', 'ETAN', 'CKNE', 'ENED', 'EENM', 'EONN', 'TNES', 'WSEN', 'XTNE', 'NINE',
                'DNOE', 'NNEO', 'ONNO', 'NOPE', 'NMRO', 'SENO', 'YNOS', 'ONTE', 'NUON', 'ELOP', 'EPOK', 'EPTO', 'OPEM',
                'PKOC', 'LPSU', 'LYAP', 'NPLA', 'PIEP', 'INPK', 'ILPL', 'ELPI', 'CIPK', 'PTSE', 'ERPA', 'APKE', 'APHT',
                'STPA', 'ATPR', 'NATP', 'ARIP', 'INAP', 'PDAI', 'CKPA', 'VAOL', 'OCHU', 'EORS', 'LRAO', 'NPOE', 'VNEO',
                'NOTO', 'NYOL', 'ENOC', 'MOTI', 'MENO', 'YAOK', 'EVOR', 'EBYO', 'ASTO', 'HOTA', 'DAQU', 'UIQD', 'UIQT',
                'UQIZ', 'URTS', 'SRUH', 'URLE', 'UINR', 'DRUE', 'EOSR', 'ORPE', 'RTOO', 'ORMO', 'ORFO', 'LLRO', 'OLER',
                'RORA', 'OAMR', 'ADOR', 'TERI', 'IRKS', 'SIER', 'SAGE', 'DSAI', 'SAIL', 'AKSE', 'AESL', 'LSAE', 'SETA',
                'ESDE', 'ESKE', 'OHSE', 'SHOP', 'HTSO', 'WSHO', 'LTIS', 'OLPS', 'TLOS', 'PYTE', 'INTW', 'KUTS', 'NTUR',
                'UETN', 'KUCT', 'OTRI', 'RTMI', 'EYRT', 'TERK', 'WTON', 'URTO', 'STOS', 'ONRT', 'LOOT', 'ONTE', 'LTLO',
                'OWTS', 'OTDL', 'ITER', 'YTIN', 'ITME', 'EIRT', 'TEDI', 'AWRP', 'RNOW', 'ORWM', 'KRWO', 'WROE', 'RWDO',
                'WLIL', 'INDW', 'WNEI', 'WGNI', 'IEWP', 'EIWR', 'SIEW', 'ISWH', 'TIWH', 'EKOW', 'LOFW', 'OWOD', 'LWOO',
                'LELW', 'WNET', 'REEW', 'ARDY', 'YRNA', 'AEYH', 'ERAY', 'YOGA', 'UYRO', 'ZROE', 'CNZI', 'ZOEN', 'OOZM',
                'RCAE', ]

level_1_ANSWER = ['ACID', 'ACNE', 'APEX', 'AQUA', 'AREA', 'ARID', 'ARIL', 'ARMY', 'ARTS', 'ARYL', 'ASHY', 'ATOM',
                  'ATOP',
                  'AUNT', 'AURA', 'AUTO', 'AWAY', 'AXEL', 'AXIS', 'AXLE', 'AXON', 'BABY', 'BACK', 'BADE', 'BATH',
                  'BAIL',
                  'BAIT', 'BAKE', 'BALD', 'BALE', 'BALK', 'BALL', 'BALM', 'BAND', 'BANE', 'BANG', 'BANK', 'BARE',
                  'BARF',
                  'BARK', 'BANK', 'BARE', 'BLOW', 'BLUE', 'BLUR', 'BOAR', 'BOAT', 'BODY', 'BOGY', 'BOIL', 'BOLD',
                  'BOLL',
                  'BOLT', 'BOMB', 'BOND', 'BONE', 'BONG', 'BONK', 'BONY', 'BOOK', 'BOOM', 'CAGE', 'CAKE', 'CALF',
                  'CALL',
                  'CALM', 'CAME', 'CAMP', 'CAST', 'CAVE', 'CELL', 'CENT', 'CHAP', 'CHAR', 'CHAT', 'CHEF', 'CHEW',
                  'CHIN',
                  'CHIP', 'CHIT', 'CHOP', 'CHOW', 'CHUB', 'CITY', 'CLAD', 'CLAM', 'CLAN', 'DARK', 'DARN', 'DART',
                  'DASH',
                  'DATA', 'DATE', 'DAWN', 'DAZE', 'DEAD', 'DEAF', 'DEAL', 'DEAN', 'DEAR', 'DEBT', 'DECK', 'DOVE',
                  'DOWN',
                  'DOZE', 'DRAG', 'DRAW', 'DREW', 'DRIP', 'DROP', 'DRUG', 'DRUM', 'DUAL', 'DUCK', 'DUCT', 'DUEL',
                  'FEUD',
                  'FILE', 'FILL', 'FILM', 'FIND', 'FINE', 'FINK', 'FIRE', 'FIRM', 'FISH', 'FIST', 'FIVE', 'FIZZ',
                  'FLAG',
                  'FLAK', 'FLAP', 'FLAT', 'FLAW', 'FLEA', 'FLED', 'FLEE', 'FLEW', 'FLEX', 'FLIP', 'FLIT', 'FLOP',
                  'FLOW',
                  'GAIN', 'GAME', 'GANG', 'GOAL', 'GASP', 'GATE', 'GAVE', 'GAZE', 'GEAR', 'GEEK', 'GEES', 'GEMS',
                  'GENE',
                  'GERM', 'GIRD', 'GIST', 'GLAD', 'GLAM', 'GLOM', 'GLOW', 'GLUE', 'GOAT', 'GOES', 'GOLD', 'GOLF',
                  'GONE',
                  'GONG', 'GOOD', 'GOWN', 'HEAD', 'HEAL', 'HEAP', 'HEAR', 'HELD', 'HELL', 'HELP', 'HERB', 'HIDE',
                  'HIGH',
                  'HIKE', 'HILL', 'HIND', 'HOPE', 'HORN', 'HOST', 'HOUR', 'HOVE', 'HOWL', 'ICED', 'ICON', 'IDEA',
                  'IDLE',
                  'IDOL', 'INCH', 'INFO', 'INTO', 'IRIS', 'IRON', 'ITCH', 'ITEM', 'JAIL', 'JAZZ', 'JEAN', 'JEEP',
                  'JERK',
                  'JINX', 'JOBS', 'JOCK', 'JOIN', 'JOKE', 'JOLT', 'JUDO', 'JUMP', 'JUNK', 'JURY', 'JUST', 'KEEN',
                  'KEEP',
                  'KEPT', 'KETO', 'KICK', 'KIND', 'KING', 'KISS', 'KITE', 'KIWI', 'KNEE', 'KNEW', 'KNIT', 'KNOT',
                  'KNOW',
                  'LACE', 'LACK', 'LADY', 'LAID', 'LAKE', 'LAKH', 'LAMB', 'LAME', 'LAMP', 'LAND', 'LEAF', 'LEAK',
                  'LEAN',
                  'LEAP', 'LEFT', 'LICK', 'LIED', 'LIES', 'LIFE', 'LIFT', 'LIKE', 'MADE', 'MAID', 'MAIL', 'MAIN',
                  'MAKE',
                  'MALE', 'MALL', 'MEAL', 'MEAN', 'MEAT', 'MICE', 'MILD', 'MILE', 'MILK', 'MILL', 'MOON', 'MOPE',
                  'MORE',
                  'MOST', 'NAIL', 'NAME', 'NAVY', 'NEAT', 'NECK', 'NEED', 'NEEM', 'NEON', 'NEST', 'NEWS', 'NEXT',
                  'NINE',
                  'NODE', 'NONE', 'NOON', 'NOPE', 'NORM', 'NOSE', 'NOSY', 'NOTE', 'NOUN', 'POLE', 'POKE', 'POET',
                  'POEM',
                  'POCK', 'PLUS', 'PLAY', 'PLAN', 'PIPE', 'PINK', 'PILL', 'PILE', 'PICK', 'PEST', 'PEAR', 'PEAK',
                  'PATH',
                  'PAST', 'PART', 'PANT', 'PAIR', 'PAIN', 'PAID', 'PACK', 'OVAL', 'OUCH', 'ORES', 'ORAL', 'OPEN',
                  'OVEN',
                  'ONTO', 'ONLY', 'ONCE', 'OMIT', 'OMEN', 'OKAY', 'OVER', 'OBEY', 'OATS', 'OATH', 'QUAD', 'QUID',
                  'QUIT',
                  'QUIZ', 'RUST', 'RUSH', 'RULE', 'RUIN', 'RUDE', 'ROSE', 'ROPE', 'ROOT', 'ROOM', 'ROOF', 'ROLL',
                  'ROLE',
                  'ROAR', 'ROAM', 'ROAD', 'RITE', 'RISK', 'RISE', 'SAGE', 'SAID', 'SAIL', 'SAKE', 'SALE', 'SEAL',
                  'SEAT',
                  'SEED', 'SEEK', 'SHOE', 'SHOP', 'SHOT', 'SHOW', 'SLIT', 'SLOP', 'SLOT', 'TYPE', 'TWIN', 'TUSK',
                  'TURN',
                  'TUNE', 'TUCK', 'TRIO', 'TRIM', 'TREY', 'TREK', 'TOWN', 'TOUR', 'TOSS', 'TORN', 'TOOL', 'TONE',
                  'TOLL',
                  'TOWS', 'TOLD', 'TIRE', 'TINY', 'TIME', 'TIER', 'TIED', 'WRAP', 'WORN', 'WORM', 'WORK', 'WORE',
                  'WORD',
                  'WILL', 'WIND', 'WINE', 'WING', 'WIPE', 'WIRE', 'WISE', 'WISH', 'WITH', 'WOKE', 'WOLF', 'WOOD',
                  'WOOL',
                  'WELL', 'WENT', 'WERE', 'YARD', 'YARN', 'YEAH', 'YEAR', 'YOGA', 'YOUR', 'ZERO', 'ZINC', 'ZONE',
                  'ZOOM',
                  'RACE', ]

ran_num = randrange(0, (len(level_1_WORD)))
jumbled_rand_word = level_1_WORD[ran_num]

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
        ran_num = randrange(0, (len(level_1_WORD)))
        word.configure(text=level_1_WORD[ran_num])
        get_input.delete(0, END)
        ans.configure(text="Answer")

    def cheak():
        global points, ran_num
        user_word = get_input.get().upper()
        if user_word == level_1_ANSWER[ran_num]:
            points += 5
            score.configure(text="Score:- " + str(points))
            messagebox.showinfo('correct', "Correct Answer.. Keep it Up!")
            ran_num = randrange(0, (len(level_1_WORD)))
            word.configure(text=level_1_WORD[ran_num])
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
            ans.configure(text="Answer= " + level_1_ANSWER[ran_num])
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
        text=level_1_WORD[ran_num],
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

