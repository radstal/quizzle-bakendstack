from fastapi import FastAPI
from schema.schema import QUESTION,CHOICE,QUIZ
app = FastAPI()
@app.get("/")
async def helloWorld():
    return {"message": "Hello World"}


@app.get("/quiz/create")
async def createQuiz(question: QUESTION):
    return {"message": "created"}



@app.get("/func/populate")
async def populateDB():
    return {"message": "Hello World"}