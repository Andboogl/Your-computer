"""Module with different gui functions"""


from PyQt6.QtWidgets import QMessageBox


def show_error_message(win, text):
    """Show error type of QMessageBox"""
    msg_box = QMessageBox(win)
    msg_box.setText(text)
    msg_box.setIcon(QMessageBox.Icon.Critical)
    msg_box.exec()
