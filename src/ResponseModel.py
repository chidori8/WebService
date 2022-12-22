from typing import Dict

from pydantic import BaseModel
from datetime import datetime


# Класс, который описывает структуру ответа сервера для метода,
# который подсчитывает символы в строке.
# Данный класс обязательно должен быть наследован от pydantic.BaseModel!
class CountLettersResponse(BaseModel):
    counted_at: datetime
    counters: Dict[str, int]


class NotesTextResponse(BaseModel):
    id: int
    text: str


class NoteInfoResponse(BaseModel):
    created_at: datetime
    updated_at: datetime


class CreateNoteResponse(BaseModel):
    id: int


class GetNotesList(BaseModel):
    listNotes: Dict[int, int]