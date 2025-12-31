import datetime

#todo docstring

class Models:
    def add_task_model(self, message: str):
        """
        Шаблон по которому создаются задачи
        :param message: добавляет задачу по сообщению
        """
        task_model = {
            'id': 1,
            'task': message,
            'status': 'to do',
            'createdAt': datetime.datetime.now().strftime('%d.%m.%Y %H:%M'),
            'updatedAt': datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
        }
        return task_model
