import datetime,random,pickle,time
class patient:                                                           #class creation
    def __init__(self):                                                  #using constructor
        self.fnaam=""
        self.lnaam=""
        self.ag=0
        self.di=""
        self.adno=0
class dot:
    def __init__(self):
        self.name1=""
        self.slipno=0
class appointt():
    def __init__(self):
        appointment_date=0
        no_appointment=0
def dat():                                                               
    global datee,tme
    datee=datetime.date.today()                                          #module of date
    tim=datetime.datetime.now()
    tme=datetime.time(tim.hour,tim.minute,tim.second)                    #module of time
    obj()
##################################################################login##########################################################################
def hospital():
    print ("``````````````````````````````````````````````````WELCOME TO Sanjeevani HOSPITAL`````````````````````````````````````````````````````")
    print ("                                                  ^^^^^^^ ^^ ^^^^^^^^^^ ^^^^^^^^ ")
    print ("```````````````````````````````````````````````````ITS OUR PLEASURE TO HELP YOU``````````````````````````````````````````````````````")
    print ("                                                   ^^^ ^^^ ^^^^^^^^ ^^ ^^^^ ^^^    ")
    print ("")
    print ("_____________________________________________________________________________________________________________________________________")


    hospital2()
def hospital2():
    print ("    1. Owner login                                                2. Patient login  ")
    print ("    ^  ^^^^^ ^^^^^                                                ^  ^^^^^^^ ^^^^^  ")
    ch=input("    Enter your choice ==>")
    if ch.isdigit():
        if int(ch)==1:
            owner()
        elif int(ch)==2:
            hospital3()
        else:
            print ("    Sorry wrong input , please try again")
            hospital2()
    elif ch.isalpha:
        print ("     Sorry wrong input, it must contain only digit, please input again")
        hospital2()
    else:
        print ("     Sorry wrong input, please input again")
        hospital()
def hospital3():
    print ("    Select your choice")
    print (" ")
    print ("    Press 1. to consult to any doctor                             Press 2. for the test")
    print ("    ^^^^^    ^^ ^^^^^^^ ^^ ^^^ ^^^^^^                             ^^^^^    ^^^ ^^^ ^^^^ ")
    print ("    Press 3. to get detail of test                                Press 4. for emergency")
    print ("    ^^^^^    ^^ ^^^ ^^^^^^ ^^ ^^^^                                ^^^^^    ^^^ ^^^^^^^^^")
    cho()
def cho():
    ch=input("    Enter your choice here ==>")
    if ch.isdigit():                                                    #taking choice of what to do
        if int(ch)==1:
            dis()
        elif int(ch)==2:
            drr()
        elif int(ch)==3:
            wh()
        elif int(ch)==4:
            em()
        else:
            print ("    Sorry wrong input, please enter again")
            cho()
    elif ch.isalpha():
        print ("     Sorry wrong input, it must contain only numbers,please input again")
        cho()
    else:
        print ("     Sorry wrong input, please input again")
        cho()

def dis():                                                               #module of disease
    print("""
_________________________________________________________________________________________________________________________________________________
    """)
    global c
    print ("    Specify your problem from below--")
    print ("    1. Stomach related problem                                    2. Brain related problem")
    print ("    ^  ^^^^^^^ ^^^^^^^ ^^^^^^^                                    ^  ^^^^^ ^^^^^^^ ^^^^^^^")
    print ("    3. Breathing problem                                          4. Skin problem(allergy,white patches)")
    print ("    ^  ^^^^^^^^^ ^^^^^^^                                          ^  ^^^^ ^^^^^^^ ^^^^^^ ^^^^^ ^^^^^^^ ")
    print ("    5. Bone related problem                                       6. Muscular problem (pain related to muscle like cramp)")
    print ("    ^  ^^^^ ^^^^^^^ ^^^^^^^                                       ^  ^^^^^^^^ ^^^^^^^  ^^^^ ^^^^^^^ ^^ ^^^^^^ ^^^^ ^^^^^")
    print ("    7. Heart related problem                                      8. Eye related problem")
    print ("    ^  ^^^^^ ^^^^^^^ ^^^^^^^                                      ^  ^^^ ^^^^^^^ ^^^^^^^ ")
    print ("""
_________________________________________________________________________________________________________________________________________________
    """)
    di=input("    Specify your problem here ==>")
    if di.isdigit():
        if int(di)==1:
            c="STOMACH"
            stomachh()
        elif int(di)==2:
            c="BRAIN"
            br()
        elif int(di)==3:
            c="BREATHING"
            breathingg()
        elif int(di)==4:
            c="SKIN"
            skinn()
        elif int(di)==5:
            c="BONE"
            bone()
        elif int(di)==6:
            c="MUSCULAR"
            musclee()
        elif int(di)==7:
            c="HEART"
            heartt()
        elif int(di)==8:
            c="EYE"
            eyee()
        else:
            print ("    Our hospital cannot serve treatment of this disease, please contact to Dr. Rajesh Tyagi")
            ext()
    else:
        print ("    Sorry wrong input , name of disease must contain only alphabets, please try again")
        dis()

def stomachh():                                                          #for stomach
    global d,doctor
    print ("    1. DR. UJJWAL JINDAL                                          2. DR. DUSHANT RAJPUT")
    print ("    ^  ^^  ^^^^^^ ^^^^^^                                          ^  ^^  ^^^^^^^ ^^^^^^  ")
    print ("    3. DR. RAHUL TYAGI                                            4. DR. SHIPRA TYAGI")
    print ("    ^  ^^  ^^^^^ ^^^^^                                            ^  ^^  ^^^^^^ ^^^^^")
    doctor=input("    ENTER THE DOCTOR OF YOUR CHOICE BY ENTERING DIGIT ==>")
    if doctor.isalpha():
        print ("    INVALID INPUT,IT MUST CONTAIN DIGITS ,please try again ")
        stomachh()
    elif doctor.isdigit():
        if int(doctor)==1:
            d="DR. UJJWAL JINDAL"
            ct1()
        elif int(doctor)==2:
            d="DR. DUSHANT RAJPUT"
            ct2()
        elif int(doctor)==3:
            d="DR. RAHUL TYAGI"
            ct3()
        elif int(doctor)==4:
            d="DR. SHIPRA TYAGI"
            ct4()
        else:
            print ("    Sorry invalid input, please try again")
            stomachh()
    else:
        print ("    Sorry invalid input, please try again")
        stomachh()
