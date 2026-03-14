from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..import schemas, crud



router = APIRouter(
    prefix="/notes",
    tags = ["Notes"]
)


@router.post("/")
def create_note(note:schemas.NoteCreate, db:Session = Depends(get_db)):
    return crud.create_note(db,note)


@router.get("/{note_id}")
def read_note(note_id: int, db:Session = Depends(get_db)):
    note = crud.get_note(db, note_id)

    if not note:
        raise HTTPException(status_code=404, detail="Note not Found")
    
    return note

@router.delete("/{note_id}")
def delete_note(note_id: int , db:Session = Depends(get_db)):

    note = crud.delete_note(db,note_id)

    if not note:
        raise HTTPException(status_code=404, detail="Note not Found")
    
    return {"message":"Note deleted"}