from typing import Annotated

from fastapi import Body, FastAPI

from app import api_models
from app.database.db_config import prepare_database

app = FastAPI()


database_result = {"title": "note_1", "content": "note_content", "tags": ["test_1", "test_2"]}
tags_from_db = ["tag1", "tag2", "tag2"]


@app.on_event("startup")
async def startup_event():
    prepare_database()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.put("/create_note/", response_model=api_models.NoteOut)
async def create_note(note: Annotated[api_models.Note, Body(embeded=True)]):
    return note


@app.get("/note/{title}", response_model=api_models.NoteOut)
async def get_note(title: str):
    return database_result


@app.get("/tags/")
async def get_tags() -> set[str]:
    tags = set(tags_from_db)
    return tags
