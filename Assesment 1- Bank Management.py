#Banking Application
acountNo=0
CusName=" "
BCode =" "
Mobile=0
Bal=0

def CreateAccount():
    global acountNo
    global CusName
    global BCode 
    global Mobile
    global Bal
    acountNo = int(input("Enter Account No="))
    CusName = input("Enter Name=")
    Bcode = input("Enter Branch Code=")
    Mobile = int(input("Enter Mobile Number="))
    Bal =int(input("Enter Current Balance="))

def ShowAcntDetails():
    print("AcountNo:",acountNo)
    print("CustomerName:",CusName)
    print("Bcode:",Bcode)
    print("mobile:",Mobile)

def Withdraw(amount):
    global Bal
    Bal = Bal-amount
    chckbalance()

def Deposit(amount):
    global Bal
    Bal= Bal+amount
    chckbalance()

def chckbalance():
    print("current Balance:",Bal)

#_Main_#
ch1='y'
while(ch1=="y"):
    print("1.Create Account \n 2.Withdraw \n 3.Deposit \n 4.check Balance")
    ch=int(input("Select Any Option:"))
    if(ch==1):
        CreateAccount()
    elif(ch==2):
        amount=int(input("Enter Amount To withdraw:"))
        Withdraw(amount)
    elif(ch==3):
        amnt=int(input("Enter Amount To deposit:"))
        Deposit(amount)
    elif(ch==4):
        chckbalance()
    else:
        print("Please Select Any Four Options Availabel = ")
    print("Do You Want To Continue...Press y")
    ch1=input()
    







