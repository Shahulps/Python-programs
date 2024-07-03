sentence = input("Enter the sentence to be written into the file:")
print("number of characters in the string is",len(sentence))
file_name=input("enter the file name :")
file_name=f"{file_name}.txt"
with open(file_name,"w") as f:
    f.write(sentence)
    f.close()
print(f"you have written {len(sentence)} characters into {file_name}")