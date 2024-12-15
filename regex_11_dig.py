import re
s=input("Enter the expression : ");
m=re.fullmatch("[0]\d{10}",s)
if m!=None:
    print("It is a valid expression")
else:
    print("Invalid expression")