from .models import teacher
from .database import teachers_table

class Teachers:
    def create_teacher(self, teacher: teacher) -> dict:
        data = teachers_table.create(teacher.dict())
        teachers_table.save()
        return data
    
    def read_teacher(self, query: dict = {}) -> list:
        data = teachers_table.read(query)
        return data
    
    def update_teacher(self, query: dict, data: dict) -> dict:
        teachers_table.update(query, data)
        teachers_table.save()
        return self.read_teacher(query)
        
    def delete_teacher(self, query: dict) -> None:
        teachers_table.delete(query)
        teachers_table.save()
        
    def count_teacher(self, query: dict = {}) -> int:
        return teachers_table.count(query)