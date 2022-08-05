
class Things():
    def __init__(self):
        self.counter = 0
        self.things = []

    def getthing(self, id):
        for thing in self.things:
            if thing['id'] == id:
                return thing

    def creatething(self, data):
        thing = data
        thing['id'] = self.counter = self.counter + 1
        self.things.append(thing)
        return thing

    def updatething(self, id, data):
        thing = self.getthing(id)
        thing.update(data)
        return thing

    def deletething(self, id):
        thing = self.getthing(id)
        self.things.remove(thing)


DAO = Things()
DAO.creatething({'task': 'Build an API'})
DAO.creatething({'task': 'test api'})
DAO.creatething({'task': 'check'})

"""
[
  {
    "id": 1,
    "task": "Build an API"
  },
  {
    "id": 2,
    "task": "?????"
  },
  {
    "id": 3,
    "task": "profit!"
  }
]
"""