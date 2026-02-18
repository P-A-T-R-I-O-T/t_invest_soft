# ui/add_participant.py
"""
Диалоговое окно для добавления участника.
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QClipboard
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QMessageBox,
    QApplication, QCheckBox
)
from data.participants_manager import ParticipantsManager


class AddParticipantDialog(QDialog):
    """
    Диалог для добавления нового участника: имя и токен.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить участника")
        self.setFixedSize(480, 360)
        self.manager = ParticipantsManager()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)

        # --- Имя участника ---
        layout.addWidget(QLabel("Имя участника:"), alignment=Qt.AlignLeft)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Введите имя участника")
        self.name_input.setFixedWidth(240)
        layout.addWidget(self.name_input, alignment=Qt.AlignLeft)

        # --- Токен ---
        layout.addWidget(QLabel("Токен:"), alignment=Qt.AlignLeft)

        self.token_input = QPlainTextEdit()
        self.token_input.setPlaceholderText("Введите токен")
        self.token_input.setFixedWidth(440)
        self.token_input.setFixedHeight(100)
        self.token_input.setTabChangesFocus(True)
        layout.addWidget(self.token_input, alignment=Qt.AlignLeft)

        # --- Галочка "Песочница" ---
        self.sandbox_checkbox = QCheckBox("Пользователь для песочницы")
        self.sandbox_checkbox.setToolTip("Если отмечено, пользователь будет создан для песочницы с ограниченными правами")
        layout.addWidget(self.sandbox_checkbox, alignment=Qt.AlignLeft)

        # --- Кнопка "Вставить" ---
        self.paste_btn = QPushButton("Вставить")
        self.paste_btn.setFixedWidth(100)
        layout.addWidget(self.paste_btn, alignment=Qt.AlignLeft)

        layout.addSpacing(20)  # Отступ

        # --- Кнопка "Добавить" ---
        self.add_btn = QPushButton("Добавить")
        self.add_btn.setFixedWidth(100)
        layout.addWidget(self.add_btn, alignment=Qt.AlignRight)

        self.setLayout(layout)

        # --- Сигналы ---
        self.paste_btn.clicked.connect(self.paste_token)
        self.add_btn.clicked.connect(self.on_add)

    def paste_token(self):
        clipboard = QApplication.clipboard()
        text = clipboard.text().strip()
        if not text:
            QMessageBox.information(self, "Буфер пуст", "Буфер обмена не содержит текста.")
            return
        self.token_input.setPlainText(text)

    def on_add(self):
        name = self.name_input.text().strip()
        token = self.token_input.toPlainText().strip()
        is_sandbox = self.sandbox_checkbox.isChecked()

        if not name:
            self.show_error("Имя участника не может быть пустым.")
            return

        try:
            self.manager.add_participant(name, token, is_sandbox)
            self.accept()
        except Exception as e:
            self.show_error(f"Ошибка при сохранении участника:\n{str(e)}")

    def show_error(self, message):
        QMessageBox.critical(self, "Ошибка", message)