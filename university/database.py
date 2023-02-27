import os
from collections import deque
import csv

from .models import get_column_names
from . import models

data_folder_path = "data"
class Table:
    def __init__(self, db_name : str, columns_names : list):
        self.db_name = db_name
        self.db_file_name = db_name + ".csv"
        self.db_sequence_id_file_name = db_name + "_sequence_id" + ".txt"
        self.db_file_path = data_folder_path + "/" + self.db_file_name
        self.db_sequence_id_file_path = data_folder_path + "/" + self.db_sequence_id_file_name
        self.columns_names = columns_names
        
        self.__create_schema()
        self.__last_sequence_id = 0
        self.__changes = deque()
    
    def __create_schema(self):
        os.makedirs(data_folder_path, exist_ok=True)
        
        if not os.path.exists(self.db_file_path):
            with open(self.db_file_path, 'w') as f:
                writer = csv.DictWriter(f, fieldnames=self.columns_names)
                writer.writeheader()
        
        if not os.path.exists(self.db_sequence_id_file_path):
            with open(self.db_sequence_id_file_path, 'w') as f:
                f.write("0")
        
    def __load_data(self, offset : int = 0, limit : int = 0, all : bool = False):
        rows = []
        with open(data_folder_path + "/" + self.db_file_name, 'r') as f:
            reader = csv.DictReader(f)
            for index, row in enumerate(reader):
                # if we want all the data, continue to append every row
                if all is True:
                    rows.append(row)
                    continue
                
                # if we have offset and we are still in the offset, continue
                if index < offset:
                    continue
                
                # if we have limit and we reached the limit, break out of the loop
                if limit > 0 and (index - offset) >= limit:
                    break
                
                rows.append(row)
                
        return rows   
    
    def __create_change(self, query : dict, action : str, data : dict):
        if action not in ["create", "update", "delete"]:
            raise Exception("Invalid action")
        
        change = {"data" : data, "action" : action, "query" : query}
        self.__changes.append(change)
        
    
    def save(self):
        with open(data_folder_path + "/" + self.db_sequence_id_file_name, 'w') as f:
            f.write(str(self.__last_sequence_id))
        
        rows = self.__load_data(all = True)
        
        for change in self.__changes:
            query = change["query"]
            action = change["action"]
            data = change["data"]
            
            if action == "create":
                rows.append(data)
               
            elif action == "delete":
                for row in rows:
                    for key, value in query.items():
                        if row.get(key) == value:
                            rows.remove(row)
                            break
                        
                    
            elif action == "update":
                for row in rows:
                    for key, value in query.items():
                        if row.get(key) == value:
                            row.update(data)  
                            break
                
                    
        with open(data_folder_path + "/" + self.db_file_name, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=self.columns_names)
            writer.writeheader()
            writer.writerows(rows)
            
        self.__changes.clear()

            
    def create(self, data : dict) -> dict:
        if data.get("id") is not None:
            data.pop("id")
        
        last_id = 0
        with open(data_folder_path + "/" + self.db_sequence_id_file_name, 'r') as f:
            id = f.read()
            if id != "":
                last_id = int(id)
            
        if self.__last_sequence_id == 0:
            self.__last_sequence_id = last_id
        
        incremented_id = self.__last_sequence_id + 1
        data["id"] = incremented_id
        self.__last_sequence_id = incremented_id
        self.__create_change({}, "create", data)
        return data
    
    def read(self, query : dict) -> list:
        result = []
        
        offset = 0
        limit = 10
        while True:
            loaded_data = self.__load_data(offset = offset, limit = limit)
            if len(loaded_data) == 0:
                break
            
            for row in loaded_data:
                for key, value in query.items():
                    if isinstance(value, (int, float)):
                        value = str(value)
                        
                    if row[key] == value:
                        result.append(row)
                    
            offset += limit
        
        return result
        
    def update(self, query : dict, data : dict) -> None:
        query.update(data)
        self.__create_change(query, "update", data)
        
    
    def delete(self, query : dict) -> None:
        self.__create_change(query, "delete", {})
        
    
    def count(self, query : dict) -> int:
        count = 0
        
        offset = 0
        limit = 10
        while True:
            loaded_data = self.__load_data(offset = offset, limit = limit)
            if len(loaded_data) == 0:
                break
            
            
            for row in loaded_data:
                for key, value in query.items():
                    if row[key] == value:
                        count += 1
                    
            offset += limit
            
        return count
            
        

student_detail_table = Table("student_details", columns_names=get_column_names(models.studentDetail))
teacher_detail_table = Table("teacher_details", columns_names= get_column_names(models.teacherDetail))
student_teacher_table = Table("student_teachers", columns_names=get_column_names(models.studentTeacher))
course_detail_table = Table("course_details", columns_names=get_column_names(models.courseDetail))
teacher_course_table = Table("teacher_courses", columns_names=get_column_names(models.teacherCourse))

# student_department_relation_table = student_details_table
# teacher_department_relation_table = teacher_details_table
# student_teacher_relation_table = student_teachers_table
# course_student_relation_table = course_details_table
# course_teacher_relation_table = teacher_courses_table

faculties_table = Table("faculties", columns_names =get_column_names(models.faculty))
departments_table = Table("departments", columns_names = get_column_names(models.department))
courses_table = Table("courses", columns_names = get_column_names(models.course))
teachers_table = Table("teachers", columns_names=get_column_names(models.teacher))
students_table = Table("students", columns_names=get_column_names(models.student))
accounts_table = Table("accounts", columns_names=get_column_names(models.account))

