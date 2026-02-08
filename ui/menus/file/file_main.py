# ui/menus/file/file_main.py
"""
Меню 'Файл' — содержит действия: Добавить участника, Выбрать основной аккаунт, Сохранить, Выход.
"""

from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QAction
from .add_participant import AddParticipantDialog
from .choosing_basics import ChooseMainAccountMenu  # Импортируем новое меню


class FileMenu:
    """
    Меню 'Файл' с действиями.
    """

    def __init__(self, menu_bar, parent):
        self.parent = parent
        self.menu = menu_bar.addMenu("Файл")
        self.choose_account_menu = None  # Сохраняем ссылку
        self._setup_actions()

    def _setup_actions(self):
        # --- Добавить участника ---
        add_action = QAction("Добавить участника", self.parent)
        add_action.setStatusTip("Открыть диалог для добавления нового участника")
        add_action.triggered.connect(self.open_add_participant_dialog)
        self.menu.addAction(add_action)

        # --- Выбрать основной аккаунт ---
        self.choose_account_menu = ChooseMainAccountMenu(self.parent)
        self.menu.addMenu(self.choose_account_menu)

        # --- Сохранить ---
        save_action = QAction("Сохранить", self.parent)
        save_action.setStatusTip("Сохранить текущие данные (в разработке)")
        self.menu.addAction(save_action)

        # --- Выход ---
        exit_action = QAction("Выход", self.parent)
        exit_action.setStatusTip("Закрыть приложение")
        exit_action.triggered.connect(self.parent.close)
        self.menu.addAction(exit_action)

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
