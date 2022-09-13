from unittest import result
from note import Note

class Notebook:
    def __init__(self):
        self.notes = []
    
    def add_note (self, content, *tags):
        note = Note (content, *tags)
        self.notes.append(note)
    
    def edit_content(self, id, new_content):
        for note in self.notes:
            if note.id == id:
                note.content = new_content

    def edit_tags(self, id, *new_tags):
        for note in self.notes:
            if note.id == id:
                note.tags = [*new_tags]

    def search(self, check):
        result = []
        for note in self.notes:
            if note.match(check):
                result.append(note)
        return result
    



#notebook = Notebook()
#notebook.add_note("Hello World", "salute", "hi")
#notebook.add_note("Hello World", "salute", "hi")
#notebook.add_note("Hello World", "salute")
#print(len(notebook.notes))
#print(notebook.notes[0].content)
#notebook.edit_content(1, 'chao')
#print(notebook.notes[0].content)

#notebook.edit_tags(1, 'viernes')
#print(notebook.notes[0].tags)
#print(len(notebook.search('hi')))

