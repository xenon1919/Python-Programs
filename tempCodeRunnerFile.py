((http|https)://)(www.)?"+"[a-zA-Z0-9@:%._\\+~?&//=]"+"{2,256}\\.[a-z]"+"{2,6}\\b([-a-zA-Z0-9@:%"+"._\\+!?&//=]*)",url)
y=re.compile(x)
if y!=None:
    print("Valid URL")
else:
    print("Invalid URL")