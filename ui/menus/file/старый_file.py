from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QClipboard
from PySide6.QtWidgets import (
QDialog, QVBoxLayout, QLabel,
QLineEdit, QPlainTextEdit, QPushButton, QMessageBox
)
from data.participants_manager import ParticipantsManager


class AddParticipantDialog(QDialog):
    """
    Диалоговое окно для добавления нового участника в систему.

    Пользователь вводит:
    - Имя участника (текст)
    - Токен (ровно 64 символа, например, API-токен)

    Особенности:
    - Фиксированный размер окна
    - Кнопка "Вставить" — слева, сразу после поля токена
    - Кнопка "Добавить" — справа, но ниже "Вставить"
    - Каждая кнопка размещена отдельно, без общего макета
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
        self.token_input.setPlaceholderText(
        "Введите токен"
        )
        self.token_input.setFixedWidth(440)
        self.token_input.setFixedHeight(100)
        self.token_input.setTabChangesFocus(True)
        layout.addWidget(self.token_input, alignment=Qt.AlignLeft)

        # --- Кнопка "Вставить" — слева, сразу после поля токена ---
        self.paste_btn = QPushButton("Вставить")
        self.paste_btn.setFixedWidth(100)
        layout.addWidget(self.paste_btn, alignment=Qt.AlignLeft)

        # --- Вертикальный отступ между кнопками (например, 20 пикселей) ---
        layout.addSpacing(20)

        # --- Кнопка "Добавить" — справа, но ниже "Вставить" ---
        self.add_btn = QPushButton("Добавить")
        self.add_btn.setFixedWidth(100)
        layout.addWidget(self.add_btn, alignment=Qt.AlignRight) # ← Прижата к правому краю

        # Применяем макет
        self.setLayout(layout)

        # --- Подключение сигналов ---
        self.paste_btn.clicked.connect(self.paste_token)
        self.add_btn.clicked.connect(self.on_add)

    def paste_token(self):
        """Вставляет токен из буфера обмена с проверкой длины."""
        clipboard = QClipboard()
        text = clipboard.text().strip()

        if not text:
            QMessageBox.information(self, "Буфер пуст", "Буфер обмена не содержит текста.")
        return

        self.token_input.setPlainText(text)


    def on_add(self):
        """Обработчик кнопки 'Добавить' — проверяет и сохраняет участника."""
        name = self.name_input.text().strip()
        token = self.token_input.toPlainText().strip()

        if not name:
            self.show_error("Имя участника не может быть пустым.")
            return

        try:
            self.manager.add_participant(name, token)
            self.accept() # Закрываем диалог с результатом Accepted
        except Exception as e:
            self.show_error(f"Ошибка при сохранении участника:\n{str(e)}")

    def show_error(self, message):
        """Показывает модальное окно с ошибкой."""
        QMessageBox.critical(self, "Ошибка", message)


class FileMenu:
    """
    Меню 'Файл' с действиями: Добавить участника, Открыть, Сохранить, Выход.
    """

    def __init__(self, menu_bar, parent):
        self.parent = parent
        self.menu = menu_bar.addMenu("Файл")
        self._setup_actions()

    def _setup_actions(self):
        # Добавить участника
        add_action = QAction("Добавить участника", self.parent)
        add_action.setStatusTip("Открыть диалог для добавления нового участника")
        add_action.triggered.connect(self.open_add_participant_dialog)
        self.menu.addAction(add_action)

        # Открыть
        open_action = QAction("Открыть", self.parent)
        open_action.setStatusTip("Загрузить данные из файла (в разработке)")
        self.menu.addAction(open_action)

        # Сохранить
        save_action = QAction("Сохранить", self.parent)
        save_action.setStatusTip("Сохранить текущие данные (в разработке)")
        self.menu.addAction(save_action)

        # Выход
        exit_action = QAction("Выход", self.parent)
        exit_action.setStatusTip("Закрыть приложение")
        exit_action.triggered.connect(self.parent.close)
        self.menu.addAction(exit_action)

    def open_add_participant_dialog(self):
        """Открывает диалог добавления участника."""
        dialog = AddParticipantDialog(self.parent)
        if dialog.exec() == QDialog.Accepted:
        # Можно добавить: self.parent.update_participants_list()
            pass # Пока заглушка