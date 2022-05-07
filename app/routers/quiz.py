from fastapi import APIRouter
from connections import QUIZ_COL
from schema.schema import QUIZ
import json 

router = APIRouter()

# quiz CRUD
@router.post("/create") #CREATE
async def createQuiz(quiz: QUIZ):
    return {"message": "created"}

@router.get("/") #READBULK
async def listQuiz():
    quizes = [json.loads(QUIZ.parse_obj(x).json()) for x in QUIZ_COL.find().limit(5)]
    return {"quizes": quizes}

@router.get("/{id}") #READONE
async def listQuiz(id):
    quiz = QUIZ_COL.find_one({"_id":id}).json()
    return {"id": id,"quiz":quiz}
