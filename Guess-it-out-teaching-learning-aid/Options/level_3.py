import os
from tkinter import *
from random import *
from tkinter import messagebox
import time
from main import option
from english import hlvl

level_3_WORD = ['ADOBRA', 'EATCCP', 'SSCACE', 'OACRSS', 'NGTCAI', 'TNAOCI', 'ETACIV', 'ACAULT', 'IECDAV', 'DEIVSA',
                'FCETFA', 'AORFDF', 'IRAFAD', 'YCAGNE', 'GENADA', 'AOTSML', 'AWLYAS', 'UONTAM', 'MIAANL', 'NNAULA',
                'NESRWA', 'AEYNON', 'ANYYWA', 'PAALPE', 'PEAAPR', 'AORNDU', 'REVIAR', 'TRITSA', 'STEPAC', 'EASSSS',
                'AITSSS', 'MUSESA', 'CAAKTT', 'NTDETA', 'ATUSGU', 'HUOART', 'ENVAUE', 'KCAEDB', 'EALYRB', 'ALBETT',
                'TAYUEB', 'EAMCBE', 'CMBEEO', 'FBOEER', 'HBLAEF', 'IBDNHE', 'LEBFIE', 'ENLGOB', 'LIBERN', 'TBETRE',
                'EBDNYO', 'IHPOSB', 'REROBD', 'LETTBO', 'BTTOOM', 'BUOGTH', 'NHCARB', 'HABTRE', 'EDGIBR', 'RTBGHI',
                'KRONBE', 'GEDTUB', 'NEBURD', 'RBUAEU', 'TONTBU', 'CAAMRE', 'ACNCER', 'OANNCT', 'OBARCN', 'EARCRE',
                'CSELAT', 'ASALCU', 'CHATUG', 'EENCRT', 'ECTREN', 'ENCAHC', 'CAGHEN', 'HCREAG', 'ECIHCO', 'SHEOOC',
                'ECHNSO', 'CHHRUC', 'ECLICR', 'CLTINE', 'ECSDLO', 'SOCREL', 'ECFEOF', 'LNMCUO', 'TOMABC', 'NGMCOI',
                'MNMOOC', 'PLOYCM', 'OECPPR', 'COENRR', 'CLTYOS', 'UCOTNY', 'ULCEPO', 'SEORCU', 'ERSOCV', 'ARTCEE',
                'DCTREI', 'SICISR', 'MTUCOS', 'ADAGEM', 'REDAGN', 'EADLRE', 'EEDBTA', 'ADDECE', 'ECDEDI', 'DATEFE',
                'EDEDFN', 'IDFNEE', 'GEREED', 'MNDAED', 'ENEDPD', 'PTUYED', 'RTDSEE', 'SDNEGI', 'DRSIEE', 'DAILTE',
                'EETTCD', 'CEVDEI', 'DFIFER', 'NIERND', 'RECDIT', 'RCODOT', 'ODLARL', 'OAIMDN', 'DOEBLU', 'RVENID',
                'IEVDRR', 'URNGID', 'ELAYIS', 'INTAGE', 'ERDIOT', 'TECEFF', 'OFFRTE', 'HGHETI', 'HETIER', 'VNELEE',
                'REMGEE', 'RIEMPE', 'YLMEPO', 'BEENLA', 'NNDGIE', 'EYNGRE', 'GENGEA', 'IENENG', 'HGOEUN', 'RSENEU',
                'ETNEIR', 'ITYNTE', 'ITEUQY', 'EAPSCE', 'TATESE', 'NECHTI', 'ECXEDE', 'TCXPEE', 'SCEXES', 'AXNPDE',
                'PEXTEC', 'ERTXPE', 'ROXTEP', 'EXDNTE', 'TENXTE', 'ACFRBI', 'AFNICG', 'RTFOCA', 'AIDLEF', 'YLRIAF',
                'ELLFAN', 'IYLMFA', 'MASOFU', 'HFEATR', 'OFLEWL', 'LFAMEE', 'GIURFE', 'GFINIL', 'NREIGF', 'FSINHI',
                'ILCFSA', 'HILGTF', 'IGYNLF', 'FLLWOO', 'RFOECD', 'ROTFSE', 'REOGFT', 'RMFALO', 'MOFART', 'MFORER',
                'OTERFS', 'OGUTFH', 'HOFUTR', 'NEFRHC', 'FENIDR', 'TFRUUE', 'DREGNA', 'GTREAH', 'RNEGDE', 'GNAMER',
                'LOBGLA', 'EGLOND', 'GOUNRD', 'WORTGH', 'GTULYI', 'NHAEDD', 'AEHLDN', 'PHNAPE', 'YRADHL', 'EDEADH',
                'HTALHE', 'HGEIHT', 'ENHDID', 'ROHELD', 'SOETNH', 'ITMPAC', 'MPRITO', 'EIMCNO', 'NEIDDE', 'YUINRJ',
                'ISEDNI', 'ENTIND', 'NEITTN', 'ENITSV', 'SANDLI', 'ILFSTE', 'SJYREE', 'JPEHSO', 'JNORIU', 'DLIEKL',
                'ABORUL', 'LEATST', 'ERATTL', 'CAULHN', 'YEAWLR', 'AEDERL', 'EGAULE', 'LAEVSE', 'AELCYG', 'LEGTNH',
                'NSSEOL', 'ELETTR', 'IGTSHL', 'KLEYIL', 'DKEINL', 'DLQIUI', 'LESNIT', 'LLEITT', 'IVLGNI', 'NLSGOI',
                'NUETCL', 'YLXRUU', 'IMNLYA', 'INAGMK', 'MANGAE', 'NARMEN', 'UAANLM', 'GAINRM', 'NRMIEA', 'EARMDK',
                'AEKMRT', 'ATMINR', 'AMTERS', 'TAMTER', 'MAREUT', 'IMMEUD', 'EBEMMR', 'MMROYE', 'ANMLET', 'MEERYL',
                'REMRGE', 'TOHEDM', 'DELIDM', 'ILRMEL', 'NINIMG', 'UNMEIT', 'IRMRRO', 'MELBIO', 'EORMDN', 'OETMDS',
                'OLEDMU', 'NMTEOM', 'TMOSYL', 'ROMTHE', 'NIOOTM', 'NIVOGM', 'RDMREU', 'USMEMU', 'LTUAMU', 'SLEFYM',
                'AOWNRR', 'OINATN', 'ETVANI', 'NATURE', 'BYEANR', 'ARELYN', 'GHITNS', 'ONODYB', 'MLNROA', 'NICTEO',
                'NINTOO', 'ERNUBM', 'EBOJCT', 'TBAOIN', 'FOFCIE', 'OFESTF', 'ONENIL', 'OOPNIT', 'GREONA', 'GORNII',
                'TTPUUO', 'OXRDFO', 'EPAKCD', 'APECAL', 'EPRNTA', 'LARPYT', 'ENTPTA', 'OEPPLE', 'ERDOPI', 'PTERIM',
                'PONERS', 'ARPSHE', 'IEPKDC', 'TNLPEA', 'LPYREA', 'LEAPES', 'TPYNLE', 'TCEPKO', 'CIELPO', 'YIPCOL',
                'REFEPR', 'PTTYER', 'PINCRE', 'SPONIR', 'OITPRF', 'PRREOP', 'ONVPRE', 'LBICPU', 'PUSEUR', 'SARDIE',
                'DMOARN', 'LRREYA', 'THRREA', 'GINRAT', 'RADERE', 'ERALLY', 'ORSEAN', 'LLACER', 'CTRENE', 'CERDOR',
                'EDCREU', 'FEMORR', 'GERADR', 'MRIEGE', 'IEORGN', 'ETLRAE', 'EIFRLE', 'RENAMI', 'MRTEOE', 'MERVOE',
                'IRRPEA', 'TEAEPR', 'RPAYLE', 'ORTPER', 'SRUECE', 'ROERTS', 'STLEUR', 'TIRLAE', 'TANEIR', 'NEURRT',
                'EVAERL', 'RVEWEI', 'RWADRE', 'RNIDGI', 'IRINGS', 'SOURBT', 'IRNLUG', 'ATYEFS', 'YASLAR', 'PMAESL',
                'SIVAGN', 'SGNIYA', 'EMCHES', 'HOCLOS', 'ERNSCE', 'AECHRS', 'OESNSA', 'ECSOND', 'CSEETR', 'RSTOEC',
                'CREUES', 'EIGNSE', 'ESCLTE', 'SRELLE', 'IOSREN', 'EISESR', 'VRSEER', 'ETESTL', 'EVSREE', 'HUSODL',
                'GISNLA', 'DENIGS', 'SITLEN', 'RLEIVS', 'EMPLIS', 'MYIPSL', 'LGIESN', 'STRESI', 'GHISTL', 'OOHTMS',
                'ILCOSA', 'LOSEYL', 'SOHGUT', 'EUSROC', 'VETSIO', 'SCHPEE', 'IPISRT', 'EKOPNS', 'RPSDEA', 'IPGNSR',
                'AERUSQ', 'BTELAS', 'USTSTA', 'DESYTA', 'NETSOL', 'INTSRA', 'MEASTR', 'SETRTE', 'TSSRES', 'TSIRTC',
                'ETRKSI', 'STNGIR', 'ONRSTG', 'TRSUCK', 'ISDOUT', 'TBSMUI', 'DDSNUE', 'ESFRUF', 'EMRMSU', 'SMITMU',
                'PSLUYP', 'UERLSY', 'RYVEUS', 'TWCSIH', 'LSMBYO', 'SMETSY', 'INKAGT', 'ELATTN', 'RTEAGT', 'AHTUTG',
                'ENNTTA', 'NETRDE', 'ETNISN', 'TAHNSK', 'TOYEHR', 'TTHRIY', 'OHGUHT', 'RATEHT', 'HORWNT', 'KITCTE',
                'IMELYT', 'GIINTM', 'ETUSIS', 'RTOAWD', 'RTAVEL', 'YETRTA', 'GRYTIN', 'ELEVTW', 'NTWTYE', 'EBNLAU',
                'UUIENQ', 'EDNIUT', 'SUNLES', 'UKENIL', 'TEAUPD', 'EFULUS', 'ALYEVL', 'DVIAER', 'NVREDO', 'SRVSEU',
                'TIICVM', 'NISIOV', 'VUASLI', 'EOUMLV', 'EWRKLA', 'TWHAEL', 'LYWEEK', 'HGWTIE', 'LWOYHL', 'IWDWNO',
                'IRWNNE', 'EWRNIT', 'INWHTI', 'RWONDE', 'RKOWRE', 'GWHRIT', 'IRTREW', 'LOLWEY', ]

