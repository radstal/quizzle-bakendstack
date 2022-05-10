from fastapi import APIRouter
from connections import QUIZ_COL
from schema.schema import QUIZ,QUIZES,QUIZ_CREATE
import json 
from bson import ObjectId

router = APIRouter()
@router.get("/populate")
async def populateDB():

    test_data = {
        "author": "populate",
        "questions": [
            {
            "question": "a",
            "choices": [
                {
                "text": "string",
                "correct": True
                },
                {
                "text": "string",
                "correct": False
                },
                {
                "text": "string",
                "correct": False
                },
                {
                "text": "string",
                "correct": False
                }
            ],
            "order": 0,
            "time": 60,
            "multipleanswer": False
            },
            {
            "question": "b",
            "choices": [
                {
                "text": "string",
                "correct": True
                },
                {
                "text": "string",
                "correct": False
                },
                {
                "text": "string",
                "correct": False
                },
                {
                "text": "string",
                "correct": False
                }
            ],
            "order": 1,
            "time": 60,
            "multipleanswer": False
            }
             
            
            ]
        }
    
    post_id = None
    error_message = None
    try:
        quiz_obj = QUIZ.parse_obj(test_data) # parse with pydantic to check for dtype mismatch
        post_id = str(QUIZ_COL.insert_one(quiz_obj.dict()).inserted_id) # insert to database
    except Exception as e:
        error_message = str(e) #send error message if fail
    
    return {"created_id": str(post_id),"msg":error_message}

