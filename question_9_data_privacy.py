class Student:
    def __init__(self,studnt_id,name,department,is_enrolled):
        self.__studnt_id = studnt_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        
    def enroll_student(self):
        if not self.__is_enrolled:
            self.__is_enrolled = True
            return f'{self.__name} is enrolled'
        else :
            return f'{self.__name} is already enrolled'
    
    def drop_student(self):
        if self.__is_enrolled == True:
            self.__is_enrolled = False
            return f'{self.__name} is drop out'
        else :
            return f'{self.__name} is already drop out'
        
    def view_student_info(self):
        return f'id : {self.__studnt_id}, Name : {self.__name}, Department : {self.__department}, Status : {self.__is_enrolled}'
        

class StudentDatabase:

    student_list = []
    
    @classmethod
    def add_student(cls,student):
        cls.student_list.append(student)
    
        
asif = Student(1,'asif','non-cse',True)
# print(asif.enroll_student())
# print(asif.drop_student())
# print(asif.drop_student())
print(asif.view_student_info())
#print(asif.name)

    
