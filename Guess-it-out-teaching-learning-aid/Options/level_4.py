import os
from tkinter import *
from random import *
from tkinter import messagebox
import time
from main import option
from english import hlvl

level_4_WORD = ['BIATYLI', 'NBSECAE', 'DMCAEAY', 'CNATUCO', 'EDCAUSC', 'CAVHEEI', 'AURQICE', 'SADDRES', 'NADCVEA',
                'EAESVDR', 'DAISEVD', 'SDEARIV', 'AATGSIN', 'IAINELR', 'OPITRAR', 'OLCLOHA', 'EELLDAG', 'AYREDAL',
                'AANTSLY', 'NNTEACI', 'OAHETRN', 'XIYNATE', 'IUXOSNA', 'OADBNYY', 'APIPDEL', 'NAGRERA', 'ILAARRV',
                'ELICATR', 'AUALSTS', 'EMUSSAD', 'SSREAUD', 'TEPTATM', 'RAATTCT', 'ATNOCIU', 'AVAERGE', 'ABGKCIN',
                'ENLABAC', 'BIKNGNA', 'RIBARER', 'BATYTRE', 'RAGIBNE', 'ETANIBG', 'CEAUSBE', 'RBMDOEO', 'IVEBELE',
                'HBAETEN', 'FNIEBTE', 'EDBSIES', 'EWBTENE', 'IBILNLO', 'IDNGBNI', 'ROTHREB', 'GOHRTBU', 'IBGUNRN',
                'CABITEN', 'RCIBALE', 'LCIALNG', 'PCAELAB', 'IPALCTA', 'NPAITCA', 'TPNACOI', 'TCUAEPR', 'UCFEALR',
                'RCREIAR', 'CNATOUI', 'NLEIGCI', 'LTRNAEC', 'RCCNTEI', 'UYCERTN', 'NTACREI', 'EMABHCR', 'HNLNACE',
                'CATHREP', 'THCIRAY', 'CIARLHE', 'TARCHRE', 'EEKCDHC', 'CKECNHI', 'RHNCCOI', 'IUCTRIC', 'SSCSLEA',
                'ACSICSL', 'CLTMAEI', 'SLGINOC', 'UCESOLR', 'ELSHCOT', 'LTOECCL', 'LGLECOE', 'IMECOBN', 'MCOFTRO',
                'NOACDMM', 'CTMOEMN', 'OATPCMC', 'NOYMCAP', 'ORAECPM', 'MEPTECO', 'CXMEOLP', 'ETONPCC', 'NCNECOR',
                'ETRCNCO', 'CTNCODU', 'RMOCNFI', 'TCECNNO', 'TCNONSE', 'NOSSITC', 'TONCCTA', 'NOTINCA', 'OTCTNNE',
                'SOTCENT', 'ETOTCNX', 'NOCRTOL', 'ENTOVRC', 'RERCCOT', 'UNLOCIC', 'LESONUC', 'ONCETRU', 'UCNOTRY',
                'CRLIUCA', 'TRLSACY', 'UELCURT', 'ETNRURC', 'NGIUTTC', 'LNIGAED', 'DDEEDIC', 'NEIDLCE', 'EDFATLU',
                'ECNFEDE', 'IIFDTEC', 'VDILERE', 'NEYDITS', 'STEIOPD', 'DPSTOKE', 'DSPIEET', 'YTEDROS', 'PVEDELO',
                'ODDEETV', 'DNDAMOI', 'GALIDTI', 'UICSSDS', 'EAEISDS', 'DLIAPSY', 'SPDEUIT', 'NTTADIS', 'DEESRVI',
                'DVEIDDI', 'NGIRWAD', 'DVRNIIG', 'CDYMNAI', 'TERENSA', 'NECOYMO', 'OTDEIIN', 'LRLDEYE', 'ETELMEN',
                'ADGGNEE', 'NCANEEH', 'ESESCEN', 'EEVNNIG', 'IVNETDE', 'EXYATLC', 'MEAXNIE', 'EEMPLAX', 'TIDEEXC',
                'CELUEDX', 'HXEIIBT', 'ESXNEEP', 'LEPXINA', 'OLXEREP', 'ESPXSER', 'EXRMEET', 'OTFRCAY', 'CTLAYUF',
                'FIIGALN', 'FEARLUI', 'FHNIAOS', 'TUEEFAR', 'FERELDA', 'IFNELGE', 'CTIOINF', 'NIEEFFT', 'IIFLGNL',
                'ANINEFC', 'INDFING', 'INSHFIG', 'STISFEN', 'IEFGRNO', 'EREOVFR', 'OFMLRUA', 'FEROTUN', 'AOWFDRR',
                'NREOUDF', 'ROEFDEM', 'HFUTERR', 'EGYALLR', 'WYTAAEG', 'ANREGEL', 'NTGECEI', 'UINGENE', 'GBITGAI',
                'GTRAERE', 'NIHGAGN', 'EHGNIDA', 'HTLAYHE', 'GNARHEI', 'LVIAYHE', 'PHFLUEL', 'LHGEPIN', 'LSHRFEE',
                'HAGYIHW', 'SLEHFIM', 'SOHYRIT', 'GDOHLIN', 'ADYIOLH', 'USOHIGN', 'RWHEEVO', 'DEHRNUD', 'NUASHBD',
                'GLEIALL', 'ELNSLSI', 'EMGIIAN', 'IGMINAG', 'MPEVRIO', 'EUNLCID', 'LITNIIA', 'YRIIQNU', 'SHNTGII',
                'ISATLLN', 'TATISNN', 'ETIDANS', 'SEENITN', 'MTREIIN', 'VNVLIEO', 'NLJITYO', 'RONJALU', 'EUYNORJ',
                'JCIUTES', 'UIFJTSY', 'EIGPNKE', 'LIILKNG', 'NIGDKOM', 'HKETICN', 'NOGNWKI', 'NNLIGAD', 'GLRELAY',
                'ASLTIGN', 'GLDNAIE', 'ELANEDR', 'ELISERU', 'LRLEAIB', 'RYTLIBE', 'ALYBRIR', 'ENISCLE', 'IMETILD',
                'SGINITL', 'LAGLICO', 'YLOLTYA', 'CEAHIMN', 'AEAGMRN', 'AMRIERD', 'SISAVEM', 'MUIXMAM', 'GEMAINN',
                'AMRUESE', 'MCADLIE', 'NTIMEEG', 'EOMNTIN', 'SEMEAGS', 'MIOILNL', 'AEMLINR', 'MLMNAII', 'MNMIIUM',
                'SMINSIG', 'NISSOMI', 'AKMEIST', 'XTUEMIR', 'NROTMOI', 'HNTYLOM', 'NORMNIG', 'CULAMIS', 'RSEYMTY',
                'AALTRUN', 'THEINER', 'NEURVSO', 'NRKETWO', 'LTURNAE', 'NTELBOA', 'HNOIGTN', 'WNOHERE', 'CELRUAN',
                'NRSNGUI', 'BIOOSVU', 'FNEESFO', 'OFCEFIR', 'INGGONO', 'GEPINNO', 'AEEPTOR', 'ONIONPI', 'PLAOTCI',
                'GNORICA', 'MOEUCOT', 'RTOOOUD', 'OTUKLOO', 'EDUITOS', 'LAVOLER', 'PICIACF', 'AKACGEP', 'NTAEIPD',
                'RKGNPAI', 'TLRAIPA', 'RATRNPE', 'AGSEASP', 'IAPSGNS', 'SOSINAP', 'VSIAEPS', 'AENITTP', 'APNTTRE',
                'APBALYE', 'YNAPEMT', 'PLYNATE', 'NNIPDEG', 'INOPNSE', 'PERNCET', 'CFRTEEP', 'EMFRORP', 'SREPPAH',
                'XNIOHEP', 'PKICNIG', 'PCIURTE', 'ORNEPIE', 'TCLIPAS', 'ENOPDIT', 'RPPALUO', 'RINOOPT', 'ERPYTOV',
                'PEESRIC', 'REPCIDT', 'REIMPER', 'RPMMIUE', 'REPRAEP', 'RNEPSTE', 'NVETREP', 'YRAMIPR', 'NPETRRI',
                'PRIYCAV', 'TVEAPIR', 'ROELMBP', 'COPRDEE', 'CROPSSE', 'RCOUPDE', 'DRCUOTP', 'LPREIOF', 'RMAOPRG',
                'OJCPERT', 'RPMOIES', 'OMTOREP', 'ETCPTOR', 'TPINROE', 'TTOSPER', 'VDERPIO', 'HSPLBIU', 'URPOPSE',
                'PNUISGH', 'IULAFQY', 'YTIQUAL', 'ARTUQER', 'CDALRIA', 'WIAAYRL', 'YDAELRI', 'NAIEDGR', 'ERYATIL',
                'EIAEZLR', 'TEIPCRE', 'EEIRECV', 'EORERCV', 'LTEFERC', 'ARREGUL', 'ERLADET', 'EAELRSE', 'EAMSIRN',
                'LAEMOVR', 'DRMEOEV', 'PEARCEL', 'RSQETUE', 'REUQIER', 'ERVESRE', 'OLSVERE', 'SECRPET', 'DSPOREN',
                'TREEORS', 'ITEDRRE', 'EUVEENR', 'ERERVES', 'ORLUTLO', 'OETINUR', 'UINNRNG', 'AYISTSF', 'NECCSIE',
                'OENSITC', 'TSGMENE', 'UOSRESI', 'CSEIRVE', 'NGERIVS', 'SINESOS', 'ENGTTIS', 'VEHTNSE', 'LVERAES',
                'YOTLHSR', 'NOWGSIH', 'EEINSCL', 'IOINCSL', 'ILRAMSI', 'ITSTGNI', 'NSXIEET', 'LDSEKLI', 'IOSGMKN',
                'CETOYIS', 'ESMWHOO', 'OMSEEON', 'EEPSAKR', 'LACIPSE', 'EPSICSE', 'NOSPRSO', 'TNAOTSI', 'GARTESO',
                'NGSTAER', 'SCRTTEH', 'STNUDET', 'TSEDIDU', 'TBUCSEJ', 'CCEDESU', 'ECSSUSC', 'TGUESSG', 'MAURYSM',
                'TOUPSRP', 'SEUPSOP', 'REMPUSE', 'CUARSEF', 'GSRUERY', 'USPSLRU', 'UVSEIVR', 'TCSPUES', 'NAUSTSI',
                'ERCTHAE', 'CTEMELO', 'EGLILTN', 'OTINSEN', 'TREAEHT', 'YPHAERT', 'HBYTERE', 'OTUTHHG', 'URHOGHT',
                'HGOINTT', 'ATTLLYO', 'THEOCUD', 'DAORWST', 'IFARCTF', 'OLRUTBE', 'TGINUNR', 'TAILCYP', 'RMUOFNI',
                'OWNUKNN', 'LAUSUUN', 'DPARGUE', 'CPLUAES', 'TTIUILY', 'YAEVITR', 'SVRUOAI', 'IHLVEEC', 'NVRTUEE',
                'ONRIVES', 'NEEVRTA', 'YIRTVCO', 'WVENIGI', 'IVALLGE', 'ITLENOV', 'VAURLTI', 'BILSIVE', 'WGNITIA',
                'GIKNAWL', 'WGNNAIT', 'RAWNIGN', 'RNWAATR', 'INGAREW', 'AWEETHR', 'CSEBAWT', 'WTEIESB', 'GEDIWDN',
                'WEENDEK', 'LEEWCOM', 'EWAELRF', 'TENRESW', 'SEEHRAW', 'YEBERWH', 'HRHWETE', 'IILLWNG', 'WNNIGNI',
                'OWTUTIH', 'TESSNIW', 'WNORGKI', 'INRIWTG', 'TITERNW', ]

