from .models import department
from .database import departments_table

class Departments:
    def create_department(self, department: department) -> dict:
        data = departments_table.create(department.dict())
        departments_table.save()
        return data
    
    def read_department(self, query: dict) -> list:
        data = departments_table.read(query)
        return data
    
    def update_department(self, query: dict, data: dict) -> dict:
        departments_table.update(query, data)
        departments_table.save()
        return self.read_department(query)
        
    def delete_department(self, query: dict) -> None:
        departments_table.delete(query)
        departments_table.save()
        
    def count_department(self, query: dict = {}) -> int:
        return departments_table.count(query)