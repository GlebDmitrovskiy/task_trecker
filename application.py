from json_module import JsonModule
from models import Models
import datetime

json_module = JsonModule()
models = Models()


class Application:
    def add_task(self, new_data: str, status: str = "to do"):
        data = json_module.load_json()
        if status == "to do":
            data[status].append(models.add_task_model(new_data))
        else:
            data[status].append(new_data)
        json_module.dump_json(data)
        self._refresh_id()

    def delete_task(self, task_id: int, status:str):
        """
        Удаляет задачу по её ID.
        :param task_id: ID по которому мы удаляем задачу
        """
        data = json_module.load_json()
        task_id_to_delete = int(task_id)
        tasks_list = data.get(status)
        if not tasks_list:
            print("Список задач пуст или некорректен.")
            return
        index_to_remove = -1
        for i in range(len(tasks_list)):
            # Проверяем ID текущей задачи
            if tasks_list[i].get('id') == task_id_to_delete:
                index_to_remove = i
                break
        if index_to_remove != -1:
            # Удаляем элемент по найденному индексу
            removed_task = tasks_list.pop(index_to_remove)
            print(f"Задача '{removed_task['task']}' (ID: {task_id_to_delete}) удалена.")
            json_module.dump_json(data)
            self._refresh_id()
        else:
            print(f"Задача с ID {task_id_to_delete} не найдена в списке.")
        self._refresh_id()

    def update_task(self, task_id: int, message: str):
        data = json_module.load_json()
        index_to_remove = -1
        task_id_to_update = int(task_id)
        tasks_list = data.get('to do')
        for i in range(len(tasks_list)):
            # Проверяем ID текущей задачи
            if tasks_list[i].get('id') == task_id_to_update:
                index_to_remove = i
                break
        if index_to_remove != -1:
            # Удаляем элемент по найденному индексу
            tasks_list[index_to_remove]["task"] = message
            tasks_list[index_to_remove]['updatedAt'] = datetime.datetime.now().strftime('(%d.%m.%Y)%H:%M')
            print(f"Задача '{tasks_list[index_to_remove]["task"]}' (ID: {task_id_to_update}) обновлена.")
            json_module.dump_json(data)
        else:
            print(f"Задача с ID {task_id_to_update} не найдена в списке.")

    def mark_in_progress(self, id_task: int):
        self._mark(id_task=id_task, status_from="to do", status_to="in progress")

    def mark_in_done(self, id_task: int):
        self._mark(id_task=id_task, status_from="in progress", status_to="done")

    def _refresh_id(self):
        data = json_module.load_json()
        total = 1
        for task in data['to do']:
            task['id'] = total
            total += 1
        total = 1
        for task in data['in progress']:
            task['id'] = total
            total += 1
        total = 1
        for task in data['done']:
            task['id'] = total
            total += 1
        json_module.dump_json(data)

    def _mark(self, id_task: int, status_from: str, status_to: str):
        data = json_module.load_json()
        task_id_to_update = int(id_task)
        tasks_list = data.get(status_from)
        index_to_remove = -1
        for i in range(len(tasks_list)):
            # Проверяем ID текущей задачи
            if tasks_list[i].get('id') == task_id_to_update:
                index_to_remove = i
                break
        if index_to_remove != -1:
            task_copy = tasks_list[index_to_remove]
            task_copy['updatedAt'] = datetime.datetime.now().strftime('(%d.%m.%Y)%H:%M')
            task_copy['status'] = status_to
            self.add_task(task_copy, status=status_to)
            self.delete_task(task_id=id_task, status=status_from)


app = Application()
#app.add_task("hui")
# app.delete_task(4)
# app.update_task(1, "Pidar")
#app.mark_in_progress(1)
#app.mark_in_done(1)