def br():                                                                #for brain
    global d,doctor
    print ("    1. DR. SHUBH GARG                                             2. DR. RAJ ARYA")
    print ("    ^  ^^  ^^^^^ ^^^^                                             ^  ^^  ^^^ ^^^^  ")
    print ("    3. DR. DIWAKAR SIROHI                                         4. DR. YOGENDER TYAGI")
    print ("    ^  ^^  ^^^^^^^ ^^^^^^                                         ^  ^^  ^^^^^^^^ ^^^^^")
    doctor=input("    ENTER THE DOCTOR OF YOUR CHOICE BY ENTERING DIGIT ==> ")
    if doctor.isalpha():
        print ("    INVALID INPUT,IT MUST CONTAIN DIGITS ,please try again ")
        br()
    elif doctor.isdigit():
        if int(doctor)==1:
            d="DR. SHUBH GARG"
            ct1()
        elif int(doctor)==2:
            d="DR. RAJ ARYA"
            ct2()
        elif int(doctor)==3:
            d="DR. DIWAKAR SIROHI"
            ct3()
        elif int(doctor)==4:
            d="DR. YOGENDER TYAGI"
            ct4()
        else:
            print ("    Sorry invalid input, please try again")
            br()
    else:
        print ("    Sorry invalid input, please try again")
        br()

def breathingg():                                                        #for breathing
    print ("    1. DR. ASHUTOSH SARAN                                         2. DR. DISHA SINGH")
    print ("    ^  ^^  ^^^^^^^^ ^^^^^                                         ^  ^^  ^^^^^ ^^^^^ ")
    print ("    3. DR. RAGHAV GOEL                                            4. DR. SHALINI GARG")
    print ("    ^  ^^  ^^^^^^ ^^^^                                            ^  ^^  ^^^^^^^ ^^^^")
    global d,doctor
    doctor=input("    ENTER THE DOCTOR OF YOUR CHOICE BY ENTERING DIGIT ==> ")
    if doctor.isalpha():
        print ("    INVALID INPUT,IT MUST CONTAIN DIGITS ,please try again ")
        breathingg()
    elif doctor.isdigit():
        if int(doctor)==1:
            d="DR. ASHUTOSH SARAN"
            ct1()
        elif int(doctor)==2:
            d="DR. DISHA SINGH"
            ct2()
        elif int(doctor)==3:
            d="DR. RAGHAV GOEL"
            ct3()
        elif int(doctor)==4:
            d="DR. SHALINI GARG"
            ct4()
        else:
            print ("    INVALID INPUT,INPUT AGAIN")
            breathingg()
    else:
        print ("    INVALID INPUT,please try again")
        breathingg()


def skinn():                                                             #for skin
    print ("    1. DR. LAKSHAY SINGHAL                                        2. DR. ABHIRUCHIKA SINGH")
    print ("    ^  ^^  ^^^^^^^ ^^^^^^^                                        ^  ^^  ^^^^^^^^^^^ ^^^^^")
    print ("    3. DR. LAKSHAY TOMAR                                          4. DR. KAVYA SINGHAL")
    print ("    ^  ^^  ^^^^^^^ ^^^^^                                          ^  ^^  ^^^^^ ^^^^^^^")
    global d,doctor
    doctor=input("ENTER THE DOCTOR OF YOUR CHOICE BY ENTERING DIGIT ==> ")
    if doctor.isalpha():
        print ("INVALID INPUT,IT MUST CONTAIN DIGITS ,please try again ")
        skinn()
    elif doctor.isdigit():
        if int(doctor)==1:
            d="DR. LAKSHAY SINGHAL"
            ct1()
        elif int(doctor)==2:
            d="DR. ABHIRUCHIKA SINGH"
            ct2()
        elif int(doctor)==3:
            d="DR. LAKSHAY TOMAR"
            ct3()
        elif int(doctor)==4:
            d="DR. KAVYA SINGHAL"
            ct4()
        else:
            print ("INVALID INPUT,INPUT AGAIN")
            skinn()
    else:
        print ("INVALID INPUT,please try again")
        skinn()

def bone():                                                              #for bone
    print ("    1. DR. PARAMJEET SINGH                                        2. DR. SURENDER SINGH")
    print ("    ^  ^^  ^^^^^^^^^ ^^^^^                                        ^  ^^  ^^^^^^^^ ^^^^^ ")
    print ("    3. DR. ARJUN SAINI                                            4. DR. ROHIT NIGHAM")
    print ("    ^  ^^  ^^^^^ ^^^^^                                            ^  ^^  ^^^^^ ^^^^^^")
    global d,doctor
    doctor=input("    ENTER THE DOCTOR OF YOUR CHOICE BY ENTERING DIGIT ==> ")
    if doctor.isalpha():
        print ("    INVALID INPUT,IT MUST CONTAIN DIGITS ,please try again ")
        bone()
    elif doctor.isdigit():
        if int(doctor)==1:
            d="DR. PARAMJEET SINGH"
            ct1()
        elif int(doctor)==2:
            d="DR. SURENDER SINGH"
            ct2()
        elif int(doctor)==3:
            d="DR. ARJUN SAINI"
            ct3()
        elif int(doctor)==4:
            d="DR. ROHIT NIGHAM"
            ct4()
        else:
            print ("    INVALID INPUT,INPUT AGAIN")
            bone()
    else:
        print ("    INVALID INPUT,please try again")
        bone()

