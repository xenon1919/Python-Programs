d1={'ID':'1', 'NAME':'STARK','AGE':'35','CITY':'CALIFORNIA'}
print("\nDictionary is :",d1)
print("\n Name : ",d1['NAME'])
#print("All keys in Dictionary ")
#or x in d1:
  #  print(x)
    #print("\nAll values in Dictionary ")
  #  f#or x in d1:
      #  print(d1[x])
d1["PHNO."]=851
print("\nUpdated Dictinary is : ",d1)
d1.pop("AGE")
print("\nUpdated Dictionary is : ",d1)
print("Length of Dictionary is : ",len(d1))
d2=d1.copy()
print("\nNew Dictionary is : ",d2)
d1.clear()
print("\nUpdated Dictionary is : ",d1)