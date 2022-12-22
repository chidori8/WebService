from ResponseModel import CountLettersResponse
from datetime import datetime
from ResponseModel import NotesTextResponse, NoteInfoResponse, GetNotesList, CreateNoteResponse
from Note import Note

if __name__ == '__main__':
    # Данный код демонстрирует процесс создания экземпляра модели и
    # заполнения его данными, а также преобразование в json.
    # Будет полезен при разработке собственной модели ответа.
    # responseText = NotesTextResponse(
    #     id=55,
    #     text="lalalalalalala"
    # )
    # print(responseText.json())
    #
    # responseInfo = NoteInfoResponse(
    #     created_at=datetime.now(),
    #     updated_at=datetime.now()
    # )
    # print(responseInfo.json())
    #
    # responseList = GetNotesList(
    #     listNotes={
    #         0: 555,
    #         1: 65,
    #         2: 3
    #     }
    # )
    # print(responseList.json())
    #
    # responseCreate = CreateNoteResponse(
    #     id=20
    # )
    # print(responseCreate.json())

    note = Note(55, "text", datetime.now(), datetime.now())
    note.saveFile()
    note.readFile()
    # note = Note.readById(note, 5)
    a = Note.readById(55)
    if (a == ValueError):
        print(a.created_at)
    else:
        print(a.created_at)
    print("createNote")
    print(note.createNote(2))
    print(note.createNote(55))
    print(Note.getAllNotes())