from datetime import datetime

import fastapi
from Note import Note
from ResponseModel import NotesTextResponse, NoteInfoResponse, GetNotesList, CreateNoteResponse, CountLettersResponse

api_router = fastapi.APIRouter()


# Обрати внимание на @api_router.get <- get - тип HTTP метода!
# Для того, чтобы создать put метод, необходимо написать @api_router.put
# /sum - url относительно сервера, по которму будет доступен метод.
# Обрати внимание на response_model <- описывает схему ответа сервера.
# В данном случае ответ сервера = число
@api_router.get("/sum", response_model=float)
def sum_(a: float, b: float):
    """
    Метод выполняет сложение 2х чисел (integer или float) и возвращает результат
    """
    return a + b


# Обрати внимание на response_model <- описывает схему ответа сервера
@api_router.get("/count_letters", response_model=CountLettersResponse)
def count_letters(text: str):
    """
    Метод выполняет выполняет подсчет количества букв в тексте и
    возвращает результат в виде словаря, состоящего из пар: буква и кол-во.
    Также этот метод возвращает дату и время по местному часовому поясу,
    когда был произведен подсчет.
    """
    letters_count = {}
    for letter in text:
        if letter in letters_count:
            letters_count[letter] += 1
        else:
            letters_count[letter] = 1
    return CountLettersResponse(
        counted_at=datetime.datetime.now(),
        counters=letters_count
    )


@api_router.get('/{token}/noteInfo', response_model=NoteInfoResponse)
def noteInfo(token, id: int):
    """
    Метод возвращает время создания заметки и ее последнего изменения по её ID
    """
    note = Note.readById(id)
    return NoteInfoResponse(
        created_at=note.created_at,
        updated_at=note.updated_at
    )

@api_router.post('/{token}/createNote', response_model=CreateNoteResponse)
def createNote(token, id: int):
    if not Note.getTokenList().__contains__(str(token)) or Note.idIsExist(id):
        CreateNoteResponse(
            id=-1
        )
    note = Note.createNote(id)
    return CreateNoteResponse(
        id=note.id
    )

@api_router.patch('/{token}/editNote', response_model=NotesTextResponse)
def editNote(token: str, id: int, text: str):
    if not Note.getTokenList().__contains__(str(token)):
        return NotesTextResponse(id=-1, text='')
    note = Note.readById(id)
    note.text = text
    return NotesTextResponse(id=note.id, text=note.text)

@api_router.post('/{token}/deleteNote', response_model=CreateNoteResponse)
def deleteNote(token, id: int):
    if not Note.getTokenList().__contains__(str(token)) or Note.idIsExist(id):
        CreateNoteResponse(
            id=-1
        )
    Note.deleteFile(id)
    return CreateNoteResponse(
        id=id
    )


# @api_router.get('/{token}/getNoteList', response_model=GetNotesList)
# def getNoteList(token: str):
#     # if not Note.getTokenList().__contains__(str(token)):
#     #     return GetNotesList(noteList=[])
#     print(Note.getAllNotes())
#     return GetNotesList(notelist=Note.getAllNotes())