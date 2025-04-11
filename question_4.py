class Student:
    def __init__(self,studnt_id,name,department,is_enrolled):
        self.studnt_id = studnt_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled

        
    def enroll_student(self):
        if not self.is_enrolled:
            self.is_enrolled = True
            return f'{self.name} is enrolled'
        else :
            return f'{self.name} is already enrolled'
            
class StudentDatabase:

    student_list = []
    
    @classmethod
    def add_student(cls,student):
        cls.student_list.append(student)
    
        
#asif = Student(1,'asif','non-cse',True)
#print(asif.enroll_student())
    
