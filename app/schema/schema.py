
from pydantic import BaseModel, validator

from typing import Optional,List
from datetime import datetime

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