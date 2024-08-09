import os
from tkinter import *
from random import *
from tkinter import messagebox
import time
from main import option
from english import elvl

level_2_WORD = ['OUATB', 'VOEBA', 'SAEUB', 'RACTO', 'CETUA', 'AITMD', 'APTOD', 'UDTLA', 'REATF', 'ANAIG', 'GENTA',
                'AEEGR', 'EAADH', 'MARAL', 'UMBAL', 'LARTE', 'IEALK', 'AVELI', 'OWLAL', 'ONAEL', 'NOLAG', 'AERTL',
                'AMNOG', 'RANGE', 'LGANE', 'ANYGR', 'APRTA', 'EPALP', 'YAPPL', 'AAREN', 'RAEUG', 'AISER', 'RARYA',
                'ISEAD', 'TEASS', 'UOAID', 'UTADI', 'IDAVO', 'DAAWR', 'ERAWA', 'YABLD', 'BERAK', 'EABSS', 'CISBA',
                'ISASB', 'ACBEH', 'NEGAB', 'ENIGB', 'NGUEB', 'IEGBN', 'BEWLO', 'ECBNH', 'YILLB', 'IHTRB', 'ALCBK',
                'ABELM', 'LIDNB', 'COLKB', 'DBLOO', 'ADROB', 'OTOBS', 'OBHTO', 'UOBND', 'BNIAR', 'RBDAN', 'RDAEB',
                'RBEKA', 'DERBE', 'REBFI', 'NIBGR', 'ORBAD', 'OBEKR', 'WOBNR', 'LIUDB', 'TIUBL', 'RUYBE', 'ALBCE',
                'LCIAF', 'AYRRC', 'HCACT', 'CSAUE', 'HNCAI', 'RAICH', 'RACTH', 'ACEHS', 'ECAHP', 'EKCHC', 'SETHC',
                'HIEFC', 'DICLH', 'NCHAI', 'COSHE', 'ICLIV', 'IMLAC', 'CLASS', 'ECLNA', 'RAECL', 'LICKC', 'LOKCC',
                'SOCLE', 'OACHC', 'CSTOA', 'CLDOU', 'NOTCU', 'RTCOU', 'RVEOC', 'CFART', 'HRACS', 'MCEAR', 'IRCME',
                'OSCSR', 'CWRDO', 'NRWOC', 'UCREV', 'YCCEL', 'ADIYL', 'ADCEN', 'TADDE', 'LEDAT', 'TAHDE', 'UETDB',
                'YDEAL', 'HETDP', 'IDOGN', 'OUTBD', 'NOZED', 'TRAFD', 'MDAAR', 'DRANW', 'DMEAR', 'DRSSE', 'LLDRI',
                'DKNIR', 'DIRVE', 'RDOVE', 'GIYND', 'IBUDA', 'AGERE', 'YALRE', 'RAHTE', 'TEHIG', 'ITLEE', 'PTMEY',
                'YNEEM', 'YNEJO', 'ERETN', 'YRNTE', 'AELQU', 'RRERO', 'TVNEE', 'EEVYR', 'ECTXA', 'EXTIS', 'TREXA',
                'AHFTI', 'AELSF', 'FLTAU', 'IFBRE', 'EFDIL', 'THIFF', 'YFITF', 'GITFH', 'IFLNA', 'IFTRS', 'FDXEI',
                'LFSHA', 'LTEEF', 'OROFL', 'FILDU', 'UFSCO', 'CFREO', 'THFOR', 'FYORT', 'ROFUM', 'OUFND', 'MRFAE',
                'AFKRN', 'UDRFA', 'ERHFS', 'RNTFO', 'UTIRF', 'YFLLU', 'UYNFN', 'TAGNI', 'GIEVN', 'SGLAS', 'GEOLB',
                'NIOGG', 'CRGEA', 'RDEAG', 'GNDRA', 'RATGN', 'GASSR', 'ATGER', 'NGREE', 'SOSRG', 'UPGOR', 'GOWRN',
                'AURGD', 'SSEUG', 'GETSU', 'DGIUE', 'PHYPA', 'ATERH', 'AYVHE', 'ENCHE', 'REHOS', 'HEOTL', 'HSEOU',
                'NUMHA', 'AIELD', 'EMAGI', 'EXIND', 'ERINN', 'PUITN', 'SSEUI', 'JNAAP', 'TIJNO', 'OJNSE', 'UEGJD',
                'NOWNK', 'BALLE', 'LAEGR', 'ESARL', 'AELTR', 'LUAGH', 'RELAY', 'RENLA', 'EEALS', 'ALEST', 'VLAEE',
                'LAEGL', 'LLEVE', 'IHLTG', 'LTIMI', 'INLSK', 'SVELI', 'OLALC', 'OLCGI', 'SOELO', 'OLEWR', 'CYLKU',
                'HNLUC', 'YNIGL', 'MCIAG', 'MAOJR', 'REKMA', 'RACHM', 'MHTCA', 'AEMBY', 'RYMOA', 'MNETA', 'MDEIA',
                'MALTE', 'HGITM', 'ORNIM', 'MNUSI', 'EIDXM', 'MLEDO', 'MENOY', 'NMHOT', 'MLROA', 'TOMRO', 'NUOTM',
                'OESUM', 'OHUTM', 'EIMOV', 'CIMUS', 'SEEND', 'ERENV', 'NYWLE', 'GNIHT', 'SIONE', 'HRTNO', 'NTEOD',
                'NLOEV', 'UERNS', 'OCRUC', 'ECAON', 'OFRFE', 'OENFT', 'DORRE', 'OHRTE', 'OUGTH', 'TNIPA', 'LENPA',
                'AERPP', 'PRTAY', 'CAEEP', 'EPETR', 'HAEPS', 'NEPOH', 'POHTO', 'CEPEI', 'TOIPL', 'PHTIC', 'ECALP',
                'LNPAI', 'PNLEA', 'LTNPA', 'ETPAL', 'PNOIT', 'PNDOU', 'OEPWR', 'ERPSS', 'CEPRI', 'IERDP', 'PREIM',
                'RTPI', 'PRORI', 'PERZI',  'ROFOP', 'RDUOP', 'EVPOR', 'ENQEU', 'UCQKI', 'ITUQE', 'IQTEU', 'IDARO',
                'RSAIE', 'ERAGN', 'IARPD', 'RITAO', 'HEACR', 'EARYD', 'FRERE', 'GRIHT', 'VRLAI', 'ERIRV', 'ORBIN',
                'RROEG', 'AMRNO', 'RGOHU', 'RDNUO', 'TUEOR', 'RYALO', 'ARLUR', 'SLACE', 'ENSCE', 'SOEPC', 'RCSEO',
                'NSEES', 'VSEER', 'NVSEE', 'AHLSL', 'SEHAP', 'RHESA', 'SPARH', 'HSTEE', 'ESFHL', 'LHESL', 'IFTHS',
                'SITRH', 'SCKOH', 'TOHOS', 'HSRTO', 'SOHNW', 'ITHSG', 'IECSN', 'THXIS', 'YXSIT', 'SDEZI', 'SLILK',
                'EESLP', 'DELIS', 'ALSLM', 'ASRMT', 'SELMI', 'MKEOS', 'OLSDI', 'SEVLO', 'ORRSY', 'UONDS', 'UHSTO',
                'PAECS', 'RPSEA', 'ESPKA', 'PSDEE', 'NEDSP', 'PETNS', 'PSTLI', 'KSOPE', 'OSRTP', 'FFSTA', 'GETSA',
                'SKTAE', 'TDNAS', 'TSRTA', 'STATE', 'METAS', 'LSEET', 'KISCT', 'STLIL', 'TKOCS', 'OESTN', 'SOOTD',
                'RTEOS', 'TMRSO', 'RYTOS', 'ITRPS', 'TSKCU', 'TYUSD', 'FUTSF', 'ESTYL', 'URGSA', 'ITSEU', 'PREUS',
                'SEETW', 'ETALB', 'NEAKT', 'TTESA', 'SATEX', 'HACET', 'HETTE', 'TAEXS', 'KTHNA', 'TTHEF', 'IHETR',
                'ETMHE', 'RHETE', 'EEHTS', 'HIKTC', 'GTNHI', 'TKHNI', 'ITDHR', 'SEOHT', 'RTEEH', 'EHTRW', 'RWOTH',
                'THIGT', 'EITSM', 'REDIT', 'LEITT', 'DTAOY', 'CITOP', 'TOLTA', 'CTOHU', 'UHOTG', 'OWETR', 'KARTC',
                'ADRTE', 'NRTAI', 'ETTRA', 'NRDTE', 'ITLAR', 'TRDIE', 'RISET', 'UCRTK', 'UYLRT', 'STRTU', 'HTRTU',
                'IWTEC', 'UNRED', 'UUEND', 'UINON', 'TNYIU', 'TIUNL', 'PRPEU', 'SUETP', 'UABNR', 'EUSGA', 'ULSAU',
                'DVLIA', 'EALUV', 'IEDVO', 'RUSIV', 'SIIVT', 'AILVT', 'IOVEC', 'ATESW', 'WHCAT', 'WAETR', 'ELEHW',
                'HREWE', 'CHIWH', 'LWHIE', 'TIHWE', 'EWLOH', 'SWHOE', 'AONWM', 'OEWMN', 'DLWOR', 'RYWOR', 'SEWOR',
                'TSWOR', 'WTROH', 'UDOLW', 'UDOWN', 'TREIW', 'RGWNO', 'ETWOR', 'DIELY', 'ONGYU', 'TOUHY', ]

