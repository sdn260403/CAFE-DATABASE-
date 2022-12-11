import Customer as c
import mysql.connector as ms
C=ms.connect(user='root',host='localhost',password='1234',database='SDN')
C.autocommit=True
L=C.cursor()
L.execute("DROP TABLE ORDER_SUMMARY")
L.execute("SELECT * FROM CAFE_MENU")
print("        -:-:-:MENU:-:-:-\n\nINDEX NO.\tNAME\tPRICE")
for i in L:
    print("{}{}\t{}".format(str(i[0]).center(5),i[1].rjust(15),i[2]))
L.execute("CREATE TABLE ORDER_SUMMARY(NAME VARCHAR(100) ,PRICE INTEGER NOT NULL ,QTY INTEGER)")
ch='y'
t=0
while ch.lower()=='y':
    X=int(input("\nPLEASE ENTER INDEX NO. "))
    Q=int(input("PLEASE ENTER QUANTITY "))
    L.execute("Select * from CAFE_MENU where IndexNo={}".format(X))
    n=L.fetchone()
    L.execute("INSERT INTO ORDER_SUMMARY values('{}',{},{})".format(n[1],n[2],Q))
    t+=(n[2]*Q)
    ch=input("ENTER Y TO CONTINUE")
L.execute("Select * from ORDER_SUMMARY")
c.create()
c.insert()
print("NAME      PRICE")
for i in L:
    print("{}      {}".format(i[0],i[1]))
print("AMOUNT PAYABLE: ",t)

