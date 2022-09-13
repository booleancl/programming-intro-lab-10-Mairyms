from tabnanny import check
from notebook import Notebook
import sys

class Menu:
    def __init__(self):
        self.notebook = Notebook()
    
    def printMenu(self):
        print(""" 
            Bienvenido a la aplicación de notas
            Menú:
            1. Ver todas las Notas
            2. Agregar Nota
            3. Modificar Nota
            4. Buscar Nota
            5.Salir
            Ver todas las notas
            """)
    def start(self):
        while True:
            self.printMenu()
            save = input('Ingrese su Opcción: ')
            if save == "1":
                self.showNote()
            elif save == "2":
                self.addNote()
            elif save == "3":
                self.editNote()
            elif save == "4":
                self.searchNote()
            elif save == "5":
                sys.exit(0)
            
    def showNote(self):
        if self.notebook.notes ==[]:
            print('el notebook esta vacio')
        for note in self.notebook.notes:
            print(note.id, note.content, note.tags)

    def addNote(self):
        content = input('Ingrese su el contenido de la Nota: ')
        tags = input('Ingrese los Tgas: ').split(' ')
        self.notebook.add_note(content, *tags)
        print('Nota agregada.')
    
    def editNote(self):
        id = int(input ('Ingrese el id de la nota a editar: '))
        content = input('Ingrese su el contenido de la Nota: ')
        tags = input('Ingrese los Tgas: ').split(' ')
        if content:
            self.notebook.edit_content(id, content)
        if tags:
            self.notebook.edit_tags(id, *tags)

    def searchNote(self):
        check = input ('Ingrese el termino de busqueda')
        result = self.notebook.search(check)
        for note in result:
            print(note.id, note.content, note.tags)
        


                
menu = Menu()
menu.start()
