from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

pseudo_db = []

class Album(BaseModel):
    title: str
    artist: str
    year: int
    genre: Optional[str] = None

@app.get("/")
def read_root():
    return {"greetings":"Welcome to the Albums API"}

@app.get("/albums")
def get_albums():
    return pseudo_db

@app.get("/albums/{album_id}")
def get_an_album(album_id: int):
    album = album_id - 1
    return pseudo_db[album]

@app.post("/albums")
def add_album(album: Album):
    pseudo_db.append(album.dict())
    return pseudo_db[-1]

@app.delete("/courses/{album_id}")
def delete_album(album_id: int):
    pseudo_db.pop(album_id - 1)
    return {"task": "deletion successful"}