# preview_widgets.py
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QSpinBox,
    QComboBox, QDateEdit, QPushButton
)

class WidgetPreview(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Образцы полей ввода — PySide6")
        self.resize(400, 500)

        layout = QVBoxLayout()

        # --- QLineEdit ---
        layout.addWidget(QLabel("QLineEdit (однострочный ввод):"))
        line_edit = QLineEdit()
        line_edit.setPlaceholderText("Введите текст...")
        layout.addWidget(line_edit)

        # --- QPlainTextEdit ---
        layout.addWidget(QLabel("QPlainTextEdit (многострочный):"))
        text_edit = QPlainTextEdit()
        text_edit.setPlaceholderText("Длинный текст...\nТокен, лог, JSON — всё сюда.")
        text_edit.setMaximumHeight(80)
        layout.addWidget(text_edit)

        # --- QSpinBox ---
        layout.addWidget(QLabel("QSpinBox (числа):"))
        spin = QSpinBox()
        spin.setRange(0, 100)
        layout.addWidget(spin)

        # --- QComboBox ---
        layout.addWidget(QLabel("QComboBox (выбор + ввод):"))
        combo = QComboBox()
        combo.setEditable(True)
        combo.addItems(["Алиса", "Боб", "Вася"])
        combo.setPlaceholderText("Выберите или введите имя")
        layout.addWidget(combo)

        # --- QDateEdit ---
        layout.addWidget(QLabel("QDateEdit (дата):"))
        date_edit = QDateEdit()
        date_edit.setCalendarPopup(True)
        layout.addWidget(date_edit)

        # --- QPushButton ---
        layout.addWidget(QLabel("Пример кнопки:"))
        btn = QPushButton("Нажми меня")
        layout.addWidget(btn)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WidgetPreview()
    window.show()
    app.exec()
