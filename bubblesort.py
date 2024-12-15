def bubble_sort(a):   
    for i in range(0,len(a)-1):  
        for j in range(len(a)-1):  
            if(a[j]>a[j+1]):  
                temp = a[j]  
                a[j] = a[j+1]  
                a[j+1] = temp  
    return a  
a=[]
n=int(input("Enter the number of elements in array:"))
for i in range(0,n):
   l=int(input())
   a.append(l)
print("The unsorted list is: ", a)  
print("The sorted list is: ", bubble_sort(a))  