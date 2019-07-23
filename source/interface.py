from tkinter import *
from tkinter.ttk import *
from models import *
import os

class Gui(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('1024x768')
        self.style = Style()
        self.style.theme_use('clam')
        self.title('Notepad')
        self.padding = 5

        self._frame = None
        self.switch_frame(IndexPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill = BOTH, expand = True)

class IndexPage(Frame):
    def __init__(self, master):
        collection = get_object_collection()
        Frame.__init__(self, master)
        frame = self
        frame.pack(fill = X)

        title_frame = Frame(frame)
        title_frame.pack(fill = X, padx = master.padding, pady = master.padding)
        title_label = Label(title_frame, text = 'Notepad', font = ("Courier", 44))
        title_label.pack(side = TOP, padx = master.padding, pady = master.padding)

        create_button_frame = Frame(frame)
        create_button_frame.pack(fill = X, padx = master.padding, pady = master.padding)
        create_button = Button(create_button_frame, text = 'New note', command = lambda: master.switch_frame(NoteFormPage).pack(), width = 10)
        create_button.pack(side = RIGHT)

        objects_frame = Frame(frame)
        objects_frame.pack(fill = X, padx = master.padding, pady = master.padding)

        listbox = Listbox(frame)
        listbox.pack(fill = X, padx = master.padding, pady = master.padding)

        for obj in collection:
            listbox.insert(END, obj.entry_text())

        # Actions
        actions_frame = Frame(self)
        actions_frame.pack(fill = X, anchor = S, pady = master.padding)

        exit_button = Button(actions_frame, text = 'Exit', command = self.quit)
        exit_button.pack(side = RIGHT, padx = master.padding, pady = master.padding)
    

class NoteFormPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Title = StringVar()

        # Title
        title_frame = self
        title_frame.pack(fill = X)

        title_label_frame = Frame(title_frame)
        title_label_frame.pack(fill = X, padx = master.padding, pady = master.padding)
        title_label = Label(title_label_frame, text = 'Title:')
        title_label.pack(side = LEFT)

        title_field_frame = Frame(title_frame)
        title_field_frame.pack(fill = X, padx = master.padding)
        title_field = Entry(title_field_frame, textvariable = Title)
        title_field.pack(fill = X)

        # Description
        description_frame = Frame(self)
        description_frame.pack(fill = X)

        description_label_frame = Frame(description_frame)
        description_label_frame.pack(fill = X, padx = master.padding, pady = master.padding)
        description_label = Label(description_label_frame, text = 'Description:')
        description_label.pack(side = LEFT)

        description_field_frame = Frame(description_frame)
        description_field_frame.pack(fill = X, padx = master.padding)
        description_field = Text(description_field_frame)
        description_field.pack(fill = X)

        # Actions
        actions_frame = Frame(self)
        actions_frame.pack(fill = X, anchor = S, pady = master.padding)

        back_button = Button(actions_frame, text = 'Back', command = lambda: master.switch_frame(IndexPage).pack())
        back_button.pack(side = RIGHT, padx = master.padding, pady = master.padding)

        save_button = Button(actions_frame, text = "Save", command = lambda: save_note(Title.get(), description_field.get('1.0', 'end-1c')) )
        save_button.pack(side = RIGHT, padx = master.padding, pady = master.padding)

def save_note(title, description):
    new_note = Note({ 'title': title, 'description': description })
    new_note.save()

def get_object_collection():
    directory = 'data'
    collection = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(directory + '/' + filename) as f:
                collection.append(Note(json.load(f)))
    return collection

def main():
    prog = Gui()
    prog.mainloop()

if __name__ == '__main__':
    main()
