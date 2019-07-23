from tkinter import *
from tkinter.ttk import *
from models import *
import os

class Gui(Frame):

  def __init__(self):
    super().__init__()
    self.initUi()

  def initUi(self):

    padding = 5
    Title = StringVar() 

    self.style = Style()
    self.style.theme_use('clam')
    self.master.title('Notepad')
    self.pack(fill = BOTH, expand = True)

    # Title
    title_frame = Frame(self)
    title_frame.pack(fill = X)

    title_label_frame = Frame(title_frame)
    title_label_frame.pack(fill = X, padx = padding, pady = padding)
    title_label = Label(title_label_frame, text = 'Title:')
    title_label.pack(side = LEFT)

    title_field_frame = Frame(title_frame)
    title_field_frame.pack(fill = X, padx = padding)
    title_field = Entry(title_field_frame, textvariable = Title)
    title_field.pack(fill = X)

    # Description
    description_frame = Frame(self)
    description_frame.pack(fill = X)

    description_label_frame = Frame(description_frame)
    description_label_frame.pack(fill = X, padx = padding, pady = padding)
    description_label = Label(description_label_frame, text = 'Description:')
    description_label.pack(side = LEFT)

    description_field_frame = Frame(description_frame)
    description_field_frame.pack(fill = X, padx = padding)
    description_field = Text(description_field_frame)
    description_field.pack(fill = X)

    # Actions
    actions_frame = Frame(self)
    actions_frame.pack(fill = X, anchor = S, pady = padding)

    exit_button = Button(actions_frame, text = "Exit", command = self.quit)
    exit_button.pack(side = RIGHT, padx = padding, pady = padding)

    save_button = Button(actions_frame, text = "Save", command = lambda: save_note(Title.get(), description_field.get('1.0', 'end-1c')) )
    save_button.pack(side = RIGHT, padx = padding, pady = padding)

def save_note(title, description):
  new_note = Note({ 'title': title, 'description': description })
  new_note.save()

def main():
  root = Tk()
  root.geometry('1024x768+300+300')
  prog = Gui()
  root.mainloop()

if __name__ == '__main__':
  main()
