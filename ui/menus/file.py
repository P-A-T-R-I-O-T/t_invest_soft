from PySide6.QtGui import QAction

class FileMenu:
    def __init__(self, menu_bar, parent):
        self.parent = parent
        self.menu = menu_bar.addMenu("Файл")
        self._setup_actions()

    def _setup_actions(self):
        self.menu.addAction("Открыть")
        self.menu.addAction("Сохранить")

        # Действие "Выход" с обработчиком
        exit_action = QAction("Выход", self.parent)
        self.menu.addAction(exit_action)
        exit_action.triggered.connect(self.parent.close)
