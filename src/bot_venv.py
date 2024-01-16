import os
import subprocess
import platform

class VirtualEnvironmentManager:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def create_virtual_environment(self):
        # Проверяем, существует ли папка
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

        # Формируем команду для создания виртуального окружения
        command = f"python -m venv {os.path.join(self.folder_path, 'venv')}"

        # Запускаем команду
        subprocess.run(command, shell=True)

    def activate_virtual_environment(self):
        # Определяем текущую операционную систему
        system = platform.system()

        # Формируем путь к скрипту активации
        activation_script = os.path.join(self.folder_path, 'venv', 'Scripts' if system == 'Windows' else 'bin', 'activate')

        # Активируем виртуальное окружение
        command = f"source {activation_script}" if system != 'Windows' else f"call {activation_script}"
        subprocess.run(command, shell=True)

if __name__ == "__main__":
    # Путь к папке, где нужно создать виртуальное окружение
    target_folder = "/bots/bot_name_1"

    # Создаем экземпляр класса VirtualEnvironmentManager
    manager = VirtualEnvironmentManager(target_folder)

    # Создаем виртуальное окружение
    manager.create_virtual_environment()

    # Активируем виртуальное окружение
    manager.activate_virtual_environment()