while(1):
# Get the student details from user input
	name = input('Enter student name: ')
	math_marks = int(input('Enter math marks: '))
	english_marks = int(input('Enter english marks: '))
	science_marks = int(input('Enter science marks: '))

# Create a dictionary to store student details
	student = {'name': name, 'subjects': {'math': math_marks, 'english': english_marks, 'science': science_marks}}

# Calculate the average of the 3 subjects
	total_marks = student['subjects']['math'] + student['subjects']['english'] + student['subjects']['science']
	average = total_marks / 3

# Print the student details and average
	print('Student Name:', student['name'])
	print('Total Marks:', total_marks)
	print('Average:', average)
	d=input("do you wanna read more student details Y/N")
	if(d=='N' or d=='n'):
	  break

