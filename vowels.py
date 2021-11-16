elem=input("enter the statement :")
vowels=['a','e','i','o','u','A','E','I','O','U']
list1=[]
for x in elem:
    if(x in vowels and x not in list1):
        list1.append(x)
print("vowels in given statment are:",list1)