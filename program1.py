l1=[]
n=int(input("Enter the number of elements in the list :"))
for i in range(n):
    a=int(input(f"Enter the {i+1} number: "))
    l1.append(a)
l1.sort()
max=l1[n-1]
l2=[i for i in range(1,max)]
for i in l2:
    if i not in l1:
        print(i,end=' ')


