from json_module import JsonModule
from models import Models
import datetime

json_module = JsonModule()
models = Models()

#todo добавить docstring ко всем методам
class Application():
    def add_task(self, new_data: str, status: str = "to do"):
        """
        Удаляет задачу по её ID.
        :param new_data: сообщение которое добавляем в задачу
        """
        data = json_module.load_json()
        if status == "to do":
            data[status].append(models.add_task_model(message=new_data))
        else:
            data[status].append(new_data)
        json_module.dump_json(data)
        self._refresh_id(status=status)

    def delete_task(self, task_id: int, status: str = "to do"):
        """
        Удаляет задачу по её ID.
        :param task_id: ID по которому мы удаляем задачу
        """
        data = json_module.load_json()
        task_id = int(task_id)
        tasks_list = data.get(status)
        if not tasks_list:
            print("Список задач пуст или некорректен.")
            return
        is_correct_id = False
        for i in range(len(tasks_list)):
            # Проверяем ID текущей задачи
            if tasks_list[i].get('id') == task_id:
                is_correct_id = True
                break
        if is_correct_id:
            # Удаляем элемент по найденному индексу
            removed_task = tasks_list.pop(task_id - 1)
            print(f"Задача '{removed_task['task']}' (ID: {task_id}) удалена.")
            json_module.dump_json(data)
            self._refresh_id(status=status)
        else:
            print(f"Задача с ID {task_id} не найдена в списке.")


    def update_task(self, task_id: int, message: str):
        """
        Обновляет задачу по её id.
        :param task_id: ID по которому мы обновляем задачу
        :param message: сообщение на которое обновляется старая задача, на новую.
        """
        data = json_module.load_json()
        task_id = int(task_id)
        tasks_list = data.get('to do')
        is_correct_id = False
        for i in range(len(tasks_list)):
            # Проверяем ID текущей задачи
            if tasks_list[i].get('id') == task_id:
                is_correct_id = True
                break
        if is_correct_id:
            # Удаляем элемент по найденному индексу
            tasks_list[task_id]["task"] = message
            tasks_list[task_id]['updatedAt'] = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
            print(f"Задача '{tasks_list[task_id]["task"]}' (ID: {task_id}) обновлена.")
            json_module.dump_json(data)
        else:
            print(f"Задача с ID {task_id} не найдена в списке.")

    def mark_in_progress(self, task_id: int):
        """
        Переносит задачу из "to do" в "in progress"
        :param task_id: ID по которому переносим задачу
        """
        self._mark(task_id=task_id, status_from="to do", status_to="in progress")

    def mark_in_done(self, task_id: int):
        """
        Переносит задачу из "in progress" в "done"
        :param task_id: ID по которому переносим задачу
        """
        self._mark(task_id=task_id, status_from="in progress", status_to="done")

    def _refresh_id(self, status: str):
        """
        Обновляет ID задач
        :param status: принимает статус, по которым происходит обновление ID
        """
        data = json_module.load_json()
        total = 1
        for task in data[status]:
            task['id'] = total
            total += 1
        json_module.dump_json(data)

    def show_task(self, status: str = "to do"):
        data = json_module.load_json()
        print(f"{status} задачи:")
        for task in data[status]:
            print(task)

    def show_task_in_progress(self, status: str = "in progress"):
        data = json_module.load_json()
        print(f"{status} задачи:")
        for task in data[status]:
            print(task)
    def show_task_in_done(self, status: str = "done"):
        data = json_module.load_json()
        print(f"{status} задачи:")
        for task in data[status]:
            print(task)

    #todo везде подавалось task_id, но в коде в некоторых местах есть id_task, исправить на task_id надо
    def _mark(self, task_id: int, status_from: str, status_to: str):
        """
        Реализация переноса задач
        :param task_id: ID по которому переносим задачу
        :param status_from: статус откуда взять задачу
        :param status_to: статус куда перенести задачу
        """
        data = json_module.load_json()
        task_id = int(task_id)
        tasks_list = data.get(status_from)
        is_correct_id = False
        for i in range(len(tasks_list)):
            # Проверяем ID текущей задачи
            if tasks_list[i].get('id') == task_id:
                is_correct_id = True
                break
        if is_correct_id:
            task_copy = tasks_list[task_id - 1]
            task_copy['updatedAt'] = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
            task_copy['status'] = status_to
            self.add_task(new_data=task_copy, status=status_to)
            self.delete_task(task_id=task_id, status=status_from)


app = Application()
#app.add_task("pidar")
# app.delete_task(1)
# app.update_task(2, "Pidar")
#app.mark_in_progress(3)
#app.mark_in_done(1)
#app.show_task_in_progress()


