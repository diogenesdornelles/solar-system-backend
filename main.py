"""
Main module
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from modules import get_data
from models.Question import Question
from typing import Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/questions/{name_player}/{difficulty}")
async def get_question(name_player: Optional[str] = None,
                       difficulty: Optional[int] = None) -> JSONResponse:
    response: Question = get_data()
    return JSONResponse(content=response,
                        media_type="application/json; charset=UTF-8")
