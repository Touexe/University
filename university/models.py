from typing import Optional
import dataclasses

def get_column_names(model : object):
    return [field.name for field in dataclasses.fields(model)]

@dataclasses.dataclass
class BaseModel:
    def dict(self):
        return dataclasses.asdict(self)

@dataclasses.dataclass
class faculty(BaseModel):
    id : Optional[int] = None
    name : str = ""
    dean_name : str = ""
    office_no : int  = 0

@dataclasses.dataclass
class department(BaseModel):
    id: Optional[int] = None
    name: str = ""
    head_name: str = ""
    office_no: str = ""
    faculty_id: Optional[int] = None

@dataclasses.dataclass
class student(BaseModel):
    id: Optional[int] = None
    name: str = ""
    gender: str = ""
    dob: str = ""
    phone_no: str = ""
    address: str = ""
    year: str = ""
    generation: str = ""
    degree: str = ""

@dataclasses.dataclass
class studentDetail(BaseModel):
    student_id: Optional[int] = None
    dept_id: Optional[int] = None
    enrolled_date: str = ""

@dataclasses.dataclass
class teacher(BaseModel):
    id: Optional[int] = None
    name: str = ""
    gender: str = ""
    dob: str = ""
    phone_no: str = ""
    address: str = ""

@dataclasses.dataclass
class teacherDetail(BaseModel):
    teacher_id: Optional[int] = None
    dept_id: Optional[int] = None

@dataclasses.dataclass
class studentTeacher(BaseModel):
    student_id: Optional[int] = None
    teacher_id: Optional[int] = None

@dataclasses.dataclass
class course(BaseModel):
    id: Optional[int] = None
    name: str = ""
    credit: str = ""
    type: str = ""
    dept_id: Optional[int] = None

class courseDetail(BaseModel):
    course_id: Optional[int] = None
    student_id: Optional[int] = None
    score: str = ""
    grade: str = ""

class account(BaseModel):
    id: Optional[int] = None
    username: str = ""
    password: str = ""
    phone_no: str = ""
    role: str = ""
    user_id: Optional[int] = None

class teacherCourse(BaseModel):
    teacher_id: Optional[int] = None
    course_id: Optional[int] = None
    
    
    
    
