counter = 0
class Note:
    def __init__(self, content, *tags):
        self.content = content
        self.tags = [*tags]
        global counter
        counter+=1
        self.id = counter

    def match(self, check):
        if check in self.content:
            return True
        elif check in self.tags:
            return True
        else:
            return False

#note_one = Note('hola mundo', 'Saludos', 'Chao')
#print(note_one.match('Chao'))



#note_one = Note('Hola mundo')
#print(note_one.content)
#print(note_one.tags)
#print(note_one.id)

#note_two = Note('1 Tag', 'salute', 'hola', 'chao')
#print(note_two.tags)
#print(note_two.id)


