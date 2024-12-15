import re
s=input("Enter an expression : ")
m=re.fullmatch("[+][9][1]\d{10}",s)
if m!=None:
    print("Valid expression")
else:
    print("Invalid expression")