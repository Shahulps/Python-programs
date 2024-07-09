user_input=input("Enter the temperatures in celcius seperated by space bar")
my_list=user_input.split()
f=32
my_list=[float(element)*1.8+f for element in my_list]
print("the converted temeperatures into farenheit is: \n")
print([print(element) for element in my_list])