from PySide6.QtWidgets import QMessageBox

def show_infomessage(title, text):
    QMessageBox.information(None, title, text)

def show_warningmessage(title, text):
    QMessageBox.warning(None, title, text)
