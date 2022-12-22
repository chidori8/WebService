from datetime import datetime
import json
from pydantic import BaseModel
import os
from typing import Dict


# info:
class Note:
    path = 'notes/'
    pathAllNotes = 'notes/id.txt'
    pathToken = 'notes/tokens.txt'
    id: int
    text: str
    created_at: datetime
    updated_at: datetime

    def __init__(self, id: int, text: str, created_at: datetime, updated_at: datetime):
        self.id = id
        self.text = text
        self.created_at = created_at
        self.updated_at = updated_at

    def saveFile(self):
        with open(self.path + str(self.id) + '.txt', 'w') as outfile:
            json.dump(self.getData(), outfile)
            self.updateNotes(self.id)

    def readFile(self):
        filename = self.path + str(self.id) + '.txt'
        try:
            with open(filename) as jsonFile:
                data = json.load(jsonFile)
            print(data)
            return data
        except FileNotFoundError:
            print(filename + ' not found')
            return {}

    @staticmethod
    def deleteFile(id: int):
        try:
            os.remove(Note.path + str(id) + '.txt')
            f = open(Note.pathAllNotes, 'r+')
            notes = f.read().split('\n')
            notes.remove(str(id))
            notes.remove('')
            for value in notes:
                f.write(str(value) + '\n')
        except FileNotFoundError:
            print('File not found')

    @staticmethod
    def createNote(id: int):
        self = Note(id, "", datetime.now(), datetime.now())
        self.saveFile()
        return self

    def editNote(self, newText: str):
        self.text = newText
        try:
            with open(self.path + str(self.id) + '.txt', 'w') as outfile:
                self.updated_at = datetime.now()
                json.dump(self.getData(), outfile)
            return True
        except FileNotFoundError:
            print('File not found')
            return False

    @staticmethod
    def readById(id: int):
        note = Note(id, None, None, None)
        note.id = id
        try:
            note.setData(note.readFile())
        except ValueError:
            note = Note(-1, 'ValueError', 'ValueError', datetime.min, datetime.max)
        return note

    def getData(self):
        data = {
            'id': self.id,
            'text': self.text,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)
        }
        return data

    def setData(self, data: dict):
        if data == {}:
            return ValueError
        self.id = data.get('id')
        self.text = data.get('text')
        self.created_at = datetime.strptime(data.get('created_at'), '%Y-%m-%d %H:%M:%S.%f')
        self.updated_at = datetime.strptime(data.get('updated_at'), '%Y-%m-%d %H:%M:%S.%f')

    @staticmethod
    def getAllNotes():
        try:
            f = open(Note.pathAllNotes, 'r')
            notes = f.read().split('\n')
            notes.remove('')
            n = list(set(notes))
            d = {}
            count = 0
            for item in n:
                d.update([(int(count), int(item))])
                count += 1
            return d
        except FileNotFoundError:
            return []

    @staticmethod
    def updateNotes(id: int):
        try:
            f = open(Note.pathAllNotes, 'a+')
            f.write(str(id) + '\n')
            Note.clearIds()
        except FileNotFoundError:
            f = open(Note.pathAllNotes, 'w')
            f.write(str(id) + '\n')

    @staticmethod
    def clearIds():
        try:
            f = open(Note.pathAllNotes, 'r')
            n1 = f.read().split('\n')
            n = list(set(n1))
            print(n)
            f = open(Note.pathAllNotes, 'w')
            n.remove('')
            for item in n:
                f.write(item + '\n')
        except FileNotFoundError:
            f = open(Note.pathAllNotes, 'w')
            f.write(str(id) + '\n')

    @staticmethod
    def getTokenList():
        try:
            with open(Note.pathToken, 'r') as f:
                tokens = f.read().split('\n')
                return tokens
        except FileNotFoundError:
            return []

    @staticmethod
    def idIsExist(id :int):
        return Note.getAllNotes().__contains__(id)