# ui/menus/file/file_main.py
"""
Меню 'Файл' — содержит действия: Добавить участника, Выбрать основной аккаунт, Сохранить, Выход.
"""

from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QAction
from .add_participant import AddParticipantDialog
from .choosing_basics import ChooseMainAccountMenu
from .delete_action import DeleteParticipantDialog
from data.participants_manager import ParticipantsManager


class FileMenu:
    """
    Меню 'Файл' с действиями.
    """

    def __init__(self, menu_bar, parent):
        self.parent = parent
        self.menu = menu_bar.addMenu("Файл")
        self.choose_account_menu = None  # Сохраняем ссылку
        self.delete_action = None
        self.manager = ParticipantsManager()  # Для проверки списка участников
        self._setup_actions()
        # Подключаем обновление состояния при открытии меню
        self.menu.aboutToShow.connect(self._update_menu_state)

    def _setup_actions(self):
        # --- Добавить участника ---
        add_action = QAction("Добавить участника", self.parent)
        add_action.setStatusTip("Открыть диалог для добавления нового участника")
        add_action.triggered.connect(self.open_add_participant_dialog)
        self.menu.addAction(add_action)

        # --- Выбрать основной аккаунт ---
        self.choose_account_menu = ChooseMainAccountMenu(self.parent)
        self.menu.addMenu(self.choose_account_menu)

        # --- Удалить участника ---
        self.delete_action = QAction("Удалить участника", self.parent)
        self.delete_action.setStatusTip("Открыть диалог для удаления одного или нескольких участников")
        self.delete_action.triggered.connect(self.open_delete_participant_dialog)
        self.menu.addAction(self.delete_action)

        # --- Выход ---
        exit_action = QAction("Выход", self.parent)
        exit_action.setStatusTip("Закрыть приложение")
        exit_action.triggered.connect(self.parent.close)
        self.menu.addAction(exit_action)


    def _update_menu_state(self):
        """Обновляет состояние пунктов меню при его открытии."""
        participants_exist = len(self.manager.list_participants()) > 0
        self.delete_action.setEnabled(participants_exist)

    def open_add_participant_dialog(self):
        """Открывает диалог добавления участника."""
        dialog = AddParticipantDialog(self.parent)
        if dialog.exec() == QDialog.Accepted:
            # После добавления — обновляем список аккаунтов
            if self.choose_account_menu:
                self.choose_account_menu._populate_menu()
                # При желании: автоматически выбрать нового
                # participants = self.choose_account_menu.manager.list_participants()
                # if participants:
                #     self.choose_account_menu._select_account(participants[-1])

    def open_delete_participant_dialog(self):
        """Открывает диалог удаления участника."""
        dialog = DeleteParticipantDialog(self.parent)
        if dialog.exec() == QDialog.Accepted:
            # После удаления — обновляем список аккаунтов
            if self.choose_account_menu:
                self.choose_account_menu._populate_menu()
