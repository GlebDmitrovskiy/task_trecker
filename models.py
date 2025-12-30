import datetime

class Models:
    def add_task_model(self, message):
        task_model = {
            'id': 1,
            'task': message,
            'status': 'to do',
            'createdAt': datetime.datetime.now().strftime('%d.%m.%Y %H:%M'),
            'updatedAt': datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
        }
        return task_model
