#import datetime
#from application import Application
#from task_trecker.user_module.user_input import UserInput
#
#UserInput.start_program()
#
#
## todo доделать in progress, done
##def show_tasks(status = None):
##    if status is None:
##        pokazat vse
##    else if status == "in-progress":
##        data = load_json()
##        #    print("in progress задачи:")
##        #    for task in data['in progress']:
##        #        print(task)
##def show_tasks():
##    data = load_json()
##    print("to do задачи:")
##    for task in data['to do']:
##        print(task)
##
##
##def show_tasks_in_progress():
##    data = load_json()
##    print("in progress задачи:")
##    for task in data['in progress']:
##        print(task)
##
##
##def show_tasks_in_done():
##    data = load_json()
##    print("done задачи:")
##    for task in data['done']:
##        print(task)
#
#
#def dump_json(data):
#    """Функция dump загружает новые данные в файл
#    :param data: словарь данных который мы загружаем в файл
#    """
#
#    with open('tasks_file.json', 'w', encoding='utf-8') as file:
#        json.dump(data, file, indent=2)
#
#
#def load_json():
#    with open('tasks_file.json', 'r', encoding='utf-8') as file:
#        data = json.load(file)
#        return data
#
#
#def add_task_to_do(task_data, status):
#    data = load_json()
#    if status == "to do":
#        data['to do'].append(task_data)
#    elif status == "in progress":
#        data['in progress'].append(task_data)
#    dump_json(data)
#    refresh_id()
#    show_tasks()
#
#
#def add_task_in_progress(task_data):
#    data = load_json()
#    data['in progress'].append(task_data)
#    dump_json(data)
#    refresh_id_progress()
#    show_tasks_in_progress()
#
#
#def add_task_done(task_data):
#    data = load_json()
#    data['done'].append(task_data)
#    dump_json(data)
#    refresh_id_done()
#    show_tasks_in_done()
#
#
#def refresh_id_done():
#    total = 1
#    data = load_json()
#    for task in data['done']:
#        task['id'] = total
#        total += 1
#    dump_json(data)
#
#
#def refresh_id_progress():
#    total = 1
#    data = load_json()
#    for task in data['in progress']:
#        task['id'] = total
#        total += 1
#    dump_json(data)
#
#
#def refresh_id():
#    total = 1
#    data = load_json()
#    for task in data['to do']:
#        task['id'] = total
#        total += 1
#    dump_json(data)
#
#
#def delete_task(task_id_str):
#    """
#    Удаляет задачу по её ID.
#    :param task_id_str: ID по которому мы удаляем задачу
#    """
#    data = load_json()
#    task_id_to_delete = int(task_id_str)
#    tasks_list = data.get('to do')
#    if not tasks_list:
#        print("Список задач пуст или некорректен.")
#        return
#    index_to_remove = -1
#    for i in range(len(tasks_list)):
#        # Проверяем ID текущей задачи
#        if tasks_list[i].get('id') == task_id_to_delete:
#            index_to_remove = i
#            break
#    if index_to_remove != -1:
#        # Удаляем элемент по найденному индексу
#        removed_task = tasks_list.pop(index_to_remove)
#        print(f"Задача '{removed_task['task']}' (ID: {task_id_to_delete}) удалена.")
#        dump_json(data)
#        refresh_id()
#        dump_json(data)
#    else:
#        print(f"Задача с ID {task_id_to_delete} не найдена в списке.")
#    refresh_id()
#    show_tasks()
#
#
#def delete_task_in_progress(task_id_str):
#    """
#    Удаляет задачу по её ID.
#    :param task_id_str: ID по которому мы удаляем задачу
#    """
#    data = load_json()
#    task_id_to_delete = int(task_id_str)
#    tasks_list = data.get('in progress')
#    if not tasks_list:
#        print("Список задач пуст или некорректен.")
#        return
#    index_to_remove = -1
#    for i in range(len(tasks_list)):
#        # Проверяем ID текущей задачи
#        if tasks_list[i].get('id') == task_id_to_delete:
#            index_to_remove = i
#            break
#    if index_to_remove != -1:
#        # Удаляем элемент по найденному индексу
#        removed_task = tasks_list.pop(index_to_remove)
#        print(f"Задача '{removed_task['task']}' (ID: {task_id_to_delete}) удалена.")
#        dump_json(data)
#        refresh_id_progress()
#        dump_json(data)
#    else:
#        print(f"Задача с ID {task_id_to_delete} не найдена в списке.")
#    refresh_id_progress()
#    show_tasks_in_progress()
#
#
#def delete_task_done(task_id_str):
#    """
#    Удаляет задачу по её ID.
#    :param task_id_str: ID по которому мы удаляем задачу
#    """
#    data = load_json()
#    task_id_to_delete = int(task_id_str)
#    tasks_list = data.get('done')
#    if not tasks_list:
#        print("Список задач пуст или некорректен.")
#        return
#    index_to_remove = -1
#    for i in range(len(tasks_list)):
#        # Проверяем ID текущей задачи
#        if tasks_list[i].get('id') == task_id_to_delete:
#            index_to_remove = i
#            break
#    if index_to_remove != -1:
#        # Удаляем элемент по найденному индексу
#        removed_task = tasks_list.pop(index_to_remove)
#        print(f"Задача '{removed_task['task']}' (ID: {task_id_to_delete}) удалена.")
#        dump_json(data)
#        refresh_id_done()
#        dump_json(data)
#    else:
#        print(f"Задача с ID {task_id_to_delete} не найдена в списке.")
#    refresh_id_done()
#    show_tasks_in_done()
#
#
#def update_task(id_task: int, task: str):
#    data = load_json()
#    task_id_to_update = int(id_task)
#    tasks_list = data.get('to do')
#    index_to_remove = -1
#    previous_task = None
#    for i in range(len(tasks_list)):
#        # Проверяем ID текущей задачи
#        if tasks_list[i].get('id') == task_id_to_update:
#            index_to_remove = i
#            previous_task = tasks_list[i]['task']
#            break
#    if index_to_remove != -1:
#        # Обновляем элемент по найденному индексу
#        print(f"Задача по ID {task_id_to_update} '{previous_task}'", end=' ')
#        tasks_list[index_to_remove]['task'] = task
#        tasks_list[index_to_remove]['updatedAT'] = datetime.datetime.now().strftime('(%d.%m.%Y)%H:%M')
#        print(f"обновлена на '{task}'")
#        dump_json(data)
#    show_tasks()
#
#
#def update_task_in_progres():
#    data = load_json()
#    tasks_list = data.get('in progress')
#    tasks_list[-1]['status'] = 'in progress'
#    tasks_list[-1]['updatedAT'] = datetime.datetime.now().strftime('(%d.%m.%Y)%H:%M')
#    dump_json(data)
#    show_tasks_in_progress()
#
#def update_task_done():
#    data = load_json()
#    tasks_list = data.get('done')
#    tasks_list[-1]['status'] = 'done'
#    tasks_list[-1]['updatedAT'] = datetime.datetime.now().strftime('(%d.%m.%Y)%H:%M')
#    dump_json(data)
#    show_tasks_in_done()
#
#
#def mark_in_progress(id_task: int):
#    data = load_json()
#    task_id_to_update = int(id_task)
#    tasks_list = data.get('to do')
#    index_to_remove = -1
#    for i in range(len(tasks_list)):
#        # Проверяем ID текущей задачи
#        if tasks_list[i].get('id') == task_id_to_update:
#            index_to_remove = i
#            break
#    if index_to_remove != -1:
#        task_copy = tasks_list[index_to_remove]
#        add_task_in_progress(task_copy)
#        delete_task(id_task)
#        update_task_in_progres()
#    show_tasks_in_progress()
#
#
#def mark_done(id_task: int):
#    data = load_json()
#    task_id_to_update = int(id_task)
#    tasks_list = data.get('in progress')
#    index_to_remove = -1
#    for i in range(len(tasks_list)):
#        # Проверяем ID текущей задачи
#        if tasks_list[i].get('id') == task_id_to_update:
#            index_to_remove = i
#            break
#    if index_to_remove != -1:
#        task_copy = tasks_list[index_to_remove]
#        add_task_done(task_copy)
#        delete_task_in_progress(id_task)
#        update_task_done()
#    show_tasks_in_progress()
#
#
#while True:
#    answer_user = input("Введите команду и описание задачи: ").split()
#    command = answer_user[0]
#    if command == 'выход':
#        print('Завершение программы.')
#        break
#    if len(answer_user) > 1:
#        answer_tasks = answer_user[1:]
#        answer_id = answer_user[1]
#        answer_update_list = answer_user[2:]
#        answer = ' '.join(answer_tasks)
#        answer_update = ' '.join(answer_update_list)
#
#    tasks_file = {
#        'id': 1,
#        'task': answer,
#        'status': 'to do',
#        'createdAt': datetime.datetime.now().strftime('(%d.%m.%Y)%H:%M)'),
#        'updatedAT': datetime.datetime.now().strftime('(%d.%m.%Y)%H:%M)')
#    }
#
#    if command.lower() == 'удалить':
#        if answer:
#            delete_task(answer)
#        else:
#            print("Пожалуйста, укажите ID задачи после команды 'удалить'.")
#
#    if command.lower() == 'добавить':
#        Application.add_task()
#        add_task_to_do(tasks_file)
#    elif command.lower() == 'все':
#        show_tasks()
#        show_tasks_in_done()
#        show_tasks_in_progress()
#    elif command.lower() == 'показать':
#        show_tasks()
#    elif command.lower() == 'прогресс':
#        show_tasks_in_progress()
#    elif command.lower() == 'обновить':
#        update_task(answer_id, answer_update)
#    elif command.lower() == 'перенос':
#        mark_in_progress(answer_id)
#    elif command.lower() == 'закончить':
#        mark_done(answer_id)
#