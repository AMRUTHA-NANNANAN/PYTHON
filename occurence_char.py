str1=input("enter the string\n")
char=str1[0]
str1=str1.replace(char,"$")
str1=char+str1[1:]
print("replaced string is :",str1)