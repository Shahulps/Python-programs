l = []
l = list(map(int,input("enter the numbers:").split()))
n = int(input("Enter the number of times to be shifted:"))
n = n%len(l)
if(n!=0):
    result = l[-n:]+l[:-n]
    print(result)
else:
    print(l)

