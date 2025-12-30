from json_module import JsonModule
from models import Models
import datetime

json_module = JsonModule()
models = Models()


class Application:
    def add_task(self, new_data: str, status: str = "to do"):
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

    def mark_in_progress(self, id_task: int):
        self._mark(id_task=id_task, status_from="to do", status_to="in progress")

    def mark_in_done(self, id_task: int):
        self._mark(id_task=id_task, status_from="in progress", status_to="done")

    def _refresh_id(self, status: str):
        data = json_module.load_json()
        total = 1
        for task in data[status]:
            task['id'] = total
            total += 1
        json_module.dump_json(data)

    def _mark(self, id_task: int, status_from: str, status_to: str):
        data = json_module.load_json()
        task_id = int(id_task)
        tasks_list = data.get(status_from)
        is_correct_id = False
        for i in range(len(tasks_list)):
            # Проверяем ID текущей задачи
            if tasks_list[i].get('id') == task_id:
                is_correct_id = True
                break
        if is_correct_id:
            task_copy = tasks_list[id_task-1]
            task_copy['updatedAt'] = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
            task_copy['status'] = status_to
            self.add_task(new_data=task_copy, status=status_to)
            self.delete_task(task_id=id_task, status=status_from)


app = Application()
# app.add_task("third")
# app.delete_task(1)
# app.update_task(2, "Pidar")
# app.mark_in_progress(1)
app.mark_in_done(2)
