from datetime import date
import random
import json
import os

class Note:

  def __init__(self, params):
    self.id = int(random.random()*10000000) 
    self.title = params['title']
    self.description = params['description']
    self.date = date.today().strftime("%d/%m/%Y")

  def save(self):
    self.save_json()
    # save_md()

  def save_json(self):
    with open('./data/'+ self.title + '.json', 'w+') as f:
      json.dump(self.__dict__, f, indent = 2)

  def delete(self):
    delete_local()
    delete_md()
