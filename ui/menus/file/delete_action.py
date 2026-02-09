# ui/menus/file/delete_action.py
"""
Диалог для удаления одного или нескольких участников.
Отображает список участников с чекбоксами, кнопку "Удалить", подтверждение.
"""

from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QListWidget,
                               QListWidgetItem, QCheckBox, QPushButton, QLabel,
                               QWidget, QScrollArea, QMessageBox)
from PySide6.QtCore import Qt
from data.participants_manager import ParticipantsManager


class DeleteParticipantDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.manager = ParticipantsManager()
        self.selected_checkboxes = []  # Список чекбоксов с именами участников
        self.setWindowTitle("Удалить участников")
        self.resize(300, 400)
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)

        # Заголовок
        label = QLabel("Выберите участников для удаления:")
        label.setStyleSheet("font-weight: bold; padding: 10px 0;")
        layout.addWidget(label)

        # Область прокрутки для списка
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(scroll_content)

        # Заполняем список участников
        self._populate_list()

        scroll.setWidget(scroll_content)
        layout.addWidget(scroll)

        # Кнопки
        button_layout = QHBoxLayout()
        self.delete_button = QPushButton("Удалить")
        self.delete_button.clicked.connect(self.on_delete_clicked)
        self.delete_button.setStyleSheet("background-color: #d32f2f; color: white; padding: 10px;")

        cancel_button = QPushButton("Отмена")
        cancel_button.clicked.connect(self.reject)

        button_layout.addStretch()
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(self.delete_button)
        layout.addLayout(button_layout)

    def _populate_list(self):
        """Заполняет список участников чекбоксами."""
        self.selected_checkboxes.clear()
        participants = self.manager.list_participants()

        if not participants:
            empty_label = QLabel("Нет участников для удаления.")
            empty_label.setAlignment(Qt.AlignCenter)
            empty_label.setStyleSheet("color: gray; font-style: italic;")
            self.scroll_layout.addWidget(empty_label)
            return

        for name in participants:
            checkbox = QCheckBox(name)
            self.scroll_layout.addWidget(checkbox)
            self.selected_checkboxes.append(checkbox)

        self.scroll_layout.addStretch()

    def on_delete_clicked(self):
        """Обработчик нажатия на кнопку 'Удалить'."""
        selected_names = [cb.text() for cb in self.selected_checkboxes if cb.isChecked()]

        if not selected_names:
            QMessageBox.warning(self, "Нет выбора", "Выберите хотя бы одного участника для удаления.")
            return

        # Подтверждение удаления
        if len(selected_names) == 1:
            message = f"Вы действительно хотите удалить участника:\n\n{selected_names[0]}?"
        else:
            names_str = "\n".join(f"• {name}" for name in selected_names)
            message = f"Вы действительно хотите удалить следующих участников:\n\n{names_str}"

        reply = QMessageBox.question(
            self,
            "Подтверждение удаления",
            message,
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            success_count = 0
            for name in selected_names:
                if self.manager.remove_participant(name):
                    success_count += 1

            # Обновляем интерфейс
            QMessageBox.information(
                self,
                "Удаление завершено",
                f"Успешно удалено: {success_count} участников."
            )
            self.accept()  # Закрываем диалог
