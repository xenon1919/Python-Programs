import re
s=input("Enter an expression : ")
m=re.fullmatch("[9][1]\d{10}",s)
if m!=None:
    print("It is a valid expression")
else:
    print("It is not a valid expression")