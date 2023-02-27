from .models import student
from .database import students_table

class Students:
    def create_student(self, student: student) -> dict:
        data = students_table.create(student.dict())
        students_table.save()
        return data
    
    def read_student(self, query: dict) -> list:
        data = students_table.read(query)
        return data
    
    def update_student(self, query: dict, data: dict) -> dict:
        students_table.update(query, data)
        students_table.save()
        return self.read_student(query)
        
    def delete_student(self, query: dict) -> None:
        students_table.delete(query)
        students_table.save()
        
    def count_student(self, query: dict) -> int:
        return students_table.count(query)
    