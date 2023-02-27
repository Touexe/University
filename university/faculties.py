from .models import faculty
from .database import faculties_table

class Faculties:
    def create_faculty(self, faculty: faculty) -> dict:
        data = faculties_table.create(faculty.dict())
        faculties_table.save()
        return data
    
    def read_faculty(self, query: dict = {}) -> list:
        data = faculties_table.read(query)
        return data
    
    def update_faculty(self, query: dict, data: dict) -> dict:
        faculties_table.update(query, data)
        faculties_table.save()
        return self.read_faculty(query)
        
    def delete_faculty(self, query: dict) -> None:
        faculties_table.delete(query)
        faculties_table.save()
        
    def count_faculty(self, query: dict = {}) -> int:
        return faculties_table.count(query)
    
    