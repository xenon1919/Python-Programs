a=float(input("Enter the length of adjacent side : "))
b=float(input("Enter the length of opposite side : "))
c=float(input("Enter the length of hypotenuse side : "))
if c**2==((a**2)+(b**2)):
    print("It is a right triangle")
else:
    print("It is not a right triangle")