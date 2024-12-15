math=float(input("Enter the marks of Mathematics :"))
phy=float(input("Enter the marks of Physics :"))
chem=float(input("Enter the marks of Chemistry "))
bio=float(input("Enter the marks of Biology :"))
eng=float(input("Enter the marks of English :"))
cs=float(input("Enter the marks of Computer Science :"))
total_marks=math+phy+chem+bio+eng+cs
avg=total_marks/6
percentage=(total_marks/600)*100
print("Total marks secured =",total_marks)
print("Average marks =",avg)
print("Percentage =",percentage)
if total_marks>=501 and total_marks<=600:
    print("Excellent, you have scored A grade")
elif total_marks>=401 and total_marks<501:
    print("Good, you have scored B grade")
elif total_marks>=301 and total_marks<401:
    print("Can do better, you have scored C grade")
elif total_marks>=201 and total_marks<301:
    print("Fair, you have scored D grade")
elif total_marks>=180 and total_marks<201:
    print("Need to work very hard, you have scored E grade")
else:
    print("You have got F grade, better luck next time")
