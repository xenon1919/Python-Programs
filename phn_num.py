import re
f1=open('input.txt','r');
f2=open('output.txt','w');
for l in f1:
    list=re.findall('[6-9]\d{9}',l)
    for num in list:
        f2.write('num+\n')
print("Extracted all mobile numbers into output text")
f1.close()
f2.close()