from task_trecker.application import Application

app = Application()

class UserInput:
    def start_program(self):
        """
        Метод выполнения ввода пользователя
        """
        while True:
            answer_user = input("Введите команду и описание задачи: ").split()
            command = answer_user[0]
            if command == 'выход':
                print('Завершение программы.')
                break
            if len(answer_user) > 1:
                answer_tasks = answer_user[1:]
                answer_id = answer_user[1]
                answer_update_list = answer_user[2:]
                answer = ' '.join(answer_tasks)
                answer_update = ' '.join(answer_update_list)

            if command.lower() == 'удалить':
                if answer:
                    app.delete_task(answer_id)
                else:
                    print("Пожалуйста, укажите ID задачи после команды 'удалить'.")

            if command.lower() == 'добавить':
                app.add_task(answer)
            elif command.lower() == 'все':
                app.show_task()
                app.show_task_in_progress()
                app.show_task_in_done()
            elif command.lower() == 'показать':
                app.show_task()
            elif command.lower() == 'прогресс':
                app.show_task_in_progress()
            elif command.lower() == 'обновить':
                app.update_task(answer_id, answer_update)
            elif command.lower() == 'перенос':
                app.mark_in_progress(answer_id)
            elif command.lower() == 'закончить':
                app.mark_done(answer_id)

start=UserInput()
start.start_program()
# todo начать писать user input, оформляй код правильно как в других файлах
'''
Копируешь appliatin.py, models.py, json_module.py пишешь гпт вот файл json_module.py
и кидаешь все что там внутри и так со всем, и кидаешь ошибку которая возникает при
запуске этого файла и спрашиваешь что не так и как не дублировать импорты
'''
