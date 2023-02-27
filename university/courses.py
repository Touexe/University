from .models import course
from .database import courses_table

class Courses:
    def create_course(self, course: course) -> dict:
        data = courses_table.create(course.dict())
        courses_table.save()
        return data
    
    def read_course(self, query: dict = {}) -> list:
        data = courses_table.read(query)
        return data
    
    def update_course(self, query: dict, data: dict) -> dict:
        courses_table.update(query, data)
        courses_table.save()
        return self.read_course(query)
        
    def delete_course(self, query: dict) -> None:
        courses_table.delete(query)
        courses_table.save()
        
    def count_course(self, query: dict = {}) -> int:
        return courses_table.count(query)
    