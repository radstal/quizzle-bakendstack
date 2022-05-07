
from pydantic import BaseModel, validator,Field as PydanticField

from typing import Optional,List
from datetime import datetime

from bson import ObjectId
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")



class CHOICE(BaseModel):
    text: str
    correct: bool
class QUESTION(BaseModel):
    question: str
    choices: List[CHOICE]
    order: int
    time: int = 60 # seconds
    multipleanswer: bool = False

class QUIZ(BaseModel):
    id: PyObjectId = PydanticField(default_factory=PyObjectId, alias="_id")
    author: str
    questions: List[QUESTION]
    created_at: datetime = None #auto update creation time
    last_modified: datetime = None #auto update update time

    @validator('created_at', pre=True, always=True)
    def default_ts_created(cls, v):
        return v or datetime.utcnow()
    @validator('last_modified', pre=True, always=True)
    def default_ts_modified(cls, v, *, values, **kwargs):
        return v or values['created_at']
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True #required for the _id 
        json_encoders = {ObjectId: str}

class QUIZES(BaseModel):
    quizes: List[QUIZ]


