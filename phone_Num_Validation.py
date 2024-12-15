import re
n=input("Enter a phone number : ")
r=re.fullmatch('[6-9][0-9]{9}',n)
if r!=None:
    print("Valid phone number")
else:
    print("Invalid phone number")