def musclee():                                                           #for muscle
    print ("    1. DR. DEEPANSHU RANA                                         2. DR. ADITI SINGHAL")
    print ("    ^  ^^  ^^^^^^^^^ ^^^^                                         ^  ^^  ^^^^^ ^^^^^^^")
    print ("    3. DR. UJJWAL RUHELA                                          4. DR. RISHI GOEL")
    print ("    ^  ^^  ^^^^^^ ^^^^^^                                          ^  ^^  ^^^^^ ^^^^")
    global d,doctor
    doctor=input("    ENTER THE DOCTOR OF YOUR CHOICE BY ENTERING DIGIT ==> ")
    if doctor.isalpha():
        print ("    INVALID INPUT,IT MUST CONTAIN DIGITS ,please try again ")
        musclee()
    elif doctor.isdigit():
        if int(doctor)==1:
            d="DR. DEEPANSHU RANA"
            ct1()
        elif int(doctor)==2:
            d="DR. ADITI SINGHAL"
            ct2()
        elif int(doctor)==3:
            d="DR. UJJWAL RUHELA"
            ct3()
        elif int(doctor)==4:
            d="DR. RISHI GOEL"
            ct4()
        else:
            print ("    INVALID INPUT,INPUT AGAIN")
            musclee()
    else:
        print ("    INVALID INPUT,please try again")
        musclee()


def heartt():                                                            #for heart
    print( "    1. DR. TANYA VERMA                                            2. DR. ISHAN BHARDWAJ")
    print ("    ^  ^^^  ^^^^^ ^^^^^                                           ^  ^^^ ^^^^^ ^^^^^^^^ ")
    print ("    3. DR. MANISH GARG                                            4. DR. RIDHI SHRIVASTHAV")
    print ("   ^  ^^^ ^^^^^^ ^^^^                                            ^  ^^^ ^^^^^ ^^^^^^^^^^^ ")
    global d,doctor
    doctor=input("    ENTER THE DOCTOR OF YOUR CHOICE ==> ")
    if doctor.isalpha():
        print ("    INVALID INPUT,IT MUST CONTAIN DIGITS ,please try again ")
        heartt()
    elif doctor.isdigit():
        if int(doctor)==1:
            d="DR. TANYA VERMA"
            ct1()
        elif int(doctor)==2:
            d="DR. ISHAN BHARDWAJ"
            ct2()
        elif int(doctor)==3:
            d="DR. MANISH GARG"
            ct3()
        elif int(doctor)==4:
            d="DR. RIDHI SHRIVASTHAV"
            ct4()
        else:
            print ("    INVALID INPUT,INPUT AGAIN")
            heartt()
    else:
        print ("    INVALID INPUT,please try again")
        heartt()

def eyee():                                                              #for eye
    print ("    1. DR. SHUSHANT SAINI                                         2. DR. AKASH SINGH TEOTIA")
    print ("    ^  ^^  ^^^^^^^^ ^^^^^                                         ^  ^^  ^^^^^ ^^^^^ ^^^^^^")
    print ("    3. DR. ABHISHEK SHARMA                                        4. DR. ABHAY CHOUDHARY")
    print ("    ^  ^^  ^^^^^^^^ ^^^^^^                                        ^  ^^  ^^^^^ ^^^^^^^^^")
    global d
    global doctor
    doctor=input("    ENTER THE DOCTOR OF YOUR CHOICE BY ENTERING DIGIT ==> ")
    if doctor.isalpha():
        print ("    INVALID INPUT,IT MUST CONTAIN DIGITS ,please try again ")
        eyee()
    elif doctor.isdigit():
        if int(doctor)==1:
            d="DR. SHUSHANT SAINI"
            ct1()
        elif int(doctor)==2:
            d="DR. ABHISHEK SHARMA"
            ct2()
        elif int(doctor)==3:
            d="DR. AKASH SINGH TEOTIA"
            ct3()
        elif int(doctor)==4:
            d="DR. ABHAY CHOUDHARY"
            ct4()
        else:
            print ("    INVALID INPUT,INPUT AGAIN")
            eyee()
    else:
        print ("    INVALID INPUT,please try again")
        eyee()

def ct1():
    print ("____________________________________________________________________________________________________________________________________ ")
    print ("          ",d,              "                                                                  Monday - Wednesday & Saturday             ")
    print ("                                                                                                                                         ")
    print ("          B.A.M.S,B.Sc,M.D                                                                 9.00 am to 1.00 pm & 5.00 pm to 8.00 pm       ")
    print ("____________________________________________________________________________________________________________________________________ ")
    c1()
def c1():
    global ch
    print ("    " )                                                                                                                                 
    print ("       Consultancy fees ==> Rs. 800")
    print ("")
    print( "    1. Want to consult?                         2. Want to exit?                      3. Want to Go back? ")
    print (" ")
    ch=input("    ENTER PATIENT'S CHOICE ===>")
    if ch.isalpha():
        print ("    Sorry wrong input, please try again")
        ct1()
    elif ch.isdigit():
        if int(ch)==1:
            name()
        elif int(ch)==2:
            ext()
        elif int(ch)==3:
            dis()
        else:
            print ("    Sorry wrong input, please try again")
            ct1()
    else:
        print ("    Sorry wrong input,please try again")
        ct1()

def ct2():
    print ("____________________________________________________________________________________________________________________________________ ")
    print ("          ",d,            "                                                                     Tuesday - Friday & Sunday              ")
    print ("                                                                                                                                     ")
    print ("          M.B.B.S , M.D                                                                   10.00 am to 12.00 pm & 3.00 pm to 7.00 pm      ")
    print ("____________________________________________________________________________________________________________________________________ ")
    c2()
def c2():
    global ch
    print (" ")
    print ("       Consultancy fees ==> Rs. 1000")
    print( " ")
    print ("    1. Want to consult?                         2. Want to exit?                      3. Want to Go back? ")
    print( " ")
    ch=input("    ENTER PATIENT'S CHOICE ===>")
    if ch.isalpha():
        print ("    Sorry wrong input, please try again")
        ct2()
    elif ch.isdigit():
        if int(ch)==1:
            name()
        elif int(ch)==2:
            ext()
        elif int(ch)==3:
            dis()
        else:
            print ("    Sorry wrong input, please try again")
            ct2()
    else:
        print ("    Sorry wrong input,please try again")
        ct2()

