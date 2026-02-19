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
        self.sandbox_action = None  # Ссылка на пункт "Настройка песочницы"

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

        # --- Разделитель ---
        self.menu.addSeparator()

        # --- Настройка песочницы ---
        self.sandbox_action = QAction("Настройка песочницы", self.parent)
        self.sandbox_action.setStatusTip("Открыть настройки песочницы для тестирования")
        self.sandbox_action.triggered.connect(self.open_sandbox_settings)
        self.menu.addAction(self.sandbox_action)

        # --- Выход ---
        exit_action = QAction("Выход", self.parent)
        exit_action.setStatusTip("Закрыть приложение")
        exit_action.triggered.connect(self.parent.close)
        self.menu.addAction(exit_action)

            # Подключаем обновление состояния при открытии меню
        self.menu.aboutToShow.connect(self._update_menu_state)


    def _update_menu_state(self):
        """Обновляет состояние пунктов меню при его открытии."""
        participants_exist = len(self.manager.list_participants()) > 0
        self.delete_action.setEnabled(participants_exist)

        # Инициализируем current_account заранее — всегда есть значение
        current_account = None

        # Проверяем существование sandbox_action и choose_account_menu
        if self.sandbox_action is not None and self.choose_account_menu is not None:
            current_account = self.choose_account_menu.get_current_account()

        # Обновляем состояние пункта «Настройка песочницы»
        if current_account and self.sandbox_action is not None:
            # Проверяем, является ли пользователь пользователем песочницы
            is_sandbox = self.manager.is_sandbox_user(current_account)
            self.sandbox_action.setEnabled(is_sandbox)
        else:
            # Если аккаунта нет или он реальный — отключаем пункт меню
            if self.sandbox_action is not None:
                self.sandbox_action.setEnabled(False)

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

    def open_sandbox_settings(self):
        """Открывает диалог настройки песочницы."""
        # TODO: Реализовать открытие диалога настроек песочницы
        print("Открывается диалог настройки песочницы")
