class Student:
    def __init__(self, roll_no, name, cgpa):
        self.roll_no = roll_no
        self.name = name
        self.cgpa = cgpa

def read_data(filename):
    students = []
    file=open(filename, 'r')
    for line in file:
        roll_no, name, cgpa = line.strip().split(',')
        student = Student(roll_no, name, float(cgpa))
        students.append(student)
    return students
    file.close()
    
def update_student(students, roll_no, new_name, new_cgpa):
    for student in students:
        if student.roll_no == roll_no:
            student.name = new_name
            student.cgpa = new_cgpa
            break

def save_data(students, filename):
    file=open(filename, 'w') 
    for student in students:
        file.write(f"{student.roll_no},{student.name},{student.cgpa}\n")
    file.close()
     
filename = 'student.txt'
students = read_data(filename)
update_student(students, '94', 'nandini', 7.9)
save_data(students, filename)
