counter = 0
class Note:
    def __init__(self, content, *tags):
        self.content = content
        self.tags = [*tags]
        global counter
        counter+=1
        self.id = counter

note_one = Note('Hola mundo')
print(note_one.content)
print(note_one.tags)
print(note_one.id)

note_two = Note('1 Tag', 'salute', 'hola', 'chao')
print(note_two.tags)
print(note_two.id)


