from PySide6.QtGui import QAction
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel
from data.participants_manager import ParticipantsManager


class AddParticipantDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.manager = ParticipantsManager()
        self.setWindowTitle("Добавить участника")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.token_input = QLineEdit()
        self.token_input.setEchoMode(QLineEdit.Password)

        layout.addWidget(QLabel("Имя участника:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Токен:"))
        layout.addWidget(self.token_input)

        btn = QPushButton("Добавить")
        btn.clicked.connect(self.on_add)
        layout.addWidget(btn)

        self.setLayout(layout)

    def on_add(self):
        name = self.name_input.text().strip()
        token = self.token_input.text().strip()
        if name and token:  # Проверка на пустоту
            self.manager.add_participant(name, token)
            self.accept()  # Закрыть окно
        else:
            # Можно добавить предупреждение, если хочешь
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Ошибка", "Имя и токен не могут быть пустыми.")


class FileMenu:
    def __init__(self, menu_bar, parent):
        self.parent = parent
        self.menu = menu_bar.addMenu("Файл")
        self._setup_actions()

    def _setup_actions(self):
        # --- Действие "Добавить участника" ---
        add_participant_action = QAction("Добавить участника", self.parent)
        add_participant_action.triggered.connect(self.open_add_participant_dialog)
        self.menu.addAction(add_participant_action)  # Добавляем первым

        # --- Действие "Открыть" ---
        open_action = QAction("Открыть", self.parent)
        self.menu.addAction(open_action)
        # open_action.triggered.connect(...)  # Подключи нужный слот

        # --- Действие "Сохранить" ---
        save_action = QAction("Сохранить", self.parent)
        self.menu.addAction(save_action)
        # save_action.triggered.connect(...)  # Подключи нужный слот

        # --- Действие "Выход" ---
        exit_action = QAction("Выход", self.parent)
        self.menu.addAction(exit_action)
        exit_action.triggered.connect(self.parent.close)

    def open_add_participant_dialog(self):
        dialog = AddParticipantDialog(self.parent)
        dialog.exec()
