"""Main module. Runs the application"""


from sys import argv
from PyQt6.QtWidgets import QApplication
from src.app import MainWindow


def main():
    """This function runs application"""
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