level_4_ANSWER = ['ABILITY', 'ABSENCE', 'ACADEMY', 'ACCOUNT', 'ACCUSED', 'ACHIEVE', 'ACQUIRE', 'ADDRESS', 'ADVANCE',
                  'ADVERSE', 'ADVISED', 'ADVISER', 'AGAINST', 'AIRLINE', 'AIRPORT', 'ALCOHOL', 'ALLEGED', 'ALREADY',
                  'ANALYST', 'ANCIENT', 'ANOTHER', 'ANXIETY', 'ANXIOUS', 'ANYBODY', 'APPLIED', 'ARRANGE', 'ARRIVAL',
                  'ARTICLE', 'ASSAULT', 'ASSUMED', 'ASSURED', 'ATTEMPT', 'ATTRACT', 'AUCTION', 'AVERAGE', 'BACKING',
                  'BALANCE', 'BANKING', 'BARRIER', 'BATTERY', 'BEARING', 'BEATING', 'BECAUSE', 'BEDROOM', 'BELIEVE',
                  'BENEATH', 'BENEFIT', 'BESIDES', 'BETWEEN', 'BILLION', 'BINDING', 'BROTHER', 'BROUGHT', 'BURNING',
                  'CABINET', 'CALIBER', 'CALLING', 'CAPABLE', 'CAPITAL', 'CAPTAIN', 'CAPTION', 'CAPTURE', 'CAREFUL',
                  'CARRIER', 'CAUTION', 'CEILING', 'CENTRAL', 'CENTRIC', 'CENTURY', 'CERTAIN', 'CHAMBER', 'CHANNEL',
                  'CHAPTER', 'CHARITY', 'CHARLIE', 'CHARTER', 'CHECKED', 'CHICKEN', 'CHRONIC', 'CIRCUIT', 'CLASSES',
                  'CLASSIC', 'CLIMATE', 'CLOSING', 'CLOSURE', 'CLOTHES', 'COLLECT', 'COLLEGE', 'COMBINE', 'COMFORT',
                  'COMMAND', 'COMMENT', 'COMPACT', 'COMPANY', 'COMPARE', 'COMPETE', 'COMPLEX', 'CONCEPT', 'CONCERN',
                  'CONCERT', 'CONDUCT', 'CONFIRM', 'CONNECT', 'CONSENT', 'CONSIST', 'CONTACT', 'CONTAIN', 'CONTENT',
                  'CONTEST', 'CONTEXT', 'CONTROL', 'CONVERT', 'CORRECT', 'COUNCIL', 'COUNSEL', 'COUNTER', 'COUNTRY',
                  'CRUCIAL', 'CRYSTAL', 'CULTURE', 'CURRENT', 'CUTTING', 'DEALING', 'DECIDED', 'DECLINE', 'DEFAULT',
                  'DEFENCE', 'DEFICIT', 'DELIVER', 'DENSITY', 'DEPOSIT', 'DESKTOP', 'DESPITE', 'DESTROY', 'DEVELOP',
                  'DEVOTED', 'DIAMOND', 'DIGITAL', 'DISCUSS', 'DISEASE', 'DISPLAY', 'DISPUTE', 'DISTANT', 'DIVERSE',
                  'DIVIDED', 'DRAWING', 'DRIVING', 'DYNAMIC', 'EASTERN', 'ECONOMY', 'EDITION', 'ELDERLY', 'ELEMENT',
                  'ENGAGED', 'ENHANCE', 'ESSENCE', 'EVENING', 'EVIDENT', 'EXACTLY', 'EXAMINE', 'EXAMPLE', 'EXCITED',
                  'EXCLUDE', 'EXHIBIT', 'EXPENSE', 'EXPLAIN', 'EXPLORE', 'EXPRESS', 'EXTREME', 'FACTORY', 'FACULTY',
                  'FAILING', 'FAILURE', 'FASHION', 'FEATURE', 'FEDERAL', 'FEELING', 'FICTION', 'FIFTEEN', 'FILLING',
                  'FINANCE', 'FINDING', 'FISHING', 'FITNESS', 'FOREIGN', 'FOREVER', 'FORMULA', 'FORTUNE', 'FORWARD',
                  'FOUNDER', 'FREEDOM', 'FURTHER', 'GALLERY', 'GATEWAY', 'GENERAL', 'GENETIC', 'GENUINE', 'GIGABIT',
                  'GREATER', 'HANGING', 'HEADING', 'HEALTHY', 'HEARING', 'HEAVILY', 'HELPFUL', 'HELPING', 'HERSELF',
                  'HIGHWAY', 'HIMSELF', 'HISTORY', 'HOLDING', 'HOLIDAY', 'HOUSING', 'HOWEVER', 'HUNDRED', 'HUSBAND',
                  'ILLEGAL', 'ILLNESS', 'IMAGINE', 'IMAGING', 'IMPROVE', 'INCLUDE', 'INITIAL', 'INQUIRY', 'INSIGHT',
                  'INSTALL', 'INSTANT', 'INSTEAD', 'INTENSE', 'INTERIM', 'INVOLVE', 'JOINTLY', 'JOURNAL', 'JOURNEY',
                  'JUSTICE', 'JUSTIFY', 'KEEPING', 'KILLING', 'KINGDOM', 'KITCHEN', 'KNOWING', 'LANDING', 'LARGELY',
                  'LASTING', 'LEADING', 'LEARNED', 'LEISURE', 'LIBERAL', 'LIBERTY', 'LIBRARY', 'LICENSE', 'LIMITED',
                  'LISTING', 'LOGICAL', 'LOYALTY', 'MACHINE', 'MANAGER', 'MARRIED', 'MASSIVE', 'MAXIMUM', 'MEANING',
                  'MEASURE', 'MEDICAL', 'MEETING', 'MENTION', 'MESSAGE', 'MILLION', 'MINERAL', 'MINIMAL', 'MINIMUM',
                  'MISSING', 'MISSION', 'MISTAKE', 'MIXTURE', 'MONITOR', 'MONTHLY', 'MORNING', 'MUSICAL', 'MYSTERY',
                  'NATURAL', 'NEITHER', 'NERVOUS', 'NETWORK', 'NEUTRAL', 'NOTABLE', 'NOTHING', 'NOWHERE', 'NUCLEAR',
                  'NURSING', 'OBVIOUS', 'OFFENSE', 'OFFICER', 'ONGOING', 'OPENING', 'OPERATE', 'OPINION', 'OPTICAL',
                  'ORGANIC', 'OUTCOME', 'OUTDOOR', 'OUTLOOK', 'OUTSIDE', 'OVERALL', 'PACIFIC', 'PACKAGE', 'PAINTED',
                  'PARKING', 'PARTIAL', 'PARTNER', 'PASSAGE', 'PASSING', 'PASSION', 'PASSIVE', 'PATIENT', 'PATTERN',
                  'PAYABLE', 'PAYMENT', 'PENALTY', 'PENDING', 'PENSION', 'PERCENT', 'PERFECT', 'PERFORM', 'PERHAPS',
                  'PHOENIX', 'PICKING', 'PICTURE', 'PIONEER', 'PLASTIC', 'POINTED', 'POPULAR', 'PORTION', 'POVERTY',
                  'PRECISE', 'PREDICT', 'PREMIER', 'PREMIUM', 'PREPARE', 'PRESENT', 'PREVENT', 'PRIMARY', 'PRINTER',
                  'PRIVACY', 'PRIVATE', 'PROBLEM', 'PROCEED', 'PROCESS', 'PRODUCE', 'PRODUCT', 'PROFILE', 'PROGRAM',
                  'PROJECT', 'PROMISE', 'PROMOTE', 'PROTECT', 'PROTEIN', 'PROTEST', 'PROVIDE', 'PUBLISH', 'PURPOSE',
                  'PUSHING', 'QUALIFY', 'QUALITY', 'QUARTER', 'RADICAL', 'RAILWAY', 'READILY', 'READING', 'REALITY',
                  'REALIZE', 'RECEIPT', 'RECEIVE', 'RECOVER', 'REFLECT', 'REGULAR', 'RELATED', 'RELEASE', 'REMAINS',
                  'REMOVAL', 'REMOVED', 'REPLACE', 'REQUEST', 'REQUIRE', 'RESERVE', 'RESOLVE', 'RESPECT', 'RESPOND',
                  'RESTORE', 'RETIRED', 'REVENUE', 'REVERSE', 'ROLLOUT', 'ROUTINE', 'RUNNING', 'SATISFY', 'SCIENCE',
                  'SECTION', 'SEGMENT', 'SERIOUS', 'SERVICE', 'SERVING', 'SESSION', 'SETTING', 'SEVENTH', 'SEVERAL',
                  'SHORTLY', 'SHOWING', 'SILENCE', 'SILICON', 'SIMILAR', 'SITTING', 'SIXTEEN', 'SKILLED', 'SMOKING',
                  'SOCIETY', 'SOMEHOW', 'SOMEONE', 'SPEAKER', 'SPECIAL', 'SPECIES', 'SPONSOR', 'STATION', 'STORAGE',
                  'STRANGE', 'STRETCH', 'STUDENT', 'STUDIED', 'SUBJECT', 'SUCCEED', 'SUCCESS', 'SUGGEST', 'SUMMARY',
                  'SUPPORT', 'SUPPOSE', 'SUPREME', 'SURFACE', 'SURGERY', 'SURPLUS', 'SURVIVE', 'SUSPECT', 'SUSTAIN',
                  'TEACHER', 'TELECOM', 'TELLING', 'TENSION', 'THEATRE', 'THERAPY', 'THEREBY', 'THOUGHT', 'THROUGH',
                  'TONIGHT', 'TOTALLY', 'TOUCHED', 'TOWARDS', 'TRAFFIC', 'TROUBLE', 'TURNING', 'TYPICAL', 'UNIFORM',
                  'UNKNOWN', 'UNUSUAL', 'UPGRADE', 'UPSCALE', 'UTILITY', 'VARIETY', 'VARIOUS', 'VEHICLE', 'VENTURE',
                  'VERSION', 'VETERAN', 'VICTORY', 'VIEWING', 'VILLAGE', 'VIOLENT', 'VIRTUAL', 'VISIBLE', 'WAITING',
                  'WALKING', 'WANTING', 'WARNING', 'WARRANT', 'WEARING', 'WEATHER', 'WEBCAST', 'WEBSITE', 'WEDDING',
                  'WEEKEND', 'WELCOME', 'WELFARE', 'WESTERN', 'WHEREAS', 'WHEREBY', 'WHETHER', 'WILLING', 'WINNING',
                  'WITHOUT', 'WITNESS', 'WORKING', 'WRITING', 'WRITTEN', ]

ran_num = randrange(0, (len(level_4_WORD)))
jumbled_rand_word = level_4_WORD[ran_num]

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
        ran_num = randrange(0, (len(level_4_WORD)))
        word.configure(text=level_4_WORD[ran_num])
        get_input.delete(0, END)
        ans.configure(text="Answer")

    def cheak():
        global points, ran_num
        user_word = get_input.get().upper()
        if user_word == level_4_ANSWER[ran_num]:
            points += 5
            score.configure(text="Score:- " + str(points))
            messagebox.showinfo('correct', "Correct Answer.. Keep it Up!")
            ran_num = randrange(0, (len(level_4_WORD)))
            word.configure(text=level_4_WORD[ran_num])
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
            ans.configure(text="Answer= " + level_4_ANSWER[ran_num])

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
        text=level_4_WORD[ran_num],
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
