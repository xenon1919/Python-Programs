import re
f1=open('input.txt','r')
f2=open('output.txt','w')
for line in f1:
    list=re.findall('[6-9]\d{9}',line)

for numbers in list:
    f2.write(numbers+'\n')
    print('extract all mobile numbers into output.txt')
    f2.close()
    f1.close()