def ct3():
    global p
    print( "____________________________________________________________________________________________________________________________________ ")
    print ("          ",d,                    "                                                                  Monday - Saturday                   ")                    
    print ("                                                                                                                                         ")
    print ("         B.Sc , M.D(Gold Medalist)                                                       8.00 am to 2.00 pm & 4.00 pm to 7.00 pm        ")
    print ("____________________________________________________________________________________________________________________________________ ")
    c3()
def c3():
    global ch
    print( "    ")
    print ("       Consultancy fees ==> Rs. 500")
    print (" ")
    print ("    1. Want to consult?                         2. Want to exit?                      3. Want to Go back? ")
    print (" ")
    ch=input("    ENTER PATIENT'S CHOICE ===>")
    if ch.isalpha():
        print ("    Sorry wrong input, please try again")
        ct3()
    elif ch.isdigit():
        if int(ch)==1:
            name()
        elif int(ch)==2:
            ext()
        elif int(ch)==3:
            dis()
        else:
            print ("    Sorry wrong input, please try again")
            ct3()
    else:
        print ("    Sorry wrong input,please try again")
        ct3()

def ct4():
    print ("____________________________________________________________________________________________________________________________________")
    print( "          ",d,                   "                                                                   Tuesday - Saturday                 ")
    print ("                                                                                                                                        ")
    print( "          B.A.M.S , M.B.B.S , M.S                                                        10.00 am to 1.00 pm & 5.00 pm to 7.00 pm       ")
    print ("____________________________________________________________________________________________________________________________________")
    c4()
def c4():
    global ch
    print ("  ")
    print ("       Consultancy fees ==> Rs. 1000")
    print (" ")
    print ("    1. Want to consult?                         2. Want to exit?                      3. Want to Go back? ")
    print (" ")
    ch=input("    ENTER PATIENT'S CHOICE ===>")
    if ch.isalpha():
        print ("    Sorry wrong input, please try again")
        ct4()
    elif ch.isdigit():
        if int(ch)==1:
            name()
        elif int(ch)==2:
            ext()
        elif int(ch)==3:
            dis()
        else:
            print( "    Sorry wrong input, please try again")
            ct4()
    else:
        print ("     Sorry wrong input,please try again")
        ct4()

def name():                                      #module of name
    global fnaam,lnaam,p1
    p1=patient()
    print( " ")
    fnaam=input("    Enter first name of patient ==>")
    if fnaam.isalpha():
        lnaam=input("    Enter last name of patient ==>")
        if lnaam.isalpha():
            fnaam=fnaam.upper()
            lnaam=lnaam.upper()
            age()
        else:
            print ("    Sorry wrong input, please try again")
            name()
    else:
        print ("    Sorry wrong input, Name only contain alphabets , please try again")
        name()
def age():                                      #module of age
    print (" ")
    global ag
    ag=input("    Enter age of patient in digits ==>")
    if ag.isdigit():
        if int(ag)>=1 and int(ag)<=100:
            ad()
        else:
            print ("    Sorry wrong input,age must contain only digits, please try again")
            age()
    else:
        print ("    Sorry wrong input,age must contain only digits, please try again")
        age()
def ad():
    global adno
    print (" ")
    adno=input("    Enter patient's aadhar number ==>")
    if adno.isdigit():
        if len(adno)==12:
            dat()
        else:
            print ("    Invalid aadhar number, Aadhar number must contain only 12 digits, please try again")
            ad()
    else:
        print ("    Invalid aadhar number, please try again")
        ad()
def obj():
    print("_____________________________________________________________________________________________________________________________________")
    print("                                                  Please Wait....")
    print("""                                                  ---------------



                """)
    time.sleep(1)
    print ("____________________________________________________________________________________________________________________________________")
    print( "                                                                                                                                        ")
    print ("`````````````````````````````````````````````````````Sanjeevani HOSPITAL````````````````````````````````````````````````````````````")
    print( "                                                     ^^^^^^^^^^ ^^^^^^^^                                                            ")
    print ("`````````````````````````````````````````````````ITS OUR PLEASURE TO HELP YOU```````````````````````````````````````````````````````")
    print ("                                                 ^^^ ^^^ ^^^^^^^^ ^^ ^^^^ ^^^                                                       ")
    print ("                                                                                                                                        ")
    print ("                                                                                                                                        ")
    print ("       Mobile No. :  9678564432,7865432860,01222354657,01222356780                                                                                 " )
    print ("____________________________________________________________________________________________________________________________________")
    ob()
