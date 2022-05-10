from fastapi import APIRouter,HTTPException
from connections import QUIZ_COL
from schema.schema import QUIZ,QUIZES,QUIZ_CREATE
import json 
from bson import ObjectId

router = APIRouter()

# quiz CRUD
@router.post("/create") #CREATE
async def createQuiz(quiz: QUIZ_CREATE):
    error_message = ""
    try:
        post_id = str(QUIZ_COL.insert_one(quiz.dict()).inserted_id) # insert to database
    except Exception as e:
        error_message = str(e) #send error message if fail
    
    return {"created_id": str(post_id),"msg":error_message}

@router.get("/",response_model=QUIZES) #READBULK
async def listQuiz(skip: int = 0, limit: int = 10):
    quiz_obj = QUIZ_COL.find().limit(
        int((skip+1)*limit)
        ) #skip limit -> can be improve with get nth id and then get next limit
    
    quizes = [(QUIZ.parse_obj(x)) for x in quiz_obj][-limit:]
    ret = QUIZES.parse_obj({"quizes": quizes})
    print(ret)
    return ret

@router.get("/{id}",response_model=QUIZ) #READONE
async def listQuiz(id):

    try:
        quiz = QUIZ_COL.find_one({"_id":ObjectId(id)})
    except Exception as e:
        raise HTTPException(status_code=406, detail=str(e))

    return QUIZ.parse_obj(quiz)