level_3_ANSWER = ['ABROAD', 'ACCEPT', 'ACCESS', 'ACROSS', 'ACTING', 'ACTION', 'ACTIVE', 'ACTUAL', 'ADVICE', 'ADVISE',
                  'AFFECT', 'AFFORD', 'AFRAID', 'AGENCY', 'AGENDA', 'ALMOST', 'ALWAYS', 'AMOUNT', 'ANIMAL', 'ANNUAL',
                  'ANSWER', 'ANYONE', 'ANYWAY', 'APPEAL', 'APPEAR', 'AROUND', 'ARRIVE', 'ARTIST', 'ASPECT', 'ASSESS',
                  'ASSIST', 'ASSUME', 'ATTACK', 'ATTEND', 'AUGUST', 'AUTHOR', 'AVENUE', 'BACKED', 'BARELY', 'BATTLE',
                  'BEAUTY', 'BECAME', 'BECOME', 'BEFORE', 'BEHALF', 'BEHIND', 'BELIEF', 'BELONG', 'BERLIN', 'BETTER',
                  'BEYOND', 'BISHOP', 'BORDER', 'BOTTLE', 'BOTTOM', 'BOUGHT', 'BRANCH', 'BREATH', 'BRIDGE', 'BRIGHT',
                  'BROKEN', 'BUDGET', 'BURDEN', 'BUREAU', 'BUTTON', 'CAMERA', 'CANCER', 'CANNOT', 'CARBON', 'CAREER',
                  'CASTLE', 'CASUAL', 'CAUGHT', 'CENTER', 'CENTRE', 'CHANCE', 'CHANGE', 'CHARGE', 'CHOICE', 'CHOOSE',
                  'CHOSEN', 'CHURCH', 'CIRCLE', 'CLIENT', 'CLOSED', 'CLOSER', 'COFFEE', 'COLUMN', 'COMBAT', 'COMING',
                  'COMMON', 'COMPLY', 'COPPER', 'CORNER', 'COSTLY', 'COUNTY', 'COUPLE', 'COURSE', 'COVERS', 'CREATE',
                  'CREDIT', 'CRISIS', 'CUSTOM', 'DAMAGE', 'DANGER', 'DEALER', 'DEBATE', 'DECADE', 'DECIDE', 'DEFEAT',
                  'DEFEND', 'DEFINE', 'DEGREE', 'DEMAND', 'DEPEND', 'DEPUTY', 'DESERT', 'DESIGN', 'DESIRE', 'DETAIL',
                  'DETECT', 'DEVICE', 'DIFFER', 'DINNER', 'DIRECT', 'DOCTOR', 'DOLLAR', 'DOMAIN', 'DOUBLE', 'DRIVEN',
                  'DRIVER', 'DURING', 'EASILY', 'EATING', 'EDITOR', 'EFFECT', 'EFFORT', 'EIGHTH', 'EITHER', 'ELEVEN',
                  'EMERGE', 'EMPIRE', 'EMPLOY', 'ENABLE', 'ENDING', 'ENERGY', 'ENGAGE', 'ENGINE', 'ENOUGH', 'ENSURE',
                  'ENTIRE', 'ENTITY', 'EQUITY', 'ESCAPE', 'ESTATE', 'ETHNIC', 'EXCEED', 'EXCEPT', 'EXCESS', 'EXPAND',
                  'EXPECT', 'EXPERT', 'EXPORT', 'EXTEND', 'EXTENT', 'FABRIC', 'FACING', 'FACTOR', 'FAILED', 'FAIRLY',
                  'FALLEN', 'FAMILY', 'FAMOUS', 'FATHER', 'FELLOW', 'FEMALE', 'FIGURE', 'FILING', 'FINGER', 'FINISH',
                  'FISCAL', 'FLIGHT', 'FLYING', 'FOLLOW', 'FORCED', 'FOREST', 'FORGET', 'FORMAL', 'FORMAT', 'FORMER',
                  'FOSTER', 'FOUGHT', 'FOURTH', 'FRENCH', 'FRIEND', 'FUTURE', 'GARDEN', 'GATHER', 'GENDER', 'GERMAN',
                  'GLOBAL', 'GOLDEN', 'GROUND', 'GROWTH', 'GUILTY', 'HANDED', 'HANDLE', 'HAPPEN', 'HARDLY', 'HEADED',
                  'HEALTH', 'HEIGHT', 'HIDDEN', 'HOLDER', 'HONEST', 'IMPACT', 'IMPORT', 'INCOME', 'INDEED', 'INJURY',
                  'INSIDE', 'INTEND', 'INTENT', 'INVEST', 'ISLAND', 'ITSELF', 'JERSEY', 'JOSEPH', 'JUNIOR', 'KILLED',
                  'LABOUR', 'LATEST', 'LATTER', 'LAUNCH', 'LAWYER', 'LEADER', 'LEAGUE', 'LEAVES', 'LEGACY', 'LENGTH',
                  'LESSON', 'LETTER', 'LIGHTS', 'LIKELY', 'LINKED', 'LIQUID', 'LISTEN', 'LITTLE', 'LIVING', 'LOSING',
                  'LUCENT', 'LUXURY', 'MAINLY', 'MAKING', 'MANAGE', 'MANNER', 'MANUAL', 'MARGIN', 'MARINE', 'MARKED',
                  'MARKET', 'MARTIN', 'MASTER', 'MATTER', 'MATURE', 'MEDIUM', 'MEMBER', 'MEMORY', 'MENTAL', 'MERELY',
                  'MERGER', 'METHOD', 'MIDDLE', 'MILLER', 'MINING', 'MINUTE', 'MIRROR', 'MOBILE', 'MODERN', 'MODEST',
                  'MODULE', 'MOMENT', 'MOSTLY', 'MOTHER', 'MOTION', 'MOVING', 'MURDER', 'MUSEUM', 'MUTUAL', 'MYSELF',
                  'NARROW', 'NATION', 'NATIVE', 'NATURE', 'NEARBY', 'NEARLY', 'NIGHTS', 'NOBODY', 'NORMAL', 'NOTICE',
                  'NOTION', 'NUMBER', 'OBJECT', 'OBTAIN', 'OFFICE', 'OFFSET', 'ONLINE', 'OPTION', 'ORANGE', 'ORIGIN',
                  'OUTPUT', 'OXFORD', 'PACKED', 'PALACE', 'PARENT', 'PARTLY', 'PATENT', 'PEOPLE', 'PERIOD', 'PERMIT',
                  'PERSON', 'PHRASE', 'PICKED', 'PLANET', 'PLAYER', 'PLEASE', 'PLENTY', 'POCKET', 'POLICE', 'POLICY',
                  'PREFER', 'PRETTY', 'PRINCE', 'PRISON', 'PROFIT', 'PROPER', 'PROVEN', 'PUBLIC', 'PURSUE', 'RAISED',
                  'RANDOM', 'RARELY', 'RATHER', 'RATING', 'READER', 'REALLY', 'REASON', 'RECALL', 'RECENT', 'RECORD',
                  'REDUCE', 'REFORM', 'REGARD', 'REGIME', 'REGION', 'RELATE', 'RELIEF', 'REMAIN', 'REMOTE', 'REMOVE',
                  'REPAIR', 'REPEAT', 'REPLAY', 'REPORT', 'RESCUE', 'RESORT', 'RESULT', 'RETAIL', 'RETAIN', 'RETURN',
                  'REVEAL', 'REVIEW', 'REWARD', 'RIDING', 'RISING', 'ROBUST', 'RULING', 'SAFETY', 'SALARY', 'SAMPLE',
                  'SAVING', 'SAYING', 'SCHEME', 'SCHOOL', 'SCREEN', 'SEARCH', 'SEASON', 'SECOND', 'SECRET', 'SECTOR',
                  'SECURE', 'SEEING', 'SELECT', 'SELLER', 'SENIOR', 'SERIES', 'SERVER', 'SETTLE', 'SEVERE', 'SHOULD',
                  'SIGNAL', 'SIGNED', 'SILENT', 'SILVER', 'SIMPLE', 'SIMPLY', 'SINGLE', 'SISTER', 'SLIGHT', 'SMOOTH',
                  'SOCIAL', 'SOLELY', 'SOUGHT', 'SOURCE', 'SOVIET', 'SPEECH', 'SPIRIT', 'SPOKEN', 'SPREAD', 'SPRING',
                  'SQUARE', 'STABLE', 'STATUS', 'STEADY', 'STOLEN', 'STRAIN', 'STREAM', 'STREET', 'STRESS', 'STRICT',
                  'STRIKE', 'STRING', 'STRONG', 'STRUCK', 'STUDIO', 'SUBMIT', 'SUDDEN', 'SUFFER', 'SUMMER', 'SUMMIT',
                  'SUPPLY', 'SURELY', 'SURVEY', 'SWITCH', 'SYMBOL', 'SYSTEM', 'TAKING', 'TALENT', 'TARGET', 'TAUGHT',
                  'TENANT', 'TENDER', 'TENNIS', 'THANKS', 'THEORY', 'THIRTY', 'THOUGH', 'THREAT', 'THROWN', 'TICKET',
                  'TIMELY', 'TIMING', 'TISSUE', 'TOWARD', 'TRAVEL', 'TREATY', 'TRYING', 'TWELVE', 'TWENTY', 'UNABLE',
                  'UNIQUE', 'UNITED', 'UNLESS', 'UNLIKE', 'UPDATE', 'USEFUL', 'VALLEY', 'VARIED', 'VENDOR', 'VERSUS',
                  'VICTIM', 'VISION', 'VISUAL', 'VOLUME', 'WALKER', 'WEALTH', 'WEEKLY', 'WEIGHT', 'WHOLLY', 'WINDOW',
                  'WINNER', 'WINTER', 'WITHIN', 'WONDER', 'WORKER', 'WRIGHT', 'WRITER', 'YELLOW', ]

ran_num = randrange(0, (len(level_3_WORD)))
jumbled_rand_word = level_3_WORD[ran_num]

points = 0


def main():
    def back():
        my_window.destroy()
        hlvl()

    def home():
        my_window.destroy()
        option()

    def change():
        global ran_num
        ran_num = randrange(0, (len(level_3_WORD)))
        word.configure(text=level_3_WORD[ran_num])
        get_input.delete(0, END)
        ans.configure(text="Answer")

    def cheak():
        global points, ran_num
        user_word = get_input.get().upper()
        if user_word == level_3_ANSWER[ran_num]:
            points += 5
            score.configure(text="Score:- " + str(points))
            messagebox.showinfo('correct', "Correct Answer.. Keep it Up!")
            ran_num = randrange(0, (len(level_3_WORD)))
            word.configure(text=level_3_WORD[ran_num])
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
            ans.configure(text="Answer= " + level_3_ANSWER[ran_num])

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
        text=level_3_WORD[ran_num],
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
