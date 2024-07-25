N=int(input("enter the number of jars : "))
l=list(map(int,input("enter the  number of chocolates in each jar : ").split()))
sum=0
n=int(input("enter the number of people"))
for i in range(N):
    a=l[i]%n
    if(a==0):
        sum=sum+l[i]//n
    else:
        sum=sum+(l[i]//n)+1
print(sum)