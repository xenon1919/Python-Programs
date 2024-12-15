import re
e=input("Enter your E-mail address : ")
m=re.match("^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-z]{1,3}$",e)
if m!=None:
    print("It is a valid E-mail address")
else:
    print("It is an invalid E-Mail address")