import Menu as M
M.create()
ch=int(input("ENTER 1 TO DELETE ITEMS\nENTER 2 TO MODIFY LENGTH\nENTER 3 TO UPDATE SPECIFIC PRICE"))
if ch==1:
    M.delete()
elif ch==2:
    M.len_modify()
elif ch==3:
    M.spec_update()
