class Student:
    def __init__(self,studnt_id,name,department,is_enrolled):
        self.studnt_id = studnt_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled
        

class StudentDatabase:

    student_list = []
    
    @classmethod
    def add_student(cls,student):
        cls.student_list.append(student)
    
        
asif = Student(1,'asif','non-cse',True)
StudentDatabase.add_student(asif)

for student in StudentDatabase.student_list:
    print(f'{asif.studnt_id} {asif.name} {asif.department} {asif.is_enrolled}')
