"""Module to handling ui"""
import os.path

from PyQt6 import QtWidgets
from design import Window, show_error_message
from base import Computer
from cache import Cache
from paths import cache_file_path


class MainWindow(QtWidgets.QMainWindow):
    """Main application window class"""
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        # Loading design
        self.design = Window()
        self.design.setupUi(self)

        # Computer info
        self.computer_info = Computer()
        self.cache = cache = Cache()

        # Loading computer info
        if os.path.exists(cache_file_path()):
            try:
                cache = self.cache.load_cache()

                if cache['ip'] == 'Undefind':
                    self.design.ip.setText('IP: Не визначенний')

                else:
                    self.design.ip.setText(f'IP: {cache['ip']}')

                self.design.architecture.setText(f'Архітектура: {cache['architecture']}')
                self.design.processor.setText(f'Процессор: {cache['processor']}')
                self.design.python_version.setText(f'Версія Python, на якій працює ця программа:\n{cache['python_version']}')
                self.design.python_build.setText(f'Збірка Python, на якій працює ця программа:\n{cache['python_build']}')

            except Exception:
                self.load_computer_info()

        else:
            self.load_computer_info()

        # Pressing buttons
        self.design.update_data.clicked.connect(self.load_computer_info)

    def load_computer_info(self):
        """Load computer info"""
        self.computer_info = Computer()

        if self.computer_info.ip == 'Undefind':
            self.design.ip.setText('IP: Не визначенний')
            show_error_message(
                self,
                'Не вдалося визначити ваш IP. Перевірте підключення до інтернету')

        else:
            self.design.ip.setText(f'IP: {self.computer_info.ip}')

        self.design.architecture.setText(f'Архітектура: {self.computer_info.architecture}')
        self.design.processor.setText(f'Процессор: {self.computer_info.processor}')
        self.design.kernel.setText(f'Ядро: {self.computer_info.kernel}')
        self.design.python_version.setText(
            f'Версія Python, на якій працює ця программа:\n{self.computer_info.python_version}')
        self.design.python_build.setText(
            f'Сбірка Python, на якій працює ця программа:\n{self.computer_info.python_build}')

        # Loading data to cache
        self.cache.upload_cache(self.computer_info)
