from .models import teacherDetail
from .database import teacher_detail_table

class TeacherDetails:
    def create_teacher_detail(self, teacher_detail: teacherDetail) -> dict:
        data = teacher_detail_table.create(teacher_detail.dict())
        teacher_detail_table.save()
        return data
    
    def read_teacher_detail(self, query: dict) -> list:
        data = teacher_detail_table.read(query)
        return data
    
    def update_teacher_detail(self, query: dict, data: dict) -> dict:
        teacher_detail_table.update(query, data)
        teacher_detail_table.save()
        return self.read_teacher_detail(query)
        
    def delete_teacher_detail(self, query: dict) -> None:
        teacher_detail_table.delete(query)
        teacher_detail_table.save()
        
    def count_teacher_detail(self, query: dict = {}) -> int:
        return teacher_detail_table.count(query)
    
    
    