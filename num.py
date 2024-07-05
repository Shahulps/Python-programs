n=input("enter the no")
count=0

l=len(n)
for i in n:
   if(i=="0" or  i=="1"):
      count+=1
     # print("count:",count)
if(count==l):
	print("binary")
else:
	print("not binary")
