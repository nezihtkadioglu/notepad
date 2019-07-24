from datetime import date
import random
import json
import os

class Note:

    def __init__(self, params):
        self.title = params['title']
        self.description = params['description']
        if 'id' in params:
            self.id = params['id']
        else:
            self.id = int(random.random()*10000000)
        if 'date' in params:
            self.date = params['date']
        else:
            self.date = date.today().strftime("%d/%m/%Y")

    def save(self):
        self.save_json()
        # save_md()

    def save_json(self):
        with open('./data/'+ str(self.id) + '.json', 'w+') as f:
            json.dump(self.__dict__, f, indent = 2)

    def delete(self):
        delete_local()
        delete_md()

    def entry_text(self):
        return "#{}: {}".format(str(self.id), self.title)

    def collection():
        directory = 'data'
        collection = []
        for filename in os.listdir(directory):
            if filename.endswith('.json'):
                with open('./' +  directory + '/' + filename) as f:
                    collection.append(Note(json.load(f)))
        return collection

    def where(args):
        if type(args) != dict:
          raise 'where arguments should be given in a dictionary'

        where_result = []
        for note in Note.collection():
            validations = 0
            for key in args:
                if getattr(note, key) == args[key]:
                    validations += 1
            if validations == len(args):
                where_result.append(note)
        return where_result

    def find(_id):
        if type(_id) != int:
            raise 'find argument should be an integer'

        find_in_array = Note.where({ 'id': _id })
        if find_in_array == []:
            raise 'could not find Note object with id {}'.format(_id)

        return find_in_array[0]

