import json

class JsonFileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path + "/structure.json"
        self.data = []
        self.load_data()

    def load_data(self):
        try:
            with open(self.file_path, 'r', encoding="utf-8") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print(f"File {self.file_path} not found. Creating a new file.")

    def save_data(self):
        with open(self.file_path, 'w', encoding="utf-8") as file:
            json.dump(self.data, file, indent=2)

    def add_entry(self, handler_type, command_action, message_text, buttons_state, buttons):
        entry = {"message_text": message_text, "buttons": buttons} if buttons_state else {"message_text": message_text}
        entry[("command_action" if handler_type == "simple" else "button_action")] = command_action
        self.data.append(entry)

    def remove_entry_by_index(self, index):
        if 0 <= index < len(self.data):
            del self.data[index]

    def remove_entry_by_command_action(self, command_action):
        for entry in self.data:
            if entry.get("command_action") == command_action or entry.get("button_action") == command_action:
                self.data.remove(entry)
                break

    def get_command_names(self):
        return [entry.get("command_action") if entry.get("command_action") != None else entry.get("button_action") for entry in self.data]

    def get_all_buttons(self):
        all_buttons = []
        for entry in self.data:
            if "buttons" in entry:
                all_buttons.extend(entry["buttons"])
        return all_buttons

    def update_command(self, old_command_action, new_message_text=None, new_buttons=None):
        for entry in self.data:
            if entry.get("command_action") == old_command_action or entry.get("button_action") == old_command_action:
                # entry["command_action"] = new_command_action
                if new_message_text is not None:
                    entry["message_text"] = new_message_text
                if new_buttons is not None:
                    entry["buttons"] = new_buttons
                break

    def get_data(self):
        return json.dumps(self.data, indent=2)

# # Пример использования класса
# file_path = 'structure.json'
# json_processor = JsonFileProcessor(file_path)

# # Пример добавления новой записи
# json_processor.add_entry("Новая команда", "Новый текст сообщения", ["Кнопка 1", "Кнопка 2"])

# # Вывод всех названий команд
# command_names = json_processor.get_command_names()
# print("Названия команд:", command_names)

# # Вывод всех кнопок
# all_buttons = json_processor.get_all_buttons()
# print("Все кнопки:", all_buttons)

# # Обновление команды
# json_processor.update_command("Название команды", "Новое название команды", "Новый текст сообщения", ["Новая кнопка"])

# # Вывод обновленных данных
# json_processor.print_data()

# # Удаление записи по индексу
# json_processor.remove_entry_by_index(0)

# # Удаление записи по значению command_action
# json_processor.remove_entry_by_command_action("Новая команда")

# # Вывод данных после удаления
# json_processor.print_data()

# # Сохранение данных обратно в файл
# json_processor.save_data()
