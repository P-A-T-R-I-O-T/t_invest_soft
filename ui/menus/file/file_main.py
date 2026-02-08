# ui/file_main.py
"""
Меню 'Файл' — содержит действия: Добавить участника, Открыть, Сохранить, Выход.
"""

from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QAction
from .add_participant import AddParticipantDialog  # Импорт из той же директории


class FileMenu:
    """
    Меню 'Файл' с действиями.
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
            # Здесь можно вызвать обновление списка, например:
            # self.parent.update_participants_list()
            pass
