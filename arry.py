a=[]
n=int(input("enter the size of the array"))
for i in range(n):
	x=input("ENTER THE ELEMENT")
	a.append(x)
print("ORGINAL ELEMENTS:"+str(a));
max=0
re=a[0]
for i in a:
	fr=a.count(i)
	if( fr>max):
		max=fr
		rs=i
print("MOST FREQUENT ELEMENT IS :"+str(rs))

