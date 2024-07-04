#op=int(input("choose an option from the list "))
arr=[]
def delloc():
 po=int(input("enter the location where you wanna delete"))
 arr.pop(po)
 print("Array after deleting from",po,":",arr)
def delend():
 arr.pop()
 print("ARRAY AFTER DELETING ",arr)
def insrtloc():
 pos=int(input("enter the positipn where you want to insert "))
 n=int(input("enter the element to be inserted"))
 arr.insert(pos,n)
 print("Array after inserting",arr)


def endofa():
 num=int(input("Enter a number to insert in array at end :"))
# adding element at the end of the array(list)
 arr.append(num)
 print("Array after inserting",num,"at end",arr)
while(True):
 print("\t1>nsert an element at end of Array")
 print("\t2>Insert an element at a given location n Array")
 print("\t3> Delete element at end of Array")
 print("\t4>Delete element from array at given index")
 print("\t5>EXIT")
 op=int(input("choose an option from the list above"))
 if(op==1):
   endofa()
 elif(op==2):
   insrtloc()
 elif(op==3):
   delend()
 elif(op==4):
   delloc()
 else:
   break

