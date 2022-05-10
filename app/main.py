from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

# from connections import QUIZ_COL
# from schema.schema import QUIZ
from routers import quiz,utilities
from fastapi.responses import HTMLResponse
# from starlette.middleware.sessions import SessionMiddleware

# login block


# app

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]
app = FastAPI(middleware=middleware)

origins = ["*"]

app.include_router(
    quiz.router,
    tags=["quiz"],
    prefix="/quiz",
    )
app.include_router(
    utilities.router,
    tags=["utilities"],
    prefix="/util",
    )


@app.get("/",response_class=HTMLResponse)
async def helloWorld():
    return "<a href=\"./docs\"> go to docs</a>"

