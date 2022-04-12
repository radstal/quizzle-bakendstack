from fastapi import FastAPI
from schema.schema import QUIZ
from connections import QUIZ_COL
import json 
app = FastAPI()
@app.get("/")
async def helloWorld():
    return {"message": "Hello World"}


# quiz CRUD
@app.post("/quiz/create") #CREATE
async def createQuiz(quiz: QUIZ):
    return {"message": "created"}

@app.get("/quiz/") #READBULK
async def listQuiz():
    quizes = [json.loads(QUIZ.parse_obj(x).json()) for x in QUIZ_COL.find().limit(5)]
    return {"quizes": quizes}

@app.get("/quiz/{id}") #READONE
async def listQuiz(id):
    quiz = QUIZ_COL.find_one({"_id":id}).json()
    return {"id": id,"quiz":quiz}

@app.get("/func/populate")
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