def ob():
    global p1
    global datee
    global fnaam
    global lnaam
    global ag
    global c
    global adno
    global doctor
    ff=open("Hospital.dat","wb+")
    p1.fnaam=fnaam
    p1.lnaam=lnaam                              #object creation
    p1.ag=ag
    p1.c=c
    p1.dat=dat
    p1.adno=adno
    pickle.dump(p1,ff)
    ff.seek(0)
    try:
        while ff:
            p1=pickle.load(ff)
            print ("         ",datee,"                                                                                ",tme)
            print ("____________________________________________________________________________________________________________________________________")                                              
            print ("      Name of patient : ",p1.fnaam,"",p1.lnaam,"                               Age : ",p1.ag)
            print ("                 ")
            print ("      Problem related to : ",p1.c)
            print ("     ")
            print ("      Prescribed Medicines : ")          
            print ("""


















                    """)
            print ("____________________________________________________________________________________________________________________________________")
            print ("      ADDRESS   :   SANJEEVANI HOSPITAL,H-33,SECTOR-27,NOIDA     "                                                     )
            print (" ")
            print ("                                                                                                                                         ")
            print ("`````````````````````````````````````````````````````THANK YOU FOR VISITING OUR HOSPITAL````````````````````````````````````````````")
            print( "                                                     ^^^^^ ^^^ ^^^ ^^^^^^^^ ^^^ ^^^^^^^^                                             ")
            print ("`````````````````````````````````````````````````````````````GET WELL SOON``````````````````````````````````````````````````````````")
            print( "                                                             ^^^ ^^^^ ^^^^                                                           ")
            print ("````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
    except EOFError:
        pass
    ff.close()
    
############################################################test####################################################################
def drr():
    e=random.randint(100,999)                                                           
    print ('''    Which Test You Want To Do?")
        1. Diabities Test                                             2. CT Scan
        ^  ^^^^^^^^^ ^^^^                                             ^  ^^ ^^^^
        3. X-Ray                                                      4. Ultra Sound
        ^  ^ ^^^^                                                     ^  ^^^^^ ^^^^^
        5. Endoscopy                                                  6. Thyroid Test
        ^  ^^^^^^^^^                                                  ^  ^^^^^^^ ^^^^
        7. MRI                                                        8. Urinalysis
        ^  ^^^                                                        ^  ^^^^^^^^^^''')
    dr=input("    Please! Enter Patient's Choice ==>")
    if dr.isalpha():
        print ("    Sorry Wrong input, please try again ")
        drr()
    elif dr.isdigit():
        if int(dr)==1:
            print("    The Test Fees Is Rs.100")
            print("    Please! Go To Testing Room With Slip No.",e)
            print("    Patient's Test Details Will Come Tommorow")
            prin()
        elif int(dr)==2:
            print("    The Test Fees Is Rs.2500")
            print("    Please! Go To Testing Room With Slip No.",e)
            print("    Patient's Test Details Will Come Tommorow")
            prin()
        elif int(dr)==3:
            print("    The Test Fees Is Rs.600")
            print("    Please! Go To Testing Room With Slip No.",e)
            print("    Patient's Test Details Will Come Tommorow")
            prin()
        elif int(dr)==4:
            print("    The Test Fees Is Rs.1000")
            print("    Please! Go To Testing Room With Slip No.",e)
            print("    Patient's Test Details Will Come Tommorow")
            prin()
        elif int(dr)==5:
            print("    The Test Fees Is Rs.3000" )                                        
            print("    Please! Go To Testing Room With Slip No.",e)
            print("    Patient's Test Details Will Come Tommorow")
            prin()
        elif int(dr)==6:
            print("    The Test Fees Is Rs.500")
            print("    Please! Go To Testing Room With Slip No.",e)
            print("    Patient's Test Details Will Come Tommorow")
            prin()
        elif int(dr)==7:
            print("    The Test Fees Is Rs.6000")
            print("    Please! Go To Testing Room With Slip No.",e)
            print("    Patient's Test Details Will Come Tommorow")
            prin()
        elif int(dr)==8:
            print("    The Test Fees Is Rs.900"  )                                            
            print("    Please! Go To Testing Room With Slip No.",e)
            print("    Patient's Test Details Will Come Tommorow")
            prin()
        else:
            print ("    Sorry wrong input, please try again")
            drr()
    else:
        print ("    Sorry wrong input, please try again")
        drr()
############################################################report###################################################################
def wh():
    global name1,p2
    p2=dot()
    name1=input("    Please! Enter patient's name ==>")
    if name1.isalpha():
        whs()
    else:
        print ("    Sorry! Wrong input")
        wh()

def whs():
    global slipno
    slipno=input("    Please! Enter Your three digit slip number ==>")
    if slipno.isdigit():
        if int(slipno)>=100 and int(slipno)<=999:
            report()
        else:
            print("    Sorry! Wrong input")
            whs()
    else:
        print("    Sorry! Wrong input,please input again")
        whs()

def report():
    global name1
    global slipno
    global p2
    L=[]
    f=open("Report.dat","wb+")
    ft=open("patient report.dat","wb+")
    I=0
    found=False
    while I<=500:
        k=random.randint(100,999)
        L.append(k)
        I=I+1
    pickle.dump(L,f)
    f.close()
    p2.name1=name1
    p2.slipno=slipno
    pickle.dump(p2,ft)
    ft.close()
    for K in L:
        if found==False:
            if int(slipno)==int(K):

                found=True
                print("```````````````````````````````````````````````````````````````Report Found``````````````````````````````````````````````````````````")
                print("                                                               ^^^^^^ ^^^^^ ")
                time.sleep(1)
                print ("")
                print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                print("```````````````````````````````````````````````````````````Your Reports Are Ready````````````````````````````````````````````````````")
                print("                                                           ^^^^ ^^^^^^^ ^^^ ^^^^^      ")
                print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                break
    if int(slipno) not in L: 
        print ("``````````````````````````````````````````````````````Sorry Your Reports Are Not Ready``````````````````````````````````````````````")
        print ("                                                      ^^^^^ ^^^^ ^^^^^^^ ^^^ ^^^ ^^^^^ ")
        prin()
    else:
        prin()
##########################################################emergency##################################################################
def em():
    print ("    1. DR. PRADEEP ARYA                                           2. DR. SUSHIL SHISHODHIYA")
    print ("    ^  ^^  ^^^^^^^ ^^^^                                           ^  ^^  ^^^^^^ ^^^^^^^^^^^")
    print ("    3. DR. DEVENDRA SHARMA                                        4. DR. RAJESH KAPOOR")
    print ("    ^  ^^  ^^^^^^^^ ^^^^^^                                        ^  ^^  ^^^^^^ ^^^^^")
    emg=["DR. PRADEEP ARYA","DR.SUSHIL SHISHODHIYA","DR.DEVENDRA SHARMA","DR.RAJESH KAPOOR"]
    em=''
    for t in range(0,7):
        h=random.randint(0,3)
    emg=em+emg[h]
    print("    Please! Take The Patient To The ICU Room.")
    print("   ",emg," is ready in the ICU Room.")
    print("    All Necessary Facilities are available in the ICU Room.")
    prin()
#############################################################owner###################################################################
def owner():
    chance=5
    for i in range(chance,0,-1):
        password=input("    Enter password ===>")
        if chance>=1:
            if password.isalpha():
                print ("    Invalid password ,it contain only digits, please try again")
                owner()
            elif password.isdigit():
                if int(password)==45678:
                    break      
                    
            else:
                print ("    Sorry wrong input, please try again")
                owner()
        else:
            print ("    Please try after 10 seconds")
            print ("                                .........................")
            time.sleep(10)
            owner()
    owner2()
        
        
def owner2():
    print ('''    Select type to be searched :--                                                                                     
                                                                                                                        
              1. Related to Doctor & appointment                                        2. Shortage of Doctor                        
              ^  ^^^^^^^ ^^ ^^^^^^ ^ ^^^^^^^^^^^                                        ^  ^^^^^^^^ ^^ ^^^^^^                        
         
              3. Shortage of Nurse                                                      4. Shortage of other things(BEDS,AC'S,ETC.)  
              ^  ^^^^^^^^ ^^ ^^^^^                                                      ^  ^^^^^^^^ ^^ ^^^^^ ^^^^^^ ^^^^ ^^ ^ ^^^    ''')
    ch=input("    Enter your choice ==>")
    if ch.isalpha():
        print ("    Sorry Wrong input, please try again ")
        owner2()
    elif ch.isdigit():
        if int(ch)==1:
            owner3()
        elif int(ch)==2:
            shortage_d()
        elif int(ch)==3:
            shortage_n()
        elif int(ch)==4:
            shortage_o()
        else:
            print ("    Sorry wrong input, please try again")
            owner2()
    else:
        print ("    Sorry wrong input, please try again")
        owner2()
def owner3():
    print('''    Specify department from below--"
               1. Gastric department                                         2. Neurology department
               ^  ^^^^^^^ ^^^^^^^^^^                                         ^  ^^^^^^^^^ ^^^^^^^^^^
               3. Respiratory department                                     4. Dermatology department
               ^  ^^^^^^^^^^^ ^^^^^^^^^^                                     ^  ^^^^^^^^^^^ ^^^^^^^^^^
               5. Osteoporosis department                                    6. Musculosketal department
               ^  ^^^^^^^^^^^^ ^^^^^^^^^^                                    ^  ^^^^^^^^^^^^^ ^^^^^^^^^^
               7. Cardiology department                                      8. Ophthalmology department
               ^  ^^^^^^^^^^ ^^^^^^^^^^                                      ^  ^^^^^^^^^^^^ ^^^^^^^^^^''')
    ch=input("    Enter your choice ==>")
    if ch.isalpha():
        print ("    Sorry wrong input, choice must be in digit")
    elif ch.isdigit():
        if int(ch)==1:
            department="Stomach"
            department_stomach()
        elif int(ch)==2:
            department="Brain"
            department_brain()
        elif int(ch)==3:
            department="Breathing"
            department_breathing()
        elif int(ch)==4:
            department="Skin"
            department_skin()
        elif int(ch)==5:
            department="Bone"
            department_bone()
        elif int(ch)==6:
            department="Muscular"
            department_muscule()
        elif int(ch)==7:
            department="Heart"
            department_heart()
        elif int(ch)==8:
            department="Eye"
            department_eye()
        else:
            print ("    Sorry wrong input, please try again")
            owner3()
    else:
        print ("    Sorry wrong input, please try again, it only contain digits")
        owner3()
def department_stomach():
    global appointment_doctor
    print ('''    1. DR. UJJWAL JINDAL                                          2. DR. DUSHANT RAJPUT
                  ^  ^^  ^^^^^^ ^^^^^^                                          ^  ^^  ^^^^^^^ ^^^^^^  
                  3. DR. RAHUL TYAGI                                            4. DR. SHIPRA TYAGI
                  ^  ^^  ^^^^^ ^^^^^                                            ^  ^^  ^^^^^^ ^^^^^''')
    ch=input("    Choose Doctor of your choice by entering digits assigned ==>")
    if ch.isalpha():
        print ("    Sorry wrong input, please input again in digits")
        department_stomach()
    elif ch.isdigit():
        if int(ch)==1:
            appointment_doctor="UJJWAL JINDAL"
            appoint()
        elif int(ch)==2:
            appointment_doctor="DUSHANT RAJPUT"
            appoint()
        elif int(ch)==3:
            appointment_doctor="RAHUL TYAGI"
            appoint()
        elif int(ch)==4:
            appointment_doctor="SHIPRA TYAGI"
            appoint()
        else:
            print ("    Sorry wrong input ,please input again by entering digits")
            department_stomach()
    else:
        print ("    Sorry wrong input ,please input again by entering digits")
        department_stomach()
def department_brain():
    global appointment_doctor
    print ("    1. DR. SHUBH GARG                                             2. DR. RAJ ARYA")
    print ("    ^  ^^  ^^^^^ ^^^^                                             ^  ^^  ^^^ ^^^^  ")
    print ("    3. DR. DIWAKAR SIROHI                                         4. DR. YOGENDER TYAGI")
    print ("    ^  ^^  ^^^^^^^ ^^^^^^                                         ^  ^^  ^^^^^^^^ ^^^^^")
    ch=input("    Choose Doctor of your choice by entering digits assigned ==>")
    if ch.isalpha():
        print ("    Sorry wrong input, please input again in digits")
        department_brain()
    elif ch.isdigit():
        if int(ch)==1:
            appointment_doctor="SHUBH GARG"
            appoint()
        elif int(ch)==2:
            appointment_doctor="RAJ ARYA"
            appoint()
        elif int(ch)==3:
            appointment_doctor="DIWAKAR SIROHI"
            appoint()
        elif int(ch)==4:
            appointment_doctor="YOGENDER TYAGI"
            appoint()
        else:
            print ("    Sorry wrong input ,please input again by entering digits")
            department_brain()
    else:
        print ("    Sorry wrong input ,please input again by entering digits")
        department_brain()
def department_breathing():
    global appointment_doctor
    print( "    1. DR. ASHUTOSH SARAN                                         2. DR. DISHA SINGH")
    print ("    ^  ^^  ^^^^^^^^ ^^^^^                                         ^  ^^  ^^^^^ ^^^^^ ")
    print ("    3. DR. RAGHAV GOEL                                            4. DR. SHALINI GARG")
    print ("    ^  ^^  ^^^^^^ ^^^^                                            ^  ^^  ^^^^^^^ ^^^^")
    ch=input("    Choose Doctor of your choice by entering digits assigned ==>")
    if ch.isalpha():
        print ("    Sorry wrong input, please input again in digits")
        department_breathing()
    elif ch.isdigit():
        if int(ch)==1:
            appointment_doctor="ASHUTOSH SARAN"
            appoint()
        elif int(ch)==2:
            appointment_doctor="DISHA SINGH"
            appoint()
        elif int(ch)==3:
            appointment_doctor="RAGHAV GOEL"
            appoint()
        elif int(ch)==4:
            appointment_doctor="SHALINI GARG"
            appoint()
        else:
            print ("    Sorry wrong input ,please input again by entering digits")
            department_breathing()
    else:
        print( "    Sorry wrong input ,please input again by entering digits")
        department_breathing()
def department_skin():
    global appointment_doctor
    print('''  1. DR. LAKSHAY SINGHAL                                        2. DR. ABHIRUCHIKA SINGH
               ^  ^^  ^^^^^^^ ^^^^^^^                                        ^  ^^  ^^^^^^^^^^^ ^^^^^
               3. DR. LAKSHAY TOMAR                                          4. DR. KAVYA SINGHAL
               ^  ^^  ^^^^^^^ ^^^^^                                          ^  ^^  ^^^^^ ^^^^^^^''')
    ch=input("    Choose Doctor of your choice by entering digits assigned ==>")
    if ch.isalpha():
        print ("    Sorry wrong input, please input again in digits")
        department_skin()
    elif ch.isdigit():
        if int(ch)==1:
            appointment_doctor="LAKSHAY SINGHAL"
            appoint()
        elif int(ch)==2:
            appointment_doctor="ABHIRUCHIKA SINGH"
            appoint()
        elif int(ch)==3:
            appointment_doctor="LAKSHAY TOMAR"
            appoint()
        elif int(ch)==4:
            appointment_doctor="KAVYA SINGHAL"
            appoint()
        else:
            print ("    Sorry wrong input ,please input again by entering digits")
            department_skin()
    else:
        print ("    Sorry wrong input ,please input again by entering digits")
        department_skin()
def department_bone():
    global appointment_doctor
    print (''' 1. DR. PARAMJEET SINGH                                        2. DR. SURENDER SINGH
               ^  ^^  ^^^^^^^^^ ^^^^^                                        ^  ^^  ^^^^^^^^ ^^^^^ 
               3. DR. ARJUN SAINI                                            4. DR. ROHIT NIGHAM
               ^  ^^  ^^^^^ ^^^^^                                            ^  ^^  ^^^^^ ^^^^^^''')
    ch=input("    Choose Doctor of your choice by entering digits assigned ==>")
    if ch.isalpha():
        print ("    Sorry wrong input, please input again in digits")
        department_bone()
    elif ch.isdigit():
        if int(ch)==1:
            appointment_doctor="PARAMJEET SINGH"
            appoint()
        elif int(ch)==2:
            appointment_doctor="SURENDER SINGH"
            appoint()
        elif int(ch)==3:
            appointment_doctor="ARJUN SAINI"
            appoint()
        elif int(ch)==4:
            appointment_doctor="ROHIT NIGHAM"
            appoint()
        else:
            print ("    Sorry wrong input ,please input again by entering digits")
            department_bone()
    else:
        print ("    Sorry wrong input ,please input again by entering digits")
        department_bone()
def department_muscule():
    global appointment_doctor
    print( "    1. DR. DEEPANSHU RANA                                         2. DR. ADITI SINGHAL")
    print ("    ^  ^^  ^^^^^^^^^ ^^^^                                         ^  ^^  ^^^^^ ^^^^^^^  ")
    print ("    3. DR. UJJWAL RUHELA                                          4. DR. RISHI GOEL")
    print ("    ^  ^^  ^^^^^^ ^^^^^^                                          ^  ^^  ^^^^^ ^^^^")
    ch=input("    Choose Doctor of your choice by entering digits assigned ==>")
    if ch.isalpha():
        print ("    Sorry wrong input, please input again in digits")
        department_muscule()
    elif ch.isdigit():
        if int(ch)==1:
            appointment_doctor="DEEPANSHU RANA"
            appoint()
        elif int(ch)==2:
            appointment_doctor="ADITI SINGHAL"
            appoint()
        elif int(ch)==3:
            appointment_doctor="UJJWAL RUHELA"
            appoint()
        elif int(ch)==4:
            appointment_doctor="RISHI GOEL"
            appoint()
        else:
            print ("    Sorry wrong input ,please input again by entering digits")
            department_muscule()
    else:
        print ("    Sorry wrong input ,please input again by entering digits")
        department_muscule()
def department_heart():
    global appointment_doctor
    print ("    1. DR. TANYA VERMA                                            2. DR. ISHAN BHARDWAJ")
    print ("    ^  ^^^  ^^^^^ ^^^^^                                           ^  ^^^ ^^^^^ ^^^^^^^^ ")
    print ("    3. DR. MANISH GARG                                            4. DR. RIDHI SHRIVASTHAV")
    print ("    ^  ^^^ ^^^^^^ ^^^^                                            ^  ^^^ ^^^^^ ^^^^^^^^^^^ ")
    ch=input("    Choose Doctor of your choice by entering digits assigned ==>")
    if ch.isalpha():
        print ("    Sorry wrong input, please input again in digits")
        department_heart()
    elif ch.isdigit():
        if int(ch)==1:
            appointment_doctor="TANYA VERMA"
            appoint()
        elif int(ch)==2:
            appointment_doctor="ISHAN BHARDWAJ"
            appoint()
        elif int(ch)==3:
            appointment_doctor="MANISH GARG"
            appoint()
        elif int(ch)==4:
            appointment_doctor="RIDHI SHRIVASTHAV"
            appoint()
        else:
            print ("    Sorry wrong input ,please input again by entering digits")
            department_heart()
    else:
        print ("    Sorry wrong input ,please input again by entering digits")
        department_heart()
def department_eye():
    global appointment_doctor
    print ("    1. DR. SHUSHANT SAINI                                         2. DR. AKASH SINGH TEOTIA")
    print ("    ^  ^^  ^^^^^^^^ ^^^^^                                         ^  ^^  ^^^^^ ^^^^^ ^^^^^^")
    print ("    3. DR. ABHISHEK SHARMA                                        4. DR. ABHAY CHOUDHARY")
    print ("    ^  ^^  ^^^^^^^^ ^^^^^^                                        ^  ^^  ^^^^^ ^^^^^^^^^")
    ch=input("    Choose Doctor of your choice by entering digits assigned ==>")
    if ch.isalpha():
        print ("    Sorry wrong input, please input again in digits")
        department_eye()
    elif ch.isdigit():
        if int(ch)==1:
            appointment_doctor="SHUSHANT SAINI"
            appoint()
        elif int(ch)==2:
            appointment_doctor="AKASH SINGH TEOTIA"
            appoint()
        elif int(ch)==3:
            appointment_doctor="ABHISHEK SHARMA"
            appoint()
        elif int(ch)==4:
            appointment_doctor="ABHAY CHOUDHARY"
            appoint()
        else:
            print ("    Sorry wrong input ,please input again by entering digits")
            department_eye()
    else:
        print ("    Sorry wrong input ,please input again by entering digits")
        department_eye()
def appoint():
    global appointment_doctor
    k=appointt()
    dateee=datetime.date.today()
    f=random.randint(1,20)
    appointfile=open("appointment_file.dat","wb+")
    k.appointment_date=dateee
    k.no_appointment=f
    pickle.dump(k,appointfile)
    appointfile.seek(0)
    try:
        while True:
            pickle.load(appointfile)
            print("        Appointment Date                                                 No. Of Appointments")
            print("        ^^^^^^^^^^^ ^^^^                                                 ^^  ^^ ^^^^^^^^^^^^")
            print("          ",dateee, "                                                            ",f," ")
    except EOFError:
        pass
    appointfile.close()
    ext()
####################################################shortage of doctor##############################################################
def shortage_d():
    b=random.randint(0,3)
    l=["Gastric","Neurology","Respiratory","Dermatology","Osteoporosis","Musculosketal","Cardiology","Ophthalmology"]
    c=""
    for j in range(0,3):
        i=random.randint(0,7)
    c=c+l[i]
    short=open("shortage of doctor.txt","w+")
    if b==0:
        k=("    Their is no shortage of Doctors in any Department")
        print (k)
        short.writelines(k)
        short.close()
        ext()
    elif b==1:
        k=("   Their is shortage of one Doctor in ",str(c),"Department")
        print( k)
        short.writelines(k)
        short.close()
        ext()
    else:
        k=("   Their is shortage of ",str(b)," Doctors in ",str(c),"Department")
        print( k)
        short.writelines(k)
        short.close()
        ext()
####################################################shortage of nurse###############################################################
def shortage_n():
    z=random.randint(0,3)
    short=open("shortage of nurse.txt","w+")
    if z==0:
        k="    Their is no shortage of Nurses in the Hospital"
        print (k)
        short.writelines(k)
        short.close()
        ext()
    elif z==1:
        k="    Their is shortage of one Nurse in the Hospital"
        short.writelines(k)
        short.close()
        print (k)
        ext()
    else:
        k="    Their is shortage of ",str(z)," Nurses in the Hospital"
        print (k)
        short.writelines(k)
        short.close()
        ext()
################################################shortage of other things############################################################
def shortage_o():
    w=random.randint(0,4)
    d=["AC'S","CURTAINS","FANS","VENTILATORS","STRECHERS","BENCHES","OXYGEN CYLINDERS","BEDS"]     
    a=["AC,CURTAIN","FAN","VENTILATOR","STRECHER","BENCH","OXYGEN CYLINDER","BED"]
    e=""
    q=""
    for t in range(0,1):
        y=random.randint(0,7)
    e=e+a[y]
    q=q+d[y]
    if w==0:
        print("    Every thing is available in the Hospital")
        ext()
    elif w==1:
        print("    Their is shortage of one ",e," in the Hospital")
        ext()
    else:
        print("    Their is shortage of ",w,"",q," in the Hospital")
        ext()
###########################################################print#####################################################################
def prin():
    print('''                                                                                                                                   
            `````````````````````````````````````````````````````THANK YOU FOR VISITING OUR HOSPITAL````````````````````````````````````````````
                                                                 ^^^^^ ^^^ ^^^ ^^^^^^^^ ^^^ ^^^^^^^^                                             
            `````````````````````````````````````````````````````````````GET WELL SOON``````````````````````````````````````````````````````````
                                                                         ^^^ ^^^^ ^^^^                                                           
            ````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````''')
    ext()
############################################################exit#####################################################################
def ext():
    print ('''
               DO YOU WANT TO DO SOMETHING ELSE
            
               Press 1. for yes                
               Press 2. for no                 ''')
    ch=input("    Enter your choice ==>")
    if ch.isdigit():
        if int(ch)==1:
           hospital2()
        elif int(ch)==2:
            print ("")
        else:
            print ("    Sorry wrong input,please try again")
            ext()
    elif ch.isalpha():
        print ("Sorry wrong input, please input again")
        ext()
    else:
        print ("Sorry wrong input,please input again")
        ext()
hospital()

