a=[]
n=int(input("enter the size of the array"))
for i in range(n):
        x=input("ENTER THE ELEMENT")
        a.append(x)
print("ORGINAL ELEMENTS:"+str(a))
largest = a[0]
lowest = a[0]
largest2 = None
lowest2 = None
for item in a[1:]:
        if item > largest:
            largest2 = largest
            largest = item
        elif largest2 is None or largest2 < item:
            largest2 = item
        if item < lowest:
            lowest2 = lowest
            lowest = item
        elif lowest2 is None or lowest2 > item:
            lowest2 = item
print("Largest element is:", largest)
print("Smallest element is:", lowest)
print("Second Largest element is:", largest2)
print("Second Smallest element is:", lowest2)
