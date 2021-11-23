astr=input("enter the string\n")
char=input("enter a charecter \n")
print("given string:\n",astr)
print("given charecter\n",char)
res=0
for i in range(len(astr)):
    if(astr[i]==char):
        res=res+1
print("no. of times charecter prsent in word is :",res)