level_2_ANSWER = ['ABOUT', 'ABOVE', 'ABUSE', 'ACTOR', 'ACUTE', 'ADMIT', 'ADOPT', 'ADULT', 'AFTER', 'AGAIN', 'AGENT',
                  'AGREE', 'AHEAD', 'ALARM', 'ALBUM', 'ALERT', 'ALIKE', 'ALIVE', 'ALLOW', 'ALONE', 'ALONG', 'ALTER',
                  'AMONG', 'ANGER', 'ANGLE', 'ANGRY', 'APART', 'APPLE', 'APPLY', 'ARENA', 'ARGUE', 'ARISE', 'ARRAY',
                  'ASIDE', 'ASSET', 'AUDIO', 'AUDIT', 'AVOID', 'AWARD', 'AWARE', 'BADLY', 'BAKER', 'BASES', 'BASIC',
                  'BASIS', 'BEACH', 'BEGAN', 'BEGIN', 'BEGUN', 'BEING', 'BELOW', 'BENCH', 'BILLY', 'BIRTH', 'BLACK',
                  'BLAME', 'BLIND', 'BLOCK', 'BLOOD', 'BOARD', 'BOOST', 'BOOTH', 'BOUND', 'BRAIN', 'BRAND', 'BREAD',
                  'BREAK', 'BREED', 'BRIEF', 'BRING', 'BROAD', 'BROKE', 'BROWN', 'BUILD', 'BUILT', 'BUYER', 'CABLE',
                  'CALIF', 'CARRY', 'CATCH', 'CAUSE', 'CHAIN', 'CHAIR', 'CHART', 'CHASE', 'CHEAP', 'CHECK', 'CHEST',
                  'CHIEF', 'CHILD', 'CHINA', 'CHOSE', 'CIVIL', 'CLAIM', 'CLASS', 'CLEAN', 'CLEAR', 'CLICK', 'CLOCK',
                  'CLOSE', 'COACH', 'COAST', 'COULD', 'COUNT', 'COURT', 'COVER', 'CRAFT', 'CRASH', 'CREAM', 'CRIME',
                  'CROSS', 'CROWD', 'CROWN', 'CURVE', 'CYCLE', 'DAILY', 'DANCE', 'DATED', 'DEALT', 'DEATH', 'DEBUT',
                  'DELAY', 'DEPTH', 'DOING', 'DOUBT', 'DOZEN', 'DRAFT', 'DRAMA', 'DRAWN', 'DREAM', 'DRESS', 'DRILL',
                  'DRINK', 'DRIVE', 'DROVE', 'DYING', 'DUBAI', 'EAGER', 'EARLY', 'EARTH', 'EIGHT', 'ELITE', 'EMPTY',
                  'ENEMY', 'ENJOY', 'ENTER', 'ENTRY', 'EQUAL', 'ERROR', 'EVENT', 'EVERY', 'EXACT', 'EXIST', 'EXTRA',
                  'FAITH', 'FALSE', 'FAULT', 'FIBER', 'FIELD', 'FIFTH', 'FIFTY', 'FIGHT', 'FINAL', 'FIRST', 'FIXED',
                  'FLASH', 'FLEET', 'FLOOR', 'FLUID', 'FOCUS', 'FORCE', 'FORTH', 'FORTY', 'FORUM', 'FOUND', 'FRAME',
                  'FRANK', 'FRAUD', 'FRESH', 'FRONT', 'FRUIT', 'FULLY', 'FUNNY', 'GIANT', 'GIVEN', 'GLASS', 'GLOBE',
                  'GOING', 'GRACE', 'GRADE', 'GRAND', 'GRANT', 'GRASS', 'GREAT', 'GREEN', 'GROSS', 'GROUP', 'GROWN',
                  'GUARD', 'GUESS', 'GUEST', 'GUIDE', 'HAPPY', 'HEART', 'HEAVY', 'HENCE', 'HORSE', 'HOTEL', 'HOUSE',
                  'HUMAN', 'IDEAL', 'IMAGE', 'INDEX', 'INNER', 'INPUT', 'ISSUE', 'JAPAN', 'JOINT', 'JONES', 'JUDGE',
                  'KNOWN', 'LABEL', 'LARGE', 'LASER', 'LATER', 'LAUGH', 'LAYER', 'LEARN', 'LEASE', 'LEAST', 'LEAVE',
                  'LEGAL', 'LEVEL', 'LIGHT', 'LIMIT', 'LINKS', 'LIVES', 'LOCAL', 'LOGIC', 'LOOSE', 'LOWER', 'LUCKY',
                  'LUNCH', 'LYING', 'MAGIC', 'MAJOR', 'MAKER', 'MARCH', 'MATCH', 'MAYBE', 'MAYOR', 'MEANT', 'MEDIA',
                  'METAL', 'MIGHT', 'MINOR', 'MINUS', 'MIXED', 'MODEL', 'MONEY', 'MONTH', 'MORAL', 'MOTOR', 'MOUNT',
                  'MOUSE', 'MOUTH', 'MOVIE', 'MUSIC', 'NEEDS', 'NEVER', 'NEWLY', 'NIGHT', 'NOISE', 'NORTH', 'NOTED',
                  'NOVEL', 'NURSE', 'OCCUR', 'OCEAN', 'OFFER', 'OFTEN', 'ORDER', 'OTHER', 'OUGHT', 'PAINT', 'PANEL',
                  'PAPER', 'PARTY', 'PEACE', 'PETER', 'PHASE', 'PHONE', 'PHOTO', 'PIECE', 'PILOT', 'PITCH', 'PLACE',
                  'PLAIN', 'PLANE', 'PLANT', 'PLATE', 'POINT', 'POUND', 'POWER', 'PRESS', 'PRICE', 'PRIDE', 'PRIME',
                  'PRINT', 'PRIOR', 'PRIZE', 'PROOF', 'PROUD', 'PROVE', 'QUEEN', 'QUICK', 'QUIET', 'QUITE', 'RADIO',
                  'RAISE', 'RANGE', 'RAPID', 'RATIO', 'REACH', 'READY', 'REFER', 'RIGHT', 'RIVAL', 'RIVER', 'ROBIN',
                  'ROGER', 'ROMAN', 'ROUGH', 'ROUND', 'ROUTE', 'ROYAL', 'RURAL', 'SCALE', 'SCENE', 'SCOPE', 'SCORE',
                  'SENSE', 'SERVE', 'SEVEN', 'SHALL', 'SHAPE', 'SHARE', 'SHARP', 'SHEET', 'SHELF', 'SHELL', 'SHIFT',
                  'SHIRT', 'SHOCK', 'SHOOT', 'SHORT', 'SHOWN', 'SIGHT', 'SINCE', 'SIXTH', 'SIXTY', 'SIZED', 'SKILL',
                  'SLEEP', 'SLIDE', 'SMALL', 'SMART', 'SMILE', 'SMOKE', 'SOLID', 'SOLVE', 'SORRY', 'SOUND', 'SOUTH',
                  'SPACE', 'SPARE', 'SPEAK', 'SPEED', 'SPEND', 'SPENT', 'SPLIT', 'SPOKE', 'SPORT', 'STAFF', 'STAGE',
                  'STAKE', 'STAND', 'START', 'STATE', 'STEAM', 'STEEL', 'STICK', 'STILL', 'STOCK', 'STONE', 'STOOD',
                  'STORE', 'STORM', 'STORY', 'STRIP', 'STUCK', 'STUDY', 'STUFF', 'STYLE', 'SUGAR', 'SUITE', 'SUPER',
                  'SWEET', 'TABLE', 'TAKEN', 'TASTE', 'TAXES', 'TEACH', 'TEETH', 'TEXAS', 'THANK', 'THEFT', 'THEIR',
                  'THEME', 'THERE', 'THESE', 'THICK', 'THING', 'THINK', 'THIRD', 'THOSE', 'THREE', 'THREW', 'THROW',
                  'TIGHT', 'TIMES', 'TIRED', 'TITLE', 'TODAY', 'TOPIC', 'TOTAL', 'TOUCH', 'TOUGH', 'TOWER', 'TRACK',
                  'TRADE', 'TRAIN', 'TREAT', 'TREND', 'TRIAL', 'TRIED', 'TRIES', 'TRUCK', 'TRULY', 'TRUST', 'TRUTH',
                  'TWICE', 'UNDER', 'UNDUE', 'UNION', 'UNITY', 'UNTIL', 'UPPER', 'UPSET', 'URBAN', 'USAGE', 'USUAL',
                  'VALID', 'VALUE', 'VIDEO', 'VIRUS', 'VISIT', 'VITAL', 'VOICE', 'WASTE', 'WATCH', 'WATER', 'WHEEL',
                  'WHERE', 'WHICH', 'WHILE', 'WHITE', 'WHOLE', 'WHOSE', 'WOMAN', 'WOMEN', 'WORLD', 'WORRY', 'WORSE',
                  'WORST', 'WORTH', 'WOULD', 'WOUND', 'WRITE', 'WRONG', 'WROTE', 'YIELD', 'YOUNG', 'YOUTH', ]

ran_num = randrange(0, (len(level_2_WORD)))
jumbled_rand_word = level_2_WORD[ran_num]

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
        ran_num = randrange(0, (len(level_2_WORD)))
        word.configure(text=level_2_WORD[ran_num])
        get_input.delete(0, END)
        ans.configure(text="Answer")

    def cheak():
        global points, ran_num
        user_word = get_input.get().upper()
        if user_word == level_2_ANSWER[ran_num]:
            points += 5
            score.configure(text="Score:- " + str(points))
            messagebox.showinfo('correct', "Correct Answer.. Keep it Up!")
            ran_num = randrange(0, (len(level_2_WORD)))
            word.configure(text=level_2_WORD[ran_num])
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
            ans.configure(text="Answer= " + level_2_ANSWER[ran_num])

        else:
            messagebox.showerror("Error", 'Not enough points')

    my_window = Tk()
    my_window.geometry("620x650+500+30")
    my_window.resizable(False, False)
    my_window.title("Guess It Out-teaching learning aid ")
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
        text=level_2_WORD[ran_num],
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
