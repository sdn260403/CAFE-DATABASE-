import mysql.connector as ms

C=ms.connect(user='root',host='localhost',password='1234',database='SDN')
C.autocommit=True
L=C.cursor(buffered=True)

def create():
    L.execute('CREATE TABLE IF NOT EXISTS CAFE_MENU(IndexNo INTEGER NOT NULL PRIMARY KEY,NAME VARCHAR(200) NOT NULL,PRICE INTEGER NOT NULL)')
    L.execute('SELECT COUNT(*) FROM CAFE_MENU')
    c=0
    r=int(input("ENTER NUMBER OF ITEMS: "))
    for i in range(r):
        n=input("ENTER NAME OF ITEM ")
        P=int(input("ENTER PRICE OF ITEM "))
        L.execute('INSERT INTO CAFE_MENU VALUES({},"{}",{})'.format(c+1,n,P))
        c+=1

def delete():
    d=input("ENTER INDEX NUMBER OF DATA TO DELETE ")
    L.execute("DELETE FROM CAFE_MENU WHERE IndexNo={}".format(d))
    L.execute("UPDATE CAFE_MENU SET IndexNo=IndexNo-1 WHERE IndexNo>={} ".format(d))

def len_modify():
    L.execute('Select count(*) from CAFE_MENU')
    c=L.fetchone()[0]
    inc=int(input("ENTER NUMBER OF ITEMS TO BE ADDED: "))
    for i in range(inc):
        n=input("ENTER NAME: ")
        P=int(input("ENTER PRICE: "))
        L.execute('INSERT INTO CAFE_MENU VALUES({},"{}",{})'.format(c+1,n,P))
        c+=1

def spec_update():
    L.execute("SELECT * FROM CAFE_MENU")
    ch='Y'
    while(ch=='Y'):
        change_name=input("ENTER NAME OF ITEM TO CHANGE PRICE: ")
        change_amount=int(input("ENTER NEW PRICE: "))
        L.execute('UPDATE CAFE_MENU SET PRICE={} WHERE NAME="{}"'.format(change_amount,change_name))
        ch=input("DO YOU WANT TO CONTINUE?(Y,N) :").upper()

