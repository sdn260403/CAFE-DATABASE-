import mysql.connector as ms

C=ms.connect(user='root',host='localhost',password='1234',database='SDN')
C.autocommit=True
L=C.cursor()
def validate(x):
    if len(x)==10:
        return True
    return False

def create():
    L.execute("CREATE TABLE IF NOT EXISTS CUSTOMER_DETAILS(NAME VARCHAR(200) NOT NULL,PHONE_NUMBER VARCHAR(200) PRIMARY KEY)")

def insert():
    s={}
    Mno=input("ENTER MOBILE NUMBER: ")
    L.execute("SELECT * FROM CUSTOMER_DETAILS")
    while validate(Mno)==False:
        Mno=input("INVALID MOBILE NUMBER PLEASE RE ENTER: ")
        
    for i in L:
        s[i[1]]=i[0]
        
    if Mno in list(s.keys()):
        Name=s[Mno]
        print("WELCOME BACK CUSTOMER ",Name)
    else:
        Name=input("ENTER NAME: ").split()[0]
        L.execute("INSERT INTO CUSTOMER_DETAILS VALUES('{}','{}')".format(Name,Mno))
    print("CUSTOMER : ",Name,"\nMOBILE NO. : ",Mno)

