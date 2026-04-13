my_student_mark_list = [] 
print("Student Mark input:")
for i in range(5): print('--'*i , end="")
print()
n = int(input("How many student mark do you want to input: "))
for x in range(n):
	roll = int(input("Student Roll: "))
	mark = int(input("Mark: "))
	my_student_mark_list.insert(roll+1, mark)

print(my_student_mark_list)

