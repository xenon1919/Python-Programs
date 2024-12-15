a= int(input("Enter 3-digit number : "))
 
sum = 0
temp = a
#Define a function
while temp > 0:
    digit = temp % 10
    sum += digit * digit * digit
    temp = temp//10
 
if sum==a:
    print('It is an Armstrong number')
else:
    print('It is not an Armstrong number')
 