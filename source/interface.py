from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk
from models import *
import os

class Gui(ThemedTk):
    def __init__(self):
        ThemedTk.__init__(self, theme = 'arc')
        self.geometry('1024x768')
        self.title('Notepad')
        self.padding = 5

        self._frame = None
        self.switch_frame(IndexPage)

    def switch_frame(self, frame_class, note = None):
        new_frame = frame_class(self, note)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill = BOTH, expand = True)


class IndexPage(Frame):
    def __init__(self, master, note = None):

        collection = Note.collection()
        collection_texts = list(map(lambda x: x.entry_text(), collection))
        self.collection_dict = { collection_texts[i]: collection[i] for i in range(0, len(collection)) }

        entry_texts = StringVar(value = collection_texts)

        Frame.__init__(self, master)
        frame = Frame(self)
        frame.pack(fill = X)

        title_frame = Frame(frame)
        title_frame.pack(fill = X, padx = master.padding, pady = master.padding)
        title_label = Label(title_frame, text = 'Notepad', font = ("Courier", 44))
        title_label.pack(side = TOP, padx = master.padding, pady = master.padding)

        create_button_frame = Frame(frame)
        create_button_frame.pack(fill = X, padx = master.padding, pady = master.padding)
        create_button = Button(create_button_frame, text = 'New note', command = lambda: master.switch_frame(NoteFormPage), width = 10)
        create_button.pack(side = RIGHT)

        objects_frame = Frame(frame)
        objects_frame.pack(fill = X, padx = master.padding, pady = master.padding)

        self.listbox = Listbox(frame, listvariable = entry_texts, selectmode = SINGLE)
        self.listbox.pack(fill = X, padx = master.padding, pady = master.padding)
        self.listbox.selection_set(0)

        # Actions
        actions_frame = Frame(self)
        actions_frame.pack(fill = X, anchor = S, pady = master.padding)

        exit_button = Button(actions_frame, text = 'Exit', command = self.quit)
        exit_button.pack(side = RIGHT, padx = master.padding, pady = master.padding)
        view_button = Button(actions_frame, text = 'View note', command = lambda: self.view_note(master))
        view_button.pack(side = RIGHT, padx = master.padding, pady = master.padding)


    def view_note(self, master):
        index = int(self.listbox.curselection()[0])
        key = self.listbox.get(index)
        note = self.collection_dict[key]
        master.switch_frame(NoteShowPage, note)
    

class NoteFormPage(Frame):
    def __init__(self, master, note = None):
        Frame.__init__(self, master)
        Title = StringVar()

        # Title
        title_frame = Frame(self)
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

        back_button = Button(actions_frame, text = 'Back', command = lambda: master.switch_frame(IndexPage))
        back_button.pack(side = RIGHT, padx = master.padding, pady = master.padding)

        save_button = Button(actions_frame, text = "Save", command = lambda: save_note(Title.get(), description_field.get('1.0', 'end-1c')) )
        save_button.pack(side = RIGHT, padx = master.padding, pady = master.padding)

class NoteShowPage(Frame):
    def __init__(self, master, note):
        Frame.__init__(self, master)

        # Id:
        id_frame = Frame(self)
        id_frame.pack(fill = X)

        id_label = Label(id_frame, text = 'ID:', width = 10, font = '-weight bold')
        id_text = Entry(id_frame)
        id_text.insert(END, note.id)
        id_text.config(state = DISABLED, foreground = '#595959')
        id_label.pack(side = LEFT, padx = master.padding, pady = master.padding)
        id_text.pack(fill = X, padx = master.padding, pady = master.padding)

        # Title:
        title_frame = Frame(self)
        title_frame.pack(fill = X)

        title_label = Label(title_frame, text = 'Title:', width = 10, font = '-weight bold')
        title_text = Entry(title_frame)
        title_text.insert(END, note.title)
        title_text.config(state = DISABLED, foreground = '#595959')
        title_label.pack(side = LEFT, padx = master.padding, pady = master.padding)
        title_text.pack(fill = X, padx = master.padding, pady = master.padding)

        # Date
        date_frame = Frame(self)
        date_frame.pack(fill = X)

        date_label = Label(date_frame, text = 'Date:', width = 10, font = '-weight bold')
        date_text = Entry(date_frame)
        date_text.insert(END, note.date)
        date_text.config(state = DISABLED, foreground = '#595959')
        date_label.pack(side = LEFT, padx = master.padding, pady = master.padding)
        date_text.pack(fill = X, padx = master.padding, pady = master.padding)

        # Description
        description_frame = Frame(self)
        description_text_frame = Frame(self)
        description_frame.pack(fill = X)
        description_text_frame.pack(fill = BOTH)

        description_label = Label(description_frame, text = 'Description:', width = 10, font = '-weight bold')
        description_text = Text(description_text_frame)
        description_text.insert(END, note.description)
        description_text.config(state = DISABLED, foreground = '#595959')
        description_label.pack(side = LEFT, padx = master.padding, pady = master.padding)
        description_text.pack(fill = BOTH, padx = master.padding, pady = master.padding, expand = True)

        # Actions
        actions_frame = Frame(self)
        actions_frame.pack(fill = X, anchor = S, pady = master.padding)

        back_button = Button(actions_frame, text = 'Back', command = lambda: master.switch_frame(IndexPage))
        back_button.pack(side = RIGHT, padx = master.padding, pady = master.padding)

def save_note(title, description):
    new_note = Note({ 'title': title, 'description': description })
    new_note.save()

def main():
    prog = Gui()
    prog.mainloop()

if __name__ == '__main__':
    main()
