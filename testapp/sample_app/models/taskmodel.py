#from sample_app.configs import tasks.json


class Tasktracker():
    def __init__(self):
        self.counter = 0
        self.tasks = []

    def gettask(self, task_Id):
        for task in self.tasks:
            if task['task_Id'] == task_Id:
                return task


    def createtask(self, data):
        task = data
        task['task_Id'] = self.counter = self.counter + 1
        self.tasks.append(task)
        return task

    def updatetask(self, task_Id, data):
        task = self.gettask(task_Id)
        task.update(data)
        return task

    def deletetask(self, task_Id):
        l = len(self.tasks)
        print("len", l)
        for idx in range(l):
            if self.tasks[idx]['task_Id'] == task_Id:
                del self.tasks[idx]
                return True
        else:
            return False

    def lookup(self, task):
        for t in self.tasks:
            if task == t['task']:
                return t['task_id']
        else:
            return None


task_obj = Tasktracker()
task_obj.createtask({'task': 'Build an API'})
task_obj.createtask({'task': 'test api'})
task_obj.createtask({'task': 'check'})
print(task_obj.tasks)

"""
[
  {
    "task_Id": 1,
    "task": "Build an API"
  },
  {
    "task_Id": 2,
    "task": "?????"
  },
  {
    "task_Id": 3,
    "task": "profit!"
  }
]
"""