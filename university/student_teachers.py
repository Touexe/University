from .models import  studentTeacher
from .database import student_teacher_table

class StudentTeachers:
    def create_student_teacher(self, student_teacher: studentTeacher) -> dict:
        data = student_teacher_table.create(student_teacher.dict())
        student_teacher_table.save()
        return data
    
    def read_student_teacher(self, query: dict) -> list:
        data = student_teacher_table.read(query)
        return data
    
    def update_student_teacher(self, query: dict, data: dict) -> dict:
        student_teacher_table.update(query, data)
        student_teacher_table.save()
        return self.read_student_teacher(query)
        
    def delete_student_teacher(self, query: dict) -> None:
        student_teacher_table.delete(query)
        student_teacher_table.save()
        
    def count_student_teacher(self, query: dict = {}) -> int:
        return student_teacher_table.count(query)
    
    