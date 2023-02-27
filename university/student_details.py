from .models import studentDetail
from .database import student_detail_table

class StudentDetails:
    def create_student_detail(self, student_detail: studentDetail) -> dict:
        data = student_detail_table.create(student_detail.dict())
        student_detail_table.save()
        return data
    
    def read_student_detail(self, query: dict) -> list:
        data = student_detail_table.read(query)
        return data
    
    def update_student_detail(self, query: dict, data: dict) -> dict:
        student_detail_table.update(query, data)
        student_detail_table.save()
        return self.read_student_detail(query)
        
    def delete_student_detail(self, query: dict) -> None:     
        student_detail_table.delete(query)
        student_detail_table.save()
        
    def count_student_detail(self, query: dict = {}) -> int:
        return student_detail_table.count(query)
    