# Create an empty dictionary stud
stud = {}

# Add details of 5 students from your class students list starting from your roll number
class_students = ['niki', 'alan', 'lisa', 'sony', 'ananya']
my_roll_number = 16
for i in range(my_roll_number, my_roll_number+5):
    stud[i] = class_students[i-my_roll_number]

# Sort and print the list in the order of rno (Convert dictionary stud into a list)
sorted_stud = sorted(stud.items())
print("Student List sorted by roll number:")
for rno, name in sorted_stud:
    print("Roll No: {} Name: {}".format(rno, name))

# Print the student list in the order of name (use lambda function)
sorted_by_name = sorted(stud.items(), key=lambda x: x[1])
print("Student List sorted by name:")
for rno, name in sorted_by_name:
    print("Name: {} Roll No: {}".format(name, rno))

# Create another dictionary stud1 with rno, name, mark (rno as key)
stud1 = {1: ['John', 80], 2: ['Mike', 65], 3: ['Jane', 50], 4: ['Mary', 75], 5: ['David', 90]}

# Print the details of the student (rno, name, mark) having highest mark
highest_mark = max(stud1.items(), key=lambda x: x[1][1])
print("Student with highest mark:")
print("Roll No: {} Name: {} Mark: {}".format(highest_mark[0], highest_mark[1][0], highest_mark[1][1]))

# Read a rno and delete that student's details from the dictionary
rno_to_delete = int(input("Enter Roll No to delete: "))
if rno_to_delete in stud:
    del stud[rno_to_delete]
    print("Roll No {} deleted successfully.".format(rno_to_delete))
else:
    print("Roll No {} not found in dictionary.".format(rno_to_delete))

# Print the list of passed students (mark >= 50, assume marks out of 100)
print("List of passed students:")
for rno, details in stud1.items():
    if details[1] >= 50:
        print("Roll No: {} Name: {} Mark: {}".format(rno, details[0], details[1]))
