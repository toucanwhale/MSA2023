import student_class
#read file skipping line 1 (intro line):
#with open('students.csv') as f:
    #student_repository = f.readlines()[1:]

student_repository = open("students.csv")

student1 = student_class.Student("Jemuel", "Lee", "Think Like a Programmer", 62, 4.595, 5174)
student2 = student_class.Student("Sean", "Cajigal", "Think Like a Programmer", 65, 1.1, 3200)

student_list = []
student_list.append(student1)
student_list.append(student2)
line=0
for line_of_data in student_repository:
    line += 1
    try:
        keys_values = line_of_data.split(",")
        first_name = keys_values[0]
        last_name = keys_values[1]
        major = keys_values[2]
        credit_hours = int(keys_values[3])
        gpa = keys_values[4]
        id = int(keys_values[5])
        
    except IndexError:
        print(f"There is an error in your data file on the line {line}")
        continue
    except ValueError:
        print(f"There is an error in your data file on the line {line}")
        continue
    student = student_class.Student(first_name, last_name, major, credit_hours, gpa, id)
    student_list.append(student)

for student in student_list:
    student.print_student_data()
    print(student.get_class_level())
