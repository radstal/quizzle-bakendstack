from fastapi import APIRouter
from connections import QUIZ_COL
from schema.schema import QUIZ,QUIZES
import json 
from bson import ObjectId

router = APIRouter()

# quiz CRUD
@router.post("/create") #CREATE
async def createQuiz(quiz: QUIZ):
    try:
        # quiz_obj = QUIZ.parse_obj(quiz) # parse with pydantic to check for dtype mismatch
        post_id = str(QUIZ_COL.insert_one(quiz.dict()).inserted_id) # insert to database
    except Exception as e:
        error_message = str(e) #send error message if fail
    
    return {"created_id": str(post_id),"msg":error_message}

@router.get("/",response_model=QUIZES) #READBULK
async def listQuiz():
    quizes = [(QUIZ.parse_obj(x)) for x in QUIZ_COL.find().limit(5)]
    ret = QUIZES.parse_obj({"quizes": quizes})
    print(ret)
    return ret

@router.get("/{id}",response_model=QUIZ) #READONE
async def listQuiz(id):

    quiz = QUIZ_COL.find_one({"_id":ObjectId(id)})
    return QUIZ.parse_obj(quiz)
