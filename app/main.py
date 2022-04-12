from fastapi import FastAPI
from schema.schema import QUIZ
from connections import QUIZ_COL
app = FastAPI()
@app.get("/")
async def helloWorld():
    return {"message": "Hello World"}


@app.post("/quiz/create")
async def createQuiz(quiz: QUIZ):
    return {"message": "created"}

@app.get("/quiz/")
async def listQuiz():
    quizes = list(QUIZ_COL.find().limit(5))
    return {"quizes": quizes}
@app.get("/quiz/{id}")
async def listQuiz(id):
    quiz = QUIZ_COL.findOne()
    return {"id": id,"quiz":quiz}

@app.get("/func/populate")
async def populateDB():

    return {"message": "Hello World"}