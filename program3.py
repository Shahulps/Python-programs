s=input("enter the string : ")
n = len(s)
y = ""
for i in range(n-1,-1,-1):
    y=y+s[i]
print(y)