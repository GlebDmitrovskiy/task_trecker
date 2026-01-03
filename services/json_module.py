import json

#todo добавить docstring
class JsonModule:
    def load_json(self):
        """
        Функция load выгружает данные из файла
        """
        with open('tasks_file.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def dump_json(self, data):

        """Функция dump загружает новые данные в файл
        :param data: словарь данных который мы загружаем в файл
        """

        with open('tasks_file.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)
