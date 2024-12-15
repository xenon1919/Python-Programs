#To match a character or set of characters at the beginning of a string
import re
result=re.match(r'Python', 'It\'s easy to learn Python. Python also has elegant syntax')
print(result)

#To match a character from anywhere in the given string
if re.search("puppy", "Daisy found a puppy"):
    print("Puppy found")
else:
    print("No puppy")

#To get a list of all matching patterns 
import re
result=re.findall(r'AV','AV Analytics Vidhya AV')
print(